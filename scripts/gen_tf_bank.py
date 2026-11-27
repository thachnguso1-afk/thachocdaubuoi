# -*- coding: utf-8 -*-
"""
Combines Block A (45) and Block B (45) into 90 unique True/False questions (15 per topic)
and writes C:\\Users\\User\\.gemini\\antigravity\\scratch\\biomaster-exam-bank\\data\\bank_tf.js.
"""
from collections import Counter
from common import validate_question_list, write_js_module
from tf_block_a import get_block_a
from tf_block_b import get_block_b


def build_tf_bank():
    items_a, next_idx = get_block_a()
    items_b, end_idx = get_block_b(start_idx=next_idx)
    all_items = items_a + items_b
    assert len(all_items) == 90, f"Expected 90 TF items, got {len(all_items)}"
    validate_question_list(all_items, kind="TF")
    write_js_module("bank_tf.js", "TF_BANK", all_items)
    return all_items


if __name__ == "__main__":
    res = build_tf_bank()
    print("Total TF:", len(res))
    print("By topic:", Counter(x["topic"] for x in res))
    print("By level:", Counter(x["level"] for x in res))
