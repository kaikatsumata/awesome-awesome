#!/usr/bin/env python3
"""enriched.json から多言語 README と docs/research-notes.md を生成する。

生成物:
  README.md (日本語) / README.en.md / README.ko.md / README.zh-Hant.md / README.zh-Hans.md
  docs/research-notes.md (日本語・詳細メタデータ)

鮮度マーカー(最終更新日基準):
  🟢 活発(12ヶ月以内) / 🟡 中程度(13-30ヶ月) / 🔴 停滞(30ヶ月超)
  📑 査読付きサーベイ(curated, 鮮度免除) / 📚 歴史的 / 📦 archived
"""
import json
import datetime
import re
from urllib.parse import quote

TODAY = datetime.date.today()

# (lang_code, output_file, autonym)
LANGS = [
    ("ja", "README.md", "日本語"),
    ("en", "README.en.md", "English"),
    ("ko", "README.ko.md", "한국어"),
    ("zh-Hant", "README.zh-Hant.md", "繁體中文"),
    ("zh-Hans", "README.zh-Hans.md", "简体中文"),
]

# 表示順
FIELD_ORDER = [
    "ml", "theory", "prob", "arch", "ssl", "learn", "cv", "cg", "lowlevel",
    "anim", "nlp", "genai", "model", "tools", "rl", "mm", "speech", "robot",
    "gnn", "recsys", "ts", "agent", "med", "app", "ad", "safety", "ethics",
    "eff", "fl", "cl", "sys", "mlops", "bench",
]

# 分野ラベル(絵文字 + 多言語)
FIELD_I18N = {
 "ml": {"ja":"🧠 機械学習一般 / Deep Learning","en":"🧠 Machine Learning & Deep Learning","ko":"🧠 머신러닝 일반 / 딥러닝","zh-Hant":"🧠 機器學習通用 / 深度學習","zh-Hans":"🧠 机器学习通用 / 深度学习"},
 "theory": {"ja":"📐 ML理論 / 最適化","en":"📐 ML Theory & Optimization","ko":"📐 ML 이론 / 최적화","zh-Hant":"📐 ML 理論 / 最佳化","zh-Hans":"📐 ML 理论 / 优化"},
 "prob": {"ja":"🎲 確率モデル / ベイズ / 因果 / 不確実性","en":"🎲 Probabilistic / Bayesian / Causal / Uncertainty","ko":"🎲 확률 모델 / 베이지안 / 인과 / 불확실성","zh-Hant":"🎲 機率模型 / 貝氏 / 因果 / 不確定性","zh-Hans":"🎲 概率模型 / 贝叶斯 / 因果 / 不确定性"},
 "arch": {"ja":"🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML)","en":"🏗️ New Architectures (SSM/Mamba/KAN/SNN/Quantum ML)","ko":"🏗️ 새로운 아키텍처 (SSM·Mamba·KAN·SNN·양자 ML)","zh-Hant":"🏗️ 新架構 (SSM・Mamba・KAN・SNN・量子 ML)","zh-Hans":"🏗️ 新架构 (SSM・Mamba・KAN・SNN・量子 ML)"},
 "ssl": {"ja":"🌱 自己教師あり / 表現学習 / 基盤モデル","en":"🌱 Self-Supervised / Representation Learning / Foundation Models","ko":"🌱 자기지도 / 표현 학습 / 파운데이션 모델","zh-Hant":"🌱 自監督 / 表徵學習 / 基礎模型","zh-Hans":"🌱 自监督 / 表征学习 / 基础模型"},
 "learn": {"ja":"🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師)","en":"🎓 Learning Paradigms (Meta/Transfer/Few-shot/OOD/Semi-sup)","ko":"🎓 학습 패러다임 (메타/전이/퓨샷/OOD/준지도)","zh-Hant":"🎓 學習範式 (元學習/遷移/少樣本/OOD/半監督)","zh-Hans":"🎓 学习范式 (元学习/迁移/少样本/OOD/半监督)"},
 "cv": {"ja":"👁️ Computer Vision","en":"👁️ Computer Vision","ko":"👁️ 컴퓨터 비전 (Computer Vision)","zh-Hant":"👁️ 電腦視覺 (Computer Vision)","zh-Hans":"👁️ 计算机视觉 (Computer Vision)"},
 "cg": {"ja":"🎨 Computer Graphics / 3D / レンダリング","en":"🎨 Computer Graphics / 3D / Rendering","ko":"🎨 컴퓨터 그래픽스 / 3D / 렌더링","zh-Hant":"🎨 電腦圖學 / 3D / 渲染","zh-Hans":"🎨 计算机图形学 / 3D / 渲染"},
 "lowlevel": {"ja":"🖌️ 低レベル画像処理 / 復元 / 圧縮","en":"🖌️ Low-level Vision / Restoration / Compression","ko":"🖌️ 저수준 영상처리 / 복원 / 압축","zh-Hant":"🖌️ 低階影像處理 / 復原 / 壓縮","zh-Hans":"🖌️ 低层图像处理 / 复原 / 压缩"},
 "anim": {"ja":"🎬 アニメ・アニメーション・イラスト・フォント","en":"🎬 Anime / Animation / Illustration / Fonts","ko":"🎬 애니메이션 · 일러스트 · 폰트","zh-Hant":"🎬 動漫・動畫・插畫・字型","zh-Hans":"🎬 动漫・动画・插画・字体"},
 "nlp": {"ja":"💬 NLP / 大規模言語モデル(LLM)","en":"💬 NLP / Large Language Models (LLM)","ko":"💬 NLP / 대규모 언어 모델(LLM)","zh-Hant":"💬 NLP / 大型語言模型(LLM)","zh-Hans":"💬 NLP / 大语言模型(LLM)"},
 "genai": {"ja":"🖼️ 生成AI / Diffusion / 画像・動画生成","en":"🖼️ Generative AI / Diffusion / Image & Video Generation","ko":"🖼️ 생성 AI / Diffusion / 이미지·동영상 생성","zh-Hant":"🖼️ 生成式 AI / Diffusion / 影像・影片生成","zh-Hans":"🖼️ 生成式 AI / Diffusion / 图像・视频生成"},
 "model": {"ja":"🍌 特定モデルのプロンプト・作例コレクション","en":"🍌 Model-Specific Prompt & Example Collections","ko":"🍌 특정 모델 프롬프트·예시 컬렉션","zh-Hant":"🍌 特定模型的提示詞・範例集","zh-Hans":"🍌 特定模型的提示词・范例集"},
 "tools": {"ja":"🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ)","en":"🧰 Model Ecosystems & Ops Tools (MCP/LLMOps/LLM Apps)","ko":"🧰 모델 에코시스템 / 운영 도구 (MCP·LLMOps·LLM 앱)","zh-Hant":"🧰 模型生態系 / 維運工具 (MCP・LLMOps・LLM 應用)","zh-Hans":"🧰 模型生态 / 运维工具 (MCP・LLMOps・LLM 应用)"},
 "rl": {"ja":"🎮 強化学習(RL)","en":"🎮 Reinforcement Learning (RL)","ko":"🎮 강화학습(RL)","zh-Hant":"🎮 強化學習(RL)","zh-Hans":"🎮 强化学习(RL)"},
 "mm": {"ja":"🔀 マルチモーダル / VLM / MLLM","en":"🔀 Multimodal / VLM / MLLM","ko":"🔀 멀티모달 / VLM / MLLM","zh-Hant":"🔀 多模態 / VLM / MLLM","zh-Hans":"🔀 多模态 / VLM / MLLM"},
 "speech": {"ja":"🔊 音声 / オーディオ","en":"🔊 Speech / Audio","ko":"🔊 음성 / 오디오","zh-Hant":"🔊 語音 / 音訊","zh-Hans":"🔊 语音 / 音频"},
 "robot": {"ja":"🤖 ロボティクス / Embodied AI","en":"🤖 Robotics / Embodied AI","ko":"🤖 로보틱스 / Embodied AI","zh-Hant":"🤖 機器人學 / Embodied AI","zh-Hans":"🤖 机器人学 / Embodied AI"},
 "gnn": {"ja":"🕸️ グラフ学習(GNN) / 知識グラフ","en":"🕸️ Graph Learning (GNN) / Knowledge Graphs","ko":"🕸️ 그래프 학습(GNN) / 지식 그래프","zh-Hant":"🕸️ 圖學習(GNN) / 知識圖譜","zh-Hans":"🕸️ 图学习(GNN) / 知识图谱"},
 "recsys": {"ja":"🛒 推薦システム(RecSys)","en":"🛒 Recommender Systems (RecSys)","ko":"🛒 추천 시스템(RecSys)","zh-Hant":"🛒 推薦系統(RecSys)","zh-Hans":"🛒 推荐系统(RecSys)"},
 "ts": {"ja":"📈 時系列(Time Series)","en":"📈 Time Series","ko":"📈 시계열(Time Series)","zh-Hant":"📈 時間序列(Time Series)","zh-Hans":"📈 时间序列(Time Series)"},
 "agent": {"ja":"🦾 AIエージェント / LLM Agents","en":"🦾 AI Agents / LLM Agents","ko":"🦾 AI 에이전트 / LLM Agents","zh-Hant":"🦾 AI 代理 / LLM Agents","zh-Hans":"🦾 AI 智能体 / LLM Agents"},
 "med": {"ja":"🔬 医療AI / AI for Science","en":"🔬 Medical AI / AI for Science","ko":"🔬 의료 AI / AI for Science","zh-Hant":"🔬 醫療 AI / AI for Science","zh-Hans":"🔬 医疗 AI / AI for Science"},
 "app": {"ja":"🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学)","en":"🌍 Applied Domains (Code/Math/Finance/Law/Science)","ko":"🌍 응용 도메인 (Code/Math/Finance/Law/과학)","zh-Hant":"🌍 應用領域 (Code/Math/Finance/Law/科學)","zh-Hans":"🌍 应用领域 (Code/Math/Finance/Law/科学)"},
 "ad": {"ja":"🚗 自動運転(Autonomous Driving)","en":"🚗 Autonomous Driving","ko":"🚗 자율주행(Autonomous Driving)","zh-Hant":"🚗 自動駕駛(Autonomous Driving)","zh-Hans":"🚗 自动驾驶(Autonomous Driving)"},
 "safety": {"ja":"🛡️ AI安全性 / Alignment / 解釈性","en":"🛡️ AI Safety / Alignment / Interpretability","ko":"🛡️ AI 안전성 / Alignment / 해석가능성","zh-Hant":"🛡️ AI 安全 / Alignment / 可解釋性","zh-Hans":"🛡️ AI 安全 / Alignment / 可解释性"},
 "ethics": {"ja":"⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction","en":"⚖️ AI Ethics / Governance / Regulation / HCI","ko":"⚖️ AI 윤리 / 거버넌스 / 규제 / Human-AI Interaction","zh-Hant":"⚖️ AI 倫理 / 治理 / 法規 / Human-AI Interaction","zh-Hans":"⚖️ AI 伦理 / 治理 / 监管 / Human-AI Interaction"},
 "eff": {"ja":"⚡ 効率化(圧縮 / 量子化 / NAS / AutoML)","en":"⚡ Efficiency (Compression/Quantization/NAS/AutoML)","ko":"⚡ 효율화 (압축/양자화/NAS/AutoML)","zh-Hant":"⚡ 高效化 (壓縮/量化/NAS/AutoML)","zh-Hans":"⚡ 高效化 (压缩/量化/NAS/AutoML)"},
 "fl": {"ja":"🔐 連合学習 / プライバシー","en":"🔐 Federated Learning / Privacy","ko":"🔐 연합학습 / 프라이버시","zh-Hant":"🔐 聯邦學習 / 隱私","zh-Hans":"🔐 联邦学习 / 隐私"},
 "cl": {"ja":"♻️ 継続学習(Continual Learning)","en":"♻️ Continual Learning","ko":"♻️ 지속 학습(Continual Learning)","zh-Hant":"♻️ 持續學習(Continual Learning)","zh-Hans":"♻️ 持续学习(Continual Learning)"},
 "sys": {"ja":"🖥️ MLシステム / 学習・推論インフラ / データ基盤","en":"🖥️ ML Systems / Training & Inference Infra / Data","ko":"🖥️ ML 시스템 / 학습·추론 인프라 / 데이터","zh-Hant":"🖥️ ML 系統 / 訓練・推論基礎設施 / 資料","zh-Hans":"🖥️ ML 系统 / 训练・推理基础设施 / 数据"},
 "mlops": {"ja":"🛠️ MLOps / データ中心AI","en":"🛠️ MLOps / Data-Centric AI","ko":"🛠️ MLOps / 데이터 중심 AI","zh-Hant":"🛠️ MLOps / 資料中心 AI","zh-Hans":"🛠️ MLOps / 数据中心 AI"},
 "bench": {"ja":"📊 データセット / ベンチマーク","en":"📊 Datasets / Benchmarks","ko":"📊 데이터셋 / 벤치마크","zh-Hant":"📊 資料集 / 基準測試","zh-Hans":"📊 数据集 / 基准测试"},
}

TYPE_LABEL = {"awesome-list":"awesome","survey":"survey","paper-list":"paper-list","model-collection":"model"}

HISTORICAL = {
    "hindupuravinash/the-gan-zoo",
    "terryum/awesome-deep-learning-papers",
    "junhyukoh/deep-reinforcement-learning-papers",
    "nightrome/really-awesome-semantic-segmentation",
    "jbhuang0604/awesome-computer-vision",
    "floodsung/Deep-Learning-Papers-Reading-Roadmap",
}

# 非GitHubの公式proceedings・論文ポータル(付録)
PRIMARY_SOURCES = [
 ("CVF Open Access", "https://openaccess.thecvf.com/menu", {"ja":"CVPR/ICCV/WACVの公式オープンアクセス論文","en":"Official open-access papers for CVPR/ICCV/WACV","ko":"CVPR/ICCV/WACV 공식 오픈액세스 논문","zh-Hant":"CVPR/ICCV/WACV 官方開放取用論文","zh-Hans":"CVPR/ICCV/WACV 官方开放获取论文"}),
 ("ECVA / ECCV Papers", "https://www.ecva.net/papers.php", {"ja":"ECCV公式論文(ECVAオープンアクセス)","en":"Official ECCV papers (ECVA open access)","ko":"ECCV 공식 논문(ECVA 오픈액세스)","zh-Hant":"ECCV 官方論文(ECVA 開放取用)","zh-Hans":"ECCV 官方论文(ECVA 开放获取)"}),
 ("Ke-Sen Huang's Home Page", "https://kesen.realtimerendering.com/", {"ja":"SIGGRAPH等グラフィックス論文リンクの定番集","en":"The classic index of SIGGRAPH & graphics paper links","ko":"SIGGRAPH 등 그래픽스 논문 링크의 정평난 모음","zh-Hant":"SIGGRAPH 等圖學論文連結的經典彙整","zh-Hans":"SIGGRAPH 等图形学论文链接的经典汇总"}),
 ("OpenReview", "https://openreview.net/", {"ja":"ICLR/NeurIPS等の査読・採択論文","en":"Reviews and accepted papers for ICLR/NeurIPS, etc.","ko":"ICLR/NeurIPS 등 리뷰·채택 논문","zh-Hant":"ICLR/NeurIPS 等審稿與錄取論文","zh-Hans":"ICLR/NeurIPS 等审稿与录用论文"}),
 ("ACL Anthology", "https://aclanthology.org/", {"ja":"NLP(ACL/EMNLP/NAACL等)の公式論文アーカイブ","en":"Official archive of NLP papers (ACL/EMNLP/NAACL, etc.)","ko":"NLP(ACL/EMNLP/NAACL 등) 공식 논문 아카이브","zh-Hant":"NLP(ACL/EMNLP/NAACL 等)官方論文典藏","zh-Hans":"NLP(ACL/EMNLP/NAACL 等)官方论文存档"}),
 ("PMLR", "https://proceedings.mlr.press/", {"ja":"ICML/AISTATS/CoLT等の公式proceedings","en":"Official proceedings for ICML/AISTATS/CoLT, etc.","ko":"ICML/AISTATS/CoLT 등 공식 프로시딩","zh-Hant":"ICML/AISTATS/CoLT 等官方論文集","zh-Hans":"ICML/AISTATS/CoLT 等官方论文集"}),
 ("NeurIPS Proceedings", "https://papers.nips.cc/", {"ja":"NeurIPS公式proceedings","en":"Official NeurIPS proceedings","ko":"NeurIPS 공식 프로시딩","zh-Hant":"NeurIPS 官方論文集","zh-Hans":"NeurIPS 官方论文集"}),
 ("Papers with Code", "https://paperswithcode.com/", {"ja":"論文+コード+SOTAリーダーボード","en":"Papers + code + SOTA leaderboards","ko":"논문 + 코드 + SOTA 리더보드","zh-Hant":"論文 + 程式碼 + SOTA 排行榜","zh-Hans":"论文 + 代码 + SOTA 排行榜"}),
 ("DBLP", "https://dblp.org/", {"ja":"計算機科学の論文書誌データベース","en":"Bibliography database for computer science","ko":"컴퓨터과학 논문 서지 데이터베이스","zh-Hant":"電腦科學論文書目資料庫","zh-Hans":"计算机科学论文书目数据库"}),
 ("arXiv", "https://arxiv.org/", {"ja":"プレプリントサーバ(cs.LG/cs.CV/cs.CL等)","en":"Preprint server (cs.LG/cs.CV/cs.CL, etc.)","ko":"프리프린트 서버(cs.LG/cs.CV/cs.CL 등)","zh-Hant":"預印本伺服器(cs.LG/cs.CV/cs.CL 等)","zh-Hans":"预印本服务器(cs.LG/cs.CV/cs.CL 等)"}),
]

# 多言語チロー(chrome)文字列
STR = {
 "ja": {
  "tagline": "AI研究の各分野を対象に、**awesome list・survey リポジトリ・学会論文リスト・特定モデルのコレクション**を横断的に収集・分類した「リストのリスト(awesome-of-awesome)」です。",
  "example": "CV / CG / NLP / RL をはじめ全分野を網羅し、`awesome-` を冠さない survey リポジトリ(例: [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))や、`awesome-nanobanana-pro` のような特定モデルの作例集も対象としています。",
  "counts": "**収録数: {total} 件** / {nfields} 分野 ・ うち🟢活発 {active} 件、🟡中程度 {mid} 件(最終更新: {date} 時点のGitHubメタデータで自動生成)",
  "legend_h": "凡例 / 掲載基準",
  "legend_p1": "各エントリには **⭐star数** と **📅最終更新(年-月)**、および鮮度マーカーを併記しています。歴史的資料を集めたリストを除き、最終更新日・更新頻度を重視して収録・並べ替えています。",
  "legend_th": "| マーカー | 意味 |",
  "lg_green": "🟢 | 活発(直近12ヶ月以内に更新)",
  "lg_yellow": "🟡 | 中程度(13〜30ヶ月)",
  "lg_red": "🔴 | 停滞(30ヶ月超 未更新)",
  "lg_survey": "📑 | 査読付きサーベイ論文に基づくキュレーション(更新頻度より網羅性・権威性が価値。古くても有用)",
  "lg_hist": "📚 | 歴史的・古典コレクション(更新停止が前提のため鮮度対象外)",
  "lg_arch": "📦 | アーカイブ済み(read-only)",
  "type_line": "種別: `awesome`=キュレーションリスト / `survey`=サーベイ論文付随 / `paper-list`=論文リスト / `model`=特定モデルの作例集",
  "notes": "> 詳細なメタデータ・全分野の調査結果・統計は [docs/research-notes.md](docs/research-notes.md)、作成手法は [docs/best-practices.md](docs/best-practices.md) を参照(日本語)。",
  "toc_h": "目次",
  "primary_h": "公式 proceedings・論文ポータル(非GitHub)",
  "primary_p": "GitHubリポジトリではないため本体リストには含めていませんが、一次情報として有用な公式論文ポータルです。",
  "about_h": "このリポジトリについて",
  "about": [
   "各分野ごとに分担した調査エージェントがGitHubを横断的にサーベイし、実在を確認したリポジトリのみを収録しています。",
   "star数・最終更新日は生成時点のGitHub APIから取得した実値です。鮮度マーカーで陳腐化を判別できます。",
   "リンクはすべてリダイレクト解決後の正規URLに統一しています。",
   "⭐star数・📅最終更新は `./scripts/refresh.sh` または GitHub Actions(週次)で再生成・自動更新できます。",
  ],
  "license_h": "ライセンス",
  "license": "本リスト(キュレーション)は [CC0 1.0](LICENSE)(パブリックドメイン)で提供します。各リンク先リポジトリのライセンスは各自に従います。",
  "lang_label": "言語",
 },
 "en": {
  "tagline": "An *awesome-of-awesome*: a curated, categorized meta-list of **awesome lists, survey repositories, conference paper lists, and model-specific collections** across every field of AI research.",
  "example": "It covers all areas including CV / CG / NLP / RL, and also includes non-`awesome-` survey repositories (e.g. [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey)) and model-specific example collections such as `awesome-nanobanana-pro`.",
  "counts": "**{total} entries** across {nfields} fields — 🟢 {active} active, 🟡 {mid} moderate (auto-generated from GitHub metadata as of {date}).",
  "legend_h": "Legend / Inclusion criteria",
  "legend_p1": "Each entry shows its **⭐ stars** and **📅 last update (YYYY-MM)** plus a freshness marker. Except for collections of historical material, recency and update frequency are emphasized for inclusion and ordering.",
  "legend_th": "| Marker | Meaning |",
  "lg_green": "🟢 | Active (updated within 12 months)",
  "lg_yellow": "🟡 | Moderate (13–30 months)",
  "lg_red": "🔴 | Stale (no update for 30+ months)",
  "lg_survey": "📑 | Curation backed by a peer-reviewed survey paper (coverage/authority matter more than update frequency; useful even if old)",
  "lg_hist": "📚 | Historical / classic collection (frozen by design; exempt from freshness)",
  "lg_arch": "📦 | Archived (read-only)",
  "type_line": "Types: `awesome`=curated list / `survey`=companion to a survey paper / `paper-list`=paper list / `model`=model-specific examples",
  "notes": "> Detailed metadata, full results and statistics are in [docs/research-notes.md](docs/research-notes.md); the methodology is in [docs/best-practices.md](docs/best-practices.md) (Japanese).",
  "toc_h": "Table of Contents",
  "primary_h": "Official proceedings & paper portals (non-GitHub)",
  "primary_p": "Not part of the main list (they are not GitHub repositories), but useful authoritative primary sources.",
  "about_h": "About this repository",
  "about": [
   "Per-field research agents swept GitHub and only repositories verified to exist are included.",
   "Star counts and last-update dates are real values from the GitHub API at generation time; the freshness marker flags staleness.",
   "All links are normalized to the canonical URL after resolving redirects.",
   "⭐ stars and 📅 last-update can be refreshed via `./scripts/refresh.sh` or weekly GitHub Actions.",
  ],
  "license_h": "License",
  "license": "This list (the curation) is released under [CC0 1.0](LICENSE) (public domain). Linked repositories are subject to their own licenses.",
  "lang_label": "Languages",
 },
 "ko": {
  "tagline": "AI 연구 전 분야의 **awesome 리스트·survey 리포지토리·학회 논문 리스트·특정 모델 컬렉션**을 가로질러 수집·분류한 “리스트의 리스트(awesome-of-awesome)”입니다.",
  "example": "CV / CG / NLP / RL을 비롯한 전 분야를 포괄하며, `awesome-`가 붙지 않은 survey 리포지토리(예: [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))나 `awesome-nanobanana-pro` 같은 특정 모델 예시 모음도 대상으로 합니다.",
  "counts": "**총 {total}건** / {nfields}개 분야 — 🟢 활발 {active}건, 🟡 보통 {mid}건 ({date} 기준 GitHub 메타데이터로 자동 생성).",
  "legend_h": "범례 / 수록 기준",
  "legend_p1": "각 항목에는 **⭐star 수**와 **📅마지막 업데이트(년-월)**, 그리고 신선도 마커를 함께 표기합니다. 역사적 자료 모음을 제외하고는 최신성·업데이트 빈도를 중시하여 수록·정렬합니다.",
  "legend_th": "| 마커 | 의미 |",
  "lg_green": "🟢 | 활발 (최근 12개월 이내 업데이트)",
  "lg_yellow": "🟡 | 보통 (13~30개월)",
  "lg_red": "🔴 | 정체 (30개월 초과 미업데이트)",
  "lg_survey": "📑 | 피어리뷰 survey 논문 기반 큐레이션 (업데이트 빈도보다 망라성·권위가 가치, 오래돼도 유용)",
  "lg_hist": "📚 | 역사적·고전 컬렉션 (업데이트 중단 전제, 신선도 대상 외)",
  "lg_arch": "📦 | 아카이브됨 (read-only)",
  "type_line": "종류: `awesome`=큐레이션 리스트 / `survey`=survey 논문 부속 / `paper-list`=논문 리스트 / `model`=특정 모델 예시",
  "notes": "> 상세 메타데이터·전체 결과·통계는 [docs/research-notes.md](docs/research-notes.md), 작성 방법론은 [docs/best-practices.md](docs/best-practices.md) 참고(일본어).",
  "toc_h": "목차",
  "primary_h": "공식 프로시딩·논문 포털 (비-GitHub)",
  "primary_p": "GitHub 리포지토리가 아니라 본 리스트에는 포함하지 않았지만, 일차 자료로 유용한 공식 논문 포털입니다.",
  "about_h": "이 리포지토리에 대하여",
  "about": [
   "분야별 조사 에이전트가 GitHub을 가로질러 조사하고, 실재가 확인된 리포지토리만 수록했습니다.",
   "star 수·마지막 업데이트는 생성 시점의 GitHub API 실값이며, 신선도 마커로 노후화를 판별할 수 있습니다.",
   "모든 링크는 리다이렉트 해소 후의 정규 URL로 통일했습니다.",
   "⭐star·📅업데이트는 `./scripts/refresh.sh` 또는 GitHub Actions(주간)로 재생성·자동 갱신할 수 있습니다.",
  ],
  "license_h": "라이선스",
  "license": "본 리스트(큐레이션)는 [CC0 1.0](LICENSE)(퍼블릭 도메인)으로 제공합니다. 링크된 리포지토리는 각자의 라이선스를 따릅니다.",
  "lang_label": "언어",
 },
 "zh-Hant": {
  "tagline": "一份「清單的清單(awesome-of-awesome)」：橫跨 AI 研究各領域，彙整並分類 **awesome 清單、survey 倉庫、會議論文清單與特定模型合集**。",
  "example": "涵蓋 CV / CG / NLP / RL 等所有領域，也納入未冠 `awesome-` 的 survey 倉庫(例如 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))與 `awesome-nanobanana-pro` 之類的特定模型範例集。",
  "counts": "**共 {total} 筆** / {nfields} 個領域 — 🟢 活躍 {active} 筆、🟡 中等 {mid} 筆(依 {date} 的 GitHub 中繼資料自動生成)。",
  "legend_h": "圖例 / 收錄標準",
  "legend_p1": "每筆條目皆標註 **⭐star 數**與 **📅最後更新(年-月)**及新鮮度標記。除歷史資料彙整外，皆以更新時間與頻率為重收錄與排序。",
  "legend_th": "| 標記 | 意義 |",
  "lg_green": "🟢 | 活躍(近 12 個月內更新)",
  "lg_yellow": "🟡 | 中等(13〜30 個月)",
  "lg_red": "🔴 | 停滯(逾 30 個月未更新)",
  "lg_survey": "📑 | 以同行評審 survey 論文為基礎的彙整(涵蓋性與權威性勝於更新頻率，雖舊仍有用)",
  "lg_hist": "📚 | 歷史・經典合集(本即停止更新，不計新鮮度)",
  "lg_arch": "📦 | 已封存(read-only)",
  "type_line": "類型: `awesome`=精選清單 / `survey`=survey 論文附屬 / `paper-list`=論文清單 / `model`=特定模型範例",
  "notes": "> 詳細中繼資料、完整結果與統計見 [docs/research-notes.md](docs/research-notes.md)；製作方法見 [docs/best-practices.md](docs/best-practices.md)(日文)。",
  "toc_h": "目錄",
  "primary_h": "官方論文集・論文入口(非 GitHub)",
  "primary_p": "因非 GitHub 倉庫而未納入主清單，但作為一手來源十分有用的官方論文入口。",
  "about_h": "關於本倉庫",
  "about": [
   "由各領域分工的調查代理橫跨 GitHub 蒐集，僅收錄確認存在的倉庫。",
   "star 數與最後更新為生成當下 GitHub API 的實際值；新鮮度標記可判別是否過時。",
   "所有連結皆解析重新導向後統一為正規 URL。",
   "⭐star・📅更新可透過 `./scripts/refresh.sh` 或 GitHub Actions(每週)重新生成與自動更新。",
  ],
  "license_h": "授權",
  "license": "本清單(彙整本身)以 [CC0 1.0](LICENSE)(公眾領域)釋出。各連結倉庫依其各自授權。",
  "lang_label": "語言",
 },
 "zh-Hans": {
  "tagline": "一份「列表的列表(awesome-of-awesome)」：横跨 AI 研究各领域，汇整并分类 **awesome 列表、survey 仓库、会议论文列表与特定模型合集**。",
  "example": "涵盖 CV / CG / NLP / RL 等所有领域，也纳入未冠 `awesome-` 的 survey 仓库(例如 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))与 `awesome-nanobanana-pro` 之类的特定模型范例集。",
  "counts": "**共 {total} 条** / {nfields} 个领域 — 🟢 活跃 {active} 条、🟡 中等 {mid} 条(依 {date} 的 GitHub 元数据自动生成)。",
  "legend_h": "图例 / 收录标准",
  "legend_p1": "每条目均标注 **⭐star 数**与 **📅最后更新(年-月)**及新鲜度标记。除历史资料汇整外，均以更新时间与频率为重收录与排序。",
  "legend_th": "| 标记 | 含义 |",
  "lg_green": "🟢 | 活跃(近 12 个月内更新)",
  "lg_yellow": "🟡 | 中等(13〜30 个月)",
  "lg_red": "🔴 | 停滞(超 30 个月未更新)",
  "lg_survey": "📑 | 以同行评审 survey 论文为基础的汇整(覆盖性与权威性胜于更新频率，虽旧仍有用)",
  "lg_hist": "📚 | 历史・经典合集(本即停止更新，不计新鲜度)",
  "lg_arch": "📦 | 已归档(read-only)",
  "type_line": "类型: `awesome`=精选列表 / `survey`=survey 论文附属 / `paper-list`=论文列表 / `model`=特定模型范例",
  "notes": "> 详细元数据、完整结果与统计见 [docs/research-notes.md](docs/research-notes.md);制作方法见 [docs/best-practices.md](docs/best-practices.md)(日文)。",
  "toc_h": "目录",
  "primary_h": "官方论文集・论文入口(非 GitHub)",
  "primary_p": "因非 GitHub 仓库而未纳入主列表,但作为一手来源十分有用的官方论文入口。",
  "about_h": "关于本仓库",
  "about": [
   "由各领域分工的调查代理横跨 GitHub 收集,仅收录确认存在的仓库。",
   "star 数与最后更新为生成当下 GitHub API 的实际值;新鲜度标记可判别是否过时。",
   "所有链接均解析重定向后统一为规范 URL。",
   "⭐star・📅更新可通过 `./scripts/refresh.sh` 或 GitHub Actions(每周)重新生成与自动更新。",
  ],
  "license_h": "许可",
  "license": "本列表(汇整本身)以 [CC0 1.0](LICENSE)(公有领域)发布。各链接仓库遵循其各自许可。",
  "lang_label": "语言",
 },
}


def gh_anchor(s):
    s = s.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


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
    if v["type"] == "survey" and base != "🟢":
        return "📑"
    return base


def stars_fmt(n):
    return (f"{n/1000:.1f}k".replace(".0k", "k")) if n >= 1000 else str(n)


def sort_key(item):
    marker = fresh_marker(*item)
    rank = {"🟢": 0, "📑": 1, "🟡": 2, "📚": 3, "📦": 4, "🔴": 5}[marker]
    return (rank, -item[1]["stars"])


# データ読み込み + 正規名重複排除
d = json.load(open("data/enriched.json"))
d = {k: v for k, v in d.items() if v["status"] == "ok"}
_seen = {}
_dedup = {}
for k, v in d.items():
    c = v["canonical"].lower()
    if c in _seen:
        continue
    _seen[c] = k
    _dedup[k] = v
d = _dedup

# 翻訳マップ
TRANS = {}
for code, _, _ in LANGS:
    if code == "ja":
        TRANS[code] = None
    else:
        try:
            TRANS[code] = json.load(open(f"data/i18n/desc.{code}.json"))
        except FileNotFoundError:
            TRANS[code] = {}


def desc_of(k, v, lang):
    tm = TRANS[lang]
    if tm is None:
        return v["desc"]
    return tm.get(k, v["desc"])


# フィールド別に分類
by_field = {f: [] for f in FIELD_ORDER}
for k, v in d.items():
    by_field.setdefault(v["field"], []).append((k, v))

total = len(d)
active = sum(1 for k, v in d.items() if fresh_marker(k, v) == "🟢")
mid = sum(1 for k, v in d.items() if fresh_marker(k, v) == "🟡")
nfields = sum(1 for f in FIELD_ORDER if by_field.get(f))


def lang_badges(current):
    out = []
    for code, fname, autonym in LANGS:
        color = "blue" if code == current else "lightgrey"
        out.append(f"[![{autonym}](https://img.shields.io/badge/{quote(autonym)}-{color})]({fname})")
    return " ".join(out)


def render(lang):
    S = STR[lang]
    L = []
    A = L.append
    A(f"# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)\n")
    A(f"**{S['lang_label']}:** {lang_badges(lang)}\n")
    A(f"> {S['tagline']}\n")
    A(S["example"] + "\n")
    A(S["counts"].format(total=total, nfields=nfields, active=active, mid=mid, date=TODAY.isoformat()) + "\n")
    # 凡例
    A(f"## {S['legend_h']}\n")
    A(S["legend_p1"] + "\n")
    A(S["legend_th"])
    A("|:--:|:--|")
    for key in ("lg_green", "lg_yellow", "lg_red", "lg_survey", "lg_hist", "lg_arch"):
        A("| " + S[key] + " |")
    A("")
    A(S["type_line"] + "\n")
    A(S["notes"] + "\n")
    # 目次
    A(f"## {S['toc_h']}\n")
    for f in FIELD_ORDER:
        items = by_field.get(f)
        if not items:
            continue
        label = FIELD_I18N[f][lang]
        A(f"- [{label}](#{gh_anchor(label)}) ({len(items)})")
    A("")
    # 本体
    for f in FIELD_ORDER:
        items = by_field.get(f)
        if not items:
            continue
        A(f"\n## {FIELD_I18N[f][lang]}\n")
        for k, v in sorted(items, key=sort_key):
            url = "https://github.com/" + v["canonical"]
            name = v["canonical"].split("/")[-1]
            marker = fresh_marker(k, v)
            A(f"- {marker} [{name}]({url}) — {desc_of(k, v, lang)} `{TYPE_LABEL.get(v['type'], v['type'])}` ⭐{stars_fmt(v['stars'])} · 📅{v['pushed'][:7]}")
    # 公式proceedings付録
    A(f"\n## {S['primary_h']}\n")
    A(S["primary_p"] + "\n")
    for name, url, descs in PRIMARY_SOURCES:
        A(f"- [{name}]({url}) — {descs[lang]}")
    # about + license
    A(f"\n---\n")
    A(f"## {S['about_h']}\n")
    for b in S["about"]:
        A(f"- {b}")
    A(f"\n## {S['license_h']}\n")
    A(S["license"] + "\n")
    A("Generated with Claude Code\n")
    return "\n".join(L)


for code, fname, _ in LANGS:
    open(fname, "w").write(render(code))

# ============ docs/research-notes.md (日本語・詳細) ============
FIELD_LABEL_JA = {f: FIELD_I18N[f]["ja"] for f in FIELD_ORDER}
r = []
B = r.append
B("# 調査結果ノート (Research Notes)\n")
B("本ドキュメントは多言語READMEの裏付けとなる、AI研究分野の awesome list / survey / 論文リスト調査の**詳細な生データと統計**です。\n")
B(f"- 収録総数: **{total} 件**(実在確認済み)")
B(f"- 生成日: {TODAY.isoformat()}(GitHubメタデータ取得時点)")
B("- 鮮度マーカー: 🟢 ≤12ヶ月 / 🟡 13-30ヶ月 / 🔴 >30ヶ月 / 📑 査読付きサーベイ(curated) / 📚 歴史的 / 📦 archived\n")
B("## 全体統計\n")
B("### 分野別 件数\n")
B("| 分野 | 件数 | 🟢 | 🟡 | その他 |")
B("|:--|--:|--:|--:|--:|")
for f in FIELD_ORDER:
    items = by_field.get(f, [])
    if not items:
        continue
    g = sum(1 for k, v in items if fresh_marker(k, v) == "🟢")
    y = sum(1 for k, v in items if fresh_marker(k, v) == "🟡")
    B(f"| {FIELD_LABEL_JA[f]} | {len(items)} | {g} | {y} | {len(items)-g-y} |")
B(f"| **合計** | **{total}** | **{active}** | **{mid}** | **{total-active-mid}** |\n")
B("### 種別別 件数\n")
B("| 種別 | 件数 |")
B("|:--|--:|")
tcount = {}
for v in d.values():
    tcount[v["type"]] = tcount.get(v["type"], 0) + 1
for t, c in sorted(tcount.items(), key=lambda x: -x[1]):
    B(f"| {TYPE_LABEL.get(t, t)} | {c} |")
B("")
B("## 分野別 詳細\n")
for f in FIELD_ORDER:
    items = by_field.get(f, [])
    if not items:
        continue
    B(f"\n### {FIELD_LABEL_JA[f]}  ({len(items)}件)\n")
    B("| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |")
    B("|:--:|:--|:--|:--|--:|:--:|:--|")
    for k, v in sorted(items, key=sort_key):
        url = "https://github.com/" + v["canonical"]
        B(f"| {fresh_marker(k, v)} | [{v['canonical']}]({url}) | {TYPE_LABEL.get(v['type'], v['type'])} | {v['subfield']} | {v['stars']} | {v['pushed'][:7]} | {v['desc']} |")
B("")
B("---\n")
B("## 調査メモ\n")
B("- 各分野は専任の調査エージェントがWebSearch/WebFetchおよびGitHub APIで実在確認のうえ収集。")
B("- 重複(複数分野に該当)は正規名で1件に集約。リダイレクトは正規 full_name に解決。404は除外。")
B("- 説明文の多言語訳は `data/i18n/desc.<lang>.json` に保持(欠損時は日本語にフォールバック)。\n")
open("docs/research-notes.md", "w").write("\n".join(r))

print(f"生成完了: {len(LANGS)}言語のREADME + research-notes.md")
print(f"total={total} fields={nfields} active={active} mid={mid}")
