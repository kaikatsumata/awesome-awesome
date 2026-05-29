# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> AI研究の各分野を対象に、**awesome list・survey リポジトリ・学会論文リスト・特定モデルのコレクション**を
> 横断的に収集・分類した「リストのリスト(awesome-of-awesome)」です。

CV / CG / NLP / RL をはじめ全分野を網羅し、`awesome-` を冠さない survey リポジトリ
(例: [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))や、
`awesome-nanobanana-pro` のような特定モデルのプロンプト・作例集も対象としています。

**収録数: 896 件** / 24 分野 ・ うち🟢活発 454 件、🟡中程度 204 件
(最終更新: 2026-05-29 時点のGitHubメタデータで自動生成)

## 凡例 / 掲載基準

各エントリには **⭐star数** と **📅最終更新(年-月)**、および鮮度マーカーを併記しています。
歴史的資料を集めたリストを除き、最終更新日・更新頻度を重視して収録・並べ替えています。

| マーカー | 意味 |
|:--:|:--|
| 🟢 | 活発(直近12ヶ月以内に更新) |
| 🟡 | 中程度(13〜30ヶ月) |
| 🔴 | 停滞(30ヶ月超 未更新) |
| 📑 | 査読付きサーベイ論文に基づくキュレーション(更新頻度より網羅性・権威性が価値。古くても有用) |
| 📚 | 歴史的・古典コレクション(更新停止が前提のため鮮度対象外) |
| 📦 | アーカイブ済み(read-only) |

種別: `awesome`=キュレーションリスト / `survey`=サーベイ論文付随 / `paper-list`=論文リスト / `model`=特定モデルの作例集

> 詳細なメタデータ・全分野の調査結果・統計は [`docs/research-notes.md`](docs/research-notes.md) を参照。

## 目次

- [🧠 機械学習一般 / Deep Learning](#-機械学習一般--deep-learning) (24)
- [📐 ML理論 / 最適化](#-ml理論--最適化) (12)
- [🎲 確率モデル / ベイズ / 因果 / 不確実性](#-確率モデル--ベイズ--因果--不確実性) (17)
- [🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML)](#-新アーキテクチャssmmambakansnn量子ml) (24)
- [🌱 自己教師あり / 表現学習 / 基盤モデル](#-自己教師あり--表現学習--基盤モデル) (6)
- [🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師)](#-学習パラダイムメタ--転移--少数--ood--半教師) (27)
- [👁️ Computer Vision](#-computer-vision) (110)
- [🎨 Computer Graphics / 3D / レンダリング](#-computer-graphics--3d--レンダリング) (65)
- [🖌️ 低レベル画像処理 / 復元 / 圧縮](#-低レベル画像処理--復元--圧縮) (25)
- [💬 NLP / 大規模言語モデル(LLM)](#-nlp--大規模言語モデルllm) (98)
- [🖼️ 生成AI / Diffusion / 画像・動画生成](#-生成ai--diffusion--画像動画生成) (42)
- [🍌 特定モデルのプロンプト・作例コレクション](#-特定モデルのプロンプト作例コレクション) (21)
- [🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ)](#-モデルのエコシステム--運用ツールmcpllmopsllmアプリ) (25)
- [🎮 強化学習(RL)](#-強化学習rl) (35)
- [🔀 マルチモーダル / VLM / MLLM](#-マルチモーダル--vlm--mllm) (30)
- [🔊 音声 / オーディオ](#-音声--オーディオ) (28)
- [🤖 ロボティクス / Embodied AI](#-ロボティクス--embodied-ai) (19)
- [🕸️ グラフ学習(GNN) / 知識グラフ](#-グラフ学習gnn--知識グラフ) (35)
- [🛒 推薦システム(RecSys)](#-推薦システムrecsys) (12)
- [📈 時系列(Time Series)](#-時系列time-series) (12)
- [🦾 AIエージェント / LLM Agents](#-aiエージェント--llm-agents) (20)
- [🔬 医療AI / AI for Science](#-医療ai--ai-for-science) (41)
- [🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学)](#-ai応用ドメインcode--math--finance--law--科学) (33)
- [🚗 自動運転(Autonomous Driving)](#-自動運転autonomous-driving) (18)
- [🛡️ AI安全性 / Alignment / 解釈性](#-ai安全性--alignment--解釈性) (37)
- [⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction](#-ai倫理--ガバナンス--規制--human-ai-interaction) (7)
- [⚡ 効率化(圧縮 / 量子化 / NAS / AutoML)](#-効率化圧縮--量子化--nas--automl) (23)
- [🔐 連合学習 / プライバシー](#-連合学習--プライバシー) (7)
- [♻️ 継続学習(Continual Learning)](#-継続学習continual-learning) (7)
- [🖥️ MLシステム / 学習・推論インフラ / データ基盤](#-mlシステム--学習推論インフラ--データ基盤) (19)
- [🛠️ MLOps / データ中心AI](#-mlops--データ中心ai) (12)
- [📊 データセット / ベンチマーク](#-データセット--ベンチマーク) (5)


## 🧠 機械学習一般 / Deep Learning

- 🟢 [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) — 言語別のMLフレームワーク・ライブラリの定番キュレーションリスト `awesome` ⭐72.6k · 📅2026-05
- 🟢 [awesome-datascience](https://github.com/academic/awesome-datascience) — データサイエンスを学び実問題に適用するための定番リソース集 `awesome` ⭐29.3k · 📅2026-05
- 🟢 [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) — DLのチュートリアル・プロジェクト・コミュニティを集めた定番リスト `awesome` ⭐28.3k · 📅2025-05
- 🟢 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) — AI研究の論文執筆・推敲を支援するツール・リソース集 `awesome` ⭐26.2k · 📅2026-05
- 🟢 [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources) — 異常検知の書籍・論文・動画・ツールボックスを網羅した定番リスト `awesome` ⭐9.3k · 📅2026-03
- 🟢 [kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) — Kaggleコンペの解法・アイデアを集めたコレクション `awesome` ⭐6.4k · 📅2026-05
- 🟢 [awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) — Pythonのデータサイエンスソフトウェアを厳選したリスト `awesome` ⭐3.4k · 📅2026-04
- 🟢 [awesome-deeplearning-resources](https://github.com/endymecy/awesome-deeplearning-resources) — DLおよび深層強化学習の論文・コードを時系列で整理 `paper-list` ⭐3k · 📅2026-01
- 🟢 [paperlists](https://github.com/papercopilot/paperlists) — Paper Copilotの整形済みデータ。主要会議を年度別JSONで横断網羅し継続更新(大型) `paper-list` ⭐932 · 📅2026-02
- 🟢 [ai-deadlines](https://github.com/huggingface/ai-deadlines) — 主要AI会議の締切カウントダウン(paperswithcode版の後継、現行主流) `awesome` ⭐342 · 📅2026-05
- 🟢 [ai_papers_scrapper](https://github.com/george-gca/ai_papers_scrapper) — 主要AI会議(2017-)のPDF・著者・要旨等を会議×年度で取得するスクレイパ `paper-list` ⭐52 · 📅2026-03
- 🟢 [ICML-2025-Papers](https://github.com/DmitryRyumin/ICML-2025-Papers) — ICML 2025採択論文をコード実装リンク付きで体系化 `paper-list` ⭐37 · 📅2025-10
- 📑 [awesome-AI-tutorials-surveys](https://github.com/qingsongedu/awesome-AI-tutorials-surveys) — トップAI会議のDL/ML/DM/CV/NLP/音声のチュートリアル・サーベイ集 `survey` ⭐165 · 📅2023-02
- 🟡 [Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) — 機械学習・深層学習のチュートリアル・記事・リソースの大規模集 `awesome` ⭐17.8k · 📅2024-06
- 🟡 [Conference-Accepted-Paper-List](https://github.com/Lionelsy/Conference-Accepted-Paper-List) — 主要AI/ML/ロボティクス会議の採択論文リンクと締切情報を2015-2025で集約(活発) `paper-list` ⭐1.3k · 📅2025-01
- 🟡 [AAAI-2024-Papers](https://github.com/DmitryRyumin/AAAI-2024-Papers) — AAAI 2024の革新的研究論文を網羅したコレクション `paper-list` ⭐591 · 📅2025-01
- 🟡 [AI-Conference-Info](https://github.com/tranhungnghiep/AI-Conference-Info) — 主要AI会議40+の採択率・投稿統計・締切を年度横断で集約 `awesome` ⭐165 · 📅2024-07
- 🟡 [Conference-Paper](https://github.com/hzxwonder/Conference-Paper) — CCF-A会議の採択論文をタイトル・著者・URL・要旨付きで整理 `paper-list` ⭐8 · 📅2024-04
- 📚 [Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) — 深層学習の主要論文を学習順に整理した古典的ロードマップ `paper-list` ⭐39.5k · 📅2022-11
- 📚 [awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) — 2012〜2016年の最も引用された重要DL論文Top100 `paper-list` ⭐26.1k · 📅2024-01
- 🔴 [awesome-project-ideas](https://github.com/NirantK/awesome-project-ideas) — ML/NLP/Vision/推薦のプロジェクトアイデアを集めたリスト `awesome` ⭐9.1k · 📅2023-03
- 🔴 [awesome-ai-awesomeness](https://github.com/amusi/awesome-ai-awesomeness) — AIに関するawesomeリストを集めた『awesomeのawesome』 `awesome` ⭐979 · 📅2023-08
- 🔴 [Awesome-Paper-List](https://github.com/Doragd/Awesome-Paper-List) — NLP/CV/MLの多数の論文リスト・関連資源を集約したメタリスト `awesome` ⭐194 · 📅2022-04
- 🔴 [awesome-machine-learning-papers](https://github.com/solaris33/awesome-machine-learning-papers) — 重要なML論文・リポジトリのキュレーションリスト `paper-list` ⭐78 · 📅2017-06

## 📐 ML理論 / 最適化

- 🟢 [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) — 組合せ最適化への機械学習適用論文を36分野超で網羅(活発) `paper-list` ⭐2.1k · 📅2026-05
- 🟢 [awesome-neuro-ai-papers](https://github.com/CYHSM/awesome-neuro-ai-papers) — 深層学習と神経科学の交差領域の論文・レビュー集(活発) `paper-list` ⭐444 · 📅2026-01
- 🟢 [awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) — grokking・二重降下・宝くじ仮説等DLの経験的現象と理論の論文リスト `paper-list` ⭐401 · 📅2026-05
- 🟡 [awesome-automl-papers](https://github.com/hibayesian/awesome-automl-papers) — AutoML論文・記事・チュートリアル・プロジェクトの定番大規模リスト `paper-list` ⭐4.1k · 📅2024-06
- 🟡 [must-read-papers-for-ml](https://github.com/hurshd0/must-read-papers-for-ml) — データサイエンス・ML/DLエンジニア向けの必読論文集(古典含む) `paper-list` ⭐1.4k · 📅2023-12
- 🟡 [NeuralTangentKernel-Papers](https://github.com/kwignb/NeuralTangentKernel-Papers) — Neural Tangent Kernel(NTK)関連論文の集約リスト `paper-list` ⭐122 · 📅2025-01
- 🟡 [awesome-language-model-analysis](https://github.com/Furyton/awesome-language-model-analysis) — 言語モデルの理論・実証分析(創発能力・スケーリング則・ICL理論・grokking) `paper-list` ⭐100 · 📅2024-12
- 🟡 [awesome-bayesian-optimization](https://github.com/materials-data-facility/awesome-bayesian-optimization) — 材料科学・化学向けベイズ最適化のソフト/論文/チュートリアル集 `awesome` ⭐49 · 📅2024-04
- 🔴 [Open-L2O](https://github.com/VITA-Group/Open-L2O) — L2O手法の初の包括的ベンチマーク兼論文整理リポジトリ `paper-list` ⭐299 · 📅2023-06
- 🔴 [awesome-deep-neuroevolution](https://github.com/Alro10/awesome-deep-neuroevolution) — 深層学習に進化計算を適用するDeep Neuroevolutionのリソース集 `awesome` ⭐227 · 📅2021-04
- 🔴 [Awesome-ScalingLaws](https://github.com/RZFan525/Awesome-ScalingLaws) — LLMのスケーリング則に特化した資源集 `awesome` ⭐84 · 📅2023-04
- 🔴 [MLT-Papers](https://github.com/guoji-fu/MLT-Papers) — 機械学習理論(汎化バウンド・最適化・深層学習の数学)の論文リスト `paper-list` ⭐10 · 📅2022-02

## 🎲 確率モデル / ベイズ / 因果 / 不確実性

- 🟢 [Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) — ACM CSUR掲載サーベイ対応の拡散・スコアベース・SDE生成モデル論文分類 `survey` ⭐3.3k · 📅2025-09
- 🟢 [awesome-normalizing-flows](https://github.com/janosh/awesome-normalizing-flows) — 正規化フローの論文・実装(PyTorch/JAX/Julia)・動画を集めた代表的リスト `awesome` ⭐1.6k · 📅2026-03
- 🟢 [awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) — 分布フリー不確実性定量化(CP)の動画・論文・ライブラリを集めた充実リスト `awesome` ⭐1.2k · 📅2026-05
- 🟢 [awesome-uncertainty-deeplearning](https://github.com/ENSTA-U2IS-AI/awesome-uncertainty-deeplearning) — 深層学習の予測的不確実性推定のサーベイ・論文・コードを網羅した活発なリスト `awesome` ⭐810 · 📅2026-05
- 🟢 [awesome-flow-matching](https://github.com/dongzhuoyao/awesome-flow-matching) — フローマッチング・確率的補間関連研究をまとめた活発なリスト `awesome` ⭐675 · 📅2026-04
- 🟢 [awesome-ebm](https://github.com/yataobian/awesome-ebm) — EBMの論文・ライブラリ・チュートリアルを年代順に整理した活発なリスト `awesome` ⭐387 · 📅2026-04
- 🟡 [awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms) — 再現可能な因果推論・因果ML手法のインデックス(サーベイ論文付き) `awesome` ⭐3.3k · 📅2025-01
- 🟡 [awesome-neural-ode](https://github.com/Zymrael/awesome-neural-ode) — Neural ODE/SDE/CDE・力学系・制御・数値解法の交差領域を網羅 `awesome` ⭐1.5k · 📅2024-09
- 🟡 [Awesome-GFlowNets](https://github.com/zdhNarsil/Awesome-GFlowNets) — GFlowNetの基礎論文・応用・チュートリアルを集めた中心的リスト `awesome` ⭐500 · 📅2024-10
- 🟡 [Awesome-Optimal-Transport-in-Deep-Learning](https://github.com/changwxx/Awesome-Optimal-Transport-in-Deep-Learning) — 深層学習における最適輸送の論文・コード・資料を集約 `awesome` ⭐349 · 📅2024-05
- 🟡 [Awesome-VQVAE](https://github.com/wenhaochai/Awesome-VQVAE) — Vector Quantized VAE(VQ-VAE)とその応用に関する論文・リソース集 `awesome` ⭐330 · 📅2025-01
- 🟡 [Awesome-Causal-Discovery](https://github.com/CharonWangg/Awesome-Causal-Discovery) — 因果発見・因果表現学習にフォーカスした論文・書籍リスト `awesome` ⭐12 · 📅2023-11
- 🔴 [Awesome-VAEs](https://github.com/matthewvowels1/Awesome-VAEs) — VAE・ディスエンタングルメント・表現学習・生成モデルの論文を約900件集約 `paper-list` ⭐843 · 📅2021-07
- 🔴 [awesome-bayesian-deep-learning](https://github.com/robi56/awesome-bayesian-deep-learning) — ベイズ深層学習の論文・学位論文を年代別に整理した定番リスト `awesome` ⭐416 · 📅2017-05
- 🔴 [awesome-optimal-transport](https://github.com/kilianFatras/awesome-optimal-transport) — 機械学習向け最適輸送(OT)の論文・チュートリアル・ライブラリ・書籍集 `awesome` ⭐246 · 📅2021-05
- 🔴 [Awesome-Causal-Inference](https://github.com/matthewvowels1/Awesome-Causal-Inference) — 機械学習寄りの因果推論・因果発見論文を年代順にまとめた文献リスト `paper-list` ⭐113 · 📅2021-05
- 🔴 [awesome-gaussian-processes](https://github.com/RaulPL/awesome-gaussian-processes) — ガウス過程を学ぶための書籍・動画・ソフトウェア・論文を集約 `awesome` ⭐42 · 📅2021-07

## 🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML)

- 🟢 [awesome-kan](https://github.com/mintisan/awesome-kan) — KANのライブラリ・実装・論文・チュートリアルを網羅する事実上の標準リスト `awesome` ⭐3.2k · 📅2026-05
- 🟢 [Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) — トップ会議・誌のSNN論文とコードを継続更新 `paper-list` ⭐776 · 📅2026-03
- 🟢 [Mamba_State_Space_Model_Paper_List](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) — Mambaサーベイ付属の応用先別ペーパーリスト `paper-list` ⭐752 · 📅2025-06
- 🟢 [Awesome-Mamba-Collection](https://github.com/XiudingCai/Awesome-Mamba-Collection) — Mambaの論文・チュートリアル・実装を分野横断で網羅した代表的キュレーション `paper-list` ⭐734 · 📅2026-04
- 🟢 [Awesome-state-space-models](https://github.com/radarFudan/Awesome-state-space-models) — S4からMambaまで状態空間モデルの理論寄り論文を集めたリスト `paper-list` ⭐621 · 📅2025-11
- 🟢 [Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) — 双曲埋め込み・双曲モデル・応用の最新論文を活発に更新 `paper-list` ⭐595 · 📅2026-05
- 🟢 [awesome-snn-conference-paper](https://github.com/AXYZdong/awesome-snn-conference-paper) — SNN分野の難関会議・誌論文とコード実装をまとめたリスト `paper-list` ⭐450 · 📅2026-05
- 🟢 [Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) — LLM向け効率アーキテクチャ(線形注意・SSM・RWKV等)の大規模サーベイ `survey` ⭐407 · 📅2025-11
- 🟢 [Efficient_Attention_Survey](https://github.com/attention-survey/Efficient_Attention_Survey) — 効率的注意機構をハードウェア効率・スパース・線形等に分類したサーベイ `survey` ⭐298 · 📅2025-12
- 🟢 [Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy) — LLM時代のニューロシンボリック学習の最新動向を追うリスト `paper-list` ⭐298 · 📅2025-06
- 🟢 [Awesome_Mamba](https://github.com/xmindflow/Awesome_Mamba) — 医療画像解析におけるSSMの包括サーベイ対応リスト `survey` ⭐267 · 📅2025-07
- 🟢 [Awesome-RWKV-in-Vision](https://github.com/Yaziwel/Awesome-RWKV-in-Vision) — RWKVのコンピュータビジョン応用論文を集めたリスト `paper-list` ⭐244 · 📅2025-06
- 🟢 [Awesome-Mamba-in-Vision](https://github.com/vgthengane/Awesome-Mamba-in-Vision) — コンピュータビジョン分野のMamba論文を集約 `paper-list` ⭐36 · 📅2026-03
- 🟢 [Awesome_Modern_Hopfield_Networks](https://github.com/Event-AHU/Awesome_Modern_Hopfield_Networks) — 現代的ホップフィールドネットワークの論文リスト `paper-list` ⭐27 · 📅2026-03
- 🟢 [Awesome-Linear-Attention-Survey](https://github.com/btzyd/Awesome-Linear-Attention-Survey) — 線形注意のアルゴリズム・理論・応用・インフラを扱うサーベイ付随リスト `survey` ⭐12 · 📅2026-02
- 🟢 [KAN-Papers](https://github.com/RamtinMoslemi/KAN-Papers) — arXivから抽出したKAN論文の完全リスト `paper-list` ⭐5 · 📅2026-05
- 🟡 [awesome-quantum-machine-learning](https://github.com/krishnakumarsekar/awesome-quantum-machine-learning) — QMLの基礎・アルゴリズム・教材・プロジェクトを大規模に収集 `awesome` ⭐3.6k · 📅2024-05
- 🟡 [awesome-quantum-ml](https://github.com/artix41/awesome-quantum-ml) — 量子デバイス上で動くMLアルゴリズムの論文・資料キュレーション `paper-list` ⭐525 · 📅2024-06
- 🟡 [awesome-deeplogic](https://github.com/ccclyu/awesome-deeplogic) — NLP応用中心のニューラル記号AI論文集 `paper-list` ⭐300 · 📅2024-08
- 🟡 [awesome-snn](https://github.com/coderonion/awesome-snn) — Spike-Driven-Transformer等の公開SNN実装集 `model` ⭐233 · 📅2024-10
- 🟡 [awesome-neuromorphic-hw](https://github.com/open-neuromorphic/awesome-neuromorphic-hw) — SNNのASIC/FPGA等ニューロモルフィックハードウェア論文集 `paper-list` ⭐210 · 📅2023-11
- 📦 [awesome-fast-attention](https://github.com/Separius/awesome-fast-attention) — 効率的注意モジュールの古典的網羅リスト `awesome` ⭐1k · 📅2021-08
- 🔴 [awesome-capsule-networks](https://github.com/sekwiatkowski/awesome-capsule-networks) — Dynamic Routing/EM Routing等カプセルネットの主要論文・実装集 `awesome` ⭐975 · 📅2020-02
- 🔴 [Neural-Symbolic-and-Probabilistic-Logic-Papers](https://github.com/thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers) — ニューラル記号・確率論理の論文キュレーション `paper-list` ⭐135 · 📅2023-09

## 🌱 自己教師あり / 表現学習 / 基盤モデル

- 🟢 [awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning) — 自己教師あり学習手法の定番キュレーションリスト `awesome` ⭐6.4k · 📅2026-02
- 🟢 [Awesome-Foundation-Models](https://github.com/uncbiag/Awesome-Foundation-Models) — 視覚・言語タスク向け基盤モデルのキュレーションリスト `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-LLM-VLM-Foundation-Models](https://github.com/srebroa/Awesome-LLM-VLM-Foundation-Models) — LLM・VLM・基盤モデルのキュレーションリスト `awesome` ⭐6 · 📅2026-02
- 🟡 [awesome-contrastive-self-supervised-learning](https://github.com/asheeshcric/awesome-contrastive-self-supervised-learning) — 対照型自己教師あり学習(SimCLR/VICReg等)の論文集 `paper-list` ⭐1.3k · 📅2024-09
- 🟡 [Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) — 時系列向け自己教師あり学習(SSL4TS)の論文・コード・データ集 `paper-list` ⭐378 · 📅2024-04
- 🟡 [awesome-self-supervised-multimodal-learning](https://github.com/ys-zong/awesome-self-supervised-multimodal-learning) — 自己教師ありマルチモーダル学習のリソース(T-PAMI連動) `paper-list` ⭐278 · 📅2024-08

## 🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師)

- 🟢 [awesome-domain-adaptation](https://github.com/zhaoxin94/awesome-domain-adaptation) — ドメイン適応に関する論文・コードを集めた定番リスト `awesome` ⭐5.4k · 📅2025-12
- 🟢 [Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise) — ノイズラベル学習の論文・コード・サーベイを網羅した最大級リスト `awesome` ⭐2.7k · 📅2025-05
- 🟢 [awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) — SFDA/TTBA/TTIA/OTTA等を網羅したテスト時適応の定番リスト `awesome` ⭐1.3k · 📅2025-11
- 🟢 [Awesome-LongTailed-Learning](https://github.com/Vanint/Awesome-LongTailed-Learning) — TPAMI2023サーベイ対応。クラス再均衡/情報拡張/モジュール改善で分類 `survey` ⭐1k · 📅2025-11
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) — OOD検出と汎化のベンチマーク・論文・ライブラリを網羅 `awesome` ⭐1k · 📅2026-04
- 🟢 [awesome-multi-task-learning](https://github.com/thuml/awesome-multi-task-learning) — MTLのデータセット・コードベース・論文を集約(清華大THUML) `awesome` ⭐837 · 📅2026-03
- 🟢 [awesome-active-learning](https://github.com/baifanxxx/awesome-active-learning) — 能動学習の論文・ツール・ベンチマークを集めたリスト `awesome` ⭐799 · 📅2026-03
- 🟢 [Awesome-Multi-Task-Learning](https://github.com/WeihongLi-ac/Awesome-Multi-Task-Learning) — マルチタスク学習の最新論文を時系列整理 `paper-list` ⭐378 · 📅2026-03
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/shuolucs/Awesome-Out-Of-Distribution-Detection) — ACM CSUR 2025採択のタスク指向OOD検出サーベイに対応する論文リスト `survey` ⭐166 · 📅2026-01
- 🟢 [Awesome-OOD-VLM](https://github.com/AtsuMiyai/Awesome-OOD-VLM) — 視覚言語モデル時代の一般化OOD検出サーベイ(TMLR2025)対応リスト `survey` ⭐101 · 📅2025-06
- 📑 [Awesome-Noisy-Labels](https://github.com/songhwanjun/Awesome-Noisy-Labels) — ノイズラベル学習のサーベイに対応する論文リスト `survey` ⭐572 · 📅2023-02
- 🟡 [transferlearning](https://github.com/jindongwang/transferlearning) — 転移学習分野の最大級リポジトリ。論文・コード・データセットを網羅 `paper-list` ⭐14.3k · 📅2025-02
- 🟡 [awesome-semi-supervised-learning](https://github.com/yassouali/awesome-semi-supervised-learning) — 半教師あり学習の論文・手法をCV/NLP/生成/グラフ別に整理 `awesome` ⭐1.9k · 📅2024-05
- 🟡 [awesome-imbalanced-learning](https://github.com/ZhiningLiu1998/awesome-imbalanced-learning) — クラス不均衡/長尾学習の論文・コード・フレームワーク・ライブラリを総覧 `awesome` ⭐1.5k · 📅2025-02
- 🟡 [awesome_OpenSetRecognition_list](https://github.com/gary23ai/awesome_OpenSetRecognition_list) — オープンセット認識・OOD・オープンワールド認識の論文を集めた定番リスト `paper-list` ⭐1.2k · 📅2024-03
- 🟡 [awesome-source-free-test-time-adaptation](https://github.com/YuejiangLIU/awesome-source-free-test-time-adaptation) — テスト時適応・テスト時訓練・ソースフリードメイン適応の論文リスト `paper-list` ⭐548 · 📅2024-06
- 🟡 [Awesome-Domain-Generalization](https://github.com/junkunyuan/Awesome-Domain-Generalization) — ドメイン汎化の論文・コード・データセットを集めたリスト `awesome` ⭐532 · 📅2025-04
- 🔴 [Awesome-Meta-Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning) — メタ学習の論文・コード・書籍・動画・データセットを網羅した定番リスト `awesome` ⭐1.6k · 📅2020-11
- 🔴 [awesome-zero-shot-learning](https://github.com/sbharadwajj/awesome-zero-shot-learning) — ゼロショット学習の論文・コード・リソースを集めたキュレーション `awesome` ⭐933 · 📅2021-07
- 🔴 [awesome-curriculum-learning](https://github.com/Openning07/awesome-curriculum-learning) — カリキュラム学習の論文を検出/分割/分類/転移/RL別にタグ付け `awesome` ⭐247 · 📅2022-08
- 🔴 [Awesome-Weak-Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) — プログラム的/ルールベース弱教師あり学習の論文・リソース集 `awesome` ⭐194 · 📅2023-03
- 🔴 [awesome-distribution-shift](https://github.com/weitianxin/awesome-distribution-shift) — 分布シフトとベンチマークの論文集 `awesome` ⭐127 · 📅2023-08
- 🔴 [awesome-few-shot-learning](https://github.com/indussky8/awesome-few-shot-learning) — 標準データセット上の比較結果を含むfew-shot学習の論文キュレーション `paper-list` ⭐126 · 📅2021-10
- 🔴 [Awesome-Zero-Shot-Learning](https://github.com/WilliamYi96/Awesome-Zero-Shot-Learning) — ゼロショット学習の最新の論文・データセットの進展をまとめたリスト `paper-list` ⭐85 · 📅2022-08
- 🔴 [Awesome-Failure-Detection](https://github.com/Impression2805/Awesome-Failure-Detection) — OOD検出と誤分類検出(failure detection)を統合的に扱う論文リスト `paper-list` ⭐53 · 📅2023-10
- 🔴 [Awesome-compositional-zero-shot-learning](https://github.com/uqzhichen/Awesome-compositional-zero-shot-learning) — 構成的ゼロショット学習(属性と物体の組合せ汎化)に特化した論文リスト `paper-list` ⭐11 · 📅2022-07
- 🔴 [awsome-domain-adaptation](https://github.com/cmhungsteve/awsome-domain-adaptation) — ドメイン適応関連の論文を分類整理した広く参照される一覧 `awesome` ⭐1 · 📅2019-09

## 👁️ Computer Vision

- 🟢 [CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) — CVPR 2026の論文とオープンソースプロジェクトの大規模集約(定番) `paper-list` ⭐22.6k · 📅2026-03
- 🟢 [awesome-industrial-anomaly-detection](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) — 産業画像の異常/欠陥検出の論文・データセット集(非常に活発) `awesome` ⭐3.6k · 📅2026-05
- 🟢 [awesome-hand-pose-estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation) — 手姿勢推定/トラッキング(3D含む)の定番リスト `awesome` ⭐3.4k · 📅2025-12
- 🟢 [Awesome-Super-Resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) — 超解像関連の論文・データ・リポジトリを集約 `awesome` ⭐3.1k · 📅2026-04
- 🟢 [Awesome-Deblurring](https://github.com/subeeshvasu/Awesome-Deblurring) — 画像・動画デブラーのリソースをまとめたリスト `awesome` ⭐2.9k · 📅2025-06
- 🟢 [ICCV2025-Papers-with-Code](https://github.com/amusi/ICCV2025-Papers-with-Code) — ICCV 2025の論文とオープンソースプロジェクト集 `paper-list` ⭐2.9k · 📅2025-07
- 🟢 [Awesome-Crowd-Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) — 群衆計数の定番リスト。データセット・コード付きで活発 `awesome` ⭐2.6k · 📅2026-01
- 🟢 [awesome-multiple-object-tracking](https://github.com/luanshiyinyang/awesome-multiple-object-tracking) — MOTのレビュー論文・年別アルゴリズム・データセットを整理 `awesome` ⭐1.5k · 📅2025-10
- 🟢 [awesome-grounding](https://github.com/TheShadow29/awesome-grounding) — 画像/動画/3Dの参照表現・grounding論文集 `paper-list` ⭐1.1k · 📅2025-09
- 🟢 [SAM4MIS](https://github.com/YichiZhang98/SAM4MIS) — 医用画像セグメンテーションへのSAM応用論文・OSSの要約 `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary](https://github.com/jianzongwu/Awesome-Open-Vocabulary) — TPAMI 2024「Towards Open Vocabulary Learning: A Survey」のcompanion `survey` ⭐998 · 📅2026-05
- 🟢 [ICCV-2023-25-Papers](https://github.com/DmitryRyumin/ICCV-2023-25-Papers) — ICCV 2023-2025採択論文のキュレーション `paper-list` ⭐964 · 📅2025-11
- 🟢 [top-cvpr-2025-papers](https://github.com/SkalskiP/top-cvpr-2025-papers) — CVPR 2025の注目論文を厳選したコレクション `paper-list` ⭐877 · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary-Semantic-Segmentation](https://github.com/Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation) — オープン語彙/ゼロショットセマンティックセグメンテーション論文リスト `paper-list` ⭐875 · 📅2026-05
- 🟢 [Awesome-Referring-Image-Segmentation](https://github.com/MarkMoHR/Awesome-Referring-Image-Segmentation) — 参照画像セグメンテーションの論文・データセット集 `awesome` ⭐822 · 📅2026-01
- 🟢 [Awesome-Skeleton-based-Action-Recognition](https://github.com/firework8/Awesome-Skeleton-based-Action-Recognition) — スケルトンベース行動認識の論文を月次更新するリスト `paper-list` ⭐712 · 📅2026-05
- 🟢 [HOI-Learning-List](https://github.com/DirtyHarryLYL/HOI-Learning-List) — データセット・ベンチマーク・論文を網羅するHOI学習リスト(活発) `awesome` ⭐709 · 📅2025-10
- 🟢 [Awesome-Scene-Graph-Generation](https://github.com/ChocoWu/Awesome-Scene-Graph-Generation) — LLM/非LLM手法・2D/3D/動画を網羅する活発なシーングラフ生成リスト `awesome` ⭐670 · 📅2026-05
- 🟢 [Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC](https://github.com/Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC) — 主要会議のAIGC関連論文・コードを集約 `paper-list` ⭐664 · 📅2026-05
- 🟢 [Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation](https://github.com/zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation) — 時系列行動検出・提案生成・弱教師ありを横断的に収集 `paper-list` ⭐587 · 📅2026-05
- 🟢 [Awesome-Gaze-Estimation](https://github.com/cvlab-uob/Awesome-Gaze-Estimation) — 視線推定論文の厳選キュレーションリスト `awesome` ⭐535 · 📅2025-06
- 🟢 [Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization) — 画像ハーモナイゼーションの論文・コード・リソース集(活発) `awesome` ⭐532 · 📅2026-02
- 🟢 [Awesome-Video-Object-Segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation) — VOSの最新論文・データセット・プロジェクト集 `awesome` ⭐498 · 📅2026-05
- 🟢 [Awesome-Face-Restoration](https://github.com/TaoWangzj/Awesome-Face-Restoration) — 顔復元手法の論文・リポジトリを集めたリスト `paper-list` ⭐492 · 📅2026-03
- 🟢 [awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) — カモフラージュ/隠蔽物体検出の厳選リソース集 `awesome` ⭐477 · 📅2025-12
- 🟢 [Awesome-Object-Pose-Estimation](https://github.com/CNJianLiu/Awesome-Object-Pose-Estimation) — IJCV2026サーベイ「Deep Learning-Based Object Pose Estimation」のプロジェクトページ `survey` ⭐422 · 📅2026-01
- 🟢 [Awesome_Long_Form_Video_Understanding](https://github.com/ttengwang/Awesome_Long_Form_Video_Understanding) — 長尺動画に特化した論文・データセット集 `paper-list` ⭐377 · 📅2025-10
- 🟢 [awesome-described-object-detection](https://github.com/Charles-Xie/awesome-described-object-detection) — Described/Open-Vocabulary物体検出・参照表現理解の論文集 `paper-list` ⭐354 · 📅2025-11
- 🟢 [awesome-concealed-object-segmentation](https://github.com/ChunmingHe/awesome-concealed-object-segmentation) — 隠蔽物体セグメンテーションのリソース集 `awesome` ⭐340 · 📅2026-01
- 🟢 [Awesome-Visual-Grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) — TPAMI 2025サーベイ。REC/phrase grounding/grounding MLLMを網羅(活発) `survey` ⭐313 · 📅2025-11
- 🟢 [Awesome-3D-Visual-Grounding](https://github.com/liudaizong/Awesome-3D-Visual-Grounding) — 3D視覚grounding論文に特化(活発) `paper-list` ⭐281 · 📅2026-01
- 🟢 [Awesome-Multimodal-Referring-Segmentation](https://github.com/henghuiding/Awesome-Multimodal-Referring-Segmentation) — マルチモーダル参照セグメンテーションのリスト `awesome` ⭐249 · 📅2026-05
- 🟢 [Awesome-Gait-Recognition](https://github.com/BNU-IVC/Awesome-Gait-Recognition) — 歩容認識の論文・データセット集(CVPR'25等収録、活発) `paper-list` ⭐187 · 📅2025-05
- 🟢 [awesome-micro-expression-recognition](https://github.com/Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition) — 微表情(micro-expression)認識・検出・スポッティングの論文集 `paper-list` ⭐180 · 📅2025-08
- 🟢 [awesome-video-self-supervised-learning](https://github.com/Malitha123/awesome-video-self-supervised-learning) — 動画における自己教師あり学習手法の論文集 `paper-list` ⭐171 · 📅2026-03
- 🟢 [Awesome-SAM2](https://github.com/GuoleiSun/Awesome-SAM2) — 画像・動画向けSAM2の論文・コード集 `paper-list` ⭐149 · 📅2025-10
- 🟢 [Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference) — トップ国際会議掲載のイベント/スパイクカメラ論文集 `paper-list` ⭐118 · 📅2026-04
- 🟢 [awesome-3d-anomaly-detection](https://github.com/M-3LAB/awesome-3d-anomaly-detection) — 点群・マルチモーダル3D異常検出のサーベイリポジトリ `awesome` ⭐112 · 📅2026-05
- 🟢 [TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding](https://github.com/iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding) — MLLMを用いた動画時間的グラウンディング(VTG-LLM)の最新論文・コード・データ集 `paper-list` ⭐91 · 📅2025-11
- 🟢 [Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) — 深層画像復元/強調における事前分布のサーベイ `survey` ⭐87 · 📅2025-05
- 🟢 [Awesome-MultiModal-Visual-Object-Tracking](https://github.com/Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking) — RGBT/RGBD/RGBE等のマルチモーダル視覚物体追跡サーベイ `survey` ⭐84 · 📅2026-04
- 🟢 [awesome-human-visual-attention](https://github.com/aimagelab/awesome-human-visual-attention) — saliency・scanpath・視線予測・視覚的注意の論文/リソース集 `paper-list` ⭐66 · 📅2025-05
- 🟢 [Awesome-Temporal-Video-Grounding](https://github.com/Tangkfan/Awesome-Temporal-Video-Grounding) — VMR/TVG/TSGVの論文リスト `paper-list` ⭐39 · 📅2025-12
- 🟢 [awesome-captioning-evaluation](https://github.com/aimagelab/awesome-captioning-evaluation) — MLLM時代の画像キャプション評価に関する論文集 `paper-list` ⭐34 · 📅2025-11
- 📑 [Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) — IJCV 2023サーベイ。LiDAR/カメラ/マルチモーダル3D検出を体系化 `survey` ⭐609 · 📅2023-05
- 📑 [360_Survey](https://github.com/vlislab22/360_Survey) — 全方位ビジョン(深度推定・3D復元・セグメンテーション)の包括サーベイ `survey` ⭐23 · 📅2024-12
- 🟡 [Awesome-Transformer-Attention](https://github.com/cmhungsteve/Awesome-Transformer-Attention) — ViT/Attentionを網羅した極めて包括的な論文リスト `paper-list` ⭐5k · 📅2024-07
- 🟡 [Awesome-Visual-Transformer](https://github.com/dk-liang/Awesome-Visual-Transformer) — CV向けTransformer論文を集めたコレクション `awesome` ⭐3.6k · 📅2025-01
- 🟡 [awesome-ocr](https://github.com/kba/awesome-ocr) — OCR・手書き文字認識(HTR)のソフト・ライブラリ・文献集(歴史文書デジタル化の中核) `awesome` ⭐3.1k · 📅2024-07
- 🟡 [ECCV2024-Papers-with-Code](https://github.com/amusi/ECCV2024-Papers-with-Code) — ECCV 2024の論文とオープンソースプロジェクト集 `paper-list` ⭐2.3k · 📅2024-08
- 🟡 [SOTA-MedSeg](https://github.com/JunMa11/SOTA-MedSeg) — 各種チャレンジに基づくSOTA医用画像セグメンテーション手法集 `paper-list` ⭐1.7k · 📅2023-12
- 🟡 [Awesome-person-re-identification](https://github.com/bismex/Awesome-person-re-identification) — 教師あり/教師なし/クロスモーダルReIDを網羅した大規模論文リスト `awesome` ⭐1.3k · 📅2024-06
- 🟡 [awesome-point-cloud-registration](https://github.com/XuyangBai/awesome-point-cloud-registration) — マッチング戦略別に整理した点群レジストレーション論文集 `paper-list` ⭐946 · 📅2024-07
- 🟡 [Awesome-Computer-Vision-Paper-List](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List) — トップ会議の採択論文を横断検索できるようまとめた論文リスト `paper-list` ⭐761 · 📅2024-04
- 🟡 [Awesome-Optical-Flow](https://github.com/hzwer/Awesome-Optical-Flow) — オプティカルフローと関連研究の論文リスト `awesome` ⭐647 · 📅2024-11
- 🟡 [awesome-diffusion-models-in-low-level-vision](https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision) — 超解像/インペインティング等の低レベル視覚向け拡散モデル論文集 `paper-list` ⭐552 · 📅2025-02
- 🟡 [CVPR-2023-24-Papers](https://github.com/DmitryRyumin/CVPR-2023-24-Papers) — CVPR 2023/2024採択論文をトピック別に整理 `paper-list` ⭐451 · 📅2024-07
- 🟡 [Awesome-Image-Matting](https://github.com/wchstrife/Awesome-Image-Matting) — 深層学習ベースのマッティング論文・コード厳選リスト `awesome` ⭐438 · 📅2023-11
- 🟡 [awesome-ocr-resources](https://github.com/ZumingHuang/awesome-ocr-resources) — OCRの論文・データセットを集めたリソース集 `awesome` ⭐431 · 📅2025-01
- 🟡 [Awesome-Segment-Anything](https://github.com/Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything) — Segment Anything Model(SAM)関連の論文・プロジェクト集 `paper-list` ⭐372 · 📅2024-12
- 🟡 [awesome-temporal-action-segmentation](https://github.com/nus-cvml/awesome-temporal-action-segmentation) — 時系列行動セグメンテーションの論文・データセット集(活発) `paper-list` ⭐250 · 📅2024-04
- 🟡 [Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — 2020年以降の単眼深度推定論文に焦点を当てたリスト `paper-list` ⭐210 · 📅2024-10
- 🟡 [awesome-salient-object-detection](https://github.com/visionxiang/awesome-salient-object-detection) — RGB-D等を含む顕著性物体検出のリソース集 `awesome` ⭐147 · 📅2024-09
- 🟡 [awesome-3D-scene-graphs](https://github.com/DennisRotondi/awesome-3D-scene-graphs) — ロボティクス応用を含む3Dシーングラフ専門リスト `awesome` ⭐109 · 📅2024-12
- 🟡 [WACV-2024-Papers](https://github.com/DmitryRyumin/WACV-2024-Papers) — WACV 2024の論文を体系的に整理したコレクション `paper-list` ⭐97 · 📅2024-09
- 📚 [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) — CV全般の書籍・講義・論文・ツール・データセットを網羅した定番リスト `awesome` ⭐23.3k · 📅2024-05
- 📚 [really-awesome-semantic-segmentation](https://github.com/nightrome/really-awesome-semantic-segmentation) — セマンティックセグメンテーション論文リスト(2018で更新停止) `paper-list` ⭐404 · 📅2018-03
- 🔴 [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) — セマンティックセグメンテーションの定番リソース集 `awesome` ⭐10.8k · 📅2021-05
- 🔴 [awesome-object-detection](https://github.com/amusi/awesome-object-detection) — R-CNN系・YOLO・SSD等の物体検出論文/実装をまとめた定番リスト `awesome` ⭐7.5k · 📅2022-12
- 🔴 [awesome-Face_Recognition](https://github.com/ChanChiChoi/awesome-Face_Recognition) — 顔検出/認識/再構成/生成等を網羅した大規模論文集 `paper-list` ⭐4.7k · 📅2023-02
- 🔴 [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition) — 行動認識と関連領域のリソースを網羅した定番リスト `awesome` ⭐4k · 📅2023-05
- 🔴 [awesome-image-classification](https://github.com/weiaicunzai/awesome-image-classification) — 2014年以降の深層学習画像分類論文/実装のリスト `paper-list` ⭐3.1k · 📅2022-04
- 🔴 [awesome-deep-text-detection-recognition](https://github.com/hwalsuklee/awesome-deep-text-detection-recognition) — 深層学習ベースのテキスト検出/認識論文を整理 `paper-list` ⭐2.5k · 📅2021-08
- 🔴 [awesome-human-pose-estimation](https://github.com/cbsudux/awesome-human-pose-estimation) — 人物姿勢推定の論文・リソース集 `awesome` ⭐2.5k · 📅2022-10
- 🔴 [awesome-cbir-papers](https://github.com/willard-yuan/awesome-cbir-papers) — 古典的・代表的な内容ベース画像検索(CBIR)論文集 `paper-list` ⭐1.8k · 📅2023-10
- 🔴 [multi-object-tracking-paper-list](https://github.com/SpyderXu/multi-object-tracking-paper-list) — 多物体追跡の論文リストとソースコード集 `paper-list` ⭐1.7k · 📅2020-04
- 🔴 [Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) — シーンテキストの位置特定・認識に特化したリソース集 `awesome` ⭐1.7k · 📅2018-07
- 🔴 [awesome-tiny-object-detection](https://github.com/kuanhungchen/awesome-tiny-object-detection) — Tiny Object Detection(微小物体検出)の論文・リソース集 `paper-list` ⭐1.6k · 📅2023-10
- 🔴 [awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation) — 2D/3D人物姿勢推定の関連論文集 `paper-list` ⭐1.4k · 📅2020-08
- 🔴 [awesome-image-captioning](https://github.com/zhjohnchan/awesome-image-captioning) — 画像キャプションと関連領域のリソースを年別整理 `awesome` ⭐1.1k · 📅2023-03
- 🔴 [activityrecognition](https://github.com/jindongwang/activityrecognition) — 行動認識(activity recognition)の資料・コード・データセット集 `paper-list` ⭐930 · 📅2019-08
- 🔴 [awesome-face](https://github.com/polarisZhao/awesome-face) — 顔関連アルゴリズム・データセット・論文のキュレーション `awesome` ⭐914 · 📅2019-08
- 🔴 [Awesome-Face-Forgery-Generation-and-Detection](https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection) — 顔偽造の生成と検出に関する論文・コード集 `paper-list` ⭐780 · 📅2022-11
- 🔴 [Awesome-Temporal-Action-Localization](https://github.com/Alvin-Zeng/Awesome-Temporal-Action-Localization) — temporal action localization/detection/proposalの論文・ベンチマークまとめ `paper-list` ⭐589 · 📅2022-09
- 🔴 [awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) — 実用的なメトリック学習とその応用のキュレーション `awesome` ⭐520 · 📅2023-04
- 🔴 [Awesome-Visual-Captioning](https://github.com/forence/Awesome-Visual-Captioning) — 画像/動画キャプションとSeq2Seq学習にフォーカスした論文集 `paper-list` ⭐410 · 📅2022-11
- 🔴 [Awesome-3D-Detectors](https://github.com/Hub-Tian/Awesome-3D-Detectors) — LiDAR中心の3D検出手法の論文・コード集 `paper-list` ⭐398 · 📅2022-02
- 🔴 [Awesome-Super-Resolution](https://github.com/ptkin/Awesome-Super-Resolution) — 超解像リソースのキュレーション `awesome` ⭐386 · 📅2019-09
- 🔴 [Awesome-FAS](https://github.com/RizhaoCai/Awesome-FAS) — 顔アンチスプーフィング/PAD/liveness論文の包括的コレクション `paper-list` ⭐383 · 📅2022-08
- 🔴 [awesome-depth](https://github.com/scott89/awesome-depth) — 深度推定の出版物を集めたキュレーションリスト `paper-list` ⭐337 · 📅2020-09
- 🔴 [Awesome-generalizable-6D-object-pose](https://github.com/liuyuan-pal/Awesome-generalizable-6D-object-pose) — 汎化可能な6DoF物体姿勢推定の最新論文集 `paper-list` ⭐328 · 📅2023-04
- 🔴 [Awesome-Vision-Transformer-Collection](https://github.com/GuanRunwei/Awesome-Vision-Transformer-Collection) — ViTの派生と下流タスクをまとめたコレクション `awesome` ⭐256 · 📅2022-07
- 🔴 [Awesome-Fine-grained-Visual-Classification](https://github.com/haoweiz23/Awesome-Fine-grained-Visual-Classification) — 細粒度視覚分類(FGVC)の論文コレクション `paper-list` ⭐241 · 📅2023-09
- 🔴 [Awesome-Person-Re-Identification](https://github.com/FDU-VTS/Awesome-Person-Re-Identification) — データセットとサーベイを含む人物再同定リスト `awesome` ⭐205 · 📅2021-12
- 🔴 [6d-object-pose-estimation](https://github.com/GeorgeDu/6d-object-pose-estimation) — 6D物体姿勢推定の論文・コードまとめ `paper-list` ⭐204 · 📅2023-06
- 🔴 [awesome-optical-flow-algorithm](https://github.com/antran89/awesome-optical-flow-algorithm) — 古典手法からRAFT等の深層学習までのフローアルゴリズム集 `awesome` ⭐159 · 📅2022-10
- 🔴 [awesome-video-understanding](https://github.com/sujiongming/awesome-video-understanding) — 動画分類・行動認識・動画データセットのリソース集 `awesome` ⭐143 · 📅2017-12
- 🔴 [Awesome-Video-Captioning](https://github.com/tgc1997/Awesome-Video-Captioning) — 動画キャプション生成の論文集 `paper-list` ⭐121 · 📅2021-01
- 🔴 [awesome-360-vision](https://github.com/hsientzucheng/awesome-360-vision) — 360度ビジョン全般の論文集 `paper-list` ⭐121 · 📅2019-01
- 🔴 [Awesome-3D-Semantic-Segmentation](https://github.com/vvincenttttt/Awesome-3D-Semantic-Segmentation) — 3Dセマンティックセグメンテーションの論文・コード集 `paper-list` ⭐74 · 📅2022-09
- 🔴 [Awesome-Events-Deep-Learning](https://github.com/vlislab2022/Awesome-Events-Deep-Learning) — イベントカメラ向け深層学習リソース集 `awesome` ⭐62 · 📅2023-09
- 🔴 [awesome-vqa-latest](https://github.com/Taaccoo/awesome-vqa-latest) — VQA論文を継続更新する読書リスト `paper-list` ⭐53 · 📅2022-08
- 🔴 [awesome-rec](https://github.com/daqingliu/awesome-rec) — Referring Expression Comprehension(REC)専用の論文リスト `paper-list` ⭐46 · 📅2021-05
- 🔴 [awesome-image-retrieval-papers](https://github.com/lgbwust/awesome-image-retrieval-papers) — 画像検索論文・実装の包括的コレクション `paper-list` ⭐36 · 📅2018-12
- 🔴 [TSGV-Learning-List](https://github.com/Huntersxsx/TSGV-Learning-List) — TSGV/NLVL/VMRの関連研究まとめ `paper-list` ⭐31 · 📅2022-03
- 🔴 [awesome-computer-vision-papers](https://github.com/tzxiang/awesome-computer-vision-papers) — CVと深層学習に関する論文・リソースのリスト `awesome` ⭐26 · 📅2020-09
- 🔴 [awesome-hyperspectral-image-classification](https://github.com/immortal13/awesome-hyperspectral-image-classification) — ハイパースペクトル画像分類の論文・コード集 `paper-list` ⭐20 · 📅2023-07
- 🔴 [Awesome-image-captioning](https://github.com/luo3300612/Awesome-image-captioning) — ICCV/ECCV/CVPR等の画像キャプション論文リスト `paper-list` ⭐8 · 📅2019-09
- 🔴 [Awesome-3D-Human-Pose-Estimation](https://github.com/bsridatta/Awesome-3D-Human-Pose-Estimation) — 3D人物姿勢推定に特化した論文コレクション `paper-list` ⭐5 · 📅2021-04
- 🔴 [Awesome-Human-Object-Interaction-Detection](https://github.com/KainingYing/Awesome-Human-Object-Interaction-Detection) — 会議・年次別のHOI検出論文集 `paper-list` ⭐3 · 📅2021-08

## 🎨 Computer Graphics / 3D / レンダリング

- 🟢 [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) — 3DGSの論文・実装・ビューア・ツールを集めた包括リスト `awesome` ⭐8.7k · 📅2026-05
- 🟢 [awesome-neural-rendering](https://github.com/weihaox/awesome-neural-rendering) — ニューラルレンダリングと微分可能レンダリングの資料集 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — 暗黙表現・NeRF・3DGSを用いたSLAM論文集 `paper-list` ⭐2k · 📅2026-05
- 🟢 [awesome-digital-human](https://github.com/weihaox/awesome-digital-human) — 2D/3D/4D人体モデリング・アバター生成の総合集 `awesome` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis) — トーキングフェイス合成の広範な資源集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion) — 3D生成向け拡散モデル論文集 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing) — 点群処理のライブラリ・ソフト・資料集 `awesome` ⭐797 · 📅2025-11
- 🟢 [awesome-dust3r](https://github.com/ruili3/awesome-dust3r) — DUSt3R系の幾何基盤モデル論文・資源追跡 `model` ⭐792 · 📅2025-11
- 🟢 [Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D) — AIGC 3D(生成・テクスチャ・素材)論文集 `awesome` ⭐776 · 📅2026-05
- 🟢 [awesome-ray-tracing](https://github.com/dannyfritz/awesome-ray-tracing) — レイトレーシングの論文・コース・実装リスト `awesome` ⭐656 · 📅2025-10
- 🟢 [Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — Text-to-3D/Diffusion-to-3D研究のキュレーション `paper-list` ⭐587 · 📅2026-05
- 🟢 [awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) — 3Dグラフィックスライブラリのキュレーション `awesome` ⭐525 · 📅2026-05
- 🟢 [Awesome-4D-Spatial-Intelligence](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) — 動画からの4D空間知能復元のサーベイ `survey` ⭐497 · 📅2026-05
- 🟢 [awesome-simulation](https://github.com/Housz/awesome-simulation) — CGの物理シミュレーション資源整理 `awesome` ⭐388 · 📅2026-03
- 🟢 [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) — arXivから毎日自動更新される3DGS論文追跡 `paper-list` ⭐287 · 📅2026-05
- 🟢 [Awesome-Transformer-based-SLAM](https://github.com/KwanWaiPang/Awesome-Transformer-based-SLAM) — Transformerベースの SLAM のサーベイ用論文集 `survey` ⭐270 · 📅2026-05
- 🟢 [Awesome-3DGS-SLAM](https://github.com/KwanWaiPang/Awesome-3DGS-SLAM) — 3DGS SLAMのサーベイ用論文集 `survey` ⭐261 · 📅2026-02
- 🟢 [Awesome-Learning-based-VO-VIO](https://github.com/KwanWaiPang/Awesome-Learning-based-VO-VIO) — 学習ベースの視覚オドメトリ(VO/VIO)のサーベイ用論文集 `survey` ⭐195 · 📅2026-04
- 🟢 [awesome-geometry-processing](https://github.com/zishun/awesome-geometry-processing) — 幾何処理のライブラリ・ツール・資料集 `awesome` ⭐171 · 📅2026-03
- 🟢 [Awesome-SIGGRAPH-Computational-Optics](https://github.com/zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics) — SIGGRAPH掲載の計算光学論文の読書リスト `paper-list` ⭐104 · 📅2026-04
- 🟢 [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation) — 3D復元・生成の論文・データセット集 `paper-list` ⭐78 · 📅2026-03
- 🟢 [awesome-dynamic-NeRF](https://github.com/pdaicode/awesome-dynamic-NeRF) — 動的シーン向けNeRFの論文集 `paper-list` ⭐67 · 📅2026-04
- 🟢 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey) — クワッドメッシング関連の論文・コード・プロジェクト集 `survey` ⭐34 · 📅2026-05
- 🟢 [Awesome-Diffusion-based-SLAM](https://github.com/KwanWaiPang/Awesome-Diffusion-based-SLAM) — 拡散モデルベースのSLAMのサーベイ用論文集 `survey` ⭐34 · 📅2026-05
- 🟢 [awesome-brep-reconstruction](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) — B-rep(境界表現)再構成の論文とOSSプロジェクト集。定期更新 `survey` ⭐29 · 📅2026-01
- 🟢 [Awesome-Event-based-SLAM](https://github.com/KwanWaiPang/Awesome-Event-based-SLAM) — イベントベースSLAMのサーベイ用論文集 `survey` ⭐21 · 📅2026-01
- 🟢 [offset-mesh-survey](https://github.com/Bigger-and-Stronger/offset-mesh-survey) — オフセットメッシュ生成に関する論文・プロジェクト・コードの継続更新サーベイ `survey` ⭐13 · 📅2026-05
- 🟢 [awesome-3d-medial-axis](https://github.com/Bigger-and-Stronger/awesome-3d-medial-axis) — 中心軸(medial axis)/スケルトンとその応用の論文・OSS集。定期更新 `survey` ⭐5 · 📅2025-10
- 🟢 [direction-field-survey](https://github.com/Bigger-and-Stronger/direction-field-survey) — 方向場(direction field)に関する論文・プロジェクト・コードの継続更新サーベイ `survey` ⭐4 · 📅2026-05
- 🟢 [parameterization-survey](https://github.com/Bigger-and-Stronger/parameterization-survey) — メッシュパラメータ化に関する論文・プロジェクト・コードの継続更新サーベイ `survey` ⭐2 · 📅2026-05
- 📑 [Gen3D](https://github.com/weihaox/Gen3D) — 深層生成的3D-aware画像合成のサーベイ(CSUR 2023) `survey` ⭐164 · 📅2025-02
- 📑 [boundary-layer-generation-survey](https://github.com/Bigger-and-Stronger/boundary-layer-generation-survey) — 境界層メッシュ生成に関する論文・プロジェクト・コードの継続更新サーベイ `survey` ⭐3 · 📅2025-02
- 🟡 [3D-Machine-Learning](https://github.com/timzhang642/3D-Machine-Learning) — 3D機械学習(点群/メッシュ/ボクセル/SDF等)のリソースリポジトリ `awesome` ⭐10.2k · 📅2024-07
- 🟡 [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) — Neural Radiance Fields論文の定番キュレーションリスト `awesome` ⭐6.8k · 📅2025-01
- 🟡 [awesome-implicit-representations](https://github.com/vsitzmann/awesome-implicit-representations) — DeepSDF等の暗黙的ニューラル表現の資料集 `awesome` ⭐2.6k · 📅2024-02
- 🟡 [awesome-point-cloud-analysis-2023](https://github.com/NUAAXQ/awesome-point-cloud-analysis-2023) — 2017年以降の点群解析論文を日次更新するリスト `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-Talking-Face](https://github.com/JosephPai/Awesome-Talking-Face) — トーキングフェイス専門のキュレーション `awesome` ⭐1.5k · 📅2024-12
- 🟡 [awesome-3d-reconstruction-papers](https://github.com/bluestyle97/awesome-3d-reconstruction-papers) — 深層学習時代の3D復元論文集 `paper-list` ⭐910 · 📅2023-12
- 🟡 [awesome-taichi](https://github.com/taichi-dev/awesome-taichi) — Taichi製シミュレーション(流体・布等)アプリ集 `awesome` ⭐683 · 📅2024-06
- 🟡 [awesome-3dbody-papers](https://github.com/3DFaceBody/awesome-3dbody-papers) — 3D人体(SMPL等)の論文集 `paper-list` ⭐661 · 📅2024-01
- 🟡 [Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) — 学習ベースMVS論文のリスト `paper-list` ⭐634 · 📅2023-11
- 🟡 [awesome-4d-generation](https://github.com/cwchenwang/awesome-4d-generation) — 4D生成(text-to-4D等)論文リスト `paper-list` ⭐331 · 📅2024-10
- 🟡 [Awesome-Avatars](https://github.com/pansanity666/Awesome-Avatars) — 人間アバターの生成・復元・編集の最新進展 `paper-list` ⭐276 · 📅2024-04
- 🟡 [Awesome-Inverse-Rendering](https://github.com/ingra14m/Awesome-Inverse-Rendering) — neural field基盤の逆レンダリング論文集 `paper-list` ⭐258 · 📅2024-12
- 🟡 [Awesome-InverseRendering](https://github.com/tkuri/Awesome-InverseRendering) — 内在分解・逆レンダリング論文リスト `paper-list` ⭐233 · 📅2025-04
- 🟡 [awesome-3dgs](https://github.com/pdaicode/awesome-3dgs) — 3DGS関連論文のキュレーション `paper-list` ⭐122 · 📅2024-08
- 🟡 [awesome-avatar](https://github.com/Jason-cs18/awesome-avatar) — talking-face/talking-body関連資源集 `awesome` ⭐59 · 📅2024-11
- 🟡 [Awesome-3D-Human-Motion-Generation](https://github.com/Run542968/Awesome-3D-Human-Motion-Generation) — Text-to-Motion中心の人体動作生成論文集 `paper-list` ⭐25 · 📅2024-07
- 🟡 [awesome-Implicit-NeRF-SLAM](https://github.com/Taeyoung96/awesome-Implicit-NeRF-SLAM) — 暗黙表現・NeRFのSLAM/ロボティクス応用論文集 `paper-list` ⭐13 · 📅2023-11
- 🟡 [awesome-dynamic-scene-representations](https://github.com/yklcs/awesome-dynamic-scene-representations) — 動的シーン表現の資料集 `paper-list` ⭐8 · 📅2024-04
- 🟡 [awesome-visualization](https://github.com/Bigger-and-Stronger/awesome-visualization) — CG関連のデータ可視化手法・レンダリング事例を記録するリポジトリ `awesome` ⭐1 · 📅2025-03
- 🔴 [awesome_3DReconstruction_list](https://github.com/openMVG/awesome_3DReconstruction_list) — 画像からの3D復元の古典的論文・資料集 `awesome` ⭐4.4k · 📅2021-10
- 🔴 [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis) — 点群解析・処理に関する論文とデータセットのリスト `awesome` ⭐4.2k · 📅2023-05
- 🔴 [awesome-visual-slam](https://github.com/tzutalin/awesome-visual-slam) — 視覚SLAM/視覚オドメトリのOSS・論文集 `awesome` ⭐2.4k · 📅2022-05
- 🔴 [awesome-slam](https://github.com/kanster/awesome-slam) — SLAMのチュートリアル・プロジェクト・コミュニティ集 `awesome` ⭐1.7k · 📅2020-07
- 🔴 [awesome-3D-generation](https://github.com/justimyhxu/awesome-3D-generation) — 3D生成論文のキュレーションリスト `awesome` ⭐1.2k · 📅2023-03
- 🔴 [awesome-graphics](https://github.com/ericjang/awesome-graphics) — CGチュートリアル・論文の総合リスト `awesome` ⭐1.1k · 📅2020-02
- 🔴 [Awesome-SLAM](https://github.com/SilenceOverflow/Awesome-SLAM) — SLAM論文の継続更新リスト `paper-list` ⭐1.1k · 📅2023-10
- 🔴 [3D-Reconstruction-with-Deep-Learning-Methods](https://github.com/natowi/3D-Reconstruction-with-Deep-Learning-Methods) — 深層学習による3D復元プロジェクトの一覧 `paper-list` ⭐1k · 📅2023-05
- 🔴 [awesome-computer-graphics](https://github.com/luisdnsantos/awesome-computer-graphics) — CG学習用の書籍・講座・資料集 `awesome` ⭐1k · 📅2021-07
- 🔴 [Awsome_Deep_Geometry_Learning](https://github.com/subeeshvasu/Awsome_Deep_Geometry_Learning) — 3D形状の深層学習ソリューション資料集 `paper-list` ⭐361 · 📅2021-08
- 🔴 [awesome-mvs](https://github.com/krahets/awesome-mvs) — MVSのチュートリアル・論文・ソフトウェア集 `awesome` ⭐277 · 📅2022-08
- 🔴 [awesome-pbr](https://github.com/neil3d/awesome-pbr) — PBRの資料・スライド・論文の総合コレクション `awesome` ⭐118 · 📅2021-01
- 🔴 [Awesome-BRDF](https://github.com/tkuri/Awesome-BRDF) — BRDF表現に関する論文を表現方式別に整理 `paper-list` ⭐28 · 📅2021-06
- 🔴 [texture-synthesis-papers](https://github.com/lzhbrian/texture-synthesis-papers) — テクスチャ合成論文(コード付き)の集積 `paper-list` ⭐4 · 📅2019-03

## 🖌️ 低レベル画像処理 / 復元 / 圧縮

- 🟢 [awesome-low-light-image-enhancement](https://github.com/zhihongz/awesome-low-light-image-enhancement) — 低照度画像強調のデータセット/手法/論文/評価指標を網羅(活発) `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment) — IQA論文/データセット/コードの包括集(非常に活発) `awesome` ⭐1.5k · 📅2026-04
- 🟢 [AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) — アニメ/漫画研究の論文・データセット集(生成・カラー化・キャラアニメ等) `awesome` ⭐1.2k · 📅2025-12
- 🟢 [Image-Fusion](https://github.com/Linfeng-Tang/Image-Fusion) — 「Deep Learning-based Image Fusion」サーベイ、赤外-可視/医用/マルチ露出等横断 `survey` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-Image-Colorization](https://github.com/MarkMoHR/Awesome-Image-Colorization) — 深層学習ベースの画像/動画カラー化論文(2025-2026まで活発) `awesome` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-Deep-Learning-Based-Video-Compression](https://github.com/ppingzhang/Awesome-Deep-Learning-Based-Video-Compression) — 深層学習ベース動画圧縮の論文リスト `paper-list` ⭐292 · 📅2025-09
- 🟢 [Awesome-High-Dynamic-Range-Imaging](https://github.com/rebeccaeexu/Awesome-High-Dynamic-Range-Imaging) — HDR論文集(マルチ/シングルフレーム・HDRTV・HDR動画・トーンマッピング) `awesome` ⭐236 · 📅2026-02
- 🟢 [awesome-computational-photography](https://github.com/visionxiang/awesome-computational-photography) — 深層学習による計算写真(画像マッチング・アラインメント・スティッチング・安定化) `paper-list` ⭐179 · 📅2025-07
- 🟢 [TypographyResearchCollection](https://github.com/IShengFang/TypographyResearchCollection) — タイポグラフィ関連のCG/CV/ML研究収集(フォント生成・アニメーション含む) `paper-list` ⭐159 · 📅2025-08
- 🟢 [Awesome-Video-Frame-Interpolation](https://github.com/CMLab-Korea/Awesome-Video-Frame-Interpolation) — IEEE TCSVT'26採録のVFIサーベイ。250+論文を体系化(活発) `survey` ⭐147 · 📅2026-04
- 🟢 [Awesome-Image-Restoration](https://github.com/TaoWangzj/Awesome-Image-Restoration) — サーベイ「Deep Image Restoration」付随、denoise/deblur/SR/dehaze/derain等横断 `survey` ⭐13 · 📅2025-11
- 🟡 [Awesome-Denoise](https://github.com/oneTaken/Awesome-Denoise) — 画像/バースト/動画デノイズ論文を色空間・ノイズモデル別に整理 `awesome` ⭐503 · 📅2024-04
- 🟡 [Awesome-Shadow-Removal](https://github.com/GuoLanqing/Awesome-Shadow-Removal) — 影除去の論文/コード/データセット/指標集(活発) `awesome` ⭐395 · 📅2025-04
- 🟡 [awesome-reflection-removal](https://github.com/ChenyangLEI/awesome-reflection-removal) — 反射除去手法集(単一画像/フラッシュ/偏光/インタラクティブ) `awesome` ⭐158 · 📅2024-12
- 🟡 [awesome-video-enhancement](https://github.com/liuzhen03/awesome-video-enhancement) — 動画超解像・補間・デノイズ・デブラー・インペインティングを横断する論文集 `paper-list` ⭐156 · 📅2024-08
- 🟡 [UIE](https://github.com/YuZhao1999/UIE) — 水中画像強調のリソースリスト `paper-list` ⭐115 · 📅2024-05
- 🟡 [Awesome-Neural-Compression](https://github.com/Xinjie-Q/Awesome-Neural-Compression) — 画像・動画・点群・NeRF・3DGSまで網羅したニューラル圧縮の論文/リソース集 `awesome` ⭐83 · 📅2024-08
- 🟡 [Awesome-Deblurring-Resources](https://github.com/kawchar85/Awesome-Deblurring-Resources) — 年別に整理された画像・動画デブラー論文/データセット(活発) `paper-list` ⭐13 · 📅2024-08
- 🔴 [Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers) — サーベイ「Neural Style Transfer: A Review」付随の代表論文・コード集 `paper-list` ⭐1.6k · 📅2022-02
- 🔴 [DerainZoo](https://github.com/nnUyi/DerainZoo) — 雨除去の手法・データセット・コード集(単一画像/動画) `paper-list` ⭐516 · 📅2022-05
- 🔴 [awesome-image-alignment-and-stitching](https://github.com/tzxiang/awesome-image-alignment-and-stitching) — 画像アラインメント・スティッチングのキュレーション `paper-list` ⭐462 · 📅2022-08
- 🔴 [Awesome-Image-Distortion-Correction](https://github.com/subeeshvasu/Awesome-Image-Distortion-Correction) — ローリングシャッター効果・放射状歪みの補正に関する資源集 `awesome` ⭐281 · 📅2023-07
- 🔴 [awesome-dehazing](https://github.com/youngguncho/awesome-dehazing) — 単一/複数画像デヘイズ・水中強調・データセットを分類した論文集 `awesome` ⭐202 · 📅2020-08
- 🔴 [Sketch-Based-Deep-Learning](https://github.com/qyzdao/Sketch-Based-Deep-Learning) — スケッチベース深層学習の論文集(線画カラー化・ベクトル化等) `paper-list` ⭐178 · 📅2021-05
- 🔴 [Video-Frame-Interpolation-Collections](https://github.com/lyh-18/Video-Frame-Interpolation-Collections) — SOTA VFI手法のコレクション `paper-list` ⭐65 · 📅2021-11

## 💬 NLP / 大規模言語モデル(LLM)

- 🟢 [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — LLM論文・モデル・ツール・コースを網羅した最大級のリスト `awesome` ⭐26.9k · 📅2025-07
- 🟢 [Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM) — オープンソースの中文大規模言語モデル(底座/領域微調整/データ/教程)を整理 `awesome` ⭐22.6k · 📅2026-05
- 🟢 [awesome-nlp](https://github.com/keon/awesome-nlp) — NLP全般のライブラリ・データ・チュートリアルを集めた定番リスト `awesome` ⭐18.7k · 📅2026-05
- 🟢 [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) — LLM進化系統樹と実務活用ガイドをまとめたサーベイ集 `survey` ⭐10.2k · 📅2026-04
- 🟢 [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) — 多モーダル生成・Agent・補助コーディング・データ処理・訓練・推論等のLLM資料総まとめ `awesome` ⭐8.4k · 📅2026-05
- 🟢 [awesome-prompts](https://github.com/ai-boost/awesome-prompts) — 高評価GPTsのプロンプトと先端プロンプト工学論文のコレクション `awesome` ⭐8.1k · 📅2026-05
- 🟢 [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) — OpenAI o1と推論技法に焦点を当てた論文・ブログ集 `paper-list` ⭐6.9k · 📅2025-12
- 🟢 [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) — GPT/ChatGPT向けプロンプト技法の論文・ツールを集めたリスト `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) — FlashAttention・PagedAttention等の推論高速化論文集 `paper-list` ⭐5.3k · 📅2026-04
- 🟢 [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) — Text2SQL/Text2DSL等のチュートリアルとリソース集 `awesome` ⭐3.7k · 📅2026-01
- 🟢 [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — CoTからo1/DeepSeek-R1までのLLM推論論文集(非常に活発) `awesome` ⭐3.6k · 📅2026-04
- 🟢 [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) — プロンプト工学から本番AIシステムまでのコンテキスト工学サーベイ `survey` ⭐3.2k · 📅2026-05
- 🟢 [Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) — グラフ関連LLMのリソースを集めたキュレーション `awesome` ⭐2.4k · 📅2025-11
- 🟢 [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) — グラフベースRAGのサーベイ・論文・ベンチマーク集 `awesome` ⭐2.4k · 📅2026-05
- 🟢 [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) — ICLとプロンプト工学の最新リソースを継続更新する論文リスト `paper-list` ⭐2.2k · 📅2026-05
- 🟢 [KG-LLM-Papers](https://github.com/zjukg/KG-LLM-Papers) — 知識グラフとLLMを統合する論文リスト `paper-list` ⭐2.2k · 📅2026-03
- 🟢 [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) — 長文脈モデリング(効率的注意・KVキャッシュ・位置符号化等)の論文集 `paper-list` ⭐2.1k · 📅2026-05
- 🟢 [Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets) — 事前学習コーパス・指示/選好/評価データセットを5観点で整理 `awesome` ⭐1.5k · 📅2026-03
- 🟢 [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) — TKDE2025サーベイに基づくLLM Text-to-SQLの論文・ベンチマーク集 `survey` ⭐1.3k · 📅2026-05
- 🟢 [SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) — 投機的デコーディングの必読論文・ブログ集(サーベイ連動) `survey` ⭐1.2k · 📅2026-05
- 🟢 [KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) — LLMの知識編集に関する論文リスト `paper-list` ⭐1.2k · 📅2025-07
- 🟢 [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) — LLMの幻覚検出論文をモデル別に整理したリスト `paper-list` ⭐1.1k · 📅2026-05
- 🟢 [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) — 「Siren's Song in the AI Ocean」幻覚サーベイの読み物リスト `survey` ⭐1.1k · 📅2025-09
- 🟢 [Paper-Reading-ConvAI](https://github.com/iwangjian/Paper-Reading-ConvAI) — 対話システムとNLG中心の会話AI論文リスト `paper-list` ⭐1k · 📅2026-05
- 🟢 [Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers) — ACL2023サーベイ「Reasoning with LM Prompting」の論文リスト `paper-list` ⭐1k · 📅2025-05
- 🟢 [awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) — 「LLM × DATA」サーベイ公式リポジトリ `survey` ⭐781 · 📅2026-03
- 🟢 [Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) — 「Stop Overthinking」効率的推論サーベイ(TMLR2025)の論文集 `survey` ⭐768 · 📅2026-02
- 🟢 [Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) — 「LLMs-as-Judges」評価手法サーベイの公式論文集 `survey` ⭐580 · 📅2025-07
- 🟢 [A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) — TKDE採択「MoE in LLMs」サーベイの公式論文集 `survey` ⭐499 · 📅2025-07
- 🟢 [LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) — ツール学習サーベイの公式リポジトリ。task planning/tool selection等で分類 `survey` ⭐484 · 📅2025-08
- 🟢 [Awesome-LLM-Quantization](https://github.com/pprp/Awesome-LLM-Quantization) — LLM量子化に特化した論文リスト `awesome` ⭐424 · 📅2026-04
- 🟢 [awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference) — MoEモデルの推論最適化論文を集めたリスト `paper-list` ⭐393 · 📅2026-03
- 🟢 [Awesome-Inference-Time-Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling) — 推論時/テスト時スケーリングの論文リスト(活発) `awesome` ⭐384 · 📅2026-05
- 🟢 [Awesome_papers_on_LLMs_detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) — LLM生成テキスト・コード検出の論文リスト `paper-list` ⭐287 · 📅2025-06
- 🟢 [Awesome-Fake-News-Detection](https://github.com/wangbing1416/Awesome-Fake-News-Detection) — フェイクニュース・噂検出の論文リスト `awesome` ⭐164 · 📅2026-04
- 🟢 [GEC-Info](https://github.com/gotutiyan/GEC-Info) — GEC論文を収集・分類したリポジトリ `paper-list` ⭐128 · 📅2026-01
- 🟢 [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) — LLM自己修正の論文リスト(サーベイ準拠) `paper-list` ⭐81 · 📅2026-05
- 🟢 [Awesome-Function-Callings](https://github.com/Applied-Machine-Learning-Lab/Awesome-Function-Callings) — LLMのfunction calling特化の論文リスト `paper-list` ⭐71 · 📅2026-04
- 🟢 [Awesome-Personalized-LLMs](https://github.com/VanillaCreamer/Awesome-Personalized-LLMs) — パーソナライズドLLM(嗜好モデル化・persona制御・記憶ベース)の最新論文集 `paper-list` ⭐46 · 📅2026-05
- 🟢 [awesome-lora-adapter](https://github.com/marlin-codes/awesome-lora-adapter) — LoRA・アダプタ系の手法を集めた論文リスト `paper-list` ⭐22 · 📅2026-05
- 🟢 [Awesome-PEFT](https://github.com/XiaoshuangJi/Awesome-PEFT) — LoRA各種派生を中心としたPEFT論文・ライブラリ・実装集 `awesome` ⭐7 · 📅2026-03
- 🟢 [Awesome-Text-Generation-Evaluation](https://github.com/SuperBruceJia/Awesome-Text-Generation-Evaluation) — NLG評価指標(参照あり/なし)のキュレーションリスト `awesome` ⭐4 · 📅2026-05
- 📑 [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) — 「A Survey of Large Language Models」公式リポジトリ `survey` ⭐12.2k · 📅2025-03
- 📑 [ABigSurvey](https://github.com/NiuTrans/ABigSurvey) — NLP・MLの数百本のサーベイ論文を一覧化したサーベイのサーベイ `survey` ⭐2k · 📅2024-03
- 📑 [RAG-Survey](https://github.com/hymie122/RAG-Survey) — 「RAG for AI-Generated Content」サーベイの分類体系と論文集 `survey` ⭐1.8k · 📅2024-08
- 📑 [Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) — 「LLMs on Graphs」TKDEサーベイの論文・リソース集 `survey` ⭐991 · 📅2025-03
- 📑 [Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) — 「Evaluating LLMs: A Comprehensive Survey」の論文集 `survey` ⭐803 · 📅2024-05
- 📑 [CNSurvey](https://github.com/NiuTrans/CNSurvey) — NLP・機械学習の中国語サーベイ文章リスト `survey` ⭐580 · 📅2023-05
- 📑 [ABigSurveyOfLLMs](https://github.com/NiuTrans/ABigSurveyOfLLMs) — LLMに関する150本以上のサーベイを集めたコレクション `survey` ⭐349 · 📅2025-02
- 📑 [Semantic-Retrieval-Models](https://github.com/caiyinqiong/Semantic-Retrieval-Models) — 意味検索モデル(DPR, RAG, RepBERT等)を網羅したTOIS採択サーベイの論文リスト `survey` ⭐340 · 📅2023-06
- 📑 [CTGSurvey](https://github.com/IAAR-Shanghai/CTGSurvey) — LLM向け制御テキスト生成のサーベイ論文リスト(学習時/推論時手法を分類) `survey` ⭐205 · 📅2024-08
- 📑 [Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models](https://github.com/THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models) — 基盤モデル向けPEFT手法を体系的にまとめたサーベイ兼論文リスト `survey` ⭐112 · 📅2025-03
- 📑 [llm-alignment-survey](https://github.com/Magnetic2014/llm-alignment-survey) — 「LLM Alignment: A Survey」のアライメント読み物リスト `survey` ⭐82 · 📅2023-09
- 📑 [Awesome_Information_Extraction](https://github.com/wutong8023/Awesome_Information_Extraction) — RE・EE・slot fillingを含むIE文献サーベイ `survey` ⭐72 · 📅2023-01
- 📑 [Awesome-Data-Efficient-LLM](https://github.com/luo-junyu/Awesome-Data-Efficient-LLM) — データ効率・データ中心のLLM論文集(サーベイ付き) `survey` ⭐57 · 📅2025-02
- 🟡 [Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) — コード生成LLM研究の厳選キュレーションリスト `awesome` ⭐1.3k · 📅2024-12
- 🟡 [Awesome-LLM4IE-Papers](https://github.com/quqxui/Awesome-LLM4IE-Papers) — LLMによる生成的情報抽出(NER/RE/EE)の論文集 `paper-list` ⭐1.1k · 📅2024-11
- 🟡 [ToolLearningPapers](https://github.com/thunlp/ToolLearningPapers) — 基盤モデルのツール学習(tool learning)の必読論文集 `paper-list` ⭐921 · 📅2024-07
- 🟡 [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) — In-Context Learningサーベイに基づく論文リスト `paper-list` ⭐876 · 📅2024-10
- 🟡 [awesome-pretrained-models-for-information-retrieval](https://github.com/ict-bigdatalab/awesome-pretrained-models-for-information-retrieval) — IR向け事前学習モデル(pretraining for IR)の論文集 `awesome` ⭐676 · 📅2024-01
- 🟡 [Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) — MoE研究の読み物リスト `paper-list` ⭐666 · 📅2024-10
- 🟡 [EventExtractionPapers](https://github.com/BaptisteBlouin/EventExtractionPapers) — イベント抽出タスク中心のNLPリソースリスト `paper-list` ⭐580 · 📅2024-03
- 🟡 [awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning) — Instruction Tuning/Following論文とデータセット集 `paper-list` ⭐510 · 📅2024-04
- 🟡 [Awesome-LLM-Watermark](https://github.com/hzy312/Awesome-LLM-Watermark) — 最新のLLMウォーターマーク論文を継続更新するリスト `paper-list` ⭐375 · 📅2024-12
- 🟡 [awesome-llm-pretraining](https://github.com/RUCAIBox/awesome-llm-pretraining) — LLM事前学習のデータ・フレームワーク・手法リソース集 `awesome` ⭐375 · 📅2025-04
- 🟡 [ABSAPapers](https://github.com/ZhengZixiang/ABSAPapers) — アスペクトベース感情分析(ABSA)の論文・リソース集 `paper-list` ⭐363 · 📅2024-03
- 🟡 [Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) — LLM幻覚に関する論文リスト `paper-list` ⭐335 · 📅2024-03
- 🟡 [LLM-Optimizers-Papers](https://github.com/AGI-Edgerunners/LLM-Optimizers-Papers) — LLMを最適化器として使う/プロンプト自動最適化の必読論文集 `paper-list` ⭐252 · 📅2024-03
- 🟡 [awesome-tool-llm](https://github.com/zorazrw/awesome-tool-llm) — ツール拡張LLM(ToRA, MINT等)を集めたキュレーションリスト `awesome` ⭐243 · 📅2024-08
- 🟡 [Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) — 「Evaluation of RAG: A Survey」公式の評価論文リスト `paper-list` ⭐198 · 📅2025-04
- 🟡 [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) — テスト時LLM(self-correction/refine含む)論文集 `awesome` ⭐152 · 📅2025-03
- 🟡 [Low-resource-KEPapers](https://github.com/zjunlp/Low-resource-KEPapers) — 低リソース情報抽出(NER/RE/EE)の論文・ツール・データセット集 `paper-list` ⭐135 · 📅2024-11
- 🟡 [EMNLP-2023-Papers](https://github.com/DmitryRyumin/EMNLP-2023-Papers) — EMNLP 2023の論文を体系的に整理したコレクション `paper-list` ⭐111 · 📅2024-05
- 🟡 [Paper-Neural-Topic-Models](https://github.com/bobxwu/Paper-Neural-Topic-Models) — ニューラルトピックモデル(NTM)の論文集 `paper-list` ⭐95 · 📅2024-07
- 🟡 [Awesome-Papers-Retrieval-Augmented-Generation](https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation) — 知識指向RAGサーベイに基づく論文分類リスト `paper-list` ⭐89 · 📅2025-03
- 🟡 [Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers) — 多言語LLMの論文リスト `paper-list` ⭐34 · 📅2025-01
- 🟡 [awesome-llm-tool-learning](https://github.com/AngxiaoYue/awesome-llm-tool-learning) — LLMのツール学習論文(Gorilla, HuggingGPT, ART等)のリスト `paper-list` ⭐28 · 📅2024-07
- 🟡 [Awesome-LLM-Reasoning-Techniques](https://github.com/Junting-Lu/Awesome-LLM-Reasoning-Techniques) — CoTやo1を含むLLM推論技法の論文・リソース集 `paper-list` ⭐18 · 📅2024-10
- 📦 [Fact-Checking-Survey](https://github.com/neemakot/Fact-Checking-Survey) — COLING2020「Explainable Automated Fact-Checking」サーベイの論文集 `survey` ⭐51 · 📅2021-01
- 🔴 [PromptPapers](https://github.com/thunlp/PromptPapers) — 事前学習モデルのプロンプトベースチューニングの必読論文集 `paper-list` ⭐4.3k · 📅2023-07
- 🔴 [Top-AI-Conferences-Paper-with-Code](https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code) — ACL/EMNLP/NAACL/COLING等トップ会議のコード付き論文集 `paper-list` ⭐2.7k · 📅2022-10
- 🔴 [Style-Transfer-in-Text](https://github.com/fuzhenxin/Style-Transfer-in-Text) — テキストスタイル変換の定番論文リスト(教師あり/なし/評価を分類) `paper-list` ⭐1.6k · 📅2023-03
- 🔴 [awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization) — テキスト要約の論文・ツール・データセット集 `awesome` ⭐1.5k · 📅2023-01
- 🔴 [awesome-relation-extraction](https://github.com/roomylee/awesome-relation-extraction) — 関係抽出に特化したリソースリスト `awesome` ⭐1.2k · 📅2022-01
- 🔴 [awesome-qa](https://github.com/seriousran/awesome-qa) — 質問応答のデータセット・論文・リソース集 `awesome` ⭐767 · 📅2022-01
- 🔴 [awesome-sentiment-analysis](https://github.com/declare-lab/awesome-sentiment-analysis) — 感情分析論文の読み物リスト `paper-list` ⭐538 · 📅2023-03
- 🔴 [awesome-nlg](https://github.com/accelerated-text/awesome-nlg) — NLG全般のリソース集(ツール/論文/データ) `awesome` ⭐480 · 📅2023-09
- 🔴 [Named-Entity-Recognition-NER-Papers](https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers) — 7会議のNER論文を網羅したリスト `paper-list` ⭐392 · 📅2022-02
- 🔴 [Awesome-Sentence-Embedding](https://github.com/Doragd/Awesome-Sentence-Embedding) — 文表現学習論文とSTSリーダーボード(SimCSE等)を収録 `awesome` ⭐314 · 📅2023-10
- 🔴 [DeltaPapers](https://github.com/thunlp/DeltaPapers) — 事前学習モデルのパラメータ効率チューニング(Delta Tuning)の必読論文集 `paper-list` ⭐285 · 📅2023-06
- 🔴 [Awesome-KBQA](https://github.com/RUCAIBox/Awesome-KBQA) — 知識ベースQA(KBQA)の論文・ツール・リーダーボード集 `paper-list` ⭐181 · 📅2022-04
- 🔴 [Accepted-Papers-Lists](https://github.com/audreycs/Accepted-Papers-Lists) — 主要ジャーナル・会議の採択論文リストをまとめたリポジトリ `paper-list` ⭐147 · 📅2022-12
- 🔴 [MT-paper-lists](https://github.com/NiuTrans/MT-paper-lists) — 会議別に機械翻訳論文を整理したリスト `paper-list` ⭐124 · 📅2020-12
- 🔴 [Data-to-Text-Generation](https://github.com/liang8qi/Data-to-Text-Generation) — data-to-text生成の論文・データセット集 `paper-list` ⭐108 · 📅2023-05
- 🔴 [awesome-NLP-Machine-Learning](https://github.com/tjunlp-lab/awesome-NLP-Machine-Learning) — NLP研究向けの機械学習技法(RL/自己教師あり等)の論文・コード集 `paper-list` ⭐35 · 📅2020-03
- 🔴 [AWESOME-Dialogue](https://github.com/thuiar/AWESOME-Dialogue) — 対話・インタラクティブシステムの論文リスト `paper-list` ⭐15 · 📅2020-06
- 🔴 [awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp) — 英語以外を対象とした多言語NLP研究のキュレーション `awesome` ⭐8 · 📅2023-07
- 🔴 [AwesomeSemanticParsing](https://github.com/aarsri/AwesomeSemanticParsing) — 意味解析の論文・リソース集 `awesome` ⭐0 · 📅2020-11

## 🖼️ 生成AI / Diffusion / 画像・動画生成

- 🟢 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) — 動画生成・編集の拡散モデルを集めた定番リスト `awesome` ⭐5.7k · 📅2026-05
- 🟢 [really-awesome-gan](https://github.com/nightrome/really-awesome-gan) — GAN論文を集めた網羅的リスト `paper-list` ⭐3.8k · 📅2025-08
- 🟢 [awesome-virtual-try-on](https://github.com/minar09/awesome-virtual-try-on) — 仮想試着の論文/コード/データセットの定番リスト `awesome` ⭐3.1k · 📅2026-05
- 🟢 [Awesome-Text-to-Image](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image) — テキストから画像生成のサーベイ的論文リスト `survey` ⭐2.4k · 📅2026-02
- 🟢 [Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) — Video Diffusion Modelのサーベイ(CSUR) `survey` ⭐2.3k · 📅2026-04
- 🟢 [awesome-diffusion-categorized](https://github.com/wangkai930418/awesome-diffusion-categorized) — Diffusion論文をサブ領域別に分類した実用的コレクション `awesome` ⭐2.2k · 📅2026-03
- 🟢 [awesome-talking-head-generation](https://github.com/harlanhong/awesome-talking-head-generation) — トーキングヘッド生成の論文リスト `paper-list` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) — Deepfake検出のツール/論文/コード `awesome` ⭐1.8k · 📅2025-09
- 🟢 [awesome-image-translation](https://github.com/weihaox/awesome-image-translation) — image-to-image translationに関する優良資源のコレクション `awesome` ⭐1.2k · 📅2025-09
- 🟢 [Awesome-diffusion-model-for-image-processing](https://github.com/lixinustc/Awesome-diffusion-model-for-image-processing) — 復元/強調/符号化/品質評価の拡散モデル整理 `survey` ⭐946 · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/showlab/Awesome-Unified-Multimodal-Models) — 理解と生成を統一するモデルの論文集 `paper-list` ⭐825 · 📅2025-10
- 🟢 [Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) — ビジョンの自己回帰モデルサーベイ(TMLR 2025) `survey` ⭐796 · 📅2026-05
- 🟢 [awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) — 動画生成研究を集めたコレクション `awesome` ⭐769 · 📅2026-03
- 🟢 [awesome-text-to-image-studies](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) — text-to-image研究を集めた継続更新リスト `awesome` ⭐759 · 📅2026-04
- 🟢 [Awesome-Deepfake-Generation-and-Detection](https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection) — Deepfake生成と検出のサーベイ `survey` ⭐637 · 📅2026-05
- 🟢 [awesome-discrete-diffusion-models](https://github.com/kuleshov-group/awesome-discrete-diffusion-models) — 離散拡散モデルに特化した資源リスト `awesome` ⭐561 · 📅2025-09
- 🟢 [Awesome-Video-World-Models-with-AR-Diffusion](https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion) — AR+拡散の動画世界モデル(アルゴリズム/応用/基盤) `awesome` ⭐561 · 📅2026-05
- 🟢 [Awesome-Controllable-Diffusion](https://github.com/atfortes/Awesome-Controllable-Diffusion) — ControlNet・DreamBooth・IP-Adapter等の制御生成資源 `awesome` ⭐505 · 📅2025-06
- 🟢 [Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model) — 動画生成から世界モデルへの流れを整理 `paper-list` ⭐484 · 📅2026-03
- 🟢 [Awesome-Image-Editing](https://github.com/FudanCVL/Awesome-Image-Editing) — T2Iモデルによる画像編集のサーベイ `survey` ⭐471 · 📅2025-08
- 🟢 [Awesome-Evaluation-of-Visual-Generation](https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation) — 視覚生成の評価指標/モデル/システム集 `paper-list` ⭐444 · 📅2026-05
- 🟢 [Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation) — 自己回帰ビジュアル生成の最新論文追跡 `paper-list` ⭐431 · 📅2025-06
- 🟢 [Awesome-Try-On-Models](https://github.com/Zheng-Chong/Awesome-Try-On-Models) — 仮想試着モデル(2025含む)を整理 `paper-list` ⭐416 · 📅2026-01
- 🟢 [Awesome-AIGC-Image-Video-Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) — AI生成画像/動画検出の最新研究集 `paper-list` ⭐387 · 📅2026-05
- 🟢 [awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) — 画像インペインティング研究のコレクション `awesome` ⭐384 · 📅2026-02
- 🟢 [Awesome-Comprehensive-Deepfake-Detection](https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection) — Deepfake検出の包括的論文リスト `paper-list` ⭐313 · 📅2026-04
- 🟢 [awesome-diffusion-v2v](https://github.com/wenhao728/awesome-diffusion-v2v) — 拡散ベースVideo-to-Video編集の論文+ベンチマーク `paper-list` ⭐287 · 📅2026-04
- 🟢 [Awesome-Text-to-Video-Generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation) — Soraサーベイ準拠のT2V/I2V論文リスト `survey` ⭐260 · 📅2026-03
- 🟢 [Awesome-Consistency-Models](https://github.com/G-U-N/Awesome-Consistency-Models) — Consistency Modelの資源リスト `awesome` ⭐131 · 📅2025-12
- 📑 [GAN-Inversion](https://github.com/weihaox/GAN-Inversion) — GAN Inversionのサーベイ(TPAMI 2022)付随リポジトリ `survey` ⭐1.1k · 📅2025-02
- 📑 [awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) — Text-to-Video生成のサーベイ `survey` ⭐730 · 📅2024-07
- 🟡 [Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) — Diffusion Modelの論文・資源を網羅した最大級のリスト `awesome` ⭐12.3k · 📅2024-08
- 🟡 [Awesome-High-Resolution-Diffusion](https://github.com/GuoLanqing/Awesome-High-Resolution-Diffusion) — 高解像度画像/動画合成の拡散論文 `paper-list` ⭐169 · 📅2024-12
- 🟡 [Awesome-Music-Generation](https://github.com/shaopengw/Awesome-Music-Generation) — 音楽生成モデルMG²の資源 `model` ⭐165 · 📅2025-03
- 🟡 [awesome-diffusion-iclr-2025](https://github.com/moatifbutt/awesome-diffusion-iclr-2025) — ICLR 2025の拡散関連投稿リスト `paper-list` ⭐61 · 📅2024-10
- 📚 [the-gan-zoo](https://github.com/hindupuravinash/the-gan-zoo) — 命名された全GANを一覧化した古典的リスト `paper-list` ⭐14.7k · 📅2023-10
- 🔴 [gans-awesome-applications](https://github.com/nashory/gans-awesome-applications) — GANの応用・デモを集めたキュレーションリスト `awesome` ⭐5.1k · 📅2023-08
- 🔴 [awesome-ai-art-image-synthesis](https://github.com/altryne/awesome-ai-art-image-synthesis) — DALL·E2/MidJourney/SD等のツール・プロンプト集 `awesome` ⭐1.8k · 📅2022-12
- 🔴 [awesome-diffusion-low-level-vision](https://github.com/yulunzhang/awesome-diffusion-low-level-vision) — 低レベルビジョン拡散モデルのリスト `paper-list` ⭐186 · 📅2023-09
- 🔴 [awesome-controlnet](https://github.com/cobanov/awesome-controlnet) — ControlNet関連資源のリスト `awesome` ⭐97 · 📅2023-03
- 🔴 [awesome-few-shot-generation](https://github.com/kobeshegu/awesome-few-shot-generation) — 少数枚画像生成の論文リスト `paper-list` ⭐87 · 📅2023-08
- 🔴 [Awsome-GAN-Training](https://github.com/subeeshvasu/Awsome-GAN-Training) — GANの学習(training)に関する資源を集めたリスト `awesome` ⭐30 · 📅2020-10

## 🍌 特定モデルのプロンプト・作例コレクション

- 🟢 [Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) — Gemini系Nano Bananaの生成例・プロンプト集(データセット公開) `model` ⭐22.9k · 📅2025-12
- 🟢 [awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) — GPT-Image-2のAPIとプロンプト・作例集 `model` ⭐15.7k · 📅2026-05
- 🟢 [awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) — 世界最大級のNano Banana Proプロンプト集10,000+/16言語(毎日更新) `model` ⭐12.3k · 📅2026-05
- 🟢 [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) — Nano Banana Pro(Nano Banana 2)のプロンプト・作例集 `model` ⭐10k · 📅2026-05
- 🟢 [awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) — Gemini-2.5-Flash-Image(Nano Banana)の作例/プロンプト集 `model` ⭐8.8k · 📅2025-09
- 🟢 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) — GPT-4o・gpt-image-1の画像・プロンプト作例集 `model` ⭐8.1k · 📅2025-05
- 🟢 [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) — Seedance 2.0動画生成プロンプト2000+(毎日更新) `model` ⭐1.2k · 📅2026-05
- 🟢 [awesome-nano-banana-pro](https://github.com/muset-ai/awesome-nano-banana-pro) — Nano Banana Proの画像・プロンプト作例集 `model` ⭐1.1k · 📅2025-11
- 🟢 [Awesome-GPT4o-Image-Prompts](https://github.com/ImgEdify/Awesome-GPT4o-Image-Prompts) — GPT-4o画像生成のプロンプト辞典 `model` ⭐561 · 📅2025-05
- 🟢 [awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) — Veo3/Kling/Hailuo向け動画プロンプト集 `model` ⭐517 · 📅2025-10
- 🟢 [awesome-grok-prompts](https://github.com/langgptai/awesome-grok-prompts) — Grok(xAI)向け高度プロンプト・テンプレート集 `model` ⭐506 · 📅2025-05
- 🟢 [Awesome-Chinese-Stable-Diffusion](https://github.com/leeguandong/Awesome-Chinese-Stable-Diffusion) — 中国系文生図SDモデル集(Kolors/HunyuanDiT等含む) `model` ⭐425 · 📅2026-05
- 🟢 [awesome-qwen-prompt-insight](https://github.com/XiaomingX/awesome-qwen-prompt-insight) — Qwen向け優良プロンプトの大規模コレクション `model` ⭐398 · 📅2026-02
- 🟢 [awesome-nano-banana-images](https://github.com/githubssg/awesome-nano-banana-images) — GPT-4o/gpt-image-1の画像・プロンプト集 `model` ⭐306 · 📅2025-09
- 🟢 [Awesome-Open-AI-Sora](https://github.com/Curated-Awesome-Lists/Awesome-Open-AI-Sora) — Sora関連記事/動画/ニュースのリソースハブ `model` ⭐260 · 📅2026-05
- 🟢 [awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) — 複数動画モデル横断のプロンプト/技法集 `model` ⭐55 · 📅2026-01
- 🟢 [awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts) — Grok Imagine(xAI)動画生成プロンプト集 `model` ⭐13 · 📅2026-05
- 🟢 [awesome-qwen-image-2512](https://github.com/shauray8/awesome-qwen-image-2512) — qwen-image-2512の作例/プロンプト集 `model` ⭐0 · 📅2025-12
- 🟡 [Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) — GPT Store掲載のGPTを集めたキュレーション `model` ⭐3.4k · 📅2024-11
- 🟡 [awesome-llama-prompts](https://github.com/langgptai/awesome-llama-prompts) — Llama2/Llama3向けプロンプト集 `model` ⭐270 · 📅2024-08
- 🟡 [awesome-flux](https://github.com/Eris2025/awesome-flux) — FLUXエコシステム(LoRA/ControlNet/量子化)の資源集 `model` ⭐105 · 📅2024-08

## 🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ)

- 🟢 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — 実行可能なLLMアプリ/RAG/エージェントのコレクション `awesome` ⭐112.1k · 📅2026-05
- 🟢 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 最大手のMCP(Model Context Protocol)サーバーコレクション `awesome` ⭐88.1k · 📅2026-05
- 🟢 [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Claude Skill/ツールのキュレーション `awesome` ⭐62.4k · 📅2026-05
- 🟢 [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code向けskill/hook/slash-command/プラグイン集 `awesome` ⭐45.1k · 📅2026-04
- 🟢 [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) — DeepSeek APIを各種ソフトに統合する公式キュレーション `model` ⭐37.6k · 📅2026-02
- 🟢 [Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) — PyTorch関連のモデル・実装・ライブラリを網羅した大規模リスト `awesome` ⭐16.5k · 📅2026-02
- 🟢 [awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) — 現代の生成AIプロジェクト・サービスを厳選したリスト `awesome` ⭐12.1k · 📅2026-05
- 🟢 [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) — LangChainフレームワークのツール・プロジェクトのリスト `awesome` ⭐9.4k · 📅2026-04
- 🟢 [ai-collection](https://github.com/ai-collection/ai-collection) — 生成AIアプリケーションを集めたランドスケープ `awesome` ⭐9k · 📅2026-05
- 🟢 [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) — ChatGPT向けawesomeリスト(sindresorhus系列) `awesome` ⭐6.3k · 📅2026-02
- 🟢 [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) — AI関連の実用ツールを収集したコレクション(中英併記) `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) — LLM開発・運用向けツール(学習/サービング/監視)の厳選リスト `awesome` ⭐5.8k · 📅2026-05
- 🟢 [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) — MCPサーバーのキュレーション `awesome` ⭐5.6k · 📅2026-05
- 🟢 [awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools) — AIのトップツールを厳選したリスト `awesome` ⭐5.3k · 📅2025-12
- 🟢 [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) — 真にオープンソースなAIプロジェクト・モデル・ツール・基盤の厳選リスト `awesome` ⭐3.7k · 📅2026-05
- 🟢 [awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) — ChatGPTのライブラリ/SDK/APIキュレーション `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-claude](https://github.com/webfuse-com/awesome-claude) — Anthropic Claude全般のキュレーションリスト `awesome` ⭐1.5k · 📅2026-05
- 🟢 [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) — 生成AIにおけるRAGアプリのawesomeリスト `awesome` ⭐1.2k · 📅2026-05
- 🟢 [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) — DeepSeek Coder関連のOSSプロジェクトをまとめた公式リスト `model` ⭐789 · 📅2025-11
- 🟢 [awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) — ComfyUIカスタムノードの大規模コレクション `awesome` ⭐695 · 📅2025-07
- 🟢 [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) — Gemini CLI向けツール/拡張/リソース集 `awesome` ⭐456 · 📅2026-05
- 🟢 [awesome-flux-ai](https://github.com/AINativeLab/awesome-flux-ai) — Flux AIのツール/ライブラリ/アプリ網羅 `awesome` ⭐111 · 📅2025-05
- 🟢 [awesome-stable-diffusion](https://github.com/doanbactam/awesome-stable-diffusion) — Stable Diffusionリソースのキュレーション `awesome` ⭐75 · 📅2026-03
- 🟢 [awesome-mistral](https://github.com/samouraiworld/awesome-mistral) — Mistral AIエコシステムのリソース/ツール/プロジェクト集 `awesome` ⭐42 · 📅2026-05
- 🟡 [awesome-gpt](https://github.com/formulahendry/awesome-gpt) — GPT/ChatGPT/OpenAI関連プロジェクト・リソース集 `awesome` ⭐1k · 📅2024-05

## 🎮 強化学習(RL)

- 🟢 [MARL-Papers](https://github.com/LantaoYu/MARL-Papers) — マルチエージェントRLの研究・サーベイ論文リスト(定番) `paper-list` ⭐4.8k · 📅2026-02
- 🟢 [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) — ロボティクス/RLへのLLM・マルチモーダル活用論文集 `paper-list` ⭐4.4k · 📅2026-04
- 🟢 [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — 人間フィードバックによるRLの論文・資源を継続更新 `paper-list` ⭐4.4k · 📅2026-05
- 🟢 [Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) — 大規模推論モデル向けRLのサーベイ論文リポジトリ `survey` ⭐2.5k · 📅2025-11
- 🟢 [Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) — ワールドモデル(動画生成・Embodied AI・自動運転)の論文網羅 `paper-list` ⭐1.7k · 📅2026-05
- 🟢 [awesome-diffusion-model-in-rl](https://github.com/opendilab/awesome-diffusion-model-in-rl) — 強化学習における拡散モデルの資源を継続更新するリスト `awesome` ⭐1.6k · 📅2025-12
- 🟢 [awesome-model-based-RL](https://github.com/opendilab/awesome-model-based-RL) — モデルベースRLの論文を継続更新で収集 `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-decision-transformer](https://github.com/opendilab/awesome-decision-transformer) — Decision Transformer資源の継続更新リスト `awesome` ⭐899 · 📅2026-05
- 🟢 [awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) — Deep RLのライブラリ・環境・ベンチマークを整理したリスト `awesome` ⭐892 · 📅2025-07
- 🟢 [Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) — Safe RLのベースライン・論文を集めたリポジトリ `paper-list` ⭐793 · 📅2026-03
- 🟢 [World-Model](https://github.com/tsinghua-fib-lab/World-Model) — 世界モデルの包括的サーベイ(ACM CSUR 2025採録) `survey` ⭐724 · 📅2025-11
- 🟢 [awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl) — 探索(exploration)に特化したRL論文リスト `paper-list` ⭐691 · 📅2026-05
- 🟢 [awesome-multi-modal-reinforcement-learning](https://github.com/opendilab/awesome-multi-modal-reinforcement-learning) — マルチモーダルRL資源を継続更新 `paper-list` ⭐607 · 📅2025-12
- 🟢 [Reinforcement-Learning-Papers](https://github.com/yingchengyang/Reinforcement-Learning-Papers) — ICLR/ICML/NeurIPSの古典+最新論文を年別に整理 `paper-list` ⭐570 · 📅2026-02
- 🟢 [Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) — 視覚RL・マルチモーダル基盤モデル向けRLの論文整理 `paper-list` ⭐445 · 📅2026-04
- 🟢 [Reinforcement-Learning-Papers](https://github.com/Allenpandas/Reinforcement-Learning-Papers) — NeurIPS/ICML/ICLR/AAAI/IJCAI/AAMAS/ICRAの論文を網羅 `paper-list` ⭐366 · 📅2025-11
- 🟢 [awesome-in-context-rl](https://github.com/dunnolab/awesome-in-context-rl) — In-Context RLの論文キュレーション `paper-list` ⭐301 · 📅2025-09
- 🟢 [Awesome-Causal-Reinforcement-Learning](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) — 因果RLのサーベイ(TNNLS 2024)公式リポジトリ `survey` ⭐220 · 📅2026-04
- 🟢 [awesome-deep-reinforcement-learning](https://github.com/jgvictores/awesome-deep-reinforcement-learning) — フレームワーク・モデル・データセット・gym・ベースラインを収録 `awesome` ⭐206 · 📅2026-03
- 🟢 [AwesomeSim2Real](https://github.com/LongchaoDa/AwesomeSim2Real) — サーベイ「A Survey of Sim-to-Real Methods in RL」のcompanion `survey` ⭐166 · 📅2025-09
- 🟢 [awesome-RLVR](https://github.com/opendilab/awesome-RLVR) — 検証可能報酬によるRL(RLVR)の論文を継続更新 `paper-list` ⭐164 · 📅2026-05
- 🟢 [awesome-world-models-for-robots](https://github.com/operator22th/awesome-world-models-for-robots) — ロボティクス向けワールドモデル論文集 `paper-list` ⭐135 · 📅2026-03
- 🟢 [Awesome-Embodied-World-Model](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) — 身体性エージェント向け世界モデルに特化した論文集 `survey` ⭐112 · 📅2026-05
- 🟡 [awesome-deep-rl](https://github.com/tigerneil/awesome-deep-rl) — Deep RLとAIの将来に向けた資源を幅広く収集したリスト `awesome` ⭐1.5k · 📅2024-03
- 🟡 [awesome-rl-envs](https://github.com/clvrai/awesome-rl-envs) — RL用環境・シミュレータを網羅したリスト `awesome` ⭐1.3k · 📅2024-05
- 🟡 [awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl) — オフラインRLのアルゴリズム索引(継続更新) `paper-list` ⭐1.1k · 📅2024-05
- 🟡 [awesome-game-ai](https://github.com/datamllab/awesome-game-ai) — マルチエージェント学習中心のゲームAI資源集 `awesome` ⭐963 · 📅2024-06
- 🟡 [Awesome-Imitation-Learning](https://github.com/kristery/Awesome-Imitation-Learning) — 模倣学習の論文・資源を集めたリスト `paper-list` ⭐608 · 📅2024-02
- 📚 [deep-reinforcement-learning-papers](https://github.com/junhyukoh/deep-reinforcement-learning-papers) — Deep RLの主要論文をトピック別にまとめた古典的リスト `paper-list` ⭐2.2k · 📅2016-06
- 🔴 [awesome-rl](https://github.com/aikorea/awesome-rl) — RL全般のコード・講義・論文・環境を集めた定番キュレーション `awesome` ⭐9.8k · 📅2023-05
- 🔴 [awesome-real-world-rl](https://github.com/ugurkanates/awesome-real-world-rl) — 実世界で強化学習を動かすための論文・プロジェクト集(sim2real含む) `awesome` ⭐453 · 📅2022-10
- 🔴 [MARL-papers-with-code](https://github.com/TimeBreaker/MARL-papers-with-code) — コード付きMARL論文を手法別に整理 `paper-list` ⭐429 · 📅2022-09
- 🔴 [Imitation-Learning-Paper-Lists](https://github.com/apexrl/Imitation-Learning-Paper-Lists) — 模倣学習の論文を簡潔な紹介付きで収集 `paper-list` ⭐157 · 📅2022-03
- 🔴 [awesome-irl](https://github.com/dit7ya/awesome-irl) — 逆強化学習の論文・コード・動画・チュートリアル集 `awesome` ⭐44 · 📅2022-02
- 🔴 [awesome-metarl](https://github.com/metarl/awesome-metarl) — メタ強化学習のキュレーションリスト `paper-list` ⭐33 · 📅2020-05

## 🔀 マルチモーダル / VLM / MLLM

- 🟢 [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) — MLLM分野の最有名サーベイ。アーキテクチャ・学習・評価を網羅追跡 `survey` ⭐17.8k · 📅2026-05
- 🟢 [Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) — 動画理解向けVid-LLMの最新論文・コード・データセット `paper-list` ⭐3.2k · 📅2026-03
- 🟢 [VLM_survey](https://github.com/jingyi0000/VLM_survey) — 視覚タスク向けVision-Languageモデルの系統的レビュー `survey` ⭐3.1k · 📅2025-10
- 🟢 [Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) — 3D世界における多モーダルLLM資源の網羅リスト `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) — 理解と生成を統合する多モーダルモデルの網羅集(活発) `survey` ⭐1.3k · 📅2026-03
- 🟢 [awesome-vlm-architectures](https://github.com/gokayfem/awesome-vlm-architectures) — 著名なVLMとそのアーキテクチャを解説したコレクション `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) — マルチモーダルLLMの幻覚(hallucination)に関する資源の厳選リスト `awesome` ⭐1k · 📅2025-09
- 🟢 [Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) — CLIP等のVLM向けプロンプト/アダプタ学習手法の厳選リスト `paper-list` ⭐778 · 📅2026-05
- 🟢 [Awesome-Spatial-Intelligence-in-VLM](https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM) — VLMの空間推論に関する論文・ベンチマーク約200本(非常に活発) `paper-list` ⭐747 · 📅2026-01
- 🟢 [Awesome_Matching_Pretraining_Transfering](https://github.com/Paranioar/Awesome_Matching_Pretraining_Transfering) — 画像テキストマッチング・VL事前学習・マルチモーダルモデルの大規模論文リスト `paper-list` ⭐445 · 📅2025-09
- 🟢 [Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) — マルチモーダル研究全般の厳選論文集 `awesome` ⭐335 · 📅2026-05
- 🟢 [Awesome-Chart-Understanding](https://github.com/khuangaf/Awesome-Chart-Understanding) — IEEE TKDEサーベイ準拠のチャート理解(QA/captioning/fact-checking)論文集 `survey` ⭐240 · 📅2025-12
- 🟢 [Awesome-Document-Understanding](https://github.com/harrytea/Awesome-Document-Understanding) — MLLM/OCR-free等のマルチモーダル文書AI論文・コード・データセット集 `paper-list` ⭐201 · 📅2025-09
- 🟢 [Evaluation-Multimodal-LLMs-Survey](https://github.com/swordlidev/Evaluation-Multimodal-LLMs-Survey) — MLLMのベンチマーク200件以上をレビューした評価サーベイ `survey` ⭐149 · 📅2026-05
- 🟢 [Awesome-Multimodal-LLM-for-Math-STEM](https://github.com/InfiMM/Awesome-Multimodal-LLM-for-Math-STEM) — Math/STEM/Code向けマルチモーダルLLMの論文集 `awesome` ⭐143 · 📅2026-05
- 🟢 [Awesome-MLLM-Tuning](https://github.com/WenkeHuang/Awesome-MLLM-Tuning) — MLLMの下流タスク向けチューニング手法サーベイ `paper-list` ⭐98 · 📅2025-08
- 🟢 [Awesome-Composed-Multi-modal-Retrieval](https://github.com/kkzhang95/Awesome-Composed-Multi-modal-Retrieval) — 合成画像検索(CIR)・合成動画検索(CVR)を含むCMRサーベイ `survey` ⭐89 · 📅2026-01
- 🟢 [Awesome-Multimodal-RAG](https://github.com/JarvisUSTC/Awesome-Multimodal-RAG) — テキスト/画像/動画/音声を跨ぐマルチモーダルRAGの論文・ツール集 `paper-list` ⭐53 · 📅2025-11
- 🟢 [Awesome-Large-Vision-Language-Model](https://github.com/SuperBruceJia/Awesome-Large-Vision-Language-Model) — 大規模VLMと医療基盤モデルの論文・リソース集 `awesome` ⭐47 · 📅2025-07
- 📑 [Efficient-Multimodal-LLMs-Survey](https://github.com/swordlidev/Efficient-Multimodal-LLMs-Survey) — 効率的MLLM(軽量構造・戦略)の体系的レビュー `survey` ⭐385 · 📅2025-04
- 🟡 [awesome-audio-visual](https://github.com/krantiparida/awesome-audio-visual) — 音声・視覚処理の各領域の論文・データセット集 `awesome` ⭐771 · 📅2024-01
- 🟡 [Awesome-Table-Recognition](https://github.com/cv-small-snails/Awesome-Table-Recognition) — 表認識の論文・データセット・コンペ解法を整理 `awesome` ⭐404 · 📅2024-12
- 🟡 [awesome-emotion-recognition-in-conversations](https://github.com/declare-lab/awesome-emotion-recognition-in-conversations) — 会話における感情認識(ERC)の網羅的リーディングリスト `paper-list` ⭐278 · 📅2024-02
- 🟡 [awesome-table-structure-recognition](https://github.com/Tan-Junwen/awesome-table-structure-recognition) — 表構造認識(TSR)のモデル・論文・データセット・コード集 `awesome` ⭐228 · 📅2024-09
- 🟡 [Prompt_Learning_Paper_List](https://github.com/Event-AHU/Prompt_Learning_Paper_List) — (視覚言語)プロンプト学習の論文リスト `paper-list` ⭐19 · 📅2024-11
- 🔴 [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) — KIE・レイアウト解析・DocQA・OCR等を網羅した定番リスト `awesome` ⭐1.5k · 📅2023-06
- 🔴 [awesome-video-text-retrieval](https://github.com/danieljf24/awesome-video-text-retrieval) — 動画テキスト検索の深層学習リソース集 `awesome` ⭐645 · 📅2023-10
- 🔴 [awesome-affective-computing](https://github.com/AmrMKayid/awesome-affective-computing) — 感情コンピューティングの論文・ソフト・OSS・リソース集 `awesome` ⭐192 · 📅2019-11
- 🔴 [AWESOME-MER](https://github.com/EvelynFan/AWESOME-MER) — マルチモーダル感情認識(MER)のリーディングリスト `paper-list` ⭐127 · 📅2020-10
- 🔴 [awesome-VLM](https://github.com/Lab-LVM/awesome-VLM) — 対照学習・PrefixLM・融合など手法別に整理したVLM論文集 `paper-list` ⭐7 · 📅2023-06

## 🔊 音声 / オーディオ

- 🟢 [awesome-diarization](https://github.com/wq2012/awesome-diarization) — 話者ダイアライゼーションの論文・ライブラリ・データセット・評価ツールを網羅した定番リスト `awesome` ⭐1.9k · 📅2025-07
- 🟢 [speech-trident](https://github.com/ga642381/speech-trident) — 音声/オーディオLLM・表現学習・codecモデルの論文集 `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [audio-ai-hub](https://github.com/BinWang28/audio-ai-hub) — オーディオ大規模言語モデルの論文・リソース集 `awesome` ⭐921 · 📅2026-05
- 🟢 [awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) — LLMのAudio AI応用に関するリソース集 `awesome` ⭐729 · 📅2026-05
- 🟢 [ICASSP-2023-24-Papers](https://github.com/DmitryRyumin/ICASSP-2023-24-Papers) — ICASSP 2023-2024の論文を網羅したコレクション `paper-list` ⭐527 · 📅2025-05
- 🟢 [Awesome-Speaker-Diarization](https://github.com/DongKeon/Awesome-Speaker-Diarization) — End-to-End/クラスタリング/マルチモーダル等を体系化した論文集(活発) `paper-list` ⭐358 · 📅2026-03
- 🟢 [awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) — OSSのTTS・音声クローン・音楽生成モデル集 `model` ⭐334 · 📅2026-04
- 🟢 [awesome-voice-conversion](https://github.com/JeffC0628/awesome-voice-conversion) — voice conversion(声質変換)のプロジェクト・コミュニティ集 `awesome` ⭐267 · 📅2025-11
- 🟢 [Awesome-Sign-Language-Processing](https://github.com/VIPL-SLP/Awesome-Sign-Language-Processing) — 手話処理(認識/翻訳/生成)の包括リソース集 `awesome` ⭐248 · 📅2026-05
- 🟢 [Awesome-Sign-Language](https://github.com/ZechengLi19/Awesome-Sign-Language) — 手話認識(SLR)・翻訳(SLT)等の論文リスト(活発) `paper-list` ⭐220 · 📅2025-11
- 🟢 [Speech-and-audio-papers-Top-Conference](https://github.com/01Zhangbw/Speech-and-audio-papers-Top-Conference) — トップ会議(INTERSPEECH/ICASSP等)の音声・音響論文を集約 `paper-list` ⭐139 · 📅2026-01
- 🟢 [awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech) — LLMベースのspeech-to-speechモデル/フレームワーク集 `awesome` ⭐56 · 📅2025-11
- 🟢 [Awesome-Large-Speech-Model](https://github.com/huangcanan/Awesome-Large-Speech-Model) — 大規模音声/オーディオモデルの論文・データ・応用・ツール集 `awesome` ⭐28 · 📅2025-11
- 🟡 [awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) — 音楽に応用された深層学習の論文・学位論文集 `paper-list` ⭐3k · 📅2023-12
- 🟡 [awesome-speech-enhancement](https://github.com/WenzheLiu-Speech/awesome-speech-enhancement) — speech enhancement・音源分離・定位の論文/コード/ツール集 `paper-list` ⭐1.2k · 📅2023-11
- 🟡 [INTERSPEECH-2023-24-Papers](https://github.com/DmitryRyumin/INTERSPEECH-2023-24-Papers) — INTERSPEECH 2023-2024の論文を網羅したコレクション `paper-list` ⭐689 · 📅2024-12
- 🟡 [awesome-sound_event_detection](https://github.com/soham97/awesome-sound_event_detection) — Sound AI(音響イベント検出、音声キャプショニング等)の研究リーディングリスト `paper-list` ⭐197 · 📅2024-08
- 🟡 [awesome-speech-emotion-recognition](https://github.com/abikaki/awesome-speech-emotion-recognition) — 音声感情認識(SER)の論文・データセット・ツールの厳選リスト `awesome` ⭐101 · 📅2024-12
- 🟡 [awesome-vad](https://github.com/bigcash/awesome-vad) — VADの実装・ツール・研究を集めたリスト `awesome` ⭐74 · 📅2024-11
- 🟡 [Awesome-Speech-Enhancement](https://github.com/DmitryRyumin/Awesome-Speech-Enhancement) — 音声強調の論文・効果指標を整理したインタラクティブなリスト `paper-list` ⭐27 · 📅2024-04
- 📦 [awesome-tts-samples](https://github.com/seungwonpark/awesome-tts-samples) — 音声サンプル付きTTS論文リスト `paper-list` ⭐61 · 📅2020-08
- 🔴 [awesome-speech-recognition-speech-synthesis-papers](https://github.com/zzw922cn/awesome-speech-recognition-speech-synthesis-papers) — ASR・話者認証・TTS・音声合成・VCを網羅した論文リスト `paper-list` ⭐3.1k · 📅2023-10
- 🔴 [speech-synthesis-paper](https://github.com/wenet-e2e/speech-synthesis-paper) — 音声合成(TTS)論文の体系的リスト `paper-list` ⭐1.1k · 📅2023-07
- 🔴 [Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion](https://github.com/guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion) — 歌声合成(SVS)・歌声変換(SVC)・自動採譜の論文/プロジェクト集 `paper-list` ⭐482 · 📅2022-09
- 🔴 [awesome-keyword-spotting](https://github.com/zycv/awesome-keyword-spotting) — 音声キーワード検出/ウェイクワード検出の論文・実装・データセット集 `awesome` ⭐287 · 📅2022-05
- 🔴 [awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) — 音楽情報学の論文・チュートリアル・ライブラリ・ツールの厳選リスト `awesome` ⭐192 · 📅2023-07
- 🔴 [awesome-speech-translation](https://github.com/dqqcasia/awesome-speech-translation) — 音声翻訳(パイプライン/E2E/ストリーミング/多言語)の論文リスト `paper-list` ⭐179 · 📅2021-11
- 🔴 [awesome-speech-to-speech-translation](https://github.com/Rongjiehuang/awesome-speech-to-speech-translation) — 直接音声間翻訳(S2ST)の論文リスト `paper-list` ⭐39 · 📅2023-01

## 🤖 ロボティクス / Embodied AI

- 🟢 [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — embodied AIのVLA・VLN・マルチモーダル学習の最先端研究集 `paper-list` ⭐3.2k · 📅2026-05
- 🟢 [awesome-robotics-libraries](https://github.com/jslee02/awesome-robotics-libraries) — ロボティクスのライブラリ・ソフトウェアを厳選したリスト `awesome` ⭐2.9k · 📅2026-05
- 🟢 [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — ヒューマノイドロボット学習の論文リスト `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — 身体性AIの知覚・相互作用・エージェント・sim-to-realを網羅(IEEE/ASME ToM 2025) `survey` ⭐2.1k · 📅2026-05
- 🟢 [Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) — LLMを用いたembodied AI/ロボット研究のキュレーション `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome_Quadrupedal_Robots](https://github.com/curieuxjy/Awesome_Quadrupedal_Robots) — 四足歩行ロボットの論文・リソース集 `paper-list` ⭐1.1k · 📅2026-05
- 🟢 [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) — ロボットマニピュレーションの論文・コード集 `paper-list` ⭐988 · 📅2026-05
- 🟢 [Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) — トップ会議採択のEmbodied AI論文を継続収集(2026会議まで反映、活発) `paper-list` ⭐654 · 📅2026-05
- 🟢 [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam) — VLAとWorld Action Model(WAM)研究のキュレーション `awesome` ⭐626 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) — embodied AI向けVLAモデルのサーベイ論文付きリスト `survey` ⭐576 · 📅2026-02
- 🟢 [Awesome-VLA-Robotics](https://github.com/Jiaaqiliu/Awesome-VLA-Robotics) — ロボティクスのVLAモデル論文・モデル・データセット集 `paper-list` ⭐477 · 📅2026-03
- 🟢 [Awesome-Robotics-Diffusion](https://github.com/showlab/Awesome-Robotics-Diffusion) — ロボット学習に拡散モデルを取り入れた最新論文の厳選リスト `paper-list` ⭐335 · 📅2026-05
- 🟢 [Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI) — embodied AIのサーベイ・VLA・データセット・シミュレータ等を網羅 `awesome` ⭐210 · 📅2026-04
- 🟢 [Awesome-VLN](https://github.com/KwanWaiPang/Awesome-VLN) — 視覚言語ナビゲーション(VLN)のサーベイ用論文集 `survey` ⭐136 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) — Vision-Language-Action(VLA)のサーベイ用論文集 `survey` ⭐79 · 📅2026-02
- 🟢 [Awesome-Legged-Robot-Localization-and-Mapping](https://github.com/KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping) — 脚式ロボットのSLAMに関するサーベイ用論文集 `survey` ⭐63 · 📅2026-04
- 🟡 [awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling) — C++/Python/ROSによるプロ向けロボット開発ツールの集約 `awesome` ⭐3.8k · 📅2023-11
- 🟡 [Awesome-Robot-Learning](https://github.com/RayYoh/Awesome-Robot-Learning) — ロボット学習(主にマニピュレーション)のリソース集 `awesome` ⭐202 · 📅2024-08
- 🔴 [awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning) — 脚式ロコモーション学習のリソース集 `awesome` ⭐477 · 📅2023-07

## 🕸️ グラフ学習(GNN) / 知識グラフ

- 🟢 [graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) — グラフ/Transformerベースの不正・異常・外れ値検知論文集 `paper-list` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Knowledge-Graph-Reasoning](https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning) — 知識グラフ推論の論文・コード・データセット集 `paper-list` ⭐1.5k · 📅2025-11
- 🟢 [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) — 時系列・時空間データ向け拡散モデルのサーベイ＆論文集(活発) `survey` ⭐986 · 📅2026-02
- 🟢 [Awesome-DynamicGraphLearning](https://github.com/SpaceLearner/Awesome-DynamicGraphLearning) — 動的(時系列)グラフ・知識グラフ上の機械学習論文集 `paper-list` ⭐709 · 📅2025-06
- 🟢 [awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation) — 生成的な分子モデリング・設計の論文集 `paper-list` ⭐343 · 📅2025-07
- 🟢 [awesome-gnn-systems](https://github.com/ch-wan/awesome-gnn-systems) — GNNシステム・高速化に関するリソース集 `awesome` ⭐342 · 📅2026-05
- 🟢 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection) — 2025年TKDEサーベイ公式リポジトリ。GNNベースのグラフ異常検知論文・データセット `survey` ⭐212 · 📅2026-05
- 🟢 [Awesome-TKGC](https://github.com/jiapuwang/Awesome-TKGC) — 時系列知識グラフ補完(TKGC)の論文・資源を5段階分類で網羅 `paper-list` ⭐115 · 📅2025-10
- 🟢 [awesome-molecular-diffusion-models](https://github.com/AzureLeon1/awesome-molecular-diffusion-models) — 分子拡散モデル関連論文の厳選リスト(活発) `paper-list` ⭐100 · 📅2026-04
- 🟢 [Awesome-Temporal-Graph-Learning](https://github.com/MGitHubL/Awesome-Temporal-Graph-Learning) — temporal graph learning手法(論文・コード・データセット)集 `paper-list` ⭐92 · 📅2025-05
- 📑 [awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) — TKDE論文(対照/生成/予測型)の付随リスト `survey` ⭐1.4k · 📅2024-08
- 📑 [Awesome-GNN4TS](https://github.com/KimMeen/Awesome-GNN4TS) — 時系列解析向けGNN(TPAMI 2024)のリソース集 `survey` ⭐858 · 📅2024-08
- 📑 [awesome-pretrain-on-molecules](https://github.com/junxia97/awesome-pretrain-on-molecules) — 化学事前学習モデル(IJCAI 2023 survey)の論文リスト `survey` ⭐539 · 📅2023-06
- 📑 [Generative_KG_Construction_Papers](https://github.com/zjunlp/Generative_KG_Construction_Papers) — 生成的知識グラフ構築のレビュー(EMNLP 2022)の論文集 `survey` ⭐113 · 📅2023-07
- 📑 [Awesome-Trustworthy-GNNs](https://github.com/Radical3-HeZhang/Awesome-Trustworthy-GNNs) — 信頼できるGNN(プライバシ/頑健性/公平性/説明性)サーベイ(Proc. IEEE 2024) `survey` ⭐98 · 📅2024-07
- 🟡 [GNNPapers](https://github.com/thunlp/GNNPapers) — グラフニューラルネットワーク(GNN)の必読論文集(定番) `paper-list` ⭐16.8k · 📅2023-12
- 🟡 [Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) — グラフニューラルネットワークの論文リスト `paper-list` ⭐2.3k · 📅2023-12
- 🟡 [awesome-self-supervised-gnn](https://github.com/ChandlerBang/awesome-self-supervised-gnn) — GNNの事前学習・自己教師あり学習の論文集 `paper-list` ⭐1.7k · 📅2024-02
- 🟡 [GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) — 交通予測向けGNN論文・コードの大規模コレクション `paper-list` ⭐1.2k · 📅2024-08
- 🟡 [awesome-graph-transformer](https://github.com/wehos/awesome-graph-transformer) — グラフトランスフォーマーの論文集 `paper-list` ⭐929 · 📅2025-03
- 🟡 [PromptKG](https://github.com/zjunlp/PromptKG) — プロンプト学習・知識グラフ関連の研究・ツール・論文ギャラリー `paper-list` ⭐734 · 📅2024-03
- 🟡 [awesome-graph-generation](https://github.com/yuanqidu/awesome-graph-generation) — グラフ・分子生成の論文を網羅した最新リスト `paper-list` ⭐360 · 📅2025-01
- 🟡 [Awesome-Hypergraph-Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network) — ハイパーグラフ学習・理論・データ・ツールの厳選集 `awesome` ⭐331 · 📅2025-02
- 🟡 [awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) — 低分子創薬向け機械学習リソースの厳選集 `awesome` ⭐241 · 📅2023-11
- 🟡 [Awesome-Fair-Graph-Learning](https://github.com/EdisonLeeeee/Awesome-Fair-Graph-Learning) — 公平なグラフ学習(FairGL)の論文リスト `paper-list` ⭐144 · 📅2024-09
- 🟡 [awesome-expressive-gnn](https://github.com/mengliu1998/awesome-expressive-gnn) — GNNの表現力に関する研究・改善論文集 `paper-list` ⭐124 · 📅2023-11
- 🟡 [Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) — グラフOOD(汎化・訓練時/テスト時適応)の論文リスト `paper-list` ⭐85 · 📅2024-10
- 🟡 [Awesome-GNN-based-drug-discovery](https://github.com/gozsari/Awesome-GNN-based-drug-discovery) — GNNによる創薬(論文・データセット・ツール)の厳選リスト `awesome` ⭐63 · 📅2024-04
- 🟡 [HGNN_Collection](https://github.com/PolarisRisingWar/HGNN_Collection) — 異種グラフNNのデータセット・アルゴリズム集 `paper-list` ⭐61 · 📅2024-05
- 🟡 [awesome-GNN-social-recsys](https://github.com/claws-lab/awesome-GNN-social-recsys) — GNNベースのソーシャル推薦論文集 `paper-list` ⭐53 · 📅2024-05
- 🔴 [awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification) — グラフ埋め込み・分類・表現学習の重要論文集(実装付) `paper-list` ⭐4.8k · 📅2023-03
- 🔴 [awesome-network-embedding](https://github.com/chihming/awesome-network-embedding) — ネットワーク埋め込み手法の定番厳選リスト `awesome` ⭐2.6k · 📅2020-12
- 🔴 [knowledge-graphs](https://github.com/shaoxiongji/knowledge-graphs) — 知識グラフ研究(埋め込み・補完・時系列KG・応用)の論文集 `paper-list` ⭐1.8k · 📅2022-10
- 🔴 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection) — 深層学習によるグラフ異常検知の論文・データセット・実装集 `awesome` ⭐384 · 📅2023-07
- 🔴 [awesome-graph-ood](https://github.com/THUMNLab/awesome-graph-ood) — グラフのOOD汎化に関する論文集 `paper-list` ⭐169 · 📅2023-06

## 🛒 推薦システム(RecSys)

- 🟢 [RSPapers](https://github.com/hongleizhang/RSPapers) — 推薦システム必読論文を17カテゴリで整理、毎週更新(LLM/Agentic RS等も追加) `awesome` ⭐6.5k · 📅2026-03
- 🟢 [Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) — 検索・推薦・広告向け深層学習論文集 `paper-list` ⭐2.5k · 📅2026-04
- 🟢 [Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys) — LLM関連の推薦システム論文集(TOIS採録サーベイ付き) `survey` ⭐1.5k · 📅2026-01
- 🟢 [Awesome-LLM4RS-Papers](https://github.com/nancheng58/Awesome-LLM4RS-Papers) — LLM強化推薦システムの論文集 `paper-list` ⭐762 · 📅2026-03
- 🟢 [Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) — コールドスタート推薦のリソース集(LLM時代のサーベイ付き) `survey` ⭐283 · 📅2026-03
- 📑 [LLM4Rec-Awesome-Papers](https://github.com/WLiK/LLM4Rec-Awesome-Papers) — LLMを用いた推薦システムの論文・リソース集(サーベイ付き) `survey` ⭐2.3k · 📅2025-03
- 📑 [RecDebiasing](https://github.com/jiawei-chen/RecDebiasing) — TOIS 2023「Bias and Debias in Recommender System: A Survey」のバイアス除去手法集 `survey` ⭐462 · 📅2024-02
- 📑 [Awesome-SSLRec-Papers](https://github.com/HKUDS/Awesome-SSLRec-Papers) — ACM CSUR「Self-Supervised Learning for Recommendation」サーベイのcompanion `survey` ⭐122 · 📅2024-08
- 🟡 [Awesome-Sequence-Modeling-for-Recommendation](https://github.com/AiHubCN/Awesome-Sequence-Modeling-for-Recommendation) — 系列推薦・系列モデリングの論文集 `paper-list` ⭐39 · 📅2023-11
- 🔴 [Awesome-RSPapers](https://github.com/RUCAIBox/Awesome-RSPapers) — 推薦システム論文の網羅的リスト `paper-list` ⭐989 · 📅2022-10
- 🔴 [CRSPapers](https://github.com/RUCAIBox/CRSPapers) — 対話型推薦システム(CRS)の論文リスト `paper-list` ⭐80 · 📅2022-11
- 🔴 [Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems](https://github.com/YuyingZhao/Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems) — 推薦システムの公平性・多様性研究を包括的に整理 `paper-list` ⭐25 · 📅2023-06

## 📈 時系列(Time Series)

- 🟢 [awesome-time-series-papers](https://github.com/TSCenter/awesome-time-series-papers) — トップAI会議の最新時系列論文・コード集 `paper-list` ⭐994 · 📅2026-04
- 🟢 [Awesome_Imputation](https://github.com/WenjieDu/Awesome_Imputation) — 時系列の欠損値補完(imputation)の論文・手法を集めたサーベイリポジトリ `survey` ⭐420 · 📅2026-03
- 🟢 [awesome-time-series-forecasting](https://github.com/TongjiFinLab/awesome-time-series-forecasting) — 時系列予測の論文・コード集 `paper-list` ⭐262 · 📅2026-04
- 🟢 [Awesome-Anomaly-Detection-Foundation-Models](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) — 基盤モデルによる異常検知の論文集 `paper-list` ⭐194 · 📅2026-05
- 🟢 [awesome-multivariate-time-series-anomaly-detection-algorithms](https://github.com/lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms) — 多変量時系列異常検知の論文リスト `paper-list` ⭐76 · 📅2025-09
- 🟢 [awesome-time-series-analysis](https://github.com/qhliu26/awesome-time-series-analysis) — 時系列の論文・ベンチマーク・データセット・チュートリアル集 `awesome` ⭐65 · 📅2025-09
- 📑 [time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) — 時系列向けTransformerのリソース(論文・コード・データ)を専門的にまとめたレビュー `survey` ⭐3k · 📅2024-08
- 🟡 [awesome-TS-anomaly-detection](https://github.com/rob-med/awesome-TS-anomaly-detection) — 時系列データの異常検知ツール・データセットのリスト `awesome` ⭐3.2k · 📅2024-10
- 🟡 [awesome-AI-for-time-series-papers](https://github.com/qingsongedu/awesome-AI-for-time-series-papers) — トップ会議・ジャーナルの時系列AI論文・チュートリアル・サーベイ集 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) — 時系列・時空間・イベントデータ向けLLM/基盤モデルの論文集 `paper-list` ⭐1.2k · 📅2024-12
- 🟡 [Awesome-TimeSeries-LLM-FM](https://github.com/start2020/Awesome-TimeSeries-LLM-FM) — 時系列タスク向けLLM・基盤モデルのリソース集 `paper-list` ⭐154 · 📅2024-06
- 🟡 [Awesome-Large-Models-for-Time-Series](https://github.com/SJTU-DMTai/Awesome-Large-Models-for-Time-Series) — 時系列解析向けLLM・基盤モデルの論文集 `paper-list` ⭐47 · 📅2024-10

## 🦾 AIエージェント / LLM Agents

- 🟢 [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) — 86ページのサーベイ「The Rise and Potential of LLM Based Agents」の論文リスト `survey` ⭐8.1k · 📅2025-09
- 🟢 [LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) — LLMエージェントの必読論文集 `paper-list` ⭐3k · 📅2026-04
- 🟢 [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) — LLMエージェントの手法・応用・課題サーベイの論文集 `survey` ⭐2.7k · 📅2025-11
- 🟢 [LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) — LLMベースエージェント関連論文のリスト `paper-list` ⭐2.3k · 📅2025-07
- 🟢 [awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) — マルチエージェント論文のキュレーション集(Swarms team) `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — LLMエージェントフレームワークの厳選リスト `awesome` ⭐1.5k · 📅2026-05
- 🟢 [Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) — マルチモーダルGUIエージェントの論文・リソース集 `paper-list` ⭐1.2k · 📅2025-08
- 🟢 [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) — LLM駆動の自律エージェントコレクション `awesome` ⭐1.1k · 📅2026-05
- 🟢 [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — AIエージェント研究論文集(工学・メモリ・評価・ワークフロー) `paper-list` ⭐897 · 📅2026-05
- 🟢 [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) — GUIエージェント論文の厳選リスト `paper-list` ⭐803 · 📅2026-05
- 🟢 [awesome-computer-use](https://github.com/ranpox/awesome-computer-use) — Computer-use GUIエージェントの動画・ブログ・論文・プロジェクト集 `awesome` ⭐557 · 📅2026-04
- 🟢 [Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) — 言語エージェントの記憶(ユーザプロファイル・対話履歴)に関する論文集 `paper-list` ⭐518 · 📅2026-05
- 🟢 [awesome-ui-agents](https://github.com/opendilab/awesome-ui-agents) — Web/App/OSを横断するUIエージェント資源の継続更新リスト `awesome` ⭐300 · 📅2026-05
- 🟢 [Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) — グラフベースのエージェント記憶のサーベイ・論文・ベンチマーク集 `survey` ⭐277 · 📅2026-04
- 🟡 [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI自律エージェント(プロジェクト/フレームワーク)の大規模リスト `awesome` ⭐28k · 📅2025-02
- 🟡 [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) — LLM駆動エージェントの論文・リポジトリ・ブログ集 `awesome` ⭐2.2k · 📅2025-04
- 🟡 [LLM-Planning-Papers](https://github.com/AGI-Edgerunners/LLM-Planning-Papers) — LLMのプランニング(planning)に関する必読論文集 `paper-list` ⭐440 · 📅2024-07
- 🟡 [awesome-llm-agents](https://github.com/junhua/awesome-llm-agents) — LLMエージェントの高品質論文・OSSプロジェクト集 `paper-list` ⭐84 · 📅2024-11
- 🟡 [Multi-Agent-Papers](https://github.com/shizhl/Multi-Agent-Papers) — 複雑タスク向けマルチエージェント協調の必読論文集 `paper-list` ⭐72 · 📅2023-11
- 🟡 [Awesome-LLM-based-MultiAgents](https://github.com/Andrewzh112/Awesome-LLM-based-MultiAgents) — LLMベースのマルチエージェント論文集 `paper-list` ⭐27 · 📅2024-10

## 🔬 医療AI / AI for Science

- 🟢 [MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) — 医療LLM実践ガイド(Nature Reviews Bioengineering掲載) `survey` ⭐2k · 📅2025-09
- 🟢 [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) — 物理・化学・生物・材料など科学的発見を加速するAIツール・論文集 `awesome` ⭐1.6k · 📅2026-05
- 🟢 [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration) — 画像レジストレーション全般の書籍・論文・ツールボックス集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — 医用画像へのマルチモーダル学習応用のリソース集 `awesome` ⭐960 · 📅2026-02
- 🟢 [Awesome-Healthcare-Foundation-Models](https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models) — ヘルスケア基盤モデルの論文コレクション `paper-list` ⭐515 · 📅2026-04
- 🟢 [awesome-foundation-model-single-cell-papers](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) — シングルセル基盤モデルに特化した論文リスト `paper-list` ⭐449 · 📅2026-01
- 🟢 [Awesome-Radiology-Report-Generation](https://github.com/mk-runner/Awesome-Radiology-Report-Generation) — 放射線レポート生成の論文・データセット・ツール集(非常に活発) `paper-list` ⭐436 · 📅2026-05
- 🟢 [Awesome-Medical-Large-Language-Models](https://github.com/burglarhobbit/Awesome-Medical-Large-Language-Models) — 医療・ヘルスケア領域のLLM論文を厳選したコレクション `paper-list` ⭐392 · 📅2025-05
- 🟢 [Awesome-LWMs](https://github.com/jaychempan/Awesome-LWMs) — 大規模気象モデル(LWMs)コレクション(AI4Earth) `awesome` ⭐360 · 📅2025-06
- 🟢 [awesome-AI4MolConformation-MD](https://github.com/AspirinCode/awesome-AI4MolConformation-MD) — 生成AI/深層学習による分子コンフォメーション・分子動力学の論文集 `paper-list` ⭐295 · 📅2026-05
- 🟢 [Awesome-Earth-Artificial-Intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) — 地球科学AIのチュートリアル・ソフト・データセット・論文集 `awesome` ⭐244 · 📅2026-05
- 🟢 [awesome-mmps](https://github.com/willxxy/awesome-mmps) — EEG/ECG/EMG等の生理信号×機械学習の資源・データセット集(活発) `awesome` ⭐159 · 📅2026-02
- 🟢 [Awesome-Active-Learning-for-Medical-Image-Analysis](https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis) — 医用画像解析の能動学習サーベイ論文・コード `survey` ⭐134 · 📅2025-06
- 🟢 [MedImgReg_Survey](https://github.com/JHU-MedImage-Reg/MedImgReg_Survey) — 学習ベース医用画像レジストレーションの論文集+損失関数/評価指標の実装 `survey` ⭐121 · 📅2025-05
- 🟢 [awesome-pathology](https://github.com/open-pathology/awesome-pathology) — デジタル/計算病理の資源(自己教師あり・特徴抽出・データセット等)を網羅 `awesome` ⭐119 · 📅2026-02
- 🟢 [awesome-drug-discovery](https://github.com/yboulaamane/awesome-drug-discovery) — 計算創薬手法に特化した厳選リソースリスト `awesome` ⭐112 · 📅2026-05
- 🟢 [SurvivalAnalysisPapers](https://github.com/shi-ang/SurvivalAnalysisPapers) — 生存時間解析の論文・資源をカテゴリ別に整理(活発) `paper-list` ⭐90 · 📅2026-05
- 🟢 [Awesome-DL-for-Medical-Imaging-Segmentation](https://github.com/faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation) — 医用画像セグメンテーションの深層学習論文集 `paper-list` ⭐66 · 📅2026-02
- 🟢 [awesome-bci-reviews](https://github.com/okbalefthanded/awesome-bci-reviews) — BCIの査読済みレビュー・サーベイを年代順に整理(活発) `survey` ⭐47 · 📅2025-08
- 🟢 [AwesomeWSI](https://github.com/BearCleverProud/AwesomeWSI) — WSI解析と病理基盤モデルの包括的コレクション(IJCAI 2025サーベイ準拠、活発) `survey` ⭐35 · 📅2026-02
- 🟢 [Awesome-Generative-Models-in-Pathology](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology) — 病理における生成モデル(画像合成・レポート生成・クロスモーダル)150本超のサーベイ `survey` ⭐27 · 📅2025-10
- 🟢 [Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) — 医療向けエージェントAIの最新サーベイ集 `paper-list` ⭐23 · 📅2026-03
- 🟢 [Awesome-MICCAI-2026](https://github.com/ambicuity/Awesome-MICCAI-2026) — MICCAI 2026論文をarXivから自動収集しbotが毎日更新、分野別分類 `paper-list` ⭐20 · 📅2026-05
- 🟢 [Awesome-AI4BCI](https://github.com/Deepak-Mewada/Awesome-AI4BCI) — 脳信号エンコーディング/デコーディングの深層学習モデル資源集 `paper-list` ⭐17 · 📅2025-09
- 📑 [Awesome-Foundation-Models-in-Medical-Imaging](https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging) — 医用画像の視覚・言語基盤モデルの厳選リスト `survey` ⭐301 · 📅2024-06
- 📑 [Awesome-Foundation-Models-for-Weather-and-Climate](https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate) — 気象・気候データ理解向け基盤モデルの包括サーベイ `survey` ⭐293 · 📅2025-02
- 📑 [Awesome-Foundation-Models-for-Advancing-Healthcare](https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare) — ヘルスケア基盤モデル(HFM)の課題・機会・将来展望の包括レビュー `survey` ⭐251 · 📅2024-12
- 📑 [DL-ECG-Review](https://github.com/hsd1503/DL-ECG-Review) — ECGの深層学習手法レビューと論文サマリ表 `survey` ⭐250 · 📅2020-10
- 🟡 [MICCAI-OpenSourcePapers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) — MICCAI 2019-2023のオープンソース論文をコードリンク付き表で整理 `paper-list` ⭐1.3k · 📅2023-11
- 🟡 [awesome-deep-learning-single-cell-papers](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) — シングルセル解析×深層学習の最新論文を30以上のタスク別に整理 `paper-list` ⭐856 · 📅2025-04
- 🟡 [awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning) — タンパク質表現学習(AlphaFold含む)の論文集 `paper-list` ⭐685 · 📅2024-11
- 🟡 [awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design) — AIベースのタンパク質設計の研究論文集 `paper-list` ⭐306 · 📅2024-05
- 🟡 [Awesome-LLM-Healthcare](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) — 医療分野のLLMレビュー論文に対応した論文リスト `paper-list` ⭐268 · 📅2023-12
- 🟡 [Awesome-Neuron-Segmentation-in-EM-Images](https://github.com/subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images) — 電子顕微鏡(EM)画像における神経突起の3Dセグメンテーション資源集 `awesome` ⭐57 · 📅2024-03
- 🟡 [awesome-molecule-protein-pretrain-papers](https://github.com/OmicsML/awesome-molecule-protein-pretrain-papers) — 分子・タンパク質の事前学習論文集(創薬・ドッキング) `paper-list` ⭐47 · 📅2024-03
- 🟡 [Awesome_AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) — 地球システム(特に気象・気候)の機械学習論文集 `paper-list` ⭐14 · 📅2023-12
- 🔴 [awesome-ehr-deeplearning](https://github.com/hurcy/awesome-ehr-deeplearning) — EHRマイニング・機械学習・深層学習論文集 `awesome` ⭐428 · 📅2022-10
- 🔴 [Physiological-Signal-Classification-Papers](https://github.com/ziyujia/Physiological-Signal-Classification-Papers) — EEG/ECG/EMG/EOGの分類論文をタスク別に整理 `paper-list` ⭐249 · 📅2022-07
- 🔴 [awesome-radiology-report-generation](https://github.com/zhjohnchan/awesome-radiology-report-generation) — 放射線/医療レポート生成と関連領域のキュレーションリスト `awesome` ⭐180 · 📅2022-05
- 🔴 [awesome-structural-bioinformatics](https://github.com/twoXes/awesome-structural-bioinformatics) — 構造バイオインフォマティクスのリソース集 `awesome` ⭐79 · 📅2023-05
- 🔴 [awesome-bio-chatgpt](https://github.com/OmicsML/awesome-bio-chatgpt) — 生物学・医療分野へのChatGPT/LLM応用の論文・資源集 `paper-list` ⭐22 · 📅2023-04

## 🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学)

- 🟢 [techniques](https://github.com/satellite-image-deep-learning/techniques) — 衛星・航空画像の深層学習手法の超大規模リファレンス `awesome` ⭐10.2k · 📅2026-05
- 🟢 [awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) — 金融市場のLLM・深層学習戦略・ツールの定番リスト `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — 機械学習に重点を置いたクオンツ/アルゴリズム取引のリソース集 `awesome` ⭐3.7k · 📅2025-05
- 🟢 [Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) — コード向け言語モデル研究とデータセットの網羅的キュレーション `paper-list` ⭐3.4k · 📅2026-05
- 🟢 [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) — RS変化検出のデータセット・手法・サーベイ集 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Remote-Sensing-Foundation-Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) — RSFMの論文・データセット・ベンチ・事前学習重みを網羅(活発) `paper-list` ⭐1.8k · 📅2026-05
- 🟢 [awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) — 農業・農場・園芸向けOSS技術(ML・GIS・リモセン・ロボティクス含む)の定番リスト `awesome` ⭐1.8k · 📅2026-01
- 🟢 [awesome-search](https://github.com/frutik/awesome-search) — EC検索を中心にセマンティック検索・LTR・クエリ理解・検索品質を網羅 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) — 原子論的機械学習プロジェクト約510件をスコア付きランキング(活発) `awesome` ⭐690 · 📅2026-05
- 🟢 [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) — 数学・物理・化学・材料・生物・地球科学等の科学ドメイン事前学習モデルの包括サーベイ `survey` ⭐660 · 📅2025-06
- 🟢 [awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) — 現代材料科学におけるマテリアルズ・インフォマティクスの取り組み集 `awesome` ⭐515 · 📅2026-03
- 🟢 [awesome-digital-humanities](https://github.com/dh-tech/awesome-digital-humanities) — 人文学者向けの定量的・計算的手法ソフト集(NLP・トピックモデル・テキスト解析) `awesome` ⭐383 · 📅2026-05
- 🟢 [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) — 要件・開発・テスト・保守までSE全領域のLLM論文を整理 `survey` ⭐329 · 📅2026-04
- 🟢 [awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) — 判決予測・契約分類・判例検索・法務QA等のLegalNLPリソース集 `awesome` ⭐325 · 📅2025-10
- 🟢 [DL4TP](https://github.com/zhaoyu-li/DL4TP) — 定理証明への深層学習の調査。autoformalization・proof search等で分類 `survey` ⭐224 · 📅2025-05
- 🟢 [awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) — トップ会議・ジャーナルの教育向けAI/LLM論文を収集 `paper-list` ⭐186 · 📅2026-04
- 🟢 [awesome-pinns](https://github.com/AI-in-Transportation-Lab/awesome-pinns) — PINN/物理情報機械学習のライブラリ・論文・チュートリアル厳選集 `awesome` ⭐110 · 📅2026-05
- 🟢 [PINN_Paper_List](https://github.com/Event-AHU/PINN_Paper_List) — 物理情報ニューラルネットワーク(PINN)の論文リスト `paper-list` ⭐77 · 📅2026-04
- 📑 [FinLLMs](https://github.com/adlnlp/FinLLMs) — 論文「Large Language Models in Finance」の関連研究・ベンチ・データセット集 `survey` ⭐370 · 📅2025-04
- 📑 [awesome-RSFMs](https://github.com/xiaoaoran/awesome-RSFMs) — サーベイ「Foundation Models for Remote Sensing and Earth Observation」公式リポジトリ `survey` ⭐50 · 📅2024-11
- 🟡 [PINNpapers](https://github.com/idrl-lab/PINNpapers) — PINNの必読論文集。並列化・加速・転移学習・不確実性定量化・応用で整理 `paper-list` ⭐1.5k · 📅2023-12
- 🟡 [LLM4SoftwareTesting](https://github.com/LLM-Testing/LLM4SoftwareTesting) — LLMを用いたテスト生成・テスト補完等の論文集 `paper-list` ⭐529 · 📅2024-01
- 🟡 [awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) — 電子設計自動化(EDA・チップ設計)へのAI応用論文集 `paper-list` ⭐208 · 📅2023-12
- 🟡 [awesome-ai4lam](https://github.com/AI4LAM/awesome-ai4lam) — 図書館・文書館・博物館(GLAM/LAM)向けAIのプロジェクト・事例・リソース集(AI4LAMコミュニティ運営) `awesome` ⭐178 · 📅2024-06
- 🟡 [Awesome-LLM4Math](https://github.com/tongyx361/Awesome-LLM4Math) — LLM数学推論の高品質厳選リスト。学習データ・SFT・RL・ベンチを整理 `paper-list` ⭐157 · 📅2024-07
- 🟡 [Awesome-Education-LLM](https://github.com/Geralt-Targaryen/Awesome-Education-LLM) — 教育向けLLM研究・応用(教授支援・問題生成・自動採点等)の整理 `paper-list` ⭐77 · 📅2024-09
- 🟡 [LLM_X_papers](https://github.com/czyssrs/LLM_X_papers) — 金融・医療・法務のLLM論文を継続更新する読書リスト `paper-list` ⭐54 · 📅2025-02
- 🔴 [awesome-machine-learning-on-source-code](https://github.com/src-d/awesome-machine-learning-on-source-code) — ソースコードに適用した機械学習(MLonCode)の論文・リンク集 `awesome` ⭐6.6k · 📅2020-12
- 🔴 [Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) — 司法AI向けのコーパス・ベンチ・QA・要約データセットを集約 `awesome` ⭐303 · 📅2023-07
- 🔴 [awesome-program](https://github.com/shaohua0116/awesome-program) — プログラム合成・帰納・実行・修復・programmatic RLの論文集 `paper-list` ⭐168 · 📅2021-10
- 🔴 [Awesome-Precision-Agriculture](https://github.com/px39n/Awesome-Precision-Agriculture) — UAV・深層学習による収量予測・作物検出・雑草検出等の論文集 `paper-list` ⭐137 · 📅2020-09
- 🔴 [awesome-ai4chem](https://github.com/sherrylixuecheng/awesome-ai4chem) — 化学向けAI論文のキュレーション `paper-list` ⭐49 · 📅2023-05
- 🔴 [Awesome-Sports-Analytics](https://github.com/wywyWang/Awesome-Sports-Analytics) — サッカー・バスケ・バドミントン等のスポーツ分析論文/コード集 `paper-list` ⭐20 · 📅2023-03

## 🚗 自動運転(Autonomous Driving)

- 🟢 [Birds-eye-view-Perception](https://github.com/OpenDriveLab/Birds-eye-view-Perception) — BEV知覚研究とクックブック(IEEE T-PAMI 2023) `survey` ⭐1.4k · 📅2025-07
- 🟢 [Awesome-Trajectory-Motion-Prediction-Papers](https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers) — 軌道・運動予測の包括的論文集 `paper-list` ⭐1.1k · 📅2026-01
- 📑 [Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) — データ中心の自動運転サーベイの公式リポジトリ `survey` ⭐180 · 📅2024-03
- 🟡 [awesome-lane-detection](https://github.com/amusi/awesome-lane-detection) — 車線検出(lane detection)の論文リスト `paper-list` ⭐3k · 📅2024-08
- 🟡 [Awesome-Interaction-Aware-Trajectory-Prediction](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction) — 相互作用を考慮した軌道予測の最先端研究資料集 `paper-list` ⭐1.7k · 📅2024-09
- 🟡 [Awesome-Autonomous-Driving](https://github.com/autodriving-heart/Awesome-Autonomous-Driving) — 自動運転全般のawesomeリスト `awesome` ⭐1.1k · 📅2024-08
- 🟡 [awesome-knowledge-driven-AD](https://github.com/PJLab-ADG/awesome-knowledge-driven-AD) — 知識駆動型自動運転の厳選論文集 `paper-list` ⭐501 · 📅2024-06
- 🟡 [Awesome-Autonomous-Driving](https://github.com/PeterJaq/Awesome-Autonomous-Driving) — 自動運転全般の広範なリスト `awesome` ⭐353 · 📅2024-08
- 🟡 [Awesome-occupancy-perception](https://github.com/autodriving-heart/Awesome-occupancy-perception) — 占有知覚(Occupancy)論文コレクション `paper-list` ⭐308 · 📅2024-08
- 🟡 [CVPR-2024-Papers-Autonomous-Driving](https://github.com/autodriving-heart/CVPR-2024-Papers-Autonomous-Driving) — CVPR 2024の自動運転関連論文リスト `paper-list` ⭐257 · 📅2024-08
- 🟡 [CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI](https://github.com/autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI) — CVPR 2025の自動運転・身体性AI関連論文リスト `paper-list` ⭐29 · 📅2025-04
- 🟡 [Awesome-4D-Radar](https://github.com/autodriving-heart/Awesome-4D-Radar) — 4Dレーダ知覚に関する論文・リソース集 `paper-list` ⭐12 · 📅2024-02
- 🔴 [awesome-end-to-end-autonomous-driving](https://github.com/opendilab/awesome-end-to-end-autonomous-driving) — End-to-End自動運転の資源を継続更新するリスト `awesome` ⭐493 · 📅2023-08
- 🔴 [Awesome-Occupancy-Prediction-Autonomous-Driving](https://github.com/chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving) — マルチカメラ意味的占有予測論文(Occ3D等) `paper-list` ⭐263 · 📅2023-07
- 🔴 [awesome-driving-behavior-prediction](https://github.com/opendilab/awesome-driving-behavior-prediction) — 運転行動予測の研究論文集 `paper-list` ⭐83 · 📅2022-12
- 🔴 [Awesome-BEV-Perception](https://github.com/autodriving-heart/Awesome-BEV-Perception) — BEV知覚の厳選論文コレクション `paper-list` ⭐32 · 📅2023-06
- 🔴 [Awesome-Trajectory-Prediction](https://github.com/autodriving-heart/Awesome-Trajectory-Prediction) — 軌道予測の論文コレクション `paper-list` ⭐27 · 📅2023-06
- 🔴 [Awesome-BEV-Perception](https://github.com/ylhua/Awesome-BEV-Perception) — BEV知覚関連論文(BEVFormer, PETRv2, FIERY等) `paper-list` ⭐5 · 📅2022-08

## 🛡️ AI安全性 / Alignment / 解釈性

- 🟢 [awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) — 責任あるML・解釈性の総合リソースリスト `awesome` ⭐4k · 📅2026-05
- 🟢 [Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) — LLM安全性の論文・記事・データセット・ベンチマーク集 `awesome` ⭐1.9k · 📅2026-05
- 🟢 [awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) — ICDM/KDD/SDM等の不正検知データマイニング論文の定番リスト `paper-list` ⭐1.8k · 📅2026-01
- 🟢 [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) — 説明可能AI/MLの研究資料集 `paper-list` ⭐1.6k · 📅2026-03
- 🟢 [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) — LLMセキュリティのツール・文献・プロジェクト集 `awesome` ⭐1.6k · 📅2025-08
- 🟢 [TAADpapers](https://github.com/thunlp/TAADpapers) — テキストの敵対的攻撃・防御(TAAD)の必読論文集 `paper-list` ⭐1.6k · 📅2025-06
- 🟢 [Awesome-Jailbreak-on-LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) — LLMジェイルブレイク手法の論文・コード・データセット・評価集(非常に活発) `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) — 機械unラーニングのサーベイ公式リスト。手法・データセット・評価指標を網羅 `awesome` ⭐950 · 📅2026-05
- 🟢 [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) — LLMの機械unラーニング論文・サーベイ・ベンチマーク集 `paper-list` ⭐591 · 📅2026-05
- 🟢 [awesome-trustworthy-deep-learning](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning) — OOD汎化・敵対的サンプル・バックドア等の信頼性論文(毎日更新) `paper-list` ⭐386 · 📅2026-05
- 🟢 [membership-inference-machine-learning-literature](https://github.com/HongshengHu/membership-inference-machine-learning-literature) — メンバーシップ推論攻撃に特化した文献集 `paper-list` ⭐371 · 📅2026-04
- 🟢 [Awesome-AI-for-cybersecurity](https://github.com/Billy1900/Awesome-AI-for-cybersecurity) — ネットワーク侵入検知・アンチマルウェア・WAF・不正対策を網羅したAIリスト `awesome` ⭐254 · 📅2026-05
- 🟢 [Awesome-model-inversion-attack](https://github.com/AndrewZhou924/Awesome-model-inversion-attack) — モデル反転攻撃サーベイの公式リスト。CV/グラフ/NLP別に整理 `paper-list` ⭐221 · 📅2026-04
- 🟢 [Awesome-LMMs-Mechanistic-Interpretability](https://github.com/itsqyh/Awesome-LMMs-Mechanistic-Interpretability) — 大規模多モーダルモデルの内部表現を扱う機械的解釈性資源集(活発) `survey` ⭐203 · 📅2026-03
- 🟢 [Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) — 生成AIのunラーニング論文をモダリティ・用途別に整理 `paper-list` ⭐188 · 📅2026-04
- 🟢 [OpenRedTeaming](https://github.com/Libr-AI/OpenRedTeaming) — LLM/マルチモーダルのレッドチーミング論文集(30+手法実装) `paper-list` ⭐165 · 📅2025-05
- 🟢 [Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) — 生成AIモデル向け電子透かし手法を画像・音声・テキスト別に整理(活発) `awesome` ⭐140 · 📅2026-05
- 🟢 [awesome-mechanistic-interpretability](https://github.com/AI-in-Transportation-Lab/awesome-mechanistic-interpretability) — ニューラルネットを理解可能な計算要素へ逆解析する機械的解釈性のリソース集 `awesome` ⭐97 · 📅2026-05
- 🟢 [awesome-fraud-detection](https://github.com/AI4Risk/awesome-fraud-detection) — GNNによる金融不正検知のサーベイ付き論文・コード集(活発) `paper-list` ⭐43 · 📅2026-05
- 📑 [Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers) — LLM安全性のサーベイ論文リスト `survey` ⭐56 · 📅2024-12
- 🟡 [awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) — マルウェア・侵入検知等にMLを使うツール・論文・教材の定番リスト `awesome` ⭐8.8k · 📅2024-08
- 🟡 [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) — プロンプトインジェクションに対する実用・提案済み防御策を網羅 `awesome` ⭐696 · 📅2025-02
- 🟡 [awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) — メンバーシップ推論・モデル反転・属性推論・モデル抽出を網羅した論文リスト `awesome` ⭐639 · 📅2024-03
- 🟡 [Awesome-Backdoor-in-Deep-Learning](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning) — 深層学習のバックドア攻撃と防御を攻撃種別・防御段階で整理した論文集(活発) `paper-list` ⭐238 · 📅2024-03
- 🟡 [awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) — AI品質・安全性に関する論文と技術記事のキュレーションリスト `paper-list` ⭐215 · 📅2025-04
- 🟡 [trojai-literature](https://github.com/usnistgov/trojai-literature) — NISTが運営するAIトロイの木馬攻撃研究文献の総覧 `paper-list` ⭐149 · 📅2024-10
- 🟡 [Learning-Deep-Hiding](https://github.com/TracyCuiq/Learning-Deep-Hiding) — 画像ステガノグラフィと電子透かしを含む「deep hiding」論文を体系整理 `paper-list` ⭐67 · 📅2024-06
- 🟡 [Constitutional-AI-awesome-papers](https://github.com/minbeomkim/Constitutional-AI-awesome-papers) — Constitutional AI/倫理指針下のAIに関する論文リスト `paper-list` ⭐13 · 📅2024-03
- 🔴 [awesome-adversarial-machine-learning](https://github.com/yenchenlin/awesome-adversarial-machine-learning) — 敵対的機械学習の論文・ブログ・講演を集めた古典的キュレーション `awesome` ⭐1.9k · 📅2020-11
- 🔴 [awesome-interpretable-machine-learning](https://github.com/lopusz/awesome-interpretable-machine-learning) — 解釈可能機械学習のリソースリスト `awesome` ⭐916 · 📅2023-03
- 🔴 [awesome-fairness-in-ai](https://github.com/datamllab/awesome-fairness-in-ai) — AIにおける公平性リソースの厳選集 `awesome` ⭐334 · 📅2023-09
- 🔴 [awesome-xai](https://github.com/altamiracorp/awesome-xai) — 説明可能AI(XAI)・解釈可能MLの論文とリソース `awesome` ⭐188 · 📅2021-05
- 🔴 [awesome-ai-alignment](https://github.com/dit7ya/awesome-ai-alignment) — AIアライメント研究の優れたリソースのキュレーションリスト `awesome` ⭐81 · 📅2023-07
- 🔴 [awesome-ml-fairness](https://github.com/brandeis-machine-learning/awesome-ml-fairness) — 機械学習の公平性に関する論文・リソース集 `paper-list` ⭐74 · 📅2023-05
- 🔴 [awesome-ai-safety](https://github.com/hari-sikchi/awesome-ai-safety) — AI安全性の論文・プロジェクト・コミュニティのリスト `awesome` ⭐64 · 📅2020-02
- 🔴 [awesome-data-poisoning](https://github.com/ch-shin/awesome-data-poisoning) — トップ会議のデータポイズニング攻撃・防御論文集 `awesome` ⭐25 · 📅2022-09
- 🔴 [Awesome-Adversarial-Training](https://github.com/KululuMi/Awesome-Adversarial-Training) — FGSM/PGD/TRADES/AutoAttack等の敵対的訓練論文リスト `paper-list` ⭐6 · 📅2022-04

## ⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction

- 🟢 [awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) — 各国のAI規制・ガイドライン・倫理規範・標準を地域別に網羅 `awesome` ⭐1.4k · 📅2026-05
- 🟢 [awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) — 計算社会科学の書籍・講座・OSS資源の網羅リスト(GESIS運営) `awesome` ⭐890 · 📅2026-05
- 🟢 [Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science) — 社会科学にLLMを応用する論文集 `paper-list` ⭐622 · 📅2026-02
- 🟢 [AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI) — 責任あるAIの研究・書籍・規制・成熟度モデル・ツールを17分野で集約 `awesome` ⭐129 · 📅2026-05
- 🟢 [Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) — LLMの人格・価値観・心の理論・認知能力を心理測定の観点で扱う論文集 `survey` ⭐109 · 📅2025-11
- 🔴 [NLP4SocialGood_Papers](https://github.com/zhijing-jin/NLP4SocialGood_Papers) — 社会善のためのNLP論文の読解リスト(救命・QoL・公平性等) `paper-list` ⭐310 · 📅2023-09
- 🔴 [awesome-HAI](https://github.com/bwang514/awesome-HAI) — HCI視点での人間とAIのインタラクション設計に関する学術資料集 `awesome` ⭐297 · 📅2021-05

## ⚡ 効率化(圧縮 / 量子化 / NAS / AutoML)

- 🟢 [Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) — iOS向けCore MLモデルの最大級のリスト `model` ⭐7k · 📅2025-06
- 🟢 [Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) — モデル量子化の論文・コード・ドキュメントのリスト `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) — 効率的LLM(枝刈り・量子化・蒸留等)のキュレーションリスト `awesome` ⭐2k · 📅2025-06
- 🟢 [Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) — 量子化・枝刈り・蒸留などLLM圧縮の論文とツール集 `awesome` ⭐1.8k · 📅2026-02
- 🟢 [tinyml-papers-and-projects](https://github.com/gigwegbe/tinyml-papers-and-projects) — TinyMLの論文・プロジェクト集(活発に更新) `paper-list` ⭐1k · 📅2025-12
- 🟢 [awesome-AutoML](https://github.com/windmaple/awesome-AutoML) — AutoMLのキュレーションリスト `awesome` ⭐936 · 📅2026-03
- 🟢 [awesome-ai-efficiency](https://github.com/PrunaAI/awesome-ai-efficiency) — AIモデルの高速化・小型化・省エネ手法のリスト `awesome` ⭐222 · 📅2026-02
- 🟢 [Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) — オンデバイスAIシステム(推論エンジン/ベンチ/論文)、活発 `awesome` ⭐156 · 📅2026-05
- 🟢 [awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) — AIの環境影響を評価・削減するGreen AIツール/論文の定番リスト `awesome` ⭐114 · 📅2026-05
- 📑 [Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) — LLMの知識蒸留サーベイ連動の論文集 `survey` ⭐1.3k · 📅2025-03
- 🟡 [awesome-ml-model-compression](https://github.com/cedrickchee/awesome-ml-model-compression) — モデル圧縮・量子化のリサーチ論文・ツール・学習資料 `awesome` ⭐543 · 📅2024-09
- 🟡 [awesome-nas-papers](https://github.com/jackguagua/awesome-nas-papers) — Neural Architecture Search論文の集約リスト `paper-list` ⭐405 · 📅2024-01
- 🔴 [deep-learning-model-convertor](https://github.com/ysh329/deep-learning-model-convertor) — 異なる深層学習フレームワーク間のモデル変換ツールの一覧 `awesome` ⭐3.2k · 📅2023-06
- 🔴 [Awesome-Knowledge-Distillation](https://github.com/FLHonker/Awesome-Knowledge-Distillation) — 知識蒸留の論文を分類整理(2014-2021) `paper-list` ⭐2.7k · 📅2023-05
- 🔴 [Awesome-AutoDL](https://github.com/D-X-Y/Awesome-AutoDL) — 自動深層学習(AutoDL)のリソースと詳細分析 `awesome` ⭐2.3k · 📅2022-09
- 🔴 [awesome-emdl](https://github.com/csarron/awesome-emdl) — 組込み・モバイル深層学習の論文/ライブラリ/ツール集 `awesome` ⭐768 · 📅2023-03
- 🔴 [awesome-edge-machine-learning](https://github.com/Bisonai/awesome-edge-machine-learning) — エッジ機械学習の論文・推論エンジン・課題・書籍を網羅 `awesome` ⭐280 · 📅2023-02
- 🔴 [awesome-transformer-search](https://github.com/automl/awesome-transformer-search) — TransformerとNASを組み合わせたリソースのリスト `awesome` ⭐270 · 📅2023-06
- 🔴 [awesome-model-compression](https://github.com/ChanChiChoi/awesome-model-compression) — モデル圧縮(構造・蒸留・二値化・量子化・枝刈り)論文集 `paper-list` ⭐166 · 📅2023-02
- 🔴 [NASPapers](https://github.com/NiuTrans/NASPapers) — ニューラルアーキテクチャ探索(NAS)の論文リスト `paper-list` ⭐135 · 📅2021-09
- 🔴 [awesome-compression-papers](https://github.com/chenbong/awesome-compression-papers) — 圧縮・高速化(枝刈り・量子化・蒸留・低ランク分解)の論文集 `paper-list` ⭐25 · 📅2020-10
- 🔴 [awesome-architecture-search](https://github.com/chenyaofo/awesome-architecture-search) — NASの進展を最新追跡する論文リスト `paper-list` ⭐9 · 📅2022-05
- 🔴 [Awesome-NAS](https://github.com/Openning07/Awesome-NAS) — ニューラルアーキテクチャ探索(NAS)リソースのキュレーション `awesome` ⭐1 · 📅2020-04

## 🔐 連合学習 / プライバシー

- 🟢 [Awesome-Differential-Privacy-and-Meachine-Learning](https://github.com/JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning) — 差分プライバシーを用いた連合学習・MLの論文と実装 `paper-list` ⭐388 · 📅2025-09
- 🟢 [Awesome-ML-SP-Papers](https://github.com/gnipping/Awesome-ML-SP-Papers) — セキュリティトップ4会議のML Security & Privacy論文集 `paper-list` ⭐347 · 📅2025-11
- 🟡 [awesome-federated-learning](https://github.com/poga/awesome-federated-learning) — 連合学習とMLにおけるプライバシーのリソース集 `awesome` ⭐547 · 📅2024-06
- 🟡 [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper) — 連合学習システム・フレームワークの論文リスト `paper-list` ⭐75 · 📅2024-02
- 🔴 [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning) — FedML連携の連合学習研究・プロダクション統合リスト `paper-list` ⭐2k · 📅2022-09
- 🔴 [awesome-secure-federated-learning-papers](https://github.com/csl-cqu/awesome-secure-federated-learning-papers) — 安全な連合学習(攻撃・防御・勾配反転)の論文集 `paper-list` ⭐26 · 📅2023-03
- 🔴 [awesome-federated-learning](https://github.com/Willjay5991/awesome-federated-learning) — 連合学習の論文・記事・フレームワーク・講義資料 `awesome` ⭐2 · 📅2020-08

## ♻️ 継続学習(Continual Learning)

- 🟢 [Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning) — 増分学習・継続学習・破滅的忘却の主要会議論文集 `paper-list` ⭐4.5k · 📅2026-05
- 🟢 [awesome-lifelong-learning-methods-for-llm](https://github.com/zzz47zzz/awesome-lifelong-learning-methods-for-llm) — LLMの生涯学習に関するサーベイ・論文集 `survey` ⭐162 · 📅2025-05
- 🟡 [Best-Incremental-Learning](https://github.com/Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning) — 増分・継続・生涯学習のリポジトリ `paper-list` ⭐607 · 📅2024-05
- 🟡 [Awesome-Continual-Learning](https://github.com/feifeiobama/Awesome-Continual-Learning) — 継続学習論文とBibTeXエントリのキュレーションリスト `paper-list` ⭐203 · 📅2024-10
- 🟡 [LLM-Continual-Learning-Papers](https://github.com/AGI-Edgerunners/LLM-Continual-Learning-Papers) — LLMの継続学習(continual learning)の必読論文集 `paper-list` ⭐149 · 📅2023-11
- 🟡 [Awesome-Continual-Learning](https://github.com/lywang3081/Awesome-Continual-Learning) — 継続学習サーベイ連動の論文リストと有用なリソース `paper-list` ⭐108 · 📅2024-02
- 🔴 [awesome-lifelong-continual-learning](https://github.com/prprbr/awesome-lifelong-continual-learning) — 生涯/継続学習の論文・ブログ・データセット・ソフトウェアのリスト `awesome` ⭐298 · 📅2021-03

## 🖥️ MLシステム / 学習・推論インフラ / データ基盤

- 🟢 [AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) — AIシステム論文と産業実践(OSDI/NSDI/MLSys等、LLM・GenAI含む)を集めた定番 `awesome` ⭐4k · 📅2025-07
- 🟢 [Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) — LLMによる合成データ生成のリーディングリスト(活発) `paper-list` ⭐1.5k · 📅2025-06
- 🟢 [rtdl](https://github.com/yandex-research/rtdl) — テーブルデータ深層学習の論文とパッケージ集(Yandex Research) `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [ML4DB-paper-list](https://github.com/LumingSun/ML4DB-paper-list) — DBシステムをAIで強化する論文集(学習型インデックス・クエリ最適化) `paper-list` ⭐773 · 📅2026-04
- 🟢 [ml-systems-papers](https://github.com/byungsoo-oh/ml-systems-papers) — MLシステム分野の論文を体系的に集めたコレクション `paper-list` ⭐556 · 📅2026-02
- 🟢 [awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) — AIシステムの論文とそのコードをまとめたリスト `paper-list` ⭐362 · 📅2026-05
- 🟢 [awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) — 高次元ベクトル検索・データベース関連の厳選リスト(活発) `awesome` ⭐353 · 📅2026-05
- 🟢 [Awesome-LLM-Inference-Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) — LLM推論最適化手法をレイテンシ/スループット/メモリ別に分類した網羅的まとめ `survey` ⭐210 · 📅2026-04
- 🟢 [Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) — 「Representation Learning for Tabular Data」サーベイ付随リスト `survey` ⭐123 · 📅2026-05
- 🟢 [awesome-ai4db-paper](https://github.com/Wind-Gone/awesome-ai4db-paper) — AI4DB論文集(学習型インデックス・基数推定・学習型クエリ最適化・LLM×DB) `paper-list` ⭐112 · 📅2026-04
- 🟡 [data-augmentation-review](https://github.com/AgaMiko/data-augmentation-review) — データ拡張の手法・ライブラリ・論文を幅広く集めたレビュー `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-vector-search](https://github.com/currentslab/awesome-vector-search) — ベクトル検索のライブラリ・サービス・論文集(Faiss, Annoy等) `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) — 大規模モデルの分散学習・推論に関するプロジェクトと論文の厳選リスト `awesome` ⭐279 · 📅2024-10
- 🟡 [awesome-synthetic-data](https://github.com/statice/awesome-synthetic-data) — OSS/商用の合成データツール厳選リスト(SDV等) `awesome` ⭐257 · 📅2024-01
- 🟡 [Awesome-LLM-Inference](https://github.com/DefTruth/Awesome-LLM-Inference) — LLM/VLM推論最適化(FlashAttention,PagedAttention,MLA等)の論文+コード集 `paper-list` ⭐16 · 📅2025-03
- 🔴 [awesome-data-augmentation](https://github.com/CrazyVertigo/awesome-data-augmentation) — データ拡張手法(AugMix, CutMix等)の厳選リスト `awesome` ⭐797 · 📅2021-03
- 🔴 [awesome-dl-hw-resources](https://github.com/RaviVijay/awesome-dl-hw-resources) — 深層学習向けハードウェア/チップ設計リソースの厳選リスト `awesome` ⭐58 · 📅2018-05
- 🔴 [awesome-ml-testing](https://github.com/yqtian-se/awesome-ml-testing) — ML/深層学習システムのテストに関する論文・ツール集 `paper-list` ⭐47 · 📅2021-10
- 🔴 [Awesome-MLSys](https://github.com/dujiangsu/Awesome-MLSys) — 大規模モデル推論を中心としたMLSys分野の学術論文集 `paper-list` ⭐6 · 📅2023-09

## 🛠️ MLOps / データ中心AI

- 🟢 [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) — MLのデプロイ・監視・スケーリング用OSSライブラリのリスト `awesome` ⭐20.6k · 📅2026-05
- 🟢 [awesome-mlops](https://github.com/kelvins/awesome-mlops) — MLOpsツールのキュレーションリスト `awesome` ⭐5.2k · 📅2026-04
- 🟢 [Awesome-Dataset-Distillation](https://github.com/Guang000/Awesome-Dataset-Distillation) — 勾配/分布マッチング・生成手法・応用を網羅した定番リスト(非常に活発) `awesome` ⭐1.9k · 📅2026-05
- 🟢 [awesome-data-centric-ai](https://github.com/Data-Centric-AI-Community/awesome-data-centric-ai) — データ中心AIのOSS・チュートリアル・研究 `awesome` ⭐350 · 📅2026-04
- 🟢 [awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) — データ評価・データ帰属・データ選定/プルーニング/コアセットを網羅 `paper-list` ⭐120 · 📅2026-05
- 🟡 [awesome-mlops](https://github.com/visenger/awesome-mlops) — MLOpsの参考文献・リソース集 `awesome` ⭐13.9k · 📅2024-11
- 🟡 [awesome-data-labeling](https://github.com/HumanSignal/awesome-data-labeling) — データラベリングツールを厳選したリスト `awesome` ⭐4.3k · 📅2024-06
- 🟡 [data-centric-AI](https://github.com/daochenzha/data-centric-AI) — データ中心AIのリソースキュレーションリスト `awesome` ⭐1.1k · 📅2024-06
- 🟡 [data-centric-ai](https://github.com/HazyResearch/data-centric-ai) — データ中心AIのリソース集(Stanford HazyResearch) `awesome` ⭐1.1k · 📅2023-12
- 🟡 [awesome-open-data-centric-ai](https://github.com/Renumics/awesome-open-data-centric-ai) — 非構造化データ向けデータ中心AIのOSSツール集 `awesome` ⭐732 · 📅2023-11
- 🟡 [Awesome-Coreset-Selection](https://github.com/PatrickZH/Awesome-Coreset-Selection) — コアセット/サブセット選択・data pruningの論文集 `awesome` ⭐183 · 📅2024-06
- 🔴 [releasing-research-code](https://github.com/paperswithcode/releasing-research-code) — ML研究コード公開のベストプラクティス(NeurIPS 2020公式推奨) `awesome` ⭐2.9k · 📅2023-05

## 📊 データセット / ベンチマーク

- 🟢 [Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) — LLM評価のツール・ベンチマーク・リーダーボード・論文の厳選リスト `awesome` ⭐637 · 📅2025-11
- 🟢 [Awesome-Datasets-Hub](https://github.com/ahammadmejbah/Awesome-Datasets-Hub) — 医療AI・NLP・マルチモーダル等のLLM向けデータセット集 `awesome` ⭐132 · 📅2026-05
- 🟢 [Awesome-LLM-Benchmark](https://github.com/SihyeongPark/Awesome-LLM-Benchmark) — 大規模言語モデル向けベンチマーク一覧 `awesome` ⭐11 · 📅2026-04
- 🟢 [awesome-llm-benchmarks](https://github.com/BenchGecko/awesome-llm-benchmarks) — LLM/AIモデルのベンチマーク・データセット・リーダーボード集 `awesome` ⭐1 · 📅2026-03
- 🟡 [llm_benchmarks](https://github.com/leobeeson/llm_benchmarks) — LLM評価用ベンチマーク・データセットのコレクション `awesome` ⭐569 · 📅2024-07

---

## このリポジトリについて

- 各分野ごとに分担した調査エージェントがGitHubを横断的にサーベイし、実在を確認したリポジトリのみを収録しています。
- star数・最終更新日は生成時点のGitHub APIから取得した実値です。鮮度マーカーで陳腐化を判別できます。
- リンクはすべてリダイレクト解決後の正規URLに統一しています。
- 調査の生データ・統計・分野別の詳細は [`docs/research-notes.md`](docs/research-notes.md) にまとめています。

### 鮮度マーカーの自動更新

各リストの ⭐star数・📅最終更新日・鮮度マーカーは、いつでも最新化できます。

- **ローカル再生成**: `./scripts/refresh.sh`(`gh` 認証と `python3` が必要)を実行すると、
  GitHub API からメタデータを取り直し README とノートを再生成します。cron/launchd 登録で完全自動化も可能です。
- **GitHub Actions(推奨)**: [`.github/workflows/refresh-freshness.yml`](.github/workflows/refresh-freshness.yml) が
  毎週月曜に自動実行され、鮮度が変化していれば README を自動コミットします(手動実行も可)。
  リポジトリを GitHub にプッシュすれば追加設定なしで動作します。

Generated with Claude Code
