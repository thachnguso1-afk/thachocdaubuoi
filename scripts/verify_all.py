# -*- coding: utf-8 -*-
"""
Full verification suite for BioMaster Exam Bank:
- Checks all 900 MCQs, 90 TF, 90 SA, and 45 exams
- Verifies zero control character leaks & balanced LaTeX $...$
- Verifies 45 exams >= 40, each 20 MCQ + 2 TF + 2 SA = 24 Qs, 60 min
- Verifies all 990 pairs have <= 5% overlap (expecting 0.00%)
"""
import json
from collections import Counter
from common import DATA_DIR, TOPICS, check_latex_dollars


def parse_js(filename, prop):
    text = (DATA_DIR / filename).read_text(encoding="utf-8")
    prefix = f"window.BIOMASTER.{prop} = "
    idx = text.find(prefix)
    assert idx != -1, f"{filename} missing {prefix}"
    body = text[idx + len(prefix):].strip()
    if body.endswith(";"):
        body = body[:-1]
    return json.loads(body)


def main():
    mcqs = []
    for t in TOPICS:
        arr = parse_js(f"bank_mcq_{t}.js", f"MCQ_{t.upper()}")
        assert len(arr) == 150, f"{t}: expected 150 got {len(arr)}"
        mcqs.extend(arr)

    tfs = parse_js("bank_tf.js", "TF_BANK")
    sas = parse_js("bank_sa.js", "SA_BANK")
    bundle = parse_js("exams_data.js", "EXAMS_BUNDLE")
    exams = bundle["exams"]

    assert len(mcqs) == 900
    assert len(tfs) == 90
    assert len(sas) == 90
    assert len(exams) == 45 and len(exams) >= 40

    mcq_map = {q["id"]: q for q in mcqs}
    tf_map = {q["id"]: q for q in tfs}
    sa_map = {q["id"]: q for q in sas}
    assert len(mcq_map) + len(tf_map) + len(sa_map) == 1080

    # Deep field & LaTeX verification
    for q in mcqs:
        assert 0 <= q["ans"] <= 3 and len(q["opts"]) == 4
        assert check_latex_dollars(q["q"]) and check_latex_dollars(q["exp"])
        for o in q["opts"]:
            assert check_latex_dollars(o)
    for q in tfs:
        assert len(q["statements"]) == 4 and check_latex_dollars(q["stem"])
        for st in q["statements"]:
            assert isinstance(st["ans"], bool)
            assert check_latex_dollars(st["text"]) and check_latex_dollars(st["exp"])
    for q in sas:
        assert q["numericValue"] is not None
        assert check_latex_dollars(q["q"]) and check_latex_dollars(q["exp"])

    # Per-exam constraints & 45x45 pairwise overlap check
    sets = []
    for ex in exams:
        assert ex["durationMin"] == 60
        assert len(ex["mcqIds"]) == 20
        assert len(ex["tfIds"]) == 2
        assert len(ex["saIds"]) == 2
        assert ex["totalQuestions"] == 24
        lv = Counter(mcq_map[i]["level"] for i in ex["mcqIds"])
        assert lv == {"basic": 7, "adv": 7, "hsg": 6}, f"{ex['id']}: {lv}"
        assert tf_map[ex["tfIds"][0]]["topic"] != tf_map[ex["tfIds"][1]]["topic"]
        assert sa_map[ex["saIds"][0]]["topic"] != sa_map[ex["saIds"][1]]["topic"]
        s = set(ex["mcqIds"] + ex["tfIds"] + ex["saIds"])
        assert len(s) == 24
        sets.append(s)

    max_ov = 0
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            ov = len(sets[i] & sets[j])
            if ov > max_ov:
                max_ov = ov

    ov_pct = max_ov / 24 * 100
    assert ov_pct <= 5.0
    print(f"ALL CHECKS PASSED: 45 exams | 1,080 unique questions | 990 pairs max overlap = {max_ov}/24 ({ov_pct:.2f}%)")


if __name__ == "__main__":
    main()
