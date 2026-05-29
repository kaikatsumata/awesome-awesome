#!/usr/bin/env python3
"""repos.json の各リポジトリを gh api で補強し、enriched.json を生成する。

取得項目: 正規 full_name(リダイレクト解決)、stargazers_count、pushed_at(最終push)、
archived、404 の有無。並列実行で高速化。
"""
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

repos = json.load(open("data/repos.json"))


def fetch(item):
    full_name, meta = item
    try:
        out = subprocess.run(
            ["gh", "api", f"repos/{full_name}",
             "--jq", "{full_name:.full_name, stars:.stargazers_count, pushed:.pushed_at, archived:.archived}"],
            capture_output=True, text=True, timeout=30,
        )
        if out.returncode != 0:
            return full_name, {**meta, "status": "error", "err": out.stderr.strip()[:120]}
        data = json.loads(out.stdout)
        return full_name, {
            **meta,
            "status": "ok",
            "canonical": data["full_name"],
            "stars": data["stars"],
            "pushed": data["pushed"],
            "archived": data["archived"],
        }
    except Exception as e:
        return full_name, {**meta, "status": "exc", "err": str(e)[:120]}


results = {}
with ThreadPoolExecutor(max_workers=16) as ex:
    for full_name, enriched in ex.map(fetch, repos.items()):
        results[full_name] = enriched

json.dump(results, open("data/enriched.json", "w"), ensure_ascii=False, indent=2)

ok = [r for r in results.values() if r["status"] == "ok"]
err = [k for k, r in results.items() if r["status"] != "ok"]
print(f"total={len(results)} ok={len(ok)} error={len(err)}")
if err:
    print("ERRORS:")
    for k in err:
        print(" ", k, "->", results[k].get("err", ""))
