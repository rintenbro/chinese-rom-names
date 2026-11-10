#!/usr/bin/env python3
"""校验 entries/：schema、id 唯一、CRC 格式、素材存在、同 CRC 不多条。"""
import json, os, glob, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    from jsonschema import validate
    schema=json.load(open(os.path.join(ROOT,"schema/entry.schema.json")))
except ImportError:
    validate=None
ids=set(); crcs={}; errs=[]
for p in glob.glob(os.path.join(ROOT,"entries/*/*.json")):
    e=json.load(open(p,encoding="utf-8"))
    if validate:
        try: validate(e,schema)
        except Exception as ex: errs.append(f"{p}: {ex}")
    if e["id"] in ids: errs.append(f"dup id {e['id']}")
    ids.add(e["id"])
    for f in e["files"]:
        if len(f["crc32"])!=8 or any(c not in "0123456789ABCDEF" for c in f["crc32"]):
            errs.append(f"{p}: bad crc")
        if f["crc32"] in crcs: errs.append(f"dup crc {f['crc32']} in {p} and {crcs[f['crc32']]}")
        crcs[f["crc32"]]=p
    a=e.get("assets") or {}
    for k in ("box","title"):
        if a.get(k) and not os.path.exists(os.path.join(ROOT,a[k])): errs.append(f"{p}: missing {a[k]}")
print(f"{len(ids)} entries, {len(errs)} errors")
for x in errs[:20]: print("  ",x)
sys.exit(1 if errs else 0)
