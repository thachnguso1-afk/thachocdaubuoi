# -*- coding: utf-8 -*-
"""
Shared helpers and strict validation utilities for BioMaster Exam Bank.
"""
import hashlib
import json
import random
import re
from pathlib import Path

ROOT = Path(r"C:\Users\User\.gemini\antigravity\scratch\biomaster-exam-bank")
DATA_DIR = ROOT / "data"
SCRIPTS_DIR = ROOT / "scripts"

TOPICS = ["cellbio", "molecular", "cellular", "mendel", "population", "physiology"]
LEVELS = ["basic", "adv", "hsg"]
LEVEL_TEXT = {
    "basic": "🟢 Cơ bản",
    "adv": "🟡 Nâng cao",
    "hsg": "🔴 HSG Tỉnh",
}


def md_bold_to_html(text):
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text.strip())


def make_mcq(qid, topic, level, subtopic, q, opts, ans, exp, shuffle_opts=True):
    assert topic in TOPICS, f"Invalid topic {topic} in {qid}"
    assert level in LEVELS, f"Invalid level {level} in {qid}"
    assert isinstance(opts, list) and len(opts) == 4, f"Must have 4 opts in {qid}"
    assert 0 <= ans <= 3, f"Invalid ans {ans} in {qid}"
    cleaned_opts = [md_bold_to_html(re.sub(r"^[A-D]\.\s*", "", o)) for o in opts]
    assert len(set(cleaned_opts)) == 4, f"Duplicate options in {qid}: {cleaned_opts}"
    assert q.strip() and exp.strip(), f"Empty question or explanation in {qid}"

    if shuffle_opts:
        correct_text = cleaned_opts[ans]
        seed = int(hashlib.md5(qid.encode("utf-8")).hexdigest()[:8], 16)
        rng = random.Random(seed)
        rng.shuffle(cleaned_opts)
        ans = cleaned_opts.index(correct_text)

    return {
        "id": qid,
        "topic": topic,
        "level": level,
        "levelText": LEVEL_TEXT[level],
        "subtopic": subtopic,
        "q": md_bold_to_html(q),
        "opts": cleaned_opts,
        "ans": ans,
        "exp": md_bold_to_html(exp),
    }


def make_tf(qid, topic, level, subtopic, stem, statements, summary_exp=""):
    assert topic in TOPICS, f"Invalid topic {topic} in {qid}"
    assert level in LEVELS, f"Invalid level {level} in {qid}"
    assert len(statements) == 4, f"TF {qid} must have 4 statements"
    keys = ["a", "b", "c", "d"]
    formatted = []
    for idx, st in enumerate(statements):
        text, ans, exp = st
        assert isinstance(ans, bool), f"TF {qid} statement {keys[idx]} ans must be bool"
        assert text.strip() and exp.strip(), f"Empty statement/exp in {qid}"
        formatted.append({
            "key": keys[idx],
            "text": md_bold_to_html(text),
            "ans": ans,
            "exp": md_bold_to_html(exp),
        })
    return {
        "id": qid,
        "topic": topic,
        "level": level,
        "levelText": LEVEL_TEXT[level],
        "subtopic": subtopic,
        "stem": md_bold_to_html(stem),
        "statements": formatted,
        "summaryExp": md_bold_to_html(summary_exp),
    }


def make_sa(qid, topic, level, subtopic, q, answer, exp, unit_hint="Nhập kết quả dạng số (dùng dấu chấm cho phần thập phân, ví dụ: 0.25)", accepted=None, numeric_value=None, tolerance=0.0):
    assert topic in TOPICS, f"Invalid topic {topic} in {qid}"
    assert level in LEVELS, f"Invalid level {level} in {qid}"
    assert q.strip() and exp.strip(), f"Empty question or exp in {qid}"
    ans_str = str(answer).strip()
    if accepted is None:
        acc = [ans_str]
        if "." in ans_str:
            acc.append(ans_str.replace(".", ","))
            trimmed = ans_str.rstrip("0").rstrip(".")
            if trimmed and trimmed not in acc:
                acc.append(trimmed)
                acc.append(trimmed.replace(".", ","))
    else:
        acc = [str(x).strip() for x in accepted]
        if ans_str not in acc:
            acc.insert(0, ans_str)
    if numeric_value is None:
        try:
            numeric_value = float(ans_str.replace(",", "."))
        except ValueError:
            numeric_value = None
    return {
        "id": qid,
        "topic": topic,
        "level": level,
        "levelText": LEVEL_TEXT[level],
        "subtopic": subtopic,
        "q": md_bold_to_html(q),
        "unitHint": unit_hint,
        "answer": ans_str,
        "accepted": acc,
        "numericValue": numeric_value,
        "tolerance": tolerance,
        "exp": md_bold_to_html(exp),
    }


def check_latex_dollars(text):
    for bad in ("\t", "\b", "\f", "\r", "\a"):
        if bad in text:
            return False
    # Remove escaped \$ if any, count unescaped $
    stripped = text.replace(r"\$", "")
    return stripped.count("$") % 2 == 0


def validate_question_list(items, kind="MCQ"):
    seen_ids = set()
    seen_texts = set()
    for it in items:
        qid = it["id"]
        assert qid not in seen_ids, f"Duplicate ID: {qid}"
        seen_ids.add(qid)
        if kind == "MCQ":
            main_txt = it["q"]
            assert check_latex_dollars(main_txt), f"Unbalanced $ in {qid}: {main_txt}"
            for o in it["opts"]:
                assert check_latex_dollars(o), f"Unbalanced $ in opt of {qid}: {o}"
            assert check_latex_dollars(it["exp"]), f"Unbalanced $ in exp of {qid}: {it['exp']}"
        elif kind == "TF":
            main_txt = it["stem"]
            assert check_latex_dollars(main_txt), f"Unbalanced $ in {qid}: {main_txt}"
            for st in it["statements"]:
                assert check_latex_dollars(st["text"]), f"Unbalanced $ in {qid}.{st['key']}"
                assert check_latex_dollars(st["exp"]), f"Unbalanced $ in exp {qid}.{st['key']}"
        elif kind == "SA":
            main_txt = it["q"]
            assert check_latex_dollars(main_txt), f"Unbalanced $ in {qid}: {main_txt}"
            assert check_latex_dollars(it["exp"]), f"Unbalanced $ in exp {qid}"

        norm = re.sub(r"\s+", " ", main_txt.lower()).strip()
        assert norm not in seen_texts, f"Exact duplicate text in {qid}: {main_txt[:80]}"
        seen_texts.add(norm)


def write_js_module(filename, global_prop, data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / filename
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    content = (
        "window.BIOMASTER = window.BIOMASTER || {};\n"
        f"window.BIOMASTER.{global_prop} = {payload};\n"
    )
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote {out_path} ({len(data)} items, {len(content):,} bytes)")
