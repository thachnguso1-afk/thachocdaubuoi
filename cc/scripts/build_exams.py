# -*- coding: utf-8 -*-
"""
Packages 900 MCQs + 90 TF + 90 SA into 45 completely disjoint 60-minute exams
(each: 20 MCQs [7 basic, 7 adv, 6 hsg across all 6 topics] + 2 TF + 2 SA).
Computes full 45x45 pairwise ID overlap matrix (assert <= 5%, achieving 0.00%)
and text near-duplicate audit across all 1,080 questions.
Emits C:\\Users\\User\\.gemini\\antigravity\\scratch\\biomaster-exam-bank\\data\\exams_data.js
"""
import json
import random
import re
from collections import Counter, defaultdict
from common import DATA_DIR, TOPICS, write_js_module


def load_js_array(filename, global_prop):
    raw = (DATA_DIR / filename).read_text(encoding="utf-8")
    prefix = f"window.BIOMASTER.{global_prop} = "
    idx = raw.find(prefix)
    assert idx != -1, f"Missing prefix {prefix} in {filename}"
    body = raw[idx + len(prefix):].strip()
    if body.endswith(";"):
        body = body[:-1]
    return json.loads(body)


def tokenize_vn(text):
    # Strip HTML tags & LaTeX wrappers lightly to compare semantic stem overlap
    s = re.sub(r"<[^>]+>", " ", text.lower())
    s = re.sub(r"\$[^$]*\$", " _math_ ", s)
    s = re.sub(r"[^0-9a-zàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]+", " ", s)
    return [w for w in s.split() if len(w) > 1]


def compute_near_duplicates(all_items):
    """Find any pairs sharing very high trigram / token Jaccard on stems (sanity check)."""
    docs = []
    for kind, item in all_items:
        txt = item["stem"] if kind == "TF" else item["q"]
        toks = tokenize_vn(txt)
        shingles = set(zip(toks, toks[1:], toks[2:])) if len(toks) >= 3 else set(toks)
        docs.append((item["id"], item["topic"], txt, shingles))

    high_pairs = []
    max_j = 0.0
    n = len(docs)
    for i in range(n):
        id_i, top_i, txt_i, s_i = docs[i]
        if not s_i:
            continue
        for j in range(i + 1, n):
            id_j, top_j, txt_j, s_j = docs[j]
            if top_i != top_j:
                continue
            inter = len(s_i & s_j)
            if inter == 0:
                continue
            jacc = inter / len(s_i | s_j)
            if jacc > max_j:
                max_j = jacc
            if jacc >= 0.70:
                high_pairs.append((round(jacc, 3), id_i, id_j, txt_i[:70], txt_j[:70]))
    high_pairs.sort(reverse=True)
    return max_j, high_pairs


def build_balanced_45_mcq_schedules():
    """
    Returns list of 45 dicts: sched[e][topic][level] = count.
    Constraints:
    - Every exam has 7 basic, 7 adv, 6 hsg (= 20 MCQs) covering all 6 topics.
    - Every topic gets 1 hsg per exam (total 45 hsg/topic).
    - Every exam assigns 4 topics to size 3 (1B+1A+1H) and 2 topics to size 4:
      one "heavy basic" (2B+1A+1H) and one "heavy adv" (1B+2A+1H).
    - Topics 0,1,2 appear 8x heavy-basic and 7x heavy-adv -> total 53B, 52A, 45H!
    - Topics 3,4,5 appear 7x heavy-basic and 8x heavy-adv -> total 52B, 53A, 45H!
    """
    pairs = []
    # Build 45 ordered pairs (first=2B+1A, second=1B+2A) using exact cycle structure:
    # Repeat 7 cycles of cross-pairs:
    # (0,3), (1,4), (2,5) [x3] -> 21, plus reverse (3,0),(4,1),(5,2) -> wait let's construct explicitly & verify!
    # We need out-degree (first) = [8,8,8,7,7,7] and in-degree (second) = [7,7,7,8,8,8].
    # Partition 45 slots:
    # - 21 exams with (first in {0,1,2}, second in {3,4,5}) -> 7x each for 0,1,2 as first; 7x each for 3,4,5 as second.
    # - 18 exams with (first in {3,4,5}, second in {0,1,2}) -> 6x each for 3,4,5 as first; 6x each for 0,1,2 as second.
    # - 3 exams internal {0,1,2}: (0,1), (1,2), (2,0) -> +1 first & +1 second each for 0,1,2!
    # - 3 exams internal {3,4,5}: (3,4), (4,5), (5,3) -> +1 first & +1 second each for 3,4,5!
    # Check sums:
    # first counts: 0,1,2 get 7+1 = 8; 3,4,5 get 6+1 = 7!
    # second counts: 0,1,2 get 6+1 = 7; 3,4,5 get 7+1 = 8!
    # Total pairs = 21 + 18 + 3 + 3 = 45!!
    raw_pairs = []
    for k in range(7):
        raw_pairs.append((TOPICS[k % 3], TOPICS[3 + (k % 3)]))
        raw_pairs.append((TOPICS[(k + 1) % 3], TOPICS[3 + ((k + 2) % 3)]))
        raw_pairs.append((TOPICS[(k + 2) % 3], TOPICS[3 + ((k + 1) % 3)]))
    for k in range(6):
        raw_pairs.append((TOPICS[3 + (k % 3)], TOPICS[k % 3]))
        raw_pairs.append((TOPICS[3 + ((k + 1) % 3)], TOPICS[(k + 2) % 3]))
        raw_pairs.append((TOPICS[3 + ((k + 2) % 3)], TOPICS[(k + 1) % 3]))
    raw_pairs.extend([
        (TOPICS[0], TOPICS[1]), (TOPICS[1], TOPICS[2]), (TOPICS[2], TOPICS[0]),
        (TOPICS[3], TOPICS[4]), (TOPICS[4], TOPICS[5]), (TOPICS[5], TOPICS[3]),
    ])
    assert len(raw_pairs) == 45

    rng = random.Random(20260405)
    rng.shuffle(raw_pairs)

    sched = []
    topic_tot = {t: Counter() for t in TOPICS}
    for first_t, sec_t in raw_pairs:
        assert first_t != sec_t
        ex_plan = {}
        for t in TOPICS:
            if t == first_t:
                ex_plan[t] = {"basic": 2, "adv": 1, "hsg": 1}
            elif t == sec_t:
                ex_plan[t] = {"basic": 1, "adv": 2, "hsg": 1}
            else:
                ex_plan[t] = {"basic": 1, "adv": 1, "hsg": 1}
            for lv, c in ex_plan[t].items():
                topic_tot[t][lv] += c
        sched.append(ex_plan)

    for i, t in enumerate(TOPICS):
        exp_b, exp_a = (53, 52) if i < 3 else (52, 53)
        assert topic_tot[t]["basic"] == exp_b, (t, topic_tot[t])
        assert topic_tot[t]["adv"] == exp_a, (t, topic_tot[t])
        assert topic_tot[t]["hsg"] == 45, (t, topic_tot[t])
    return sched


def build_distinct_topic_pairs(seed):
    """Generate 45 unordered distinct pairs (t1, t2) where each of 6 topics appears exactly 15 times."""
    # Every edge in K_6 occurs 3 times: C(6,2) * 3 = 15 * 3 = 45 pairs! Degree per node = 5 * 3 = 15!
    edges = []
    for rep in range(3):
        for i in range(6):
            for j in range(i + 1, 6):
                edges.append((TOPICS[i], TOPICS[j]) if (rep + i + j) % 2 == 0 else (TOPICS[j], TOPICS[i]))
    assert len(edges) == 45
    rng = random.Random(seed)
    rng.shuffle(edges)
    deg = Counter(t for a, b in edges for t in (a, b))
    assert all(deg[t] == 15 for t in TOPICS)
    return edges


EXAM_THEMES = [
    "Đề Chuẩn Cấu Trúc Số",
    "Đề Luyện Tổng Hợp Số",
    "Đề Chuyên Đề Trọng Tâm",
    "Đề Kiểm Định Năng Lực",
    "Đề Bứt Phá Điểm Cao",
]


def main():
    mcq_by_topic_lvl = defaultdict(list)
    all_mcq = []
    for t in TOPICS:
        arr = load_js_array(f"bank_mcq_{t}.js", f"MCQ_{t.upper()}")
        assert len(arr) == 150, f"{t} has {len(arr)} MCQs"
        all_mcq.extend(arr)
        for q in arr:
            mcq_by_topic_lvl[(t, q["level"])].append(q)

    tf_all = load_js_array("bank_tf.js", "TF_BANK")
    sa_all = load_js_array("bank_sa.js", "SA_BANK")
    assert len(tf_all) == 90 and len(sa_all) == 90

    # Near-duplicate audit before packaging
    combined_for_dup = [("MCQ", q) for q in all_mcq] + [("TF", q) for q in tf_all] + [("SA", q) for q in sa_all]
    max_jacc, high_pairs = compute_near_duplicates(combined_for_dup)
    print(f"Max intra-topic stem 3-shingle Jaccard across 1,080 questions: {max_jacc:.3f}")
    if high_pairs:
        print("Warning high-similarity pairs:")
        for p in high_pairs[:10]:
            print(" ", p)

    # Interleave buckets evenly so orig questions & new subtopics spread nicely across all 45 exams
    rng = random.Random(20261127)
    for k in mcq_by_topic_lvl:
        rng.shuffle(mcq_by_topic_lvl[k])

    tf_by_topic = defaultdict(list)
    for q in tf_all:
        tf_by_topic[q["topic"]].append(q)
    for t in tf_by_topic:
        rng.shuffle(tf_by_topic[t])

    sa_by_topic = defaultdict(list)
    for q in sa_all:
        sa_by_topic[q["topic"]].append(q)
    for t in sa_by_topic:
        rng.shuffle(sa_by_topic[t])

    mcq_sched = build_balanced_45_mcq_schedules()
    tf_pairs = build_distinct_topic_pairs(seed=777)
    sa_pairs = build_distinct_topic_pairs(seed=999)

    # Adjust sa_pairs via swaps if any exam happens to have identical topic pair as TF
    for e in range(45):
        if set(sa_pairs[e]) == set(tf_pairs[e]):
            swap_idx = (e + 7) % 45
            sa_pairs[e], sa_pairs[swap_idx] = sa_pairs[swap_idx], sa_pairs[e]

    exams = []
    used_ids_per_exam = []

    lvl_order = {"basic": 0, "adv": 1, "hsg": 2}

    for e in range(45):
        mcqs_picked = []
        for t in TOPICS:
            for lv, count in mcq_sched[e][t].items():
                for _ in range(count):
                    mcqs_picked.append(mcq_by_topic_lvl[(t, lv)].pop())
        # Order within exam smoothly: basic -> adv -> hsg (mixed topics within each difficulty tier!)
        rng.shuffle(mcqs_picked)
        mcqs_picked.sort(key=lambda x: lvl_order[x["level"]])

        tf_t1, tf_t2 = tf_pairs[e]
        tfs_picked = [tf_by_topic[tf_t1].pop(), tf_by_topic[tf_t2].pop()]

        sa_t1, sa_t2 = sa_pairs[e]
        sas_picked = [sa_by_topic[sa_t1].pop(), sa_by_topic[sa_t2].pop()]

        assert len(mcqs_picked) == 20
        assert len(tfs_picked) == 2
        assert len(sas_picked) == 2
        lv_counts = Counter(x["level"] for x in mcqs_picked)
        assert lv_counts["basic"] == 7 and lv_counts["adv"] == 7 and lv_counts["hsg"] == 6, lv_counts

        ex_ids = {x["id"] for x in mcqs_picked + tfs_picked + sas_picked}
        assert len(ex_ids) == 24
        used_ids_per_exam.append(ex_ids)

        topic_counts = Counter(x["topic"] for x in mcqs_picked + tfs_picked + sas_picked)
        theme = EXAM_THEMES[e % len(EXAM_THEMES)]

        exams.append({
            "id": f"DE-{e + 1:02d}",
            "num": e + 1,
            "title": f"Đề {e + 1:02d} — {theme} #{e + 1:02d}",
            "subtitle": "20 Trắc nghiệm + 2 Đúng/Sai + 2 Trả lời ngắn • Toàn diện 6 chuyên đề",
            "durationMin": 60,
            "totalQuestions": 24,
            "maxScore": 10.0,
            "mcqIds": [x["id"] for x in mcqs_picked],
            "tfIds": [x["id"] for x in tfs_picked],
            "saIds": [x["id"] for x in sas_picked],
            "levelCounts": dict(lv_counts),
            "topicCounts": {t: topic_counts[t] for t in TOPICS},
            "part2Topics": [tf_t1, tf_t2],
            "part3Topics": [sa_t1, sa_t2],
        })

    # Verify all pools completely depleted (every 1,080 question assigned once)
    assert all(len(v) == 0 for v in mcq_by_topic_lvl.values()), "Unconsumed MCQs remain!"
    assert all(len(v) == 0 for v in tf_by_topic.values()), "Unconsumed TFs remain!"
    assert all(len(v) == 0 for v in sa_by_topic.values()), "Unconsumed SAs remain!"

    # Pairwise overlap audit across all C(45, 2) = 990 pairs
    max_overlap_cnt = 0
    total_overlap_cnt = 0
    total_pairs = 0
    for i in range(45):
        for j in range(i + 1, 45):
            ov = len(used_ids_per_exam[i] & used_ids_per_exam[j])
            total_overlap_cnt += ov
            total_pairs += 1
            if ov > max_overlap_cnt:
                max_overlap_cnt = ov

    max_overlap_pct = (max_overlap_cnt / 24.0) * 100.0
    avg_overlap_pct = ((total_overlap_cnt / total_pairs) / 24.0) * 100.0
    assert max_overlap_pct <= 5.0, f"Overlap violation: {max_overlap_pct:.2f}% > 5%"

    payload = {
        "exams": exams,
        "audit": {
            "totalExams": len(exams),
            "totalUniqueQuestions": 1080,
            "mcqCount": 900,
            "tfCount": 90,
            "saCount": 90,
            "totalPairsChecked": total_pairs,
            "maxPairwiseOverlapCount": max_overlap_cnt,
            "maxPairwiseOverlapPct": round(max_overlap_pct, 2),
            "avgPairwiseOverlapPct": round(avg_overlap_pct, 4),
            "maxIntraTopicStemJaccard": round(max_jacc, 3),
            "highSimilarityPairsCount": len(high_pairs),
        },
    }
    write_js_module("exams_data.js", "EXAMS_BUNDLE", payload)
    print(f"Verified 45 exams across {total_pairs} pairs:")
    print(f"  Max pairwise question overlap: {max_overlap_cnt}/24 ({max_overlap_pct:.2f}%) <= 5.00% PASS")
    print(f"  Avg pairwise overlap: {avg_overlap_pct:.4f}%")


if __name__ == "__main__":
    main()
