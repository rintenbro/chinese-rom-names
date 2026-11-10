#!/usr/bin/env python3
"""由 entries/ 重建 index.json（含每条内容哈希）。"""
import json, os, hashlib, datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx=[]
for plat in sorted(os.listdir(os.path.join(ROOT,"entries"))):
    d=os.path.join(ROOT,"entries",plat)
    if not os.path.isdir(d): continue
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".json"): continue
        p=os.path.join(d,fn); blob=open(p,encoding="utf-8").read()
        e=json.loads(blob)
        idx.append({"id":e["id"],"layer":e["layer"],"platform":e["platform"],"group":e.get("group"),
                    "titles":e["titles"],"crc32":[f["crc32"] for f in e["files"]],
                    "assets":e.get("assets",{}),"hash":hashlib.sha256(blob.encode()).hexdigest()[:16]})
old=json.load(open(os.path.join(ROOT,"index.json"),encoding="utf-8")) if os.path.exists(os.path.join(ROOT,"index.json")) else {}
json.dump({"version":old.get("version","0.1.0"),"generated_at":datetime.datetime.now().isoformat(timespec="seconds"),
           "count":len(idx),"counts":{"verified":sum(1 for x in idx if x["layer"]=="verified"),
                                       "self":sum(1 for x in idx if x["layer"]=="self")},
           "entries":idx},open(os.path.join(ROOT,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(f"{len(idx)} entries -> index.json")
