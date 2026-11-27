# -*- coding: utf-8 -*-
import ast
import sys
from pathlib import Path

path = Path(sys.argv[1])
src = path.read_text(encoding="utf-8")
tree = ast.parse(src)

# Walk and inspect basic_new, adv_new, hsg_new list sizes by counting calls/items
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id in ("basic_new", "adv_new", "hsg_new"):
                if isinstance(node.value, ast.List):
                    print(f"{t.id} literal len: {len(node.value.elts)} (line {node.lineno})")
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        c = node.value
        if isinstance(c.func, ast.Attribute) and c.func.attr == "extend":
            if isinstance(c.func.value, ast.Name) and c.func.value.id in ("basic_new", "adv_new", "hsg_new"):
                if c.args and isinstance(c.args[0], ast.List):
                    print(f"{c.func.value.id}.extend len: {len(c.args[0].elts)} (line {node.lineno})")
