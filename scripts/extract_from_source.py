# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

SRC = Path(r"c:\Users\User\Downloads\index (2).html")
OUT_ORIG_JSON = Path(r"C:\Users\User\.gemini\antigravity\scratch\biomaster-exam-bank\scripts\original_132.json")
OUT_THEORY_JS = Path(r"C:\Users\User\.gemini\antigravity\scratch\biomaster-exam-bank\data\theory_data.js")

text = SRC.read_text(encoding="utf-8")

# 1. Extract contentGrid inner HTML
m_grid = re.search(r'<div id="contentGrid" class="space-y-6">\s*(.*?)\s*</div>\s*</div>\s*<!-- Footer -->', text, re.DOTALL)
if not m_grid:
    raise RuntimeError("Could not find contentGrid in source HTML")
theory_html = m_grid.group(1).strip()

theory_js = (
    "window.BIOMASTER = window.BIOMASTER || {};\n"
    f"window.BIOMASTER.THEORY_HTML = {json.dumps(theory_html, ensure_ascii=False)};\n"
)
OUT_THEORY_JS.write_text(theory_js, encoding="utf-8")
print(f"Wrote {OUT_THEORY_JS} ({len(theory_html):,} chars of theory HTML)")

# 2. Extract mcqData entries
m_mcq = re.search(r'const mcqData = \[\s*(.*?)\s*\];\s*let currentTopic', text, re.DOTALL)
if not m_mcq:
    raise RuntimeError("Could not find mcqData in source HTML")

raw_block = m_mcq.group(1)
# Parse line by line: each object is on a single line starting with {id:
items = []
for line in raw_block.splitlines():
    s = line.strip()
    if not s.startswith("{id:"):
        continue
    if s.endswith(","):
        s = s[:-1]
    # Convert JS object keys to JSON
    # Keys are: id, topic, level, levelText, q, opts, ans, exp
    s_json = re.sub(r'(\{|,)\s*(id|topic|level|levelText|q|opts|ans|exp):', r'\1"\2":', s)
    obj = json.loads(s_json)
    # Clean "Câu X [Tag]: " prefix and extract subtopic if present
    q_clean = obj["q"]
    subtopic = "Tổng hợp"
    m_tag = re.match(r'^Câu\s+\d+\s*\[([^\]]+)\]:\s*(.*)$', q_clean, re.DOTALL)
    if m_tag:
        subtopic = m_tag.group(1).strip()
        q_clean = m_tag.group(2).strip()
    opts_clean = [re.sub(r'^[A-D]\.\s*', '', o.strip()) for o in obj["opts"]]
    items.append({
        "orig_id": obj["id"],
        "topic": obj["topic"],
        "level": obj["level"],
        "levelText": obj["levelText"],
        "subtopic": subtopic,
        "q": q_clean,
        "opts": opts_clean,
        "ans": obj["ans"],
        "exp": obj["exp"],
    })

assert len(items) == 132, f"Expected 132 items, got {len(items)}"
OUT_ORIG_JSON.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Extracted {len(items)} original MCQs to {OUT_ORIG_JSON}")
