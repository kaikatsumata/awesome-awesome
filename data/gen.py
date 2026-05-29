#!/usr/bin/env python3
"""enriched.json から README.md と docs/research-notes.md を生成する。

鮮度マーカー(最終更新日基準):
  🟢 活発(12ヶ月以内) / 🟡 中程度(13-30ヶ月) / 🔴 停滞(30ヶ月超)
  📚 歴史的・古典(更新停止が前提のアーカイブ的コレクション) / 📦 archived
"""
import json
import datetime
import re


def gh_anchor(s):
    """GitHub(GFM)の見出しアンカー生成規則を再現する。"""
    s = s.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)  # 絵文字・記号(/()等)を除去、CJK/英数は保持
    return s.replace(" ", "-")

# 実行日を基準に鮮度を算出(GitHub Actions / ローカル定期実行で自動更新される)
TODAY = datetime.date.today()

# 表示順とラベル(絵文字)
FIELDS = [
    ("ml",      "🧠 機械学習一般 / Deep Learning"),
    ("theory",  "📐 ML理論 / 最適化"),
    ("prob",    "🎲 確率モデル / ベイズ / 因果 / 不確実性"),
    ("arch",    "🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML)"),
    ("ssl",     "🌱 自己教師あり / 表現学習 / 基盤モデル"),
    ("learn",   "🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師)"),
    ("cv",      "👁️ Computer Vision"),
    ("cg",      "🎨 Computer Graphics / 3D / レンダリング"),
    ("lowlevel","🖌️ 低レベル画像処理 / 復元 / 圧縮"),
    ("nlp",     "💬 NLP / 大規模言語モデル(LLM)"),
    ("genai",   "🖼️ 生成AI / Diffusion / 画像・動画生成"),
    ("model",   "🍌 特定モデルのプロンプト・作例コレクション"),
    ("tools",   "🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ)"),
    ("rl",      "🎮 強化学習(RL)"),
    ("mm",      "🔀 マルチモーダル / VLM / MLLM"),
    ("speech",  "🔊 音声 / オーディオ"),
    ("robot",   "🤖 ロボティクス / Embodied AI"),
    ("gnn",     "🕸️ グラフ学習(GNN) / 知識グラフ"),
    ("recsys",  "🛒 推薦システム(RecSys)"),
    ("ts",      "📈 時系列(Time Series)"),
    ("agent",   "🦾 AIエージェント / LLM Agents"),
    ("med",     "🔬 医療AI / AI for Science"),
    ("app",     "🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学)"),
    ("ad",      "🚗 自動運転(Autonomous Driving)"),
    ("safety",  "🛡️ AI安全性 / Alignment / 解釈性"),
    ("ethics",  "⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction"),
    ("eff",     "⚡ 効率化(圧縮 / 量子化 / NAS / AutoML)"),
    ("fl",      "🔐 連合学習 / プライバシー"),
    ("cl",      "♻️ 継続学習(Continual Learning)"),
    ("sys",     "🖥️ MLシステム / 学習・推論インフラ / データ基盤"),
    ("mlops",   "🛠️ MLOps / データ中心AI"),
    ("bench",   "📊 データセット / ベンチマーク"),
]
FIELD_LABEL = dict(FIELDS)

TYPE_LABEL = {
    "awesome-list": "awesome",
    "survey": "survey",
    "paper-list": "paper-list",
    "model-collection": "model",
}

# 歴史的・古典コレクション(更新停止が前提。鮮度警告の対象外)
HISTORICAL = {
    "hindupuravinash/the-gan-zoo",
    "terryum/awesome-deep-learning-papers",
    "junhyukoh/deep-reinforcement-learning-papers",
    "nightrome/really-awesome-semantic-segmentation",
    # 古いが分野の基礎として重要な定番コレクション
    "jbhuang0604/awesome-computer-vision",
    "floodsung/Deep-Learning-Papers-Reading-Roadmap",
}

d = json.load(open("data/enriched.json"))
d = {k: v for k, v in d.items() if v["status"] == "ok"}

# リダイレクトで正規名が衝突する重複を排除(先勝ち)
_seen_canon = {}
_dedup = {}
for k, v in d.items():
    canon = v["canonical"].lower()
    if canon in _seen_canon:
        continue
    _seen_canon[canon] = k
    _dedup[k] = v
d = _dedup


def months_since(p):
    dt = datetime.date.fromisoformat(p[:10])
    return (TODAY.year - dt.year) * 12 + (TODAY.month - dt.month)


def fresh_marker(k, v):
    if k in HISTORICAL:
        return "📚"
    if v["archived"]:
        return "📦"
    m = months_since(v["pushed"])
    base = "🟢" if m <= 12 else ("🟡" if m <= 30 else "🔴")
    # 査読付きサーベイ論文に基づくキュレーションは、更新が止まっていても
    # 網羅性・権威性で有用なため、停滞扱い(🟡/🔴)にせず📑で示す
    if v["type"] == "survey" and base != "🟢":
        return "📑"
    return base


def stars_fmt(n):
    if n >= 1000:
        return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)


def sort_key(item):
    # 鮮度(歴史的・archived は中庸扱い) → star数 でソート
    k, v = item
    marker = fresh_marker(k, v)
    rank = {"🟢": 0, "📑": 1, "🟡": 2, "📚": 3, "📦": 4, "🔴": 5}[marker]
    return (rank, -v["stars"])


# フィールドごとに分類
by_field = {f: [] for f, _ in FIELDS}
for k, v in d.items():
    by_field.setdefault(v["field"], []).append((k, v))

# ============ README.md ============
total = len(d)
active = sum(1 for k, v in d.items() if fresh_marker(k, v) == "🟢")
mid = sum(1 for k, v in d.items() if fresh_marker(k, v) == "🟡")
lines = []
A = lines.append
A("# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
A("> AI研究の各分野を対象に、**awesome list・survey リポジトリ・学会論文リスト・特定モデルのコレクション**を")
A("> 横断的に収集・分類した「リストのリスト(awesome-of-awesome)」です。\n")
A("CV / CG / NLP / RL をはじめ全分野を網羅し、`awesome-` を冠さない survey リポジトリ")
A("(例: [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))や、")
A("`awesome-nanobanana-pro` のような特定モデルのプロンプト・作例集も対象としています。\n")
A(f"**収録数: {total} 件** / 24 分野 ・ うち🟢活発 {active} 件、🟡中程度 {mid} 件")
A(f"(最終更新: {TODAY.isoformat()} 時点のGitHubメタデータで自動生成)\n")
A("## 凡例 / 掲載基準\n")
A("各エントリには **⭐star数** と **📅最終更新(年-月)**、および鮮度マーカーを併記しています。")
A("歴史的資料を集めたリストを除き、最終更新日・更新頻度を重視して収録・並べ替えています。\n")
A("| マーカー | 意味 |")
A("|:--:|:--|")
A("| 🟢 | 活発(直近12ヶ月以内に更新) |")
A("| 🟡 | 中程度(13〜30ヶ月) |")
A("| 🔴 | 停滞(30ヶ月超 未更新) |")
A("| 📑 | 査読付きサーベイ論文に基づくキュレーション(更新頻度より網羅性・権威性が価値。古くても有用) |")
A("| 📚 | 歴史的・古典コレクション(更新停止が前提のため鮮度対象外) |")
A("| 📦 | アーカイブ済み(read-only) |\n")
A("種別: `awesome`=キュレーションリスト / `survey`=サーベイ論文付随 / `paper-list`=論文リスト / `model`=特定モデルの作例集\n")
A("> 詳細なメタデータ・全分野の調査結果・統計は [`docs/research-notes.md`](docs/research-notes.md) を参照。\n")

# 目次
A("## 目次\n")
for f, label in FIELDS:
    if by_field.get(f):
        A(f"- [{label}](#{gh_anchor(label)}) ({len(by_field[f])})")
A("")

for f, label in FIELDS:
    items = by_field.get(f, [])
    if not items:
        continue
    A(f"\n## {label}\n")
    for k, v in sorted(items, key=sort_key):
        url = "https://github.com/" + v["canonical"]
        name = v["canonical"].split("/")[-1]
        marker = fresh_marker(k, v)
        ym = v["pushed"][:7]
        A(f"- {marker} [{name}]({url}) — {v['desc']} `{TYPE_LABEL.get(v['type'], v['type'])}` ⭐{stars_fmt(v['stars'])} · 📅{ym}")

A("\n---\n")
A("## このリポジトリについて\n")
A("- 各分野ごとに分担した調査エージェントがGitHubを横断的にサーベイし、実在を確認したリポジトリのみを収録しています。")
A("- star数・最終更新日は生成時点のGitHub APIから取得した実値です。鮮度マーカーで陳腐化を判別できます。")
A("- リンクはすべてリダイレクト解決後の正規URLに統一しています。")
A("- 調査の生データ・統計・分野別の詳細は [`docs/research-notes.md`](docs/research-notes.md) にまとめています。\n")
A("### 鮮度マーカーの自動更新\n")
A("各リストの ⭐star数・📅最終更新日・鮮度マーカーは、いつでも最新化できます。\n")
A("- **ローカル再生成**: `./scripts/refresh.sh`(`gh` 認証と `python3` が必要)を実行すると、")
A("  GitHub API からメタデータを取り直し README とノートを再生成します。cron/launchd 登録で完全自動化も可能です。")
A("- **GitHub Actions(推奨)**: [`.github/workflows/refresh-freshness.yml`](.github/workflows/refresh-freshness.yml) が")
A("  毎週月曜に自動実行され、鮮度が変化していれば README を自動コミットします(手動実行も可)。")
A("  リポジトリを GitHub にプッシュすれば追加設定なしで動作します。\n")
A("Generated with Claude Code\n")

open("README.md", "w").write("\n".join(lines))

# ============ docs/research-notes.md ============
r = []
B = r.append
B("# 調査結果ノート (Research Notes)\n")
B("本ドキュメントは [README.md](../README.md) の分類済みリストの裏付けとなる、")
B("AI研究分野の awesome list / survey / 論文リスト調査の**詳細な生データと統計**です。\n")
B(f"- 収録総数: **{total} 件**(実在確認済み)")
B(f"- 生成日: {TODAY.isoformat()}(GitHubメタデータ取得時点)")
B("- 鮮度マーカー: 🟢 ≤12ヶ月 / 🟡 13-30ヶ月 / 🔴 >30ヶ月 / 📑 査読付きサーベイ(curated) / 📚 歴史的 / 📦 archived\n")

# 統計
B("## 全体統計\n")
B("### 分野別 件数\n")
B("| 分野 | 件数 | 🟢 | 🟡 | 🔴/📦/📚 |")
B("|:--|--:|--:|--:|--:|")
for f, label in FIELDS:
    items = by_field.get(f, [])
    if not items:
        continue
    g = sum(1 for k, v in items if fresh_marker(k, v) == "🟢")
    y = sum(1 for k, v in items if fresh_marker(k, v) == "🟡")
    o = len(items) - g - y
    B(f"| {label} | {len(items)} | {g} | {y} | {o} |")
B(f"| **合計** | **{total}** | **{active}** | **{mid}** | **{total-active-mid}** |\n")

# 種別統計
B("### 種別別 件数\n")
B("| 種別 | 件数 |")
B("|:--|--:|")
tcount = {}
for v in d.values():
    tcount[v["type"]] = tcount.get(v["type"], 0) + 1
for t, c in sorted(tcount.items(), key=lambda x: -x[1]):
    B(f"| {TYPE_LABEL.get(t, t)} | {c} |")
B("")

# 分野別 詳細テーブル
B("## 分野別 詳細\n")
for f, label in FIELDS:
    items = by_field.get(f, [])
    if not items:
        continue
    B(f"\n### {label}  ({len(items)}件)\n")
    B("| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |")
    B("|:--:|:--|:--|:--|--:|:--:|:--|")
    for k, v in sorted(items, key=sort_key):
        url = "https://github.com/" + v["canonical"]
        name = v["canonical"]
        marker = fresh_marker(k, v)
        B(f"| {marker} | [{name}]({url}) | {TYPE_LABEL.get(v['type'], v['type'])} | {v['subfield']} | {v['stars']} | {v['pushed'][:7]} | {v['desc']} |")
B("")
B("---\n")
B("## 調査メモ\n")
B("- 各分野は専任の調査エージェントがWebSearch/WebFetchおよびGitHub APIで実在確認のうえ収集。")
B("- 重複(複数分野に該当するリスト)は代表分野に正規化して1件に集約。")
B("- HTTP 404 のリポジトリ(例: `steve-zeyu-zhang/Awesome-3D-Medical-Imaging-Segmentation`)は除外済み。")
B("- リダイレクト(リネーム/移管)されたリポジトリは正規 full_name に解決済み。\n")

open("docs/research-notes.md", "w").write("\n".join(r))
print("README.md と docs/research-notes.md を生成しました。")
print(f"total={total} active={active} mid={mid} stale/other={total-active-mid}")
