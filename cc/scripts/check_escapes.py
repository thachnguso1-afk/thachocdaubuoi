# -*- coding: utf-8 -*-
import ast
import sys
from pathlib import Path

for p_str in sys.argv[1:]:
    p = Path(p_str)
    src = p.read_text(encoding="utf-8")
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for ch, name in [("\t", "TAB"), ("\b", "BS"), ("\f", "FF"), ("\r", "CR"), ("\a", "BEL"), ("\v", "VT")]:
                if ch in node.value:
                    bad.append((node.lineno, name, repr(node.value[:80])))
    print(f"{p.name}: {len(bad)} control-char escape bugs")
    for b in bad:
        print(" ", b)
