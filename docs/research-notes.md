# 調査結果ノート (Research Notes)

本ドキュメントは [README.md](../README.md) の分類済みリストの裏付けとなる、
AI研究分野の awesome list / survey / 論文リスト調査の**詳細な生データと統計**です。

- 収録総数: **855 件**(実在確認済み)
- 生成日: 2026-05-29(GitHubメタデータ取得時点)
- 鮮度マーカー: 🟢 ≤12ヶ月 / 🟡 13-30ヶ月 / 🔴 >30ヶ月 / 📑 査読付きサーベイ(curated) / 📚 歴史的 / 📦 archived

## 全体統計

### 分野別 件数

| 分野 | 件数 | 🟢 | 🟡 | 🔴/📦/📚 |
|:--|--:|--:|--:|--:|
| 🧠 機械学習一般 / Deep Learning | 17 | 7 | 4 | 6 |
| 📐 ML理論 / 最適化 | 12 | 3 | 5 | 4 |
| 🎲 確率モデル / ベイズ / 因果 / 不確実性 | 17 | 6 | 6 | 5 |
| 🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML) | 24 | 16 | 5 | 3 |
| 🌱 自己教師あり / 表現学習 / 基盤モデル | 6 | 3 | 3 | 0 |
| 🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師) | 27 | 10 | 6 | 11 |
| 👁️ Computer Vision | 108 | 43 | 18 | 47 |
| 🎨 Computer Graphics / 3D / レンダリング | 64 | 30 | 18 | 16 |
| 🖌️ 低レベル画像処理 / 復元 / 圧縮 | 25 | 11 | 7 | 7 |
| 💬 NLP / 大規模言語モデル(LLM) | 96 | 40 | 23 | 33 |
| 🖼️ 生成AI / Diffusion / 画像・動画生成 | 42 | 29 | 4 | 9 |
| 🍌 特定モデルのプロンプト・作例コレクション | 20 | 17 | 3 | 0 |
| 🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ) | 18 | 17 | 1 | 0 |
| 🎮 強化学習(RL) | 33 | 22 | 5 | 6 |
| 🔀 マルチモーダル / VLM / MLLM | 30 | 19 | 5 | 6 |
| 🔊 音声 / オーディオ | 28 | 13 | 7 | 8 |
| 🤖 ロボティクス / Embodied AI | 17 | 15 | 1 | 1 |
| 🕸️ グラフ学習(GNN) / 知識グラフ | 35 | 10 | 15 | 10 |
| 🛒 推薦システム(RecSys) | 9 | 5 | 1 | 3 |
| 📈 時系列(Time Series) | 11 | 6 | 4 | 1 |
| 🦾 AIエージェント / LLM Agents | 19 | 14 | 5 | 0 |
| 🔬 医療AI / AI for Science | 41 | 24 | 8 | 9 |
| 🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学) | 28 | 16 | 6 | 6 |
| 🚗 自動運転(Autonomous Driving) | 18 | 2 | 9 | 7 |
| 🛡️ AI安全性 / Alignment / 解釈性 | 37 | 19 | 8 | 10 |
| ⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction | 7 | 5 | 0 | 2 |
| ⚡ 効率化(圧縮 / 量子化 / NAS / AutoML) | 21 | 8 | 2 | 11 |
| 🔐 連合学習 / プライバシー | 7 | 2 | 2 | 3 |
| ♻️ 継続学習(Continual Learning) | 7 | 2 | 4 | 1 |
| 🖥️ MLシステム / 学習・推論インフラ / データ基盤 | 16 | 8 | 5 | 3 |
| 🛠️ MLOps / データ中心AI | 10 | 5 | 5 | 0 |
| 📊 データセット / ベンチマーク | 5 | 4 | 1 | 0 |
| **合計** | **855** | **431** | **196** | **228** |

### 種別別 件数

| 種別 | 件数 |
|:--|--:|
| paper-list | 396 |
| awesome | 312 |
| survey | 121 |
| model | 26 |

## 分野別 詳細


### 🧠 機械学習一般 / Deep Learning  (17件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | awesome | ML全般 | 72610 | 2026-05 | 言語別のMLフレームワーク・ライブラリの定番キュレーションリスト |
| 🟢 | [ChristosChristofidis/awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) | awesome | DL全般 | 28317 | 2025-05 | DLのチュートリアル・プロジェクト・コミュニティを集めた定番リスト |
| 🟢 | [endymecy/awesome-deeplearning-resources](https://github.com/endymecy/awesome-deeplearning-resources) | paper-list | DL論文 | 3004 | 2026-01 | DLおよび深層強化学習の論文・コードを時系列で整理 |
| 🟢 | [papercopilot/paperlists](https://github.com/papercopilot/paperlists) | paper-list | 会議論文横断 | 932 | 2026-02 | Paper Copilotの整形済みデータ。主要会議を年度別JSONで横断網羅し継続更新(大型) |
| 🟢 | [huggingface/ai-deadlines](https://github.com/huggingface/ai-deadlines) | awesome | 会議締切トラッカー | 342 | 2026-05 | 主要AI会議の締切カウントダウン(paperswithcode版の後継、現行主流) |
| 🟢 | [george-gca/ai_papers_scrapper](https://github.com/george-gca/ai_papers_scrapper) | paper-list | 会議論文スクレイパ | 52 | 2026-03 | 主要AI会議(2017-)のPDF・著者・要旨等を会議×年度で取得するスクレイパ |
| 🟢 | [DmitryRyumin/ICML-2025-Papers](https://github.com/DmitryRyumin/ICML-2025-Papers) | paper-list | 会議論文(ICML) | 37 | 2025-10 | ICML 2025採択論文をコード実装リンク付きで体系化 |
| 📑 | [qingsongedu/awesome-AI-tutorials-surveys](https://github.com/qingsongedu/awesome-AI-tutorials-surveys) | survey | チュートリアル/サーベイ | 165 | 2023-02 | トップAI会議のDL/ML/DM/CV/NLP/音声のチュートリアル・サーベイ集 |
| 🟡 | [Lionelsy/Conference-Accepted-Paper-List](https://github.com/Lionelsy/Conference-Accepted-Paper-List) | paper-list | 会議採択論文 | 1337 | 2025-01 | 主要AI/ML/ロボティクス会議の採択論文リンクと締切情報を2015-2025で集約(活発) |
| 🟡 | [DmitryRyumin/AAAI-2024-Papers](https://github.com/DmitryRyumin/AAAI-2024-Papers) | paper-list | 会議論文(AAAI) | 591 | 2025-01 | AAAI 2024の革新的研究論文を網羅したコレクション |
| 🟡 | [tranhungnghiep/AI-Conference-Info](https://github.com/tranhungnghiep/AI-Conference-Info) | awesome | 会議採択率/情報 | 165 | 2024-07 | 主要AI会議40+の採択率・投稿統計・締切を年度横断で集約 |
| 🟡 | [hzxwonder/Conference-Paper](https://github.com/hzxwonder/Conference-Paper) | paper-list | CCF-A会議論文 | 8 | 2024-04 | CCF-A会議の採択論文をタイトル・著者・URL・要旨付きで整理 |
| 📚 | [floodsung/Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) | paper-list | DL研究ロードマップ | 39502 | 2022-11 | 深層学習の主要論文を学習順に整理した古典的ロードマップ |
| 📚 | [terryum/awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) | paper-list | DL論文(歴史的) | 26140 | 2024-01 | 2012〜2016年の最も引用された重要DL論文Top100 |
| 🔴 | [amusi/awesome-ai-awesomeness](https://github.com/amusi/awesome-ai-awesomeness) | awesome | awesome of awesome | 979 | 2023-08 | AIに関するawesomeリストを集めた『awesomeのawesome』 |
| 🔴 | [Doragd/Awesome-Paper-List](https://github.com/Doragd/Awesome-Paper-List) | awesome | 論文リスト集約 | 194 | 2022-04 | NLP/CV/MLの多数の論文リスト・関連資源を集約したメタリスト |
| 🔴 | [solaris33/awesome-machine-learning-papers](https://github.com/solaris33/awesome-machine-learning-papers) | paper-list | ML論文 | 78 | 2017-06 | 重要なML論文・リポジトリのキュレーションリスト |

### 📐 ML理論 / 最適化  (12件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [Thinklab-SJTU/awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) | paper-list | 組合せ最適化×ML | 2123 | 2026-05 | 組合せ最適化への機械学習適用論文を36分野超で網羅(活発) |
| 🟢 | [CYHSM/awesome-neuro-ai-papers](https://github.com/CYHSM/awesome-neuro-ai-papers) | paper-list | NeuroAI | 445 | 2026-01 | 深層学習と神経科学の交差領域の論文・レビュー集(活発) |
| 🟢 | [MinghuiChen43/awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) | paper-list | DL現象/理論 | 401 | 2026-05 | grokking・二重降下・宝くじ仮説等DLの経験的現象と理論の論文リスト |
| 🟡 | [hibayesian/awesome-automl-papers](https://github.com/hibayesian/awesome-automl-papers) | paper-list | AutoML/HPO | 4145 | 2024-06 | AutoML論文・記事・チュートリアル・プロジェクトの定番大規模リスト |
| 🟡 | [hurshd0/must-read-papers-for-ml](https://github.com/hurshd0/must-read-papers-for-ml) | paper-list | ML/DL必読論文 | 1350 | 2023-12 | データサイエンス・ML/DLエンジニア向けの必読論文集(古典含む) |
| 🟡 | [kwignb/NeuralTangentKernel-Papers](https://github.com/kwignb/NeuralTangentKernel-Papers) | paper-list | NTK | 122 | 2025-01 | Neural Tangent Kernel(NTK)関連論文の集約リスト |
| 🟡 | [Furyton/awesome-language-model-analysis](https://github.com/Furyton/awesome-language-model-analysis) | paper-list | 言語モデル理論分析 | 100 | 2024-12 | 言語モデルの理論・実証分析(創発能力・スケーリング則・ICL理論・grokking) |
| 🟡 | [materials-data-facility/awesome-bayesian-optimization](https://github.com/materials-data-facility/awesome-bayesian-optimization) | awesome | ベイズ最適化 | 49 | 2024-04 | 材料科学・化学向けベイズ最適化のソフト/論文/チュートリアル集 |
| 🔴 | [VITA-Group/Open-L2O](https://github.com/VITA-Group/Open-L2O) | paper-list | Learning to Optimize | 299 | 2023-06 | L2O手法の初の包括的ベンチマーク兼論文整理リポジトリ |
| 🔴 | [Alro10/awesome-deep-neuroevolution](https://github.com/Alro10/awesome-deep-neuroevolution) | awesome | 神経進化 | 227 | 2021-04 | 深層学習に進化計算を適用するDeep Neuroevolutionのリソース集 |
| 🔴 | [RZFan525/Awesome-ScalingLaws](https://github.com/RZFan525/Awesome-ScalingLaws) | awesome | スケーリング則 | 84 | 2023-04 | LLMのスケーリング則に特化した資源集 |
| 🔴 | [guoji-fu/MLT-Papers](https://github.com/guoji-fu/MLT-Papers) | paper-list | ML理論 | 10 | 2022-02 | 機械学習理論(汎化バウンド・最適化・深層学習の数学)の論文リスト |

### 🎲 確率モデル / ベイズ / 因果 / 不確実性  (17件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) | survey | 拡散・スコアベース生成 | 3347 | 2025-09 | ACM CSUR掲載サーベイ対応の拡散・スコアベース・SDE生成モデル論文分類 |
| 🟢 | [janosh/awesome-normalizing-flows](https://github.com/janosh/awesome-normalizing-flows) | awesome | 正規化フロー | 1626 | 2026-03 | 正規化フローの論文・実装(PyTorch/JAX/Julia)・動画を集めた代表的リスト |
| 🟢 | [valeman/awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) | awesome | コンフォーマル予測 | 1229 | 2026-05 | 分布フリー不確実性定量化(CP)の動画・論文・ライブラリを集めた充実リスト |
| 🟢 | [ENSTA-U2IS-AI/awesome-uncertainty-deeplearning](https://github.com/ENSTA-U2IS-AI/awesome-uncertainty-deeplearning) | awesome | 不確実性推定 | 810 | 2026-05 | 深層学習の予測的不確実性推定のサーベイ・論文・コードを網羅した活発なリスト |
| 🟢 | [dongzhuoyao/awesome-flow-matching](https://github.com/dongzhuoyao/awesome-flow-matching) | awesome | フローマッチング | 675 | 2026-04 | フローマッチング・確率的補間関連研究をまとめた活発なリスト |
| 🟢 | [yataobian/awesome-ebm](https://github.com/yataobian/awesome-ebm) | awesome | エネルギーベースモデル | 387 | 2026-04 | EBMの論文・ライブラリ・チュートリアルを年代順に整理した活発なリスト |
| 🟡 | [rguo12/awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms) | awesome | 因果推論 | 3267 | 2025-01 | 再現可能な因果推論・因果ML手法のインデックス(サーベイ論文付き) |
| 🟡 | [Zymrael/awesome-neural-ode](https://github.com/Zymrael/awesome-neural-ode) | awesome | ニューラル微分方程式 | 1531 | 2024-09 | Neural ODE/SDE/CDE・力学系・制御・数値解法の交差領域を網羅 |
| 🟡 | [zdhNarsil/Awesome-GFlowNets](https://github.com/zdhNarsil/Awesome-GFlowNets) | awesome | GFlowNets | 500 | 2024-10 | GFlowNetの基礎論文・応用・チュートリアルを集めた中心的リスト |
| 🟡 | [changwxx/Awesome-Optimal-Transport-in-Deep-Learning](https://github.com/changwxx/Awesome-Optimal-Transport-in-Deep-Learning) | awesome | 深層学習×最適輸送 | 349 | 2024-05 | 深層学習における最適輸送の論文・コード・資料を集約 |
| 🟡 | [wenhaochai/Awesome-VQVAE](https://github.com/wenhaochai/Awesome-VQVAE) | awesome | VQ-VAE | 330 | 2025-01 | Vector Quantized VAE(VQ-VAE)とその応用に関する論文・リソース集 |
| 🟡 | [CharonWangg/Awesome-Causal-Discovery](https://github.com/CharonWangg/Awesome-Causal-Discovery) | awesome | 因果発見 | 12 | 2023-11 | 因果発見・因果表現学習にフォーカスした論文・書籍リスト |
| 🔴 | [matthewvowels1/Awesome-VAEs](https://github.com/matthewvowels1/Awesome-VAEs) | paper-list | VAE | 843 | 2021-07 | VAE・ディスエンタングルメント・表現学習・生成モデルの論文を約900件集約 |
| 🔴 | [robi56/awesome-bayesian-deep-learning](https://github.com/robi56/awesome-bayesian-deep-learning) | awesome | ベイズ深層学習 | 416 | 2017-05 | ベイズ深層学習の論文・学位論文を年代別に整理した定番リスト |
| 🔴 | [kilianFatras/awesome-optimal-transport](https://github.com/kilianFatras/awesome-optimal-transport) | awesome | 最適輸送 | 246 | 2021-05 | 機械学習向け最適輸送(OT)の論文・チュートリアル・ライブラリ・書籍集 |
| 🔴 | [matthewvowels1/Awesome-Causal-Inference](https://github.com/matthewvowels1/Awesome-Causal-Inference) | paper-list | 因果推論 | 113 | 2021-05 | 機械学習寄りの因果推論・因果発見論文を年代順にまとめた文献リスト |
| 🔴 | [RaulPL/awesome-gaussian-processes](https://github.com/RaulPL/awesome-gaussian-processes) | awesome | ガウス過程 | 42 | 2021-07 | ガウス過程を学ぶための書籍・動画・ソフトウェア・論文を集約 |

### 🏗️ 新アーキテクチャ(SSM・Mamba・KAN・SNN・量子ML)  (24件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [mintisan/awesome-kan](https://github.com/mintisan/awesome-kan) | awesome | KAN | 3239 | 2026-05 | KANのライブラリ・実装・論文・チュートリアルを網羅する事実上の標準リスト |
| 🟢 | [TheBrainLab/Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) | paper-list | SNN | 776 | 2026-03 | トップ会議・誌のSNN論文とコードを継続更新 |
| 🟢 | [Event-AHU/Mamba_State_Space_Model_Paper_List](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) | paper-list | SSM/Mamba | 752 | 2025-06 | Mambaサーベイ付属の応用先別ペーパーリスト |
| 🟢 | [XiudingCai/Awesome-Mamba-Collection](https://github.com/XiudingCai/Awesome-Mamba-Collection) | paper-list | SSM/Mamba | 734 | 2026-04 | Mambaの論文・チュートリアル・実装を分野横断で網羅した代表的キュレーション |
| 🟢 | [radarFudan/Awesome-state-space-models](https://github.com/radarFudan/Awesome-state-space-models) | paper-list | SSM/S4 | 621 | 2025-11 | S4からMambaまで状態空間モデルの理論寄り論文を集めたリスト |
| 🟢 | [marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) | paper-list | 双曲DL | 595 | 2026-05 | 双曲埋め込み・双曲モデル・応用の最新論文を活発に更新 |
| 🟢 | [AXYZdong/awesome-snn-conference-paper](https://github.com/AXYZdong/awesome-snn-conference-paper) | paper-list | SNN | 450 | 2026-05 | SNN分野の難関会議・誌論文とコード実装をまとめたリスト |
| 🟢 | [weigao266/Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) | survey | 効率的アーキテクチャ | 407 | 2025-11 | LLM向け効率アーキテクチャ(線形注意・SSM・RWKV等)の大規模サーベイ |
| 🟢 | [attention-survey/Efficient_Attention_Survey](https://github.com/attention-survey/Efficient_Attention_Survey) | survey | efficient attention | 298 | 2025-12 | 効率的注意機構をハードウェア効率・スパース・線形等に分類したサーベイ |
| 🟢 | [LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy) | paper-list | neuro-symbolic(LLM) | 298 | 2025-06 | LLM時代のニューロシンボリック学習の最新動向を追うリスト |
| 🟢 | [xmindflow/Awesome_Mamba](https://github.com/xmindflow/Awesome_Mamba) | survey | SSM/Mamba(医療画像) | 267 | 2025-07 | 医療画像解析におけるSSMの包括サーベイ対応リスト |
| 🟢 | [Yaziwel/Awesome-RWKV-in-Vision](https://github.com/Yaziwel/Awesome-RWKV-in-Vision) | paper-list | RWKV(視覚) | 244 | 2025-06 | RWKVのコンピュータビジョン応用論文を集めたリスト |
| 🟢 | [vgthengane/Awesome-Mamba-in-Vision](https://github.com/vgthengane/Awesome-Mamba-in-Vision) | paper-list | SSM/Mamba(視覚) | 36 | 2026-03 | コンピュータビジョン分野のMamba論文を集約 |
| 🟢 | [Event-AHU/Awesome_Modern_Hopfield_Networks](https://github.com/Event-AHU/Awesome_Modern_Hopfield_Networks) | paper-list | Hopfield Networks | 27 | 2026-03 | 現代的ホップフィールドネットワークの論文リスト |
| 🟢 | [btzyd/Awesome-Linear-Attention-Survey](https://github.com/btzyd/Awesome-Linear-Attention-Survey) | survey | linear attention | 12 | 2026-02 | 線形注意のアルゴリズム・理論・応用・インフラを扱うサーベイ付随リスト |
| 🟢 | [RamtinMoslemi/KAN-Papers](https://github.com/RamtinMoslemi/KAN-Papers) | paper-list | KAN | 5 | 2026-05 | arXivから抽出したKAN論文の完全リスト |
| 🟡 | [krishnakumarsekar/awesome-quantum-machine-learning](https://github.com/krishnakumarsekar/awesome-quantum-machine-learning) | awesome | 量子ML | 3551 | 2024-05 | QMLの基礎・アルゴリズム・教材・プロジェクトを大規模に収集 |
| 🟡 | [artix41/awesome-quantum-ml](https://github.com/artix41/awesome-quantum-ml) | paper-list | 量子ML | 525 | 2024-06 | 量子デバイス上で動くMLアルゴリズムの論文・資料キュレーション |
| 🟡 | [ccclyu/awesome-deeplogic](https://github.com/ccclyu/awesome-deeplogic) | paper-list | neuro-symbolic(NLP) | 300 | 2024-08 | NLP応用中心のニューラル記号AI論文集 |
| 🟡 | [coderonion/awesome-snn](https://github.com/coderonion/awesome-snn) | model | SNN | 233 | 2024-10 | Spike-Driven-Transformer等の公開SNN実装集 |
| 🟡 | [open-neuromorphic/awesome-neuromorphic-hw](https://github.com/open-neuromorphic/awesome-neuromorphic-hw) | paper-list | ニューロモルフィックHW | 210 | 2023-11 | SNNのASIC/FPGA等ニューロモルフィックハードウェア論文集 |
| 📦 | [Separius/awesome-fast-attention](https://github.com/Separius/awesome-fast-attention) | awesome | efficient attention | 1023 | 2021-08 | 効率的注意モジュールの古典的網羅リスト |
| 🔴 | [sekwiatkowski/awesome-capsule-networks](https://github.com/sekwiatkowski/awesome-capsule-networks) | awesome | capsule networks | 975 | 2020-02 | Dynamic Routing/EM Routing等カプセルネットの主要論文・実装集 |
| 🔴 | [thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers](https://github.com/thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers) | paper-list | neuro-symbolic | 135 | 2023-09 | ニューラル記号・確率論理の論文キュレーション |

### 🌱 自己教師あり / 表現学習 / 基盤モデル  (6件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [jason718/awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning) | awesome | 自己教師あり | 6392 | 2026-02 | 自己教師あり学習手法の定番キュレーションリスト |
| 🟢 | [uncbiag/Awesome-Foundation-Models](https://github.com/uncbiag/Awesome-Foundation-Models) | paper-list | 基盤モデル | 1158 | 2026-04 | 視覚・言語タスク向け基盤モデルのキュレーションリスト |
| 🟢 | [srebroa/Awesome-LLM-VLM-Foundation-Models](https://github.com/srebroa/Awesome-LLM-VLM-Foundation-Models) | awesome | 基盤モデル | 6 | 2026-02 | LLM・VLM・基盤モデルのキュレーションリスト |
| 🟡 | [asheeshcric/awesome-contrastive-self-supervised-learning](https://github.com/asheeshcric/awesome-contrastive-self-supervised-learning) | paper-list | 対照学習 | 1311 | 2024-09 | 対照型自己教師あり学習(SimCLR/VICReg等)の論文集 |
| 🟡 | [qingsongedu/Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) | paper-list | 時系列SSL | 378 | 2024-04 | 時系列向け自己教師あり学習(SSL4TS)の論文・コード・データ集 |
| 🟡 | [ys-zong/awesome-self-supervised-multimodal-learning](https://github.com/ys-zong/awesome-self-supervised-multimodal-learning) | paper-list | マルチモーダルSSL | 278 | 2024-08 | 自己教師ありマルチモーダル学習のリソース(T-PAMI連動) |

### 🎓 学習パラダイム(メタ / 転移 / 少数 / OOD / 半教師)  (27件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [zhaoxin94/awesome-domain-adaptation](https://github.com/zhaoxin94/awesome-domain-adaptation) | awesome | ドメイン適応 | 5440 | 2025-12 | ドメイン適応に関する論文・コードを集めた定番リスト |
| 🟢 | [subeeshvasu/Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise) | awesome | ラベルノイズ学習 | 2718 | 2025-05 | ノイズラベル学習の論文・コード・サーベイを網羅した最大級リスト |
| 🟢 | [tim-learn/awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) | awesome | テスト時適応 | 1278 | 2025-11 | SFDA/TTBA/TTIA/OTTA等を網羅したテスト時適応の定番リスト |
| 🟢 | [Vanint/Awesome-LongTailed-Learning](https://github.com/Vanint/Awesome-LongTailed-Learning) | survey | 長尾学習 | 1019 | 2025-11 | TPAMI2023サーベイ対応。クラス再均衡/情報拡張/モジュール改善で分類 |
| 🟢 | [huytransformer/Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) | awesome | OOD検出 | 1004 | 2026-04 | OOD検出と汎化のベンチマーク・論文・ライブラリを網羅 |
| 🟢 | [thuml/awesome-multi-task-learning](https://github.com/thuml/awesome-multi-task-learning) | awesome | マルチタスク学習 | 837 | 2026-03 | MTLのデータセット・コードベース・論文を集約(清華大THUML) |
| 🟢 | [baifanxxx/awesome-active-learning](https://github.com/baifanxxx/awesome-active-learning) | awesome | 能動学習 | 799 | 2026-03 | 能動学習の論文・ツール・ベンチマークを集めたリスト |
| 🟢 | [WeihongLi-ac/Awesome-Multi-Task-Learning](https://github.com/WeihongLi-ac/Awesome-Multi-Task-Learning) | paper-list | マルチタスク学習 | 378 | 2026-03 | マルチタスク学習の最新論文を時系列整理 |
| 🟢 | [shuolucs/Awesome-Out-Of-Distribution-Detection](https://github.com/shuolucs/Awesome-Out-Of-Distribution-Detection) | survey | OOD検出 | 166 | 2026-01 | ACM CSUR 2025採択のタスク指向OOD検出サーベイに対応する論文リスト |
| 🟢 | [AtsuMiyai/Awesome-OOD-VLM](https://github.com/AtsuMiyai/Awesome-OOD-VLM) | survey | OOD検出(VLM) | 101 | 2025-06 | 視覚言語モデル時代の一般化OOD検出サーベイ(TMLR2025)対応リスト |
| 📑 | [songhwanjun/Awesome-Noisy-Labels](https://github.com/songhwanjun/Awesome-Noisy-Labels) | survey | ラベルノイズ学習 | 572 | 2023-02 | ノイズラベル学習のサーベイに対応する論文リスト |
| 🟡 | [jindongwang/transferlearning](https://github.com/jindongwang/transferlearning) | paper-list | 転移学習 | 14334 | 2025-02 | 転移学習分野の最大級リポジトリ。論文・コード・データセットを網羅 |
| 🟡 | [yassouali/awesome-semi-supervised-learning](https://github.com/yassouali/awesome-semi-supervised-learning) | awesome | 半教師あり学習 | 1855 | 2024-05 | 半教師あり学習の論文・手法をCV/NLP/生成/グラフ別に整理 |
| 🟡 | [ZhiningLiu1998/awesome-imbalanced-learning](https://github.com/ZhiningLiu1998/awesome-imbalanced-learning) | awesome | 不均衡学習 | 1518 | 2025-02 | クラス不均衡/長尾学習の論文・コード・フレームワーク・ライブラリを総覧 |
| 🟡 | [gary23ai/awesome_OpenSetRecognition_list](https://github.com/gary23ai/awesome_OpenSetRecognition_list) | paper-list | open-set認識 | 1209 | 2024-03 | オープンセット認識・OOD・オープンワールド認識の論文を集めた定番リスト |
| 🟡 | [YuejiangLIU/awesome-source-free-test-time-adaptation](https://github.com/YuejiangLIU/awesome-source-free-test-time-adaptation) | paper-list | TTA/SFDA | 548 | 2024-06 | テスト時適応・テスト時訓練・ソースフリードメイン適応の論文リスト |
| 🟡 | [junkunyuan/Awesome-Domain-Generalization](https://github.com/junkunyuan/Awesome-Domain-Generalization) | awesome | ドメイン汎化 | 532 | 2025-04 | ドメイン汎化の論文・コード・データセットを集めたリスト |
| 🔴 | [sudharsan13296/Awesome-Meta-Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning) | awesome | メタ学習 | 1558 | 2020-11 | メタ学習の論文・コード・書籍・動画・データセットを網羅した定番リスト |
| 🔴 | [sbharadwajj/awesome-zero-shot-learning](https://github.com/sbharadwajj/awesome-zero-shot-learning) | awesome | zero-shot | 933 | 2021-07 | ゼロショット学習の論文・コード・リソースを集めたキュレーション |
| 🔴 | [Openning07/awesome-curriculum-learning](https://github.com/Openning07/awesome-curriculum-learning) | awesome | カリキュラム学習 | 247 | 2022-08 | カリキュラム学習の論文を検出/分割/分類/転移/RL別にタグ付け |
| 🔴 | [JieyuZ2/Awesome-Weak-Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) | awesome | 弱教師あり学習 | 194 | 2023-03 | プログラム的/ルールベース弱教師あり学習の論文・リソース集 |
| 🔴 | [weitianxin/awesome-distribution-shift](https://github.com/weitianxin/awesome-distribution-shift) | awesome | 分布シフト | 127 | 2023-08 | 分布シフトとベンチマークの論文集 |
| 🔴 | [indussky8/awesome-few-shot-learning](https://github.com/indussky8/awesome-few-shot-learning) | paper-list | few-shot | 126 | 2021-10 | 標準データセット上の比較結果を含むfew-shot学習の論文キュレーション |
| 🔴 | [WilliamYi96/Awesome-Zero-Shot-Learning](https://github.com/WilliamYi96/Awesome-Zero-Shot-Learning) | paper-list | zero-shot | 85 | 2022-08 | ゼロショット学習の最新の論文・データセットの進展をまとめたリスト |
| 🔴 | [Impression2805/Awesome-Failure-Detection](https://github.com/Impression2805/Awesome-Failure-Detection) | paper-list | 誤分類検出 | 53 | 2023-10 | OOD検出と誤分類検出(failure detection)を統合的に扱う論文リスト |
| 🔴 | [uqzhichen/Awesome-compositional-zero-shot-learning](https://github.com/uqzhichen/Awesome-compositional-zero-shot-learning) | paper-list | compositional ZSL | 11 | 2022-07 | 構成的ゼロショット学習(属性と物体の組合せ汎化)に特化した論文リスト |
| 🔴 | [cmhungsteve/awsome-domain-adaptation](https://github.com/cmhungsteve/awsome-domain-adaptation) | awesome | ドメイン適応 | 1 | 2019-09 | ドメイン適応関連の論文を分類整理した広く参照される一覧 |

### 👁️ Computer Vision  (108件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [amusi/CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) | paper-list | 会議論文(CVPR) | 22623 | 2026-03 | CVPR 2026の論文とオープンソースプロジェクトの大規模集約(定番) |
| 🟢 | [M-3LAB/awesome-industrial-anomaly-detection](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) | awesome | 産業異常検知 | 3568 | 2026-05 | 産業画像の異常/欠陥検出の論文・データセット集(非常に活発) |
| 🟢 | [xinghaochen/awesome-hand-pose-estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation) | awesome | 手姿勢推定 | 3370 | 2025-12 | 手姿勢推定/トラッキング(3D含む)の定番リスト |
| 🟢 | [ChaofWang/Awesome-Super-Resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) | awesome | 超解像 | 3068 | 2026-04 | 超解像関連の論文・データ・リポジトリを集約 |
| 🟢 | [subeeshvasu/Awesome-Deblurring](https://github.com/subeeshvasu/Awesome-Deblurring) | awesome | デブラー | 2886 | 2025-06 | 画像・動画デブラーのリソースをまとめたリスト |
| 🟢 | [amusi/ICCV2025-Papers-with-Code](https://github.com/amusi/ICCV2025-Papers-with-Code) | paper-list | 会議論文(ICCV) | 2878 | 2025-07 | ICCV 2025の論文とオープンソースプロジェクト集 |
| 🟢 | [gjy3035/Awesome-Crowd-Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) | awesome | 群衆計数 | 2597 | 2026-01 | 群衆計数の定番リスト。データセット・コード付きで活発 |
| 🟢 | [luanshiyinyang/awesome-multiple-object-tracking](https://github.com/luanshiyinyang/awesome-multiple-object-tracking) | awesome | 多物体追跡 | 1476 | 2025-10 | MOTのレビュー論文・年別アルゴリズム・データセットを整理 |
| 🟢 | [TheShadow29/awesome-grounding](https://github.com/TheShadow29/awesome-grounding) | paper-list | Visual Grounding | 1125 | 2025-09 | 画像/動画/3Dの参照表現・grounding論文集 |
| 🟢 | [YichiZhang98/SAM4MIS](https://github.com/YichiZhang98/SAM4MIS) | paper-list | 医用画像SAM | 1105 | 2026-04 | 医用画像セグメンテーションへのSAM応用論文・OSSの要約 |
| 🟢 | [DmitryRyumin/ICCV-2023-25-Papers](https://github.com/DmitryRyumin/ICCV-2023-25-Papers) | paper-list | 会議論文(ICCV) | 964 | 2025-11 | ICCV 2023-2025採択論文のキュレーション |
| 🟢 | [SkalskiP/top-cvpr-2025-papers](https://github.com/SkalskiP/top-cvpr-2025-papers) | paper-list | 会議論文(CVPR) | 877 | 2026-04 | CVPR 2025の注目論文を厳選したコレクション |
| 🟢 | [Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation](https://github.com/Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation) | paper-list | オープン語彙セグメンテーション | 875 | 2026-05 | オープン語彙/ゼロショットセマンティックセグメンテーション論文リスト |
| 🟢 | [MarkMoHR/Awesome-Referring-Image-Segmentation](https://github.com/MarkMoHR/Awesome-Referring-Image-Segmentation) | awesome | Referring Seg | 822 | 2026-01 | 参照画像セグメンテーションの論文・データセット集 |
| 🟢 | [firework8/Awesome-Skeleton-based-Action-Recognition](https://github.com/firework8/Awesome-Skeleton-based-Action-Recognition) | paper-list | スケルトン行動認識 | 712 | 2026-05 | スケルトンベース行動認識の論文を月次更新するリスト |
| 🟢 | [DirtyHarryLYL/HOI-Learning-List](https://github.com/DirtyHarryLYL/HOI-Learning-List) | awesome | HOI検出 | 709 | 2025-10 | データセット・ベンチマーク・論文を網羅するHOI学習リスト(活発) |
| 🟢 | [ChocoWu/Awesome-Scene-Graph-Generation](https://github.com/ChocoWu/Awesome-Scene-Graph-Generation) | awesome | Scene Graph | 670 | 2026-05 | LLM/非LLM手法・2D/3D/動画を網羅する活発なシーングラフ生成リスト |
| 🟢 | [Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC](https://github.com/Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC) | paper-list | 会議論文(AIGC) | 664 | 2026-05 | 主要会議のAIGC関連論文・コードを集約 |
| 🟢 | [zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation](https://github.com/zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation) | paper-list | 時系列行動検出 | 587 | 2026-05 | 時系列行動検出・提案生成・弱教師ありを横断的に収集 |
| 🟢 | [cvlab-uob/Awesome-Gaze-Estimation](https://github.com/cvlab-uob/Awesome-Gaze-Estimation) | awesome | 視線推定 | 535 | 2025-06 | 視線推定論文の厳選キュレーションリスト |
| 🟢 | [bcmi/Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization) | awesome | Image Harmonization | 532 | 2026-02 | 画像ハーモナイゼーションの論文・コード・リソース集(活発) |
| 🟢 | [gaomingqi/Awesome-Video-Object-Segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation) | awesome | VOS | 498 | 2026-05 | VOSの最新論文・データセット・プロジェクト集 |
| 🟢 | [TaoWangzj/Awesome-Face-Restoration](https://github.com/TaoWangzj/Awesome-Face-Restoration) | paper-list | 顔復元 | 492 | 2026-03 | 顔復元手法の論文・リポジトリを集めたリスト |
| 🟢 | [visionxiang/awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) | awesome | カモフラージュ物体検出 | 477 | 2025-12 | カモフラージュ/隠蔽物体検出の厳選リソース集 |
| 🟢 | [CNJianLiu/Awesome-Object-Pose-Estimation](https://github.com/CNJianLiu/Awesome-Object-Pose-Estimation) | survey | 6D姿勢推定 | 422 | 2026-01 | IJCV2026サーベイ「Deep Learning-Based Object Pose Estimation」のプロジェクトページ |
| 🟢 | [ttengwang/Awesome_Long_Form_Video_Understanding](https://github.com/ttengwang/Awesome_Long_Form_Video_Understanding) | paper-list | 長尺動画理解 | 377 | 2025-10 | 長尺動画に特化した論文・データセット集 |
| 🟢 | [Charles-Xie/awesome-described-object-detection](https://github.com/Charles-Xie/awesome-described-object-detection) | paper-list | オープン語彙検出 | 354 | 2025-11 | Described/Open-Vocabulary物体検出・参照表現理解の論文集 |
| 🟢 | [ChunmingHe/awesome-concealed-object-segmentation](https://github.com/ChunmingHe/awesome-concealed-object-segmentation) | awesome | 隠蔽物体セグメンテーション | 340 | 2026-01 | 隠蔽物体セグメンテーションのリソース集 |
| 🟢 | [linhuixiao/Awesome-Visual-Grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) | survey | Visual Grounding | 313 | 2025-11 | TPAMI 2025サーベイ。REC/phrase grounding/grounding MLLMを網羅(活発) |
| 🟢 | [liudaizong/Awesome-3D-Visual-Grounding](https://github.com/liudaizong/Awesome-3D-Visual-Grounding) | paper-list | 3D Visual Grounding | 281 | 2026-01 | 3D視覚grounding論文に特化(活発) |
| 🟢 | [henghuiding/Awesome-Multimodal-Referring-Segmentation](https://github.com/henghuiding/Awesome-Multimodal-Referring-Segmentation) | awesome | Referring Seg | 249 | 2026-05 | マルチモーダル参照セグメンテーションのリスト |
| 🟢 | [BNU-IVC/Awesome-Gait-Recognition](https://github.com/BNU-IVC/Awesome-Gait-Recognition) | paper-list | 歩容認識 | 187 | 2025-05 | 歩容認識の論文・データセット集(CVPR'25等収録、活発) |
| 🟢 | [Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition](https://github.com/Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition) | paper-list | 微表情認識 | 180 | 2025-08 | 微表情(micro-expression)認識・検出・スポッティングの論文集 |
| 🟢 | [Malitha123/awesome-video-self-supervised-learning](https://github.com/Malitha123/awesome-video-self-supervised-learning) | paper-list | 動画自己教師あり | 171 | 2026-03 | 動画における自己教師あり学習手法の論文集 |
| 🟢 | [GuoleiSun/Awesome-SAM2](https://github.com/GuoleiSun/Awesome-SAM2) | paper-list | SAM2/動画 | 149 | 2025-10 | 画像・動画向けSAM2の論文・コード集 |
| 🟢 | [Event-AHU/Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference) | paper-list | イベントカメラ | 118 | 2026-04 | トップ国際会議掲載のイベント/スパイクカメラ論文集 |
| 🟢 | [M-3LAB/awesome-3d-anomaly-detection](https://github.com/M-3LAB/awesome-3d-anomaly-detection) | awesome | 3D異常検知 | 112 | 2026-05 | 点群・マルチモーダル3D異常検出のサーベイリポジトリ |
| 🟢 | [iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding](https://github.com/iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding) | paper-list | 動画時間的グラウンディング | 91 | 2025-11 | MLLMを用いた動画時間的グラウンディング(VTG-LLM)の最新論文・コード・データ集 |
| 🟢 | [yunfanLu/Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) | survey | 画像復元 | 87 | 2025-05 | 深層画像復元/強調における事前分布のサーベイ |
| 🟢 | [Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking](https://github.com/Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking) | survey | マルチモーダル追跡 | 84 | 2026-04 | RGBT/RGBD/RGBE等のマルチモーダル視覚物体追跡サーベイ |
| 🟢 | [aimagelab/awesome-human-visual-attention](https://github.com/aimagelab/awesome-human-visual-attention) | paper-list | 視覚的注意/saliency | 66 | 2025-05 | saliency・scanpath・視線予測・視覚的注意の論文/リソース集 |
| 🟢 | [Tangkfan/Awesome-Temporal-Video-Grounding](https://github.com/Tangkfan/Awesome-Temporal-Video-Grounding) | paper-list | 動画時間的グラウンディング | 39 | 2025-12 | VMR/TVG/TSGVの論文リスト |
| 🟢 | [aimagelab/awesome-captioning-evaluation](https://github.com/aimagelab/awesome-captioning-evaluation) | paper-list | キャプション評価 | 34 | 2025-11 | MLLM時代の画像キャプション評価に関する論文集 |
| 📑 | [PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) | survey | LiDAR 3D検出 | 609 | 2023-05 | IJCV 2023サーベイ。LiDAR/カメラ/マルチモーダル3D検出を体系化 |
| 📑 | [vlislab22/360_Survey](https://github.com/vlislab22/360_Survey) | survey | 全方位ビジョン | 23 | 2024-12 | 全方位ビジョン(深度推定・3D復元・セグメンテーション)の包括サーベイ |
| 🟡 | [cmhungsteve/Awesome-Transformer-Attention](https://github.com/cmhungsteve/Awesome-Transformer-Attention) | paper-list | Vision Transformer | 5036 | 2024-07 | ViT/Attentionを網羅した極めて包括的な論文リスト |
| 🟡 | [dk-liang/Awesome-Visual-Transformer](https://github.com/dk-liang/Awesome-Visual-Transformer) | awesome | Vision Transformer | 3584 | 2025-01 | CV向けTransformer論文を集めたコレクション |
| 🟡 | [amusi/ECCV2024-Papers-with-Code](https://github.com/amusi/ECCV2024-Papers-with-Code) | paper-list | 会議論文(ECCV) | 2275 | 2024-08 | ECCV 2024の論文とオープンソースプロジェクト集 |
| 🟡 | [JunMa11/SOTA-MedSeg](https://github.com/JunMa11/SOTA-MedSeg) | paper-list | 医用画像セグメンテーション | 1675 | 2023-12 | 各種チャレンジに基づくSOTA医用画像セグメンテーション手法集 |
| 🟡 | [bismex/Awesome-person-re-identification](https://github.com/bismex/Awesome-person-re-identification) | awesome | Person ReID | 1346 | 2024-06 | 教師あり/教師なし/クロスモーダルReIDを網羅した大規模論文リスト |
| 🟡 | [XuyangBai/awesome-point-cloud-registration](https://github.com/XuyangBai/awesome-point-cloud-registration) | paper-list | 点群レジストレーション | 946 | 2024-07 | マッチング戦略別に整理した点群レジストレーション論文集 |
| 🟡 | [yarkable/Awesome-Computer-Vision-Paper-List](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List) | paper-list | 会議論文横断 | 761 | 2024-04 | トップ会議の採択論文を横断検索できるようまとめた論文リスト |
| 🟡 | [hzwer/Awesome-Optical-Flow](https://github.com/hzwer/Awesome-Optical-Flow) | awesome | オプティカルフロー | 647 | 2024-11 | オプティカルフローと関連研究の論文リスト |
| 🟡 | [ChunmingHe/awesome-diffusion-models-in-low-level-vision](https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision) | paper-list | 低レベル視覚 | 552 | 2025-02 | 超解像/インペインティング等の低レベル視覚向け拡散モデル論文集 |
| 🟡 | [DmitryRyumin/CVPR-2023-24-Papers](https://github.com/DmitryRyumin/CVPR-2023-24-Papers) | paper-list | 会議論文(CVPR) | 451 | 2024-07 | CVPR 2023/2024採択論文をトピック別に整理 |
| 🟡 | [wchstrife/Awesome-Image-Matting](https://github.com/wchstrife/Awesome-Image-Matting) | awesome | Image Matting | 438 | 2023-11 | 深層学習ベースのマッティング論文・コード厳選リスト |
| 🟡 | [ZumingHuang/awesome-ocr-resources](https://github.com/ZumingHuang/awesome-ocr-resources) | awesome | OCR | 431 | 2025-01 | OCRの論文・データセットを集めたリソース集 |
| 🟡 | [Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything](https://github.com/Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything) | paper-list | SAM | 372 | 2024-12 | Segment Anything Model(SAM)関連の論文・プロジェクト集 |
| 🟡 | [nus-cvml/awesome-temporal-action-segmentation](https://github.com/nus-cvml/awesome-temporal-action-segmentation) | paper-list | 行動セグメンテーション | 250 | 2024-04 | 時系列行動セグメンテーションの論文・データセット集(活発) |
| 🟡 | [choyingw/Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) | paper-list | 単眼深度推定 | 210 | 2024-10 | 2020年以降の単眼深度推定論文に焦点を当てたリスト |
| 🟡 | [visionxiang/awesome-salient-object-detection](https://github.com/visionxiang/awesome-salient-object-detection) | awesome | 顕著性物体検出 | 147 | 2024-09 | RGB-D等を含む顕著性物体検出のリソース集 |
| 🟡 | [DennisRotondi/awesome-3D-scene-graphs](https://github.com/DennisRotondi/awesome-3D-scene-graphs) | awesome | 3D Scene Graph | 109 | 2024-12 | ロボティクス応用を含む3Dシーングラフ専門リスト |
| 🟡 | [DmitryRyumin/WACV-2024-Papers](https://github.com/DmitryRyumin/WACV-2024-Papers) | paper-list | 会議論文(WACV) | 97 | 2024-09 | WACV 2024の論文を体系的に整理したコレクション |
| 📚 | [jbhuang0604/awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) | awesome | CV全般 | 23290 | 2024-05 | CV全般の書籍・講義・論文・ツール・データセットを網羅した定番リスト |
| 📚 | [nightrome/really-awesome-semantic-segmentation](https://github.com/nightrome/really-awesome-semantic-segmentation) | paper-list | セマンティックセグメンテーション | 404 | 2018-03 | セマンティックセグメンテーション論文リスト(2018で更新停止) |
| 🔴 | [mrgloom/awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) | awesome | セマンティックセグメンテーション | 10834 | 2021-05 | セマンティックセグメンテーションの定番リソース集 |
| 🔴 | [amusi/awesome-object-detection](https://github.com/amusi/awesome-object-detection) | awesome | 物体検出 | 7501 | 2022-12 | R-CNN系・YOLO・SSD等の物体検出論文/実装をまとめた定番リスト |
| 🔴 | [ChanChiChoi/awesome-Face_Recognition](https://github.com/ChanChiChoi/awesome-Face_Recognition) | paper-list | 顔認識 | 4740 | 2023-02 | 顔検出/認識/再構成/生成等を網羅した大規模論文集 |
| 🔴 | [jinwchoi/awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition) | awesome | 行動認識・動画理解 | 4003 | 2023-05 | 行動認識と関連領域のリソースを網羅した定番リスト |
| 🔴 | [weiaicunzai/awesome-image-classification](https://github.com/weiaicunzai/awesome-image-classification) | paper-list | 画像分類 | 3058 | 2022-04 | 2014年以降の深層学習画像分類論文/実装のリスト |
| 🔴 | [hwalsuklee/awesome-deep-text-detection-recognition](https://github.com/hwalsuklee/awesome-deep-text-detection-recognition) | paper-list | テキスト検出・認識 | 2526 | 2021-08 | 深層学習ベースのテキスト検出/認識論文を整理 |
| 🔴 | [cbsudux/awesome-human-pose-estimation](https://github.com/cbsudux/awesome-human-pose-estimation) | awesome | 人物姿勢推定 | 2480 | 2022-10 | 人物姿勢推定の論文・リソース集 |
| 🔴 | [willard-yuan/awesome-cbir-papers](https://github.com/willard-yuan/awesome-cbir-papers) | paper-list | 画像検索(CBIR) | 1763 | 2023-10 | 古典的・代表的な内容ベース画像検索(CBIR)論文集 |
| 🔴 | [SpyderXu/multi-object-tracking-paper-list](https://github.com/SpyderXu/multi-object-tracking-paper-list) | paper-list | 多物体追跡 | 1686 | 2020-04 | 多物体追跡の論文リストとソースコード集 |
| 🔴 | [chongyangtao/Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) | awesome | シーンテキスト認識 | 1675 | 2018-07 | シーンテキストの位置特定・認識に特化したリソース集 |
| 🔴 | [kuanhungchen/awesome-tiny-object-detection](https://github.com/kuanhungchen/awesome-tiny-object-detection) | paper-list | 微小物体検出 | 1626 | 2023-10 | Tiny Object Detection(微小物体検出)の論文・リソース集 |
| 🔴 | [wangzheallen/awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation) | paper-list | 人物姿勢推定 | 1374 | 2020-08 | 2D/3D人物姿勢推定の関連論文集 |
| 🔴 | [zhjohnchan/awesome-image-captioning](https://github.com/zhjohnchan/awesome-image-captioning) | awesome | 画像キャプション | 1072 | 2023-03 | 画像キャプションと関連領域のリソースを年別整理 |
| 🔴 | [jindongwang/activityrecognition](https://github.com/jindongwang/activityrecognition) | paper-list | 行動認識 | 930 | 2019-08 | 行動認識(activity recognition)の資料・コード・データセット集 |
| 🔴 | [polarisZhao/awesome-face](https://github.com/polarisZhao/awesome-face) | awesome | 顔全般 | 914 | 2019-08 | 顔関連アルゴリズム・データセット・論文のキュレーション |
| 🔴 | [clpeng/Awesome-Face-Forgery-Generation-and-Detection](https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection) | paper-list | 顔偽造検出 | 780 | 2022-11 | 顔偽造の生成と検出に関する論文・コード集 |
| 🔴 | [Alvin-Zeng/Awesome-Temporal-Action-Localization](https://github.com/Alvin-Zeng/Awesome-Temporal-Action-Localization) | paper-list | 時系列行動位置推定 | 589 | 2022-09 | temporal action localization/detection/proposalの論文・ベンチマークまとめ |
| 🔴 | [qdrant/awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) | awesome | メトリック学習 | 520 | 2023-04 | 実用的なメトリック学習とその応用のキュレーション |
| 🔴 | [forence/Awesome-Visual-Captioning](https://github.com/forence/Awesome-Visual-Captioning) | paper-list | 視覚キャプション | 410 | 2022-11 | 画像/動画キャプションとSeq2Seq学習にフォーカスした論文集 |
| 🔴 | [Hub-Tian/Awesome-3D-Detectors](https://github.com/Hub-Tian/Awesome-3D-Detectors) | paper-list | 3D物体検出 | 398 | 2022-02 | LiDAR中心の3D検出手法の論文・コード集 |
| 🔴 | [ptkin/Awesome-Super-Resolution](https://github.com/ptkin/Awesome-Super-Resolution) | awesome | 超解像 | 386 | 2019-09 | 超解像リソースのキュレーション |
| 🔴 | [RizhaoCai/Awesome-FAS](https://github.com/RizhaoCai/Awesome-FAS) | paper-list | 顔アンチスプーフィング | 383 | 2022-08 | 顔アンチスプーフィング/PAD/liveness論文の包括的コレクション |
| 🔴 | [scott89/awesome-depth](https://github.com/scott89/awesome-depth) | paper-list | 深度推定 | 337 | 2020-09 | 深度推定の出版物を集めたキュレーションリスト |
| 🔴 | [liuyuan-pal/Awesome-generalizable-6D-object-pose](https://github.com/liuyuan-pal/Awesome-generalizable-6D-object-pose) | paper-list | 6D姿勢推定 | 328 | 2023-04 | 汎化可能な6DoF物体姿勢推定の最新論文集 |
| 🔴 | [GuanRunwei/Awesome-Vision-Transformer-Collection](https://github.com/GuanRunwei/Awesome-Vision-Transformer-Collection) | awesome | Vision Transformer | 256 | 2022-07 | ViTの派生と下流タスクをまとめたコレクション |
| 🔴 | [haoweiz23/Awesome-Fine-grained-Visual-Classification](https://github.com/haoweiz23/Awesome-Fine-grained-Visual-Classification) | paper-list | 細粒度画像分類 | 241 | 2023-09 | 細粒度視覚分類(FGVC)の論文コレクション |
| 🔴 | [FDU-VTS/Awesome-Person-Re-Identification](https://github.com/FDU-VTS/Awesome-Person-Re-Identification) | awesome | Person ReID | 205 | 2021-12 | データセットとサーベイを含む人物再同定リスト |
| 🔴 | [GeorgeDu/6d-object-pose-estimation](https://github.com/GeorgeDu/6d-object-pose-estimation) | paper-list | 6D姿勢推定 | 204 | 2023-06 | 6D物体姿勢推定の論文・コードまとめ |
| 🔴 | [antran89/awesome-optical-flow-algorithm](https://github.com/antran89/awesome-optical-flow-algorithm) | awesome | オプティカルフロー | 159 | 2022-10 | 古典手法からRAFT等の深層学習までのフローアルゴリズム集 |
| 🔴 | [sujiongming/awesome-video-understanding](https://github.com/sujiongming/awesome-video-understanding) | awesome | 動画理解 | 143 | 2017-12 | 動画分類・行動認識・動画データセットのリソース集 |
| 🔴 | [tgc1997/Awesome-Video-Captioning](https://github.com/tgc1997/Awesome-Video-Captioning) | paper-list | 動画キャプション | 121 | 2021-01 | 動画キャプション生成の論文集 |
| 🔴 | [hsientzucheng/awesome-360-vision](https://github.com/hsientzucheng/awesome-360-vision) | paper-list | 360度ビジョン | 121 | 2019-01 | 360度ビジョン全般の論文集 |
| 🔴 | [vvincenttttt/Awesome-3D-Semantic-Segmentation](https://github.com/vvincenttttt/Awesome-3D-Semantic-Segmentation) | paper-list | 3Dセマンティックセグメンテーション | 74 | 2022-09 | 3Dセマンティックセグメンテーションの論文・コード集 |
| 🔴 | [vlislab2022/Awesome-Events-Deep-Learning](https://github.com/vlislab2022/Awesome-Events-Deep-Learning) | awesome | イベントカメラ | 62 | 2023-09 | イベントカメラ向け深層学習リソース集 |
| 🔴 | [Taaccoo/awesome-vqa-latest](https://github.com/Taaccoo/awesome-vqa-latest) | paper-list | VQA | 53 | 2022-08 | VQA論文を継続更新する読書リスト |
| 🔴 | [daqingliu/awesome-rec](https://github.com/daqingliu/awesome-rec) | paper-list | 参照表現理解 | 46 | 2021-05 | Referring Expression Comprehension(REC)専用の論文リスト |
| 🔴 | [lgbwust/awesome-image-retrieval-papers](https://github.com/lgbwust/awesome-image-retrieval-papers) | paper-list | 画像検索 | 36 | 2018-12 | 画像検索論文・実装の包括的コレクション |
| 🔴 | [Huntersxsx/TSGV-Learning-List](https://github.com/Huntersxsx/TSGV-Learning-List) | paper-list | 時間文グラウンディング | 31 | 2022-03 | TSGV/NLVL/VMRの関連研究まとめ |
| 🔴 | [tzxiang/awesome-computer-vision-papers](https://github.com/tzxiang/awesome-computer-vision-papers) | awesome | CV全般・深層学習 | 26 | 2020-09 | CVと深層学習に関する論文・リソースのリスト |
| 🔴 | [immortal13/awesome-hyperspectral-image-classification](https://github.com/immortal13/awesome-hyperspectral-image-classification) | paper-list | ハイパースペクトル画像分類 | 20 | 2023-07 | ハイパースペクトル画像分類の論文・コード集 |
| 🔴 | [luo3300612/Awesome-image-captioning](https://github.com/luo3300612/Awesome-image-captioning) | paper-list | 画像キャプション | 8 | 2019-09 | ICCV/ECCV/CVPR等の画像キャプション論文リスト |
| 🔴 | [bsridatta/Awesome-3D-Human-Pose-Estimation](https://github.com/bsridatta/Awesome-3D-Human-Pose-Estimation) | paper-list | 3D人物姿勢推定 | 5 | 2021-04 | 3D人物姿勢推定に特化した論文コレクション |
| 🔴 | [KainingYing/Awesome-Human-Object-Interaction-Detection](https://github.com/KainingYing/Awesome-Human-Object-Interaction-Detection) | paper-list | HOI検出 | 3 | 2021-08 | 会議・年次別のHOI検出論文集 |

### 🎨 Computer Graphics / 3D / レンダリング  (64件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | awesome | 3D Gaussian Splatting | 8654 | 2026-05 | 3DGSの論文・実装・ビューア・ツールを集めた包括リスト |
| 🟢 | [weihaox/awesome-neural-rendering](https://github.com/weihaox/awesome-neural-rendering) | awesome | neural/differentiable rendering | 2350 | 2026-03 | ニューラルレンダリングと微分可能レンダリングの資料集 |
| 🟢 | [3D-Vision-World/awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) | paper-list | SLAM(NeRF/3DGS) | 2019 | 2026-05 | 暗黙表現・NeRF・3DGSを用いたSLAM論文集 |
| 🟢 | [weihaox/awesome-digital-human](https://github.com/weihaox/awesome-digital-human) | awesome | digital humans | 1945 | 2026-04 | 2D/3D/4D人体モデリング・アバター生成の総合集 |
| 🟢 | [Kedreamix/Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis) | awesome | talking head | 1507 | 2026-05 | トーキングフェイス合成の広範な資源集 |
| 🟢 | [cwchenwang/awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion) | paper-list | 3D generation(拡散) | 1254 | 2026-01 | 3D生成向け拡散モデル論文集 |
| 🟢 | [mmolero/awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing) | awesome | point cloud processing | 797 | 2025-11 | 点群処理のライブラリ・ソフト・資料集 |
| 🟢 | [ruili3/awesome-dust3r](https://github.com/ruili3/awesome-dust3r) | model | 3D基盤モデル | 792 | 2025-11 | DUSt3R系の幾何基盤モデル論文・資源追跡 |
| 🟢 | [hitcslj/Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D) | awesome | 3D generation(AIGC) | 776 | 2026-05 | AIGC 3D(生成・テクスチャ・素材)論文集 |
| 🟢 | [dannyfritz/awesome-ray-tracing](https://github.com/dannyfritz/awesome-ray-tracing) | awesome | ray/path tracing | 656 | 2025-10 | レイトレーシングの論文・コース・実装リスト |
| 🟢 | [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) | paper-list | text-to-3D | 587 | 2026-05 | Text-to-3D/Diffusion-to-3D研究のキュレーション |
| 🟢 | [jslee02/awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) | awesome | 3D graphics libraries | 525 | 2026-05 | 3Dグラフィックスライブラリのキュレーション |
| 🟢 | [yukangcao/Awesome-4D-Spatial-Intelligence](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) | survey | 4D reconstruction | 497 | 2026-05 | 動画からの4D空間知能復元のサーベイ |
| 🟢 | [Housz/awesome-simulation](https://github.com/Housz/awesome-simulation) | awesome | physics simulation | 388 | 2026-03 | CGの物理シミュレーション資源整理 |
| 🟢 | [longxiang-ai/awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) | paper-list | 3D Gaussian Splatting | 287 | 2026-05 | arXivから毎日自動更新される3DGS論文追跡 |
| 🟢 | [KwanWaiPang/Awesome-Transformer-based-SLAM](https://github.com/KwanWaiPang/Awesome-Transformer-based-SLAM) | survey | Transformer SLAM | 270 | 2026-05 | Transformerベースの SLAM のサーベイ用論文集 |
| 🟢 | [KwanWaiPang/Awesome-3DGS-SLAM](https://github.com/KwanWaiPang/Awesome-3DGS-SLAM) | survey | SLAM(3DGS) | 261 | 2026-02 | 3DGS SLAMのサーベイ用論文集 |
| 🟢 | [KwanWaiPang/Awesome-Learning-based-VO-VIO](https://github.com/KwanWaiPang/Awesome-Learning-based-VO-VIO) | survey | 学習ベースVO/VIO | 195 | 2026-04 | 学習ベースの視覚オドメトリ(VO/VIO)のサーベイ用論文集 |
| 🟢 | [zishun/awesome-geometry-processing](https://github.com/zishun/awesome-geometry-processing) | awesome | geometry processing | 171 | 2026-03 | 幾何処理のライブラリ・ツール・資料集 |
| 🟢 | [zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics](https://github.com/zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics) | paper-list | computational optics(SIGGRAPH) | 104 | 2026-04 | SIGGRAPH掲載の計算光学論文の読書リスト |
| 🟢 | [PolySummit/Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation) | paper-list | 3D reconstruction/generation | 78 | 2026-03 | 3D復元・生成の論文・データセット集 |
| 🟢 | [pdaicode/awesome-dynamic-NeRF](https://github.com/pdaicode/awesome-dynamic-NeRF) | paper-list | NeRF(動的) | 67 | 2026-04 | 動的シーン向けNeRFの論文集 |
| 🟢 | [Bigger-and-Stronger/quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey) | survey | quad meshing | 34 | 2026-05 | クワッドメッシング関連の論文・コード・プロジェクト集 |
| 🟢 | [KwanWaiPang/Awesome-Diffusion-based-SLAM](https://github.com/KwanWaiPang/Awesome-Diffusion-based-SLAM) | survey | 拡散SLAM | 34 | 2026-05 | 拡散モデルベースのSLAMのサーベイ用論文集 |
| 🟢 | [Bigger-and-Stronger/awesome-brep-reconstruction](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) | survey | B-rep reconstruction | 29 | 2026-01 | B-rep(境界表現)再構成の論文とOSSプロジェクト集。定期更新 |
| 🟢 | [KwanWaiPang/Awesome-Event-based-SLAM](https://github.com/KwanWaiPang/Awesome-Event-based-SLAM) | survey | イベントSLAM | 21 | 2026-01 | イベントベースSLAMのサーベイ用論文集 |
| 🟢 | [Bigger-and-Stronger/offset-mesh-survey](https://github.com/Bigger-and-Stronger/offset-mesh-survey) | survey | offset mesh | 13 | 2026-05 | オフセットメッシュ生成に関する論文・プロジェクト・コードの継続更新サーベイ |
| 🟢 | [Bigger-and-Stronger/awesome-3d-medial-axis](https://github.com/Bigger-and-Stronger/awesome-3d-medial-axis) | survey | medial axis/skeleton | 5 | 2025-10 | 中心軸(medial axis)/スケルトンとその応用の論文・OSS集。定期更新 |
| 🟢 | [Bigger-and-Stronger/direction-field-survey](https://github.com/Bigger-and-Stronger/direction-field-survey) | survey | direction field | 4 | 2026-05 | 方向場(direction field)に関する論文・プロジェクト・コードの継続更新サーベイ |
| 🟢 | [Bigger-and-Stronger/parameterization-survey](https://github.com/Bigger-and-Stronger/parameterization-survey) | survey | parameterization | 2 | 2026-05 | メッシュパラメータ化に関する論文・プロジェクト・コードの継続更新サーベイ |
| 📑 | [weihaox/Gen3D](https://github.com/weihaox/Gen3D) | survey | 生成的3D画像合成 | 164 | 2025-02 | 深層生成的3D-aware画像合成のサーベイ(CSUR 2023) |
| 📑 | [Bigger-and-Stronger/boundary-layer-generation-survey](https://github.com/Bigger-and-Stronger/boundary-layer-generation-survey) | survey | boundary layer generation | 3 | 2025-02 | 境界層メッシュ生成に関する論文・プロジェクト・コードの継続更新サーベイ |
| 🟡 | [awesome-NeRF/awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) | awesome | NeRF | 6769 | 2025-01 | Neural Radiance Fields論文の定番キュレーションリスト |
| 🟡 | [vsitzmann/awesome-implicit-representations](https://github.com/vsitzmann/awesome-implicit-representations) | awesome | implicit neural representation/SDF | 2635 | 2024-02 | DeepSDF等の暗黙的ニューラル表現の資料集 |
| 🟡 | [NUAAXQ/awesome-point-cloud-analysis-2023](https://github.com/NUAAXQ/awesome-point-cloud-analysis-2023) | paper-list | point cloud | 1589 | 2024-04 | 2017年以降の点群解析論文を日次更新するリスト |
| 🟡 | [JosephPai/Awesome-Talking-Face](https://github.com/JosephPai/Awesome-Talking-Face) | awesome | talking face | 1541 | 2024-12 | トーキングフェイス専門のキュレーション |
| 🟡 | [bluestyle97/awesome-3d-reconstruction-papers](https://github.com/bluestyle97/awesome-3d-reconstruction-papers) | paper-list | 3D reconstruction | 910 | 2023-12 | 深層学習時代の3D復元論文集 |
| 🟡 | [taichi-dev/awesome-taichi](https://github.com/taichi-dev/awesome-taichi) | awesome | physics simulation(Taichi) | 683 | 2024-06 | Taichi製シミュレーション(流体・布等)アプリ集 |
| 🟡 | [3DFaceBody/awesome-3dbody-papers](https://github.com/3DFaceBody/awesome-3dbody-papers) | paper-list | 3D body | 661 | 2024-01 | 3D人体(SMPL等)の論文集 |
| 🟡 | [XYZ-qiyh/Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) | paper-list | multi-view stereo | 634 | 2023-11 | 学習ベースMVS論文のリスト |
| 🟡 | [cwchenwang/awesome-4d-generation](https://github.com/cwchenwang/awesome-4d-generation) | paper-list | 4D generation | 331 | 2024-10 | 4D生成(text-to-4D等)論文リスト |
| 🟡 | [pansanity666/Awesome-Avatars](https://github.com/pansanity666/Awesome-Avatars) | paper-list | avatars | 276 | 2024-04 | 人間アバターの生成・復元・編集の最新進展 |
| 🟡 | [ingra14m/Awesome-Inverse-Rendering](https://github.com/ingra14m/Awesome-Inverse-Rendering) | paper-list | inverse rendering | 258 | 2024-12 | neural field基盤の逆レンダリング論文集 |
| 🟡 | [tkuri/Awesome-InverseRendering](https://github.com/tkuri/Awesome-InverseRendering) | paper-list | inverse rendering | 233 | 2025-04 | 内在分解・逆レンダリング論文リスト |
| 🟡 | [pdaicode/awesome-3dgs](https://github.com/pdaicode/awesome-3dgs) | paper-list | 3D Gaussian Splatting | 122 | 2024-08 | 3DGS関連論文のキュレーション |
| 🟡 | [Jason-cs18/awesome-avatar](https://github.com/Jason-cs18/awesome-avatar) | awesome | avatars(talking) | 59 | 2024-11 | talking-face/talking-body関連資源集 |
| 🟡 | [Run542968/Awesome-3D-Human-Motion-Generation](https://github.com/Run542968/Awesome-3D-Human-Motion-Generation) | paper-list | human motion/animation | 25 | 2024-07 | Text-to-Motion中心の人体動作生成論文集 |
| 🟡 | [Taeyoung96/awesome-Implicit-NeRF-SLAM](https://github.com/Taeyoung96/awesome-Implicit-NeRF-SLAM) | paper-list | SLAM(暗黙表現) | 13 | 2023-11 | 暗黙表現・NeRFのSLAM/ロボティクス応用論文集 |
| 🟡 | [yklcs/awesome-dynamic-scene-representations](https://github.com/yklcs/awesome-dynamic-scene-representations) | paper-list | dynamic/4D scene | 8 | 2024-04 | 動的シーン表現の資料集 |
| 🟡 | [Bigger-and-Stronger/awesome-visualization](https://github.com/Bigger-and-Stronger/awesome-visualization) | awesome | data visualization | 1 | 2025-03 | CG関連のデータ可視化手法・レンダリング事例を記録するリポジトリ |
| 🔴 | [openMVG/awesome_3DReconstruction_list](https://github.com/openMVG/awesome_3DReconstruction_list) | awesome | 3D reconstruction | 4407 | 2021-10 | 画像からの3D復元の古典的論文・資料集 |
| 🔴 | [Yochengliu/awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis) | awesome | point cloud | 4214 | 2023-05 | 点群解析・処理に関する論文とデータセットのリスト |
| 🔴 | [tzutalin/awesome-visual-slam](https://github.com/tzutalin/awesome-visual-slam) | awesome | visual SLAM | 2420 | 2022-05 | 視覚SLAM/視覚オドメトリのOSS・論文集 |
| 🔴 | [kanster/awesome-slam](https://github.com/kanster/awesome-slam) | awesome | SLAM | 1663 | 2020-07 | SLAMのチュートリアル・プロジェクト・コミュニティ集 |
| 🔴 | [justimyhxu/awesome-3D-generation](https://github.com/justimyhxu/awesome-3D-generation) | awesome | 3D generation | 1192 | 2023-03 | 3D生成論文のキュレーションリスト |
| 🔴 | [ericjang/awesome-graphics](https://github.com/ericjang/awesome-graphics) | awesome | computer graphics | 1109 | 2020-02 | CGチュートリアル・論文の総合リスト |
| 🔴 | [SilenceOverflow/Awesome-SLAM](https://github.com/SilenceOverflow/Awesome-SLAM) | paper-list | SLAM | 1096 | 2023-10 | SLAM論文の継続更新リスト |
| 🔴 | [natowi/3D-Reconstruction-with-Deep-Learning-Methods](https://github.com/natowi/3D-Reconstruction-with-Deep-Learning-Methods) | paper-list | 3D reconstruction | 1016 | 2023-05 | 深層学習による3D復元プロジェクトの一覧 |
| 🔴 | [luisdnsantos/awesome-computer-graphics](https://github.com/luisdnsantos/awesome-computer-graphics) | awesome | computer graphics(学習) | 1004 | 2021-07 | CG学習用の書籍・講座・資料集 |
| 🔴 | [subeeshvasu/Awsome_Deep_Geometry_Learning](https://github.com/subeeshvasu/Awsome_Deep_Geometry_Learning) | paper-list | deep geometry | 361 | 2021-08 | 3D形状の深層学習ソリューション資料集 |
| 🔴 | [krahets/awesome-mvs](https://github.com/krahets/awesome-mvs) | awesome | multi-view stereo | 277 | 2022-08 | MVSのチュートリアル・論文・ソフトウェア集 |
| 🔴 | [neil3d/awesome-pbr](https://github.com/neil3d/awesome-pbr) | awesome | physically based rendering | 118 | 2021-01 | PBRの資料・スライド・論文の総合コレクション |
| 🔴 | [tkuri/Awesome-BRDF](https://github.com/tkuri/Awesome-BRDF) | paper-list | material/BRDF | 28 | 2021-06 | BRDF表現に関する論文を表現方式別に整理 |
| 🔴 | [lzhbrian/texture-synthesis-papers](https://github.com/lzhbrian/texture-synthesis-papers) | paper-list | texture synthesis | 4 | 2019-03 | テクスチャ合成論文(コード付き)の集積 |

### 🖌️ 低レベル画像処理 / 復元 / 圧縮  (25件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [zhihongz/awesome-low-light-image-enhancement](https://github.com/zhihongz/awesome-low-light-image-enhancement) | awesome | 低照度強調 | 1821 | 2026-05 | 低照度画像強調のデータセット/手法/論文/評価指標を網羅(活発) |
| 🟢 | [chaofengc/Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment) | awesome | 画質評価(IQA) | 1514 | 2026-04 | IQA論文/データセット/コードの包括集(非常に活発) |
| 🟢 | [SerialLain3170/AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) | awesome | アニメ | 1237 | 2025-12 | アニメ/漫画研究の論文・データセット集(生成・カラー化・キャラアニメ等) |
| 🟢 | [Linfeng-Tang/Image-Fusion](https://github.com/Linfeng-Tang/Image-Fusion) | survey | 画像融合 | 1193 | 2026-04 | 「Deep Learning-based Image Fusion」サーベイ、赤外-可視/医用/マルチ露出等横断 |
| 🟢 | [MarkMoHR/Awesome-Image-Colorization](https://github.com/MarkMoHR/Awesome-Image-Colorization) | awesome | カラー化 | 1157 | 2026-04 | 深層学習ベースの画像/動画カラー化論文(2025-2026まで活発) |
| 🟢 | [ppingzhang/Awesome-Deep-Learning-Based-Video-Compression](https://github.com/ppingzhang/Awesome-Deep-Learning-Based-Video-Compression) | paper-list | 動画圧縮 | 292 | 2025-09 | 深層学習ベース動画圧縮の論文リスト |
| 🟢 | [rebeccaeexu/Awesome-High-Dynamic-Range-Imaging](https://github.com/rebeccaeexu/Awesome-High-Dynamic-Range-Imaging) | awesome | HDR | 236 | 2026-02 | HDR論文集(マルチ/シングルフレーム・HDRTV・HDR動画・トーンマッピング) |
| 🟢 | [visionxiang/awesome-computational-photography](https://github.com/visionxiang/awesome-computational-photography) | paper-list | 計算写真 | 179 | 2025-07 | 深層学習による計算写真(画像マッチング・アラインメント・スティッチング・安定化) |
| 🟢 | [IShengFang/TypographyResearchCollection](https://github.com/IShengFang/TypographyResearchCollection) | paper-list | フォント生成 | 159 | 2025-08 | タイポグラフィ関連のCG/CV/ML研究収集(フォント生成・アニメーション含む) |
| 🟢 | [CMLab-Korea/Awesome-Video-Frame-Interpolation](https://github.com/CMLab-Korea/Awesome-Video-Frame-Interpolation) | survey | 動画フレーム補間 | 147 | 2026-04 | IEEE TCSVT'26採録のVFIサーベイ。250+論文を体系化(活発) |
| 🟢 | [TaoWangzj/Awesome-Image-Restoration](https://github.com/TaoWangzj/Awesome-Image-Restoration) | survey | 画像復元(包括) | 13 | 2025-11 | サーベイ「Deep Image Restoration」付随、denoise/deblur/SR/dehaze/derain等横断 |
| 🟡 | [oneTaken/Awesome-Denoise](https://github.com/oneTaken/Awesome-Denoise) | awesome | デノイズ | 503 | 2024-04 | 画像/バースト/動画デノイズ論文を色空間・ノイズモデル別に整理 |
| 🟡 | [GuoLanqing/Awesome-Shadow-Removal](https://github.com/GuoLanqing/Awesome-Shadow-Removal) | awesome | 影除去 | 395 | 2025-04 | 影除去の論文/コード/データセット/指標集(活発) |
| 🟡 | [ChenyangLEI/awesome-reflection-removal](https://github.com/ChenyangLEI/awesome-reflection-removal) | awesome | 反射除去 | 158 | 2024-12 | 反射除去手法集(単一画像/フラッシュ/偏光/インタラクティブ) |
| 🟡 | [liuzhen03/awesome-video-enhancement](https://github.com/liuzhen03/awesome-video-enhancement) | paper-list | 動画強調 | 156 | 2024-08 | 動画超解像・補間・デノイズ・デブラー・インペインティングを横断する論文集 |
| 🟡 | [YuZhao1999/UIE](https://github.com/YuZhao1999/UIE) | paper-list | 水中画像強調 | 115 | 2024-05 | 水中画像強調のリソースリスト |
| 🟡 | [Xinjie-Q/Awesome-Neural-Compression](https://github.com/Xinjie-Q/Awesome-Neural-Compression) | awesome | ニューラル圧縮 | 83 | 2024-08 | 画像・動画・点群・NeRF・3DGSまで網羅したニューラル圧縮の論文/リソース集 |
| 🟡 | [kawchar85/Awesome-Deblurring-Resources](https://github.com/kawchar85/Awesome-Deblurring-Resources) | paper-list | デブラー | 13 | 2024-08 | 年別に整理された画像・動画デブラー論文/データセット(活発) |
| 🔴 | [ycjing/Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers) | paper-list | スタイル変換 | 1639 | 2022-02 | サーベイ「Neural Style Transfer: A Review」付随の代表論文・コード集 |
| 🔴 | [nnUyi/DerainZoo](https://github.com/nnUyi/DerainZoo) | paper-list | 雨除去 | 516 | 2022-05 | 雨除去の手法・データセット・コード集(単一画像/動画) |
| 🔴 | [tzxiang/awesome-image-alignment-and-stitching](https://github.com/tzxiang/awesome-image-alignment-and-stitching) | paper-list | 画像スティッチング | 462 | 2022-08 | 画像アラインメント・スティッチングのキュレーション |
| 🔴 | [subeeshvasu/Awesome-Image-Distortion-Correction](https://github.com/subeeshvasu/Awesome-Image-Distortion-Correction) | awesome | 歪み補正 | 281 | 2023-07 | ローリングシャッター効果・放射状歪みの補正に関する資源集 |
| 🔴 | [youngguncho/awesome-dehazing](https://github.com/youngguncho/awesome-dehazing) | awesome | デヘイズ | 202 | 2020-08 | 単一/複数画像デヘイズ・水中強調・データセットを分類した論文集 |
| 🔴 | [qyzdao/Sketch-Based-Deep-Learning](https://github.com/qyzdao/Sketch-Based-Deep-Learning) | paper-list | スケッチ/線画 | 178 | 2021-05 | スケッチベース深層学習の論文集(線画カラー化・ベクトル化等) |
| 🔴 | [lyh-18/Video-Frame-Interpolation-Collections](https://github.com/lyh-18/Video-Frame-Interpolation-Collections) | paper-list | 動画フレーム補間 | 65 | 2021-11 | SOTA VFI手法のコレクション |

### 💬 NLP / 大規模言語モデル(LLM)  (96件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) | awesome | LLM全般 | 26875 | 2025-07 | LLM論文・モデル・ツール・コースを網羅した最大級のリスト |
| 🟢 | [keon/awesome-nlp](https://github.com/keon/awesome-nlp) | awesome | NLP全般 | 18653 | 2026-05 | NLP全般のライブラリ・データ・チュートリアルを集めた定番リスト |
| 🟢 | [Mooler0410/LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) | survey | LLM全般 | 10189 | 2026-04 | LLM進化系統樹と実務活用ガイドをまとめたサーベイ集 |
| 🟢 | [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) | awesome | prompt engineering | 8059 | 2026-05 | 高評価GPTsのプロンプトと先端プロンプト工学論文のコレクション |
| 🟢 | [hijkzzz/Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) | paper-list | reasoning(o1) | 6898 | 2025-12 | OpenAI o1と推論技法に焦点を当てた論文・ブログ集 |
| 🟢 | [promptslab/Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) | awesome | prompt engineering | 5979 | 2026-05 | GPT/ChatGPT向けプロンプト技法の論文・ツールを集めたリスト |
| 🟢 | [xlite-dev/Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) | paper-list | efficient transformers/inference | 5260 | 2026-04 | FlashAttention・PagedAttention等の推論高速化論文集 |
| 🟢 | [eosphoros-ai/Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) | awesome | text-to-SQL | 3658 | 2026-01 | Text2SQL/Text2DSL等のチュートリアルとリソース集 |
| 🟢 | [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) | awesome | LLM推論 | 3622 | 2026-04 | CoTからo1/DeepSeek-R1までのLLM推論論文集(非常に活発) |
| 🟢 | [Meirtz/Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) | survey | context engineering | 3157 | 2026-05 | プロンプト工学から本番AIシステムまでのコンテキスト工学サーベイ |
| 🟢 | [XiaoxinHe/Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) | awesome | graph + LLM | 2431 | 2025-11 | グラフ関連LLMのリソースを集めたキュレーション |
| 🟢 | [DEEP-PolyU/Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | awesome | RAG(graph-based) | 2410 | 2026-05 | グラフベースRAGのサーベイ・論文・ベンチマーク集 |
| 🟢 | [EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) | paper-list | in-context learning | 2236 | 2026-05 | ICLとプロンプト工学の最新リソースを継続更新する論文リスト |
| 🟢 | [zjukg/KG-LLM-Papers](https://github.com/zjukg/KG-LLM-Papers) | paper-list | knowledge graph + LLM | 2194 | 2026-03 | 知識グラフとLLMを統合する論文リスト |
| 🟢 | [Xnhyacinth/Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) | paper-list | long context | 2104 | 2026-05 | 長文脈モデリング(効率的注意・KVキャッシュ・位置符号化等)の論文集 |
| 🟢 | [lmmlzn/Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets) | awesome | LLMデータセット | 1466 | 2026-03 | 事前学習コーパス・指示/選好/評価データセットを5観点で整理 |
| 🟢 | [DEEP-PolyU/Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) | survey | text-to-SQL | 1322 | 2026-05 | TKDE2025サーベイに基づくLLM Text-to-SQLの論文・ベンチマーク集 |
| 🟢 | [hemingkx/SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) | survey | 投機的デコーディング | 1238 | 2026-05 | 投機的デコーディングの必読論文・ブログ集(サーベイ連動) |
| 🟢 | [zjunlp/KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) | paper-list | knowledge editing | 1231 | 2025-07 | LLMの知識編集に関する論文リスト |
| 🟢 | [EdinburghNLP/awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) | paper-list | hallucination detection | 1095 | 2026-05 | LLMの幻覚検出論文をモデル別に整理したリスト |
| 🟢 | [HillZhang1999/llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) | survey | hallucination | 1083 | 2025-09 | 「Siren's Song in the AI Ocean」幻覚サーベイの読み物リスト |
| 🟢 | [iwangjian/Paper-Reading-ConvAI](https://github.com/iwangjian/Paper-Reading-ConvAI) | paper-list | conversational AI | 1041 | 2026-05 | 対話システムとNLG中心の会話AI論文リスト |
| 🟢 | [zjunlp/Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers) | paper-list | chain-of-thought reasoning | 1007 | 2025-05 | ACL2023サーベイ「Reasoning with LM Prompting」の論文リスト |
| 🟢 | [OpenDataBox/awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) | survey | データキュレーション | 781 | 2026-03 | 「LLM × DATA」サーベイ公式リポジトリ |
| 🟢 | [Eclipsess/Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) | survey | 効率的推論 | 768 | 2026-02 | 「Stop Overthinking」効率的推論サーベイ(TMLR2025)の論文集 |
| 🟢 | [CSHaitao/Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) | survey | LLM-as-judge | 580 | 2025-07 | 「LLMs-as-Judges」評価手法サーベイの公式論文集 |
| 🟢 | [withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) | survey | MoE | 499 | 2025-07 | TKDE採択「MoE in LLMs」サーベイの公式論文集 |
| 🟢 | [quchangle1/LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) | survey | tool learning | 484 | 2025-08 | ツール学習サーベイの公式リポジトリ。task planning/tool selection等で分類 |
| 🟢 | [pprp/Awesome-LLM-Quantization](https://github.com/pprp/Awesome-LLM-Quantization) | awesome | quantization | 424 | 2026-04 | LLM量子化に特化した論文リスト |
| 🟢 | [MoE-Inf/awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference) | paper-list | MoE inference | 393 | 2026-03 | MoEモデルの推論最適化論文を集めたリスト |
| 🟢 | [ThreeSR/Awesome-Inference-Time-Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling) | awesome | 推論時スケーリング | 384 | 2026-05 | 推論時/テスト時スケーリングの論文リスト(活発) |
| 🟢 | [Xianjun-Yang/Awesome_papers_on_LLMs_detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) | paper-list | 生成テキスト検出 | 287 | 2025-06 | LLM生成テキスト・コード検出の論文リスト |
| 🟢 | [wangbing1416/Awesome-Fake-News-Detection](https://github.com/wangbing1416/Awesome-Fake-News-Detection) | awesome | フェイクニュース検出 | 164 | 2026-04 | フェイクニュース・噂検出の論文リスト |
| 🟢 | [gotutiyan/GEC-Info](https://github.com/gotutiyan/GEC-Info) | paper-list | 文法誤り訂正(GEC) | 128 | 2026-01 | GEC論文を収集・分類したリポジトリ |
| 🟢 | [ryokamoi/llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) | paper-list | 自己修正 | 81 | 2026-05 | LLM自己修正の論文リスト(サーベイ準拠) |
| 🟢 | [Applied-Machine-Learning-Lab/Awesome-Function-Callings](https://github.com/Applied-Machine-Learning-Lab/Awesome-Function-Callings) | paper-list | function calling | 71 | 2026-04 | LLMのfunction calling特化の論文リスト |
| 🟢 | [VanillaCreamer/Awesome-Personalized-LLMs](https://github.com/VanillaCreamer/Awesome-Personalized-LLMs) | paper-list | パーソナライズLLM | 46 | 2026-05 | パーソナライズドLLM(嗜好モデル化・persona制御・記憶ベース)の最新論文集 |
| 🟢 | [marlin-codes/awesome-lora-adapter](https://github.com/marlin-codes/awesome-lora-adapter) | paper-list | LoRA/adapter | 22 | 2026-05 | LoRA・アダプタ系の手法を集めた論文リスト |
| 🟢 | [XiaoshuangJi/Awesome-PEFT](https://github.com/XiaoshuangJi/Awesome-PEFT) | awesome | PEFT/LoRA | 7 | 2026-03 | LoRA各種派生を中心としたPEFT論文・ライブラリ・実装集 |
| 🟢 | [SuperBruceJia/Awesome-Text-Generation-Evaluation](https://github.com/SuperBruceJia/Awesome-Text-Generation-Evaluation) | awesome | NLG評価 | 4 | 2026-05 | NLG評価指標(参照あり/なし)のキュレーションリスト |
| 📑 | [RUCAIBox/LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) | survey | LLM全般 | 12164 | 2025-03 | 「A Survey of Large Language Models」公式リポジトリ |
| 📑 | [NiuTrans/ABigSurvey](https://github.com/NiuTrans/ABigSurvey) | survey | NLP/ML全般 | 2032 | 2024-03 | NLP・MLの数百本のサーベイ論文を一覧化したサーベイのサーベイ |
| 📑 | [hymie122/RAG-Survey](https://github.com/hymie122/RAG-Survey) | survey | RAG | 1788 | 2024-08 | 「RAG for AI-Generated Content」サーベイの分類体系と論文集 |
| 📑 | [PeterGriffinJin/Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) | survey | LLM on graphs | 991 | 2025-03 | 「LLMs on Graphs」TKDEサーベイの論文・リソース集 |
| 📑 | [tjunlp-lab/Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) | survey | LLM evaluation | 803 | 2024-05 | 「Evaluating LLMs: A Comprehensive Survey」の論文集 |
| 📑 | [NiuTrans/CNSurvey](https://github.com/NiuTrans/CNSurvey) | survey | 中文サーベイ集 | 580 | 2023-05 | NLP・機械学習の中国語サーベイ文章リスト |
| 📑 | [NiuTrans/ABigSurveyOfLLMs](https://github.com/NiuTrans/ABigSurveyOfLLMs) | survey | LLMサーベイ集 | 349 | 2025-02 | LLMに関する150本以上のサーベイを集めたコレクション |
| 📑 | [caiyinqiong/Semantic-Retrieval-Models](https://github.com/caiyinqiong/Semantic-Retrieval-Models) | survey | dense retrieval | 340 | 2023-06 | 意味検索モデル(DPR, RAG, RepBERT等)を網羅したTOIS採択サーベイの論文リスト |
| 📑 | [IAAR-Shanghai/CTGSurvey](https://github.com/IAAR-Shanghai/CTGSurvey) | survey | 制御テキスト生成 | 205 | 2024-08 | LLM向け制御テキスト生成のサーベイ論文リスト(学習時/推論時手法を分類) |
| 📑 | [THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models](https://github.com/THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models) | survey | PEFT | 112 | 2025-03 | 基盤モデル向けPEFT手法を体系的にまとめたサーベイ兼論文リスト |
| 📑 | [Magnetic2014/llm-alignment-survey](https://github.com/Magnetic2014/llm-alignment-survey) | survey | alignment | 82 | 2023-09 | 「LLM Alignment: A Survey」のアライメント読み物リスト |
| 📑 | [wutong8023/Awesome_Information_Extraction](https://github.com/wutong8023/Awesome_Information_Extraction) | survey | 情報抽出 | 72 | 2023-01 | RE・EE・slot fillingを含むIE文献サーベイ |
| 📑 | [luo-junyu/Awesome-Data-Efficient-LLM](https://github.com/luo-junyu/Awesome-Data-Efficient-LLM) | survey | データ効率LLM | 57 | 2025-02 | データ効率・データ中心のLLM論文集(サーベイ付き) |
| 🟡 | [huybery/Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) | awesome | code generation | 1288 | 2024-12 | コード生成LLM研究の厳選キュレーションリスト |
| 🟡 | [quqxui/Awesome-LLM4IE-Papers](https://github.com/quqxui/Awesome-LLM4IE-Papers) | paper-list | 生成的情報抽出 | 1060 | 2024-11 | LLMによる生成的情報抽出(NER/RE/EE)の論文集 |
| 🟡 | [thunlp/ToolLearningPapers](https://github.com/thunlp/ToolLearningPapers) | paper-list | tool learning | 921 | 2024-07 | 基盤モデルのツール学習(tool learning)の必読論文集 |
| 🟡 | [dqxiu/ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) | paper-list | in-context learning | 876 | 2024-10 | In-Context Learningサーベイに基づく論文リスト |
| 🟡 | [ict-bigdatalab/awesome-pretrained-models-for-information-retrieval](https://github.com/ict-bigdatalab/awesome-pretrained-models-for-information-retrieval) | awesome | neural IR | 676 | 2024-01 | IR向け事前学習モデル(pretraining for IR)の論文集 |
| 🟡 | [codecaution/Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) | paper-list | MoE | 666 | 2024-10 | MoE研究の読み物リスト |
| 🟡 | [BaptisteBlouin/EventExtractionPapers](https://github.com/BaptisteBlouin/EventExtractionPapers) | paper-list | イベント抽出 | 580 | 2024-03 | イベント抽出タスク中心のNLPリソースリスト |
| 🟡 | [RenzeLou/awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning) | paper-list | instruction tuning | 510 | 2024-04 | Instruction Tuning/Following論文とデータセット集 |
| 🟡 | [hzy312/Awesome-LLM-Watermark](https://github.com/hzy312/Awesome-LLM-Watermark) | paper-list | LLMウォーターマーク | 375 | 2024-12 | 最新のLLMウォーターマーク論文を継続更新するリスト |
| 🟡 | [RUCAIBox/awesome-llm-pretraining](https://github.com/RUCAIBox/awesome-llm-pretraining) | awesome | 事前学習データ | 375 | 2025-04 | LLM事前学習のデータ・フレームワーク・手法リソース集 |
| 🟡 | [ZhengZixiang/ABSAPapers](https://github.com/ZhengZixiang/ABSAPapers) | paper-list | aspect-based sentiment | 363 | 2024-03 | アスペクトベース感情分析(ABSA)の論文・リソース集 |
| 🟡 | [LuckyyySTA/Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) | paper-list | hallucination | 335 | 2024-03 | LLM幻覚に関する論文リスト |
| 🟡 | [AGI-Edgerunners/LLM-Optimizers-Papers](https://github.com/AGI-Edgerunners/LLM-Optimizers-Papers) | paper-list | LLMオプティマイザ | 252 | 2024-03 | LLMを最適化器として使う/プロンプト自動最適化の必読論文集 |
| 🟡 | [zorazrw/awesome-tool-llm](https://github.com/zorazrw/awesome-tool-llm) | awesome | tool use | 243 | 2024-08 | ツール拡張LLM(ToRA, MINT等)を集めたキュレーションリスト |
| 🟡 | [YHPeter/Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) | paper-list | RAG evaluation | 198 | 2025-04 | 「Evaluation of RAG: A Survey」公式の評価論文リスト |
| 🟡 | [Dereck0602/Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) | awesome | テスト時計算 | 152 | 2025-03 | テスト時LLM(self-correction/refine含む)論文集 |
| 🟡 | [zjunlp/Low-resource-KEPapers](https://github.com/zjunlp/Low-resource-KEPapers) | paper-list | 低リソース情報抽出 | 135 | 2024-11 | 低リソース情報抽出(NER/RE/EE)の論文・ツール・データセット集 |
| 🟡 | [DmitryRyumin/EMNLP-2023-Papers](https://github.com/DmitryRyumin/EMNLP-2023-Papers) | paper-list | 会議論文(EMNLP) | 111 | 2024-05 | EMNLP 2023の論文を体系的に整理したコレクション |
| 🟡 | [bobxwu/Paper-Neural-Topic-Models](https://github.com/bobxwu/Paper-Neural-Topic-Models) | paper-list | トピックモデル | 95 | 2024-07 | ニューラルトピックモデル(NTM)の論文集 |
| 🟡 | [USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation](https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation) | paper-list | RAG | 89 | 2025-03 | 知識指向RAGサーベイに基づく論文分類リスト |
| 🟡 | [tjunlp-lab/Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers) | paper-list | multilingual NLP | 34 | 2025-01 | 多言語LLMの論文リスト |
| 🟡 | [AngxiaoYue/awesome-llm-tool-learning](https://github.com/AngxiaoYue/awesome-llm-tool-learning) | paper-list | tool learning | 28 | 2024-07 | LLMのツール学習論文(Gorilla, HuggingGPT, ART等)のリスト |
| 🟡 | [Junting-Lu/Awesome-LLM-Reasoning-Techniques](https://github.com/Junting-Lu/Awesome-LLM-Reasoning-Techniques) | paper-list | reasoning | 18 | 2024-10 | CoTやo1を含むLLM推論技法の論文・リソース集 |
| 📦 | [neemakot/Fact-Checking-Survey](https://github.com/neemakot/Fact-Checking-Survey) | survey | ファクトチェック | 51 | 2021-01 | COLING2020「Explainable Automated Fact-Checking」サーベイの論文集 |
| 🔴 | [thunlp/PromptPapers](https://github.com/thunlp/PromptPapers) | paper-list | プロンプトチューニング | 4312 | 2023-07 | 事前学習モデルのプロンプトベースチューニングの必読論文集 |
| 🔴 | [MLNLP-World/Top-AI-Conferences-Paper-with-Code](https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code) | paper-list | conference papers | 2653 | 2022-10 | ACL/EMNLP/NAACL/COLING等トップ会議のコード付き論文集 |
| 🔴 | [fuzhenxin/Style-Transfer-in-Text](https://github.com/fuzhenxin/Style-Transfer-in-Text) | paper-list | テキストスタイル変換 | 1623 | 2023-03 | テキストスタイル変換の定番論文リスト(教師あり/なし/評価を分類) |
| 🔴 | [mathsyouth/awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization) | awesome | summarization | 1539 | 2023-01 | テキスト要約の論文・ツール・データセット集 |
| 🔴 | [roomylee/awesome-relation-extraction](https://github.com/roomylee/awesome-relation-extraction) | awesome | 関係抽出 | 1225 | 2022-01 | 関係抽出に特化したリソースリスト |
| 🔴 | [seriousran/awesome-qa](https://github.com/seriousran/awesome-qa) | awesome | question answering | 767 | 2022-01 | 質問応答のデータセット・論文・リソース集 |
| 🔴 | [declare-lab/awesome-sentiment-analysis](https://github.com/declare-lab/awesome-sentiment-analysis) | paper-list | sentiment analysis | 538 | 2023-03 | 感情分析論文の読み物リスト |
| 🔴 | [accelerated-text/awesome-nlg](https://github.com/accelerated-text/awesome-nlg) | awesome | NLG全般 | 480 | 2023-09 | NLG全般のリソース集(ツール/論文/データ) |
| 🔴 | [pfliu-nlp/Named-Entity-Recognition-NER-Papers](https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers) | paper-list | named entity recognition | 392 | 2022-02 | 7会議のNER論文を網羅したリスト |
| 🔴 | [Doragd/Awesome-Sentence-Embedding](https://github.com/Doragd/Awesome-Sentence-Embedding) | awesome | 文埋め込み | 314 | 2023-10 | 文表現学習論文とSTSリーダーボード(SimCSE等)を収録 |
| 🔴 | [thunlp/DeltaPapers](https://github.com/thunlp/DeltaPapers) | paper-list | PEFT/Delta Tuning | 285 | 2023-06 | 事前学習モデルのパラメータ効率チューニング(Delta Tuning)の必読論文集 |
| 🔴 | [RUCAIBox/Awesome-KBQA](https://github.com/RUCAIBox/Awesome-KBQA) | paper-list | knowledge base QA | 181 | 2022-04 | 知識ベースQA(KBQA)の論文・ツール・リーダーボード集 |
| 🔴 | [audreycs/Accepted-Papers-Lists](https://github.com/audreycs/Accepted-Papers-Lists) | paper-list | conference papers | 147 | 2022-12 | 主要ジャーナル・会議の採択論文リストをまとめたリポジトリ |
| 🔴 | [NiuTrans/MT-paper-lists](https://github.com/NiuTrans/MT-paper-lists) | paper-list | machine translation | 124 | 2020-12 | 会議別に機械翻訳論文を整理したリスト |
| 🔴 | [liang8qi/Data-to-Text-Generation](https://github.com/liang8qi/Data-to-Text-Generation) | paper-list | Data-to-text | 108 | 2023-05 | data-to-text生成の論文・データセット集 |
| 🔴 | [tjunlp-lab/awesome-NLP-Machine-Learning](https://github.com/tjunlp-lab/awesome-NLP-Machine-Learning) | paper-list | NLP×ML技法 | 35 | 2020-03 | NLP研究向けの機械学習技法(RL/自己教師あり等)の論文・コード集 |
| 🔴 | [thuiar/AWESOME-Dialogue](https://github.com/thuiar/AWESOME-Dialogue) | paper-list | dialogue systems | 15 | 2020-06 | 対話・インタラクティブシステムの論文リスト |
| 🔴 | [simran-khanuja/awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp) | awesome | multilingual NLP | 8 | 2023-07 | 英語以外を対象とした多言語NLP研究のキュレーション |
| 🔴 | [aarsri/AwesomeSemanticParsing](https://github.com/aarsri/AwesomeSemanticParsing) | awesome | 意味解析 | 0 | 2020-11 | 意味解析の論文・リソース集 |

### 🖼️ 生成AI / Diffusion / 画像・動画生成  (42件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [showlab/Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) | awesome | 動画生成 | 5672 | 2026-05 | 動画生成・編集の拡散モデルを集めた定番リスト |
| 🟢 | [nightrome/really-awesome-gan](https://github.com/nightrome/really-awesome-gan) | paper-list | GAN | 3774 | 2025-08 | GAN論文を集めた網羅的リスト |
| 🟢 | [minar09/awesome-virtual-try-on](https://github.com/minar09/awesome-virtual-try-on) | awesome | 仮想試着 | 3105 | 2026-05 | 仮想試着の論文/コード/データセットの定番リスト |
| 🟢 | [Yutong-Zhou-cv/Awesome-Text-to-Image](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image) | survey | text-to-image | 2435 | 2026-02 | テキストから画像生成のサーベイ的論文リスト |
| 🟢 | [ChenHsing/Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) | survey | 動画生成 | 2293 | 2026-04 | Video Diffusion Modelのサーベイ(CSUR) |
| 🟢 | [wangkai930418/awesome-diffusion-categorized](https://github.com/wangkai930418/awesome-diffusion-categorized) | awesome | diffusion総合 | 2207 | 2026-03 | Diffusion論文をサブ領域別に分類した実用的コレクション |
| 🟢 | [harlanhong/awesome-talking-head-generation](https://github.com/harlanhong/awesome-talking-head-generation) | paper-list | talking head | 1910 | 2026-04 | トーキングヘッド生成の論文リスト |
| 🟢 | [Daisy-Zhang/Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) | awesome | Deepfake検出 | 1789 | 2025-09 | Deepfake検出のツール/論文/コード |
| 🟢 | [weihaox/awesome-image-translation](https://github.com/weihaox/awesome-image-translation) | awesome | 画像間変換 | 1233 | 2025-09 | image-to-image translationに関する優良資源のコレクション |
| 🟢 | [lixinustc/Awesome-diffusion-model-for-image-processing](https://github.com/lixinustc/Awesome-diffusion-model-for-image-processing) | survey | 画像処理 | 946 | 2026-04 | 復元/強調/符号化/品質評価の拡散モデル整理 |
| 🟢 | [showlab/Awesome-Unified-Multimodal-Models](https://github.com/showlab/Awesome-Unified-Multimodal-Models) | paper-list | 統一マルチモーダル | 825 | 2025-10 | 理解と生成を統一するモデルの論文集 |
| 🟢 | [ChaofanTao/Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) | survey | 自己回帰生成 | 796 | 2026-05 | ビジョンの自己回帰モデルサーベイ(TMLR 2025) |
| 🟢 | [AlonzoLeeeooo/awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | awesome | 動画生成 | 769 | 2026-03 | 動画生成研究を集めたコレクション |
| 🟢 | [AlonzoLeeeooo/awesome-text-to-image-studies](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) | awesome | text-to-image | 759 | 2026-04 | text-to-image研究を集めた継続更新リスト |
| 🟢 | [flyingby/Awesome-Deepfake-Generation-and-Detection](https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection) | survey | Deepfake検出 | 637 | 2026-05 | Deepfake生成と検出のサーベイ |
| 🟢 | [kuleshov-group/awesome-discrete-diffusion-models](https://github.com/kuleshov-group/awesome-discrete-diffusion-models) | awesome | 離散拡散 | 561 | 2025-09 | 離散拡散モデルに特化した資源リスト |
| 🟢 | [gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion](https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion) | awesome | 世界モデル | 561 | 2026-05 | AR+拡散の動画世界モデル(アルゴリズム/応用/基盤) |
| 🟢 | [atfortes/Awesome-Controllable-Diffusion](https://github.com/atfortes/Awesome-Controllable-Diffusion) | awesome | 制御生成 | 505 | 2025-06 | ControlNet・DreamBooth・IP-Adapter等の制御生成資源 |
| 🟢 | [ziqihuangg/Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model) | paper-list | 世界モデル | 484 | 2026-03 | 動画生成から世界モデルへの流れを整理 |
| 🟢 | [FudanCVL/Awesome-Image-Editing](https://github.com/FudanCVL/Awesome-Image-Editing) | survey | 画像編集 | 471 | 2025-08 | T2Iモデルによる画像編集のサーベイ |
| 🟢 | [ziqihuangg/Awesome-Evaluation-of-Visual-Generation](https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation) | paper-list | 生成評価 | 444 | 2026-05 | 視覚生成の評価指標/モデル/システム集 |
| 🟢 | [lxa9867/Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation) | paper-list | 自己回帰生成 | 431 | 2025-06 | 自己回帰ビジュアル生成の最新論文追跡 |
| 🟢 | [Zheng-Chong/Awesome-Try-On-Models](https://github.com/Zheng-Chong/Awesome-Try-On-Models) | paper-list | 仮想試着 | 416 | 2026-01 | 仮想試着モデル(2025含む)を整理 |
| 🟢 | [ant-research/Awesome-AIGC-Image-Video-Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) | paper-list | AI生成検出 | 387 | 2026-05 | AI生成画像/動画検出の最新研究集 |
| 🟢 | [AlonzoLeeeooo/awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) | awesome | inpainting | 384 | 2026-02 | 画像インペインティング研究のコレクション |
| 🟢 | [qiqitao77/Awesome-Comprehensive-Deepfake-Detection](https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection) | paper-list | Deepfake検出 | 313 | 2026-04 | Deepfake検出の包括的論文リスト |
| 🟢 | [wenhao728/awesome-diffusion-v2v](https://github.com/wenhao728/awesome-diffusion-v2v) | paper-list | 動画編集 | 287 | 2026-04 | 拡散ベースVideo-to-Video編集の論文+ベンチマーク |
| 🟢 | [soraw-ai/Awesome-Text-to-Video-Generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation) | survey | text-to-video | 260 | 2026-03 | Soraサーベイ準拠のT2V/I2V論文リスト |
| 🟢 | [G-U-N/Awesome-Consistency-Models](https://github.com/G-U-N/Awesome-Consistency-Models) | awesome | consistency/flow | 131 | 2025-12 | Consistency Modelの資源リスト |
| 📑 | [weihaox/GAN-Inversion](https://github.com/weihaox/GAN-Inversion) | survey | GAN Inversion | 1126 | 2025-02 | GAN Inversionのサーベイ(TPAMI 2022)付随リポジトリ |
| 📑 | [jianzhnie/awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) | survey | text-to-video | 730 | 2024-07 | Text-to-Video生成のサーベイ |
| 🟡 | [diff-usion/Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) | awesome | diffusion総合 | 12336 | 2024-08 | Diffusion Modelの論文・資源を網羅した最大級のリスト |
| 🟡 | [GuoLanqing/Awesome-High-Resolution-Diffusion](https://github.com/GuoLanqing/Awesome-High-Resolution-Diffusion) | paper-list | 高解像度生成 | 169 | 2024-12 | 高解像度画像/動画合成の拡散論文 |
| 🟡 | [shaopengw/Awesome-Music-Generation](https://github.com/shaopengw/Awesome-Music-Generation) | model | 音楽生成 | 165 | 2025-03 | 音楽生成モデルMG²の資源 |
| 🟡 | [moatifbutt/awesome-diffusion-iclr-2025](https://github.com/moatifbutt/awesome-diffusion-iclr-2025) | paper-list | 学会拡散 | 61 | 2024-10 | ICLR 2025の拡散関連投稿リスト |
| 📚 | [hindupuravinash/the-gan-zoo](https://github.com/hindupuravinash/the-gan-zoo) | paper-list | GAN | 14698 | 2023-10 | 命名された全GANを一覧化した古典的リスト |
| 🔴 | [nashory/gans-awesome-applications](https://github.com/nashory/gans-awesome-applications) | awesome | GAN応用 | 5100 | 2023-08 | GANの応用・デモを集めたキュレーションリスト |
| 🔴 | [altryne/awesome-ai-art-image-synthesis](https://github.com/altryne/awesome-ai-art-image-synthesis) | awesome | AIアート | 1798 | 2022-12 | DALL·E2/MidJourney/SD等のツール・プロンプト集 |
| 🔴 | [yulunzhang/awesome-diffusion-low-level-vision](https://github.com/yulunzhang/awesome-diffusion-low-level-vision) | paper-list | 低レベルビジョン | 186 | 2023-09 | 低レベルビジョン拡散モデルのリスト |
| 🔴 | [cobanov/awesome-controlnet](https://github.com/cobanov/awesome-controlnet) | awesome | ControlNet | 97 | 2023-03 | ControlNet関連資源のリスト |
| 🔴 | [kobeshegu/awesome-few-shot-generation](https://github.com/kobeshegu/awesome-few-shot-generation) | paper-list | few-shot生成 | 87 | 2023-08 | 少数枚画像生成の論文リスト |
| 🔴 | [subeeshvasu/Awsome-GAN-Training](https://github.com/subeeshvasu/Awsome-GAN-Training) | awesome | GAN学習 | 30 | 2020-10 | GANの学習(training)に関する資源を集めたリスト |

### 🍌 特定モデルのプロンプト・作例コレクション  (20件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [PicoTrex/Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) | model | Nano Banana | 22885 | 2025-12 | Gemini系Nano Bananaの生成例・プロンプト集(データセット公開) |
| 🟢 | [YouMind-OpenLab/awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) | model | Nano Banana Pro | 12269 | 2026-05 | 世界最大級のNano Banana Proプロンプト集10,000+/16言語(毎日更新) |
| 🟢 | [ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) | model | Nano Banana | 10027 | 2026-05 | Nano Banana Pro(Nano Banana 2)のプロンプト・作例集 |
| 🟢 | [JimmyLv/awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) | model | Nano Banana | 8755 | 2025-09 | Gemini-2.5-Flash-Image(Nano Banana)の作例/プロンプト集 |
| 🟢 | [jamez-bondos/awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) | model | GPT-4o/gpt-image-1 | 8062 | 2025-05 | GPT-4o・gpt-image-1の画像・プロンプト作例集 |
| 🟢 | [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | model | Seedance 2.0 | 1244 | 2026-05 | Seedance 2.0動画生成プロンプト2000+(毎日更新) |
| 🟢 | [muset-ai/awesome-nano-banana-pro](https://github.com/muset-ai/awesome-nano-banana-pro) | model | Nano Banana Pro | 1056 | 2025-11 | Nano Banana Proの画像・プロンプト作例集 |
| 🟢 | [ImgEdify/Awesome-GPT4o-Image-Prompts](https://github.com/ImgEdify/Awesome-GPT4o-Image-Prompts) | model | GPT-4o画像 | 561 | 2025-05 | GPT-4o画像生成のプロンプト辞典 |
| 🟢 | [songguoxs/awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) | model | Veo3/Kling/Hailuo | 517 | 2025-10 | Veo3/Kling/Hailuo向け動画プロンプト集 |
| 🟢 | [langgptai/awesome-grok-prompts](https://github.com/langgptai/awesome-grok-prompts) | model | Grok | 506 | 2025-05 | Grok(xAI)向け高度プロンプト・テンプレート集 |
| 🟢 | [leeguandong/Awesome-Chinese-Stable-Diffusion](https://github.com/leeguandong/Awesome-Chinese-Stable-Diffusion) | model | 中文SD/Kolors/Hunyuan | 425 | 2026-05 | 中国系文生図SDモデル集(Kolors/HunyuanDiT等含む) |
| 🟢 | [XiaomingX/awesome-qwen-prompt-insight](https://github.com/XiaomingX/awesome-qwen-prompt-insight) | model | Qwen | 398 | 2026-02 | Qwen向け優良プロンプトの大規模コレクション |
| 🟢 | [githubssg/awesome-nano-banana-images](https://github.com/githubssg/awesome-nano-banana-images) | model | GPT-4o/Sora画像 | 306 | 2025-09 | GPT-4o/gpt-image-1の画像・プロンプト集 |
| 🟢 | [Curated-Awesome-Lists/Awesome-Open-AI-Sora](https://github.com/Curated-Awesome-Lists/Awesome-Open-AI-Sora) | model | Sora | 260 | 2026-05 | Sora関連記事/動画/ニュースのリソースハブ |
| 🟢 | [geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) | model | Veo/Sora/Kling/Runway | 55 | 2026-01 | 複数動画モデル横断のプロンプト/技法集 |
| 🟢 | [YouMind-OpenLab/awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts) | model | Grok Imagine | 13 | 2026-05 | Grok Imagine(xAI)動画生成プロンプト集 |
| 🟢 | [shauray8/awesome-qwen-image-2512](https://github.com/shauray8/awesome-qwen-image-2512) | model | Qwen-Image | 0 | 2025-12 | qwen-image-2512の作例/プロンプト集 |
| 🟡 | [ai-boost/Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) | model | GPT Store | 3389 | 2024-11 | GPT Store掲載のGPTを集めたキュレーション |
| 🟡 | [langgptai/awesome-llama-prompts](https://github.com/langgptai/awesome-llama-prompts) | model | Llama | 270 | 2024-08 | Llama2/Llama3向けプロンプト集 |
| 🟡 | [Eris2025/awesome-flux](https://github.com/Eris2025/awesome-flux) | model | FLUX | 105 | 2024-08 | FLUXエコシステム(LoRA/ControlNet/量子化)の資源集 |

### 🧰 モデルのエコシステム / 運用ツール(MCP・LLMOps・LLMアプリ)  (18件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | awesome | LLMアプリ/RAG/Agent | 112084 | 2026-05 | 実行可能なLLMアプリ/RAG/エージェントのコレクション |
| 🟢 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | awesome | MCP | 88117 | 2026-05 | 最大手のMCP(Model Context Protocol)サーバーコレクション |
| 🟢 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | awesome | Claude Skills | 62361 | 2026-05 | Claude Skill/ツールのキュレーション |
| 🟢 | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | awesome | Claude Code | 45114 | 2026-04 | Claude Code向けskill/hook/slash-command/プラグイン集 |
| 🟢 | [deepseek-ai/awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | model | DeepSeek | 37650 | 2026-02 | DeepSeek APIを各種ソフトに統合する公式キュレーション |
| 🟢 | [sindresorhus/awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) | awesome | ChatGPT | 6269 | 2026-02 | ChatGPT向けawesomeリスト(sindresorhus系列) |
| 🟢 | [tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) | awesome | LLMOps | 5809 | 2026-05 | LLM開発・運用向けツール(学習/サービング/監視)の厳選リスト |
| 🟢 | [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | awesome | MCP | 5567 | 2026-05 | MCPサーバーのキュレーション |
| 🟢 | [eon01/awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) | awesome | ChatGPT | 2370 | 2026-03 | ChatGPTのライブラリ/SDK/APIキュレーション |
| 🟢 | [webfuse-com/awesome-claude](https://github.com/webfuse-com/awesome-claude) | awesome | Claude | 1486 | 2026-05 | Anthropic Claude全般のキュレーションリスト |
| 🟢 | [Danielskry/Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) | awesome | RAGアプリ | 1207 | 2026-05 | 生成AIにおけるRAGアプリのawesomeリスト |
| 🟢 | [deepseek-ai/awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | model | DeepSeek Coder | 789 | 2025-11 | DeepSeek Coder関連のOSSプロジェクトをまとめた公式リスト |
| 🟢 | [ComfyUI-Workflow/awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) | awesome | ComfyUI | 695 | 2025-07 | ComfyUIカスタムノードの大規模コレクション |
| 🟢 | [Piebald-AI/awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) | awesome | Gemini CLI | 456 | 2026-05 | Gemini CLI向けツール/拡張/リソース集 |
| 🟢 | [AINativeLab/awesome-flux-ai](https://github.com/AINativeLab/awesome-flux-ai) | awesome | FLUX | 111 | 2025-05 | Flux AIのツール/ライブラリ/アプリ網羅 |
| 🟢 | [doanbactam/awesome-stable-diffusion](https://github.com/doanbactam/awesome-stable-diffusion) | awesome | Stable Diffusion | 75 | 2026-03 | Stable Diffusionリソースのキュレーション |
| 🟢 | [samouraiworld/awesome-mistral](https://github.com/samouraiworld/awesome-mistral) | awesome | Mistral AI | 42 | 2026-05 | Mistral AIエコシステムのリソース/ツール/プロジェクト集 |
| 🟡 | [formulahendry/awesome-gpt](https://github.com/formulahendry/awesome-gpt) | awesome | GPT/ChatGPT | 1045 | 2024-05 | GPT/ChatGPT/OpenAI関連プロジェクト・リソース集 |

### 🎮 強化学習(RL)  (33件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [LantaoYu/MARL-Papers](https://github.com/LantaoYu/MARL-Papers) | paper-list | MARL | 4838 | 2026-02 | マルチエージェントRLの研究・サーベイ論文リスト(定番) |
| 🟢 | [GT-RIPL/Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) | paper-list | RL for robotics/LLM | 4381 | 2026-04 | ロボティクス/RLへのLLM・マルチモーダル活用論文集 |
| 🟢 | [opendilab/awesome-RLHF](https://github.com/opendilab/awesome-RLHF) | paper-list | RLHF | 4371 | 2026-05 | 人間フィードバックによるRLの論文・資源を継続更新 |
| 🟢 | [TsinghuaC3I/Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) | survey | RL for LLM/推論 | 2459 | 2025-11 | 大規模推論モデル向けRLのサーベイ論文リポジトリ |
| 🟢 | [leofan90/Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) | paper-list | world models | 1714 | 2026-05 | ワールドモデル(動画生成・Embodied AI・自動運転)の論文網羅 |
| 🟢 | [opendilab/awesome-diffusion-model-in-rl](https://github.com/opendilab/awesome-diffusion-model-in-rl) | awesome | RL拡散モデル | 1604 | 2025-12 | 強化学習における拡散モデルの資源を継続更新するリスト |
| 🟢 | [opendilab/awesome-model-based-RL](https://github.com/opendilab/awesome-model-based-RL) | paper-list | model-based RL | 1353 | 2026-05 | モデルベースRLの論文を継続更新で収集 |
| 🟢 | [opendilab/awesome-decision-transformer](https://github.com/opendilab/awesome-decision-transformer) | awesome | Decision Transformer | 899 | 2026-05 | Decision Transformer資源の継続更新リスト |
| 🟢 | [kengz/awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) | awesome | deep RL | 892 | 2025-07 | Deep RLのライブラリ・環境・ベンチマークを整理したリスト |
| 🟢 | [chauncygu/Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) | paper-list | safe RL | 793 | 2026-03 | Safe RLのベースライン・論文を集めたリポジトリ |
| 🟢 | [tsinghua-fib-lab/World-Model](https://github.com/tsinghua-fib-lab/World-Model) | survey | 世界モデル(包括) | 724 | 2025-11 | 世界モデルの包括的サーベイ(ACM CSUR 2025採録) |
| 🟢 | [opendilab/awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl) | paper-list | exploration | 691 | 2026-05 | 探索(exploration)に特化したRL論文リスト |
| 🟢 | [opendilab/awesome-multi-modal-reinforcement-learning](https://github.com/opendilab/awesome-multi-modal-reinforcement-learning) | paper-list | multi-modal RL | 607 | 2025-12 | マルチモーダルRL資源を継続更新 |
| 🟢 | [yingchengyang/Reinforcement-Learning-Papers](https://github.com/yingchengyang/Reinforcement-Learning-Papers) | paper-list | 総合(トップ会議) | 570 | 2026-02 | ICLR/ICML/NeurIPSの古典+最新論文を年別に整理 |
| 🟢 | [weijiawu/Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) | paper-list | visual/multimodal RL | 445 | 2026-04 | 視覚RL・マルチモーダル基盤モデル向けRLの論文整理 |
| 🟢 | [Allenpandas/Reinforcement-Learning-Papers](https://github.com/Allenpandas/Reinforcement-Learning-Papers) | paper-list | 総合(トップ会議) | 366 | 2025-11 | NeurIPS/ICML/ICLR/AAAI/IJCAI/AAMAS/ICRAの論文を網羅 |
| 🟢 | [dunnolab/awesome-in-context-rl](https://github.com/dunnolab/awesome-in-context-rl) | paper-list | in-context RL/meta RL | 301 | 2025-09 | In-Context RLの論文キュレーション |
| 🟢 | [libo-huang/Awesome-Causal-Reinforcement-Learning](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) | survey | causal RL | 220 | 2026-04 | 因果RLのサーベイ(TNNLS 2024)公式リポジトリ |
| 🟢 | [jgvictores/awesome-deep-reinforcement-learning](https://github.com/jgvictores/awesome-deep-reinforcement-learning) | awesome | deep RL | 206 | 2026-03 | フレームワーク・モデル・データセット・gym・ベースラインを収録 |
| 🟢 | [opendilab/awesome-RLVR](https://github.com/opendilab/awesome-RLVR) | paper-list | RLVR | 164 | 2026-05 | 検証可能報酬によるRL(RLVR)の論文を継続更新 |
| 🟢 | [operator22th/awesome-world-models-for-robots](https://github.com/operator22th/awesome-world-models-for-robots) | paper-list | world models/robotics | 135 | 2026-03 | ロボティクス向けワールドモデル論文集 |
| 🟢 | [tsinghua-fib-lab/Awesome-Embodied-World-Model](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) | survey | 身体性世界モデル | 112 | 2026-05 | 身体性エージェント向け世界モデルに特化した論文集 |
| 🟡 | [tigerneil/awesome-deep-rl](https://github.com/tigerneil/awesome-deep-rl) | awesome | deep RL | 1507 | 2024-03 | Deep RLとAIの将来に向けた資源を幅広く収集したリスト |
| 🟡 | [clvrai/awesome-rl-envs](https://github.com/clvrai/awesome-rl-envs) | awesome | benchmarks/environments | 1340 | 2024-05 | RL用環境・シミュレータを網羅したリスト |
| 🟡 | [hanjuku-kaso/awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl) | paper-list | offline RL | 1064 | 2024-05 | オフラインRLのアルゴリズム索引(継続更新) |
| 🟡 | [datamllab/awesome-game-ai](https://github.com/datamllab/awesome-game-ai) | awesome | game AI/MARL | 963 | 2024-06 | マルチエージェント学習中心のゲームAI資源集 |
| 🟡 | [kristery/Awesome-Imitation-Learning](https://github.com/kristery/Awesome-Imitation-Learning) | paper-list | imitation learning | 608 | 2024-02 | 模倣学習の論文・資源を集めたリスト |
| 📚 | [junhyukoh/deep-reinforcement-learning-papers](https://github.com/junhyukoh/deep-reinforcement-learning-papers) | paper-list | deep RL | 2197 | 2016-06 | Deep RLの主要論文をトピック別にまとめた古典的リスト |
| 🔴 | [aikorea/awesome-rl](https://github.com/aikorea/awesome-rl) | awesome | 総合 | 9773 | 2023-05 | RL全般のコード・講義・論文・環境を集めた定番キュレーション |
| 🔴 | [TimeBreaker/MARL-papers-with-code](https://github.com/TimeBreaker/MARL-papers-with-code) | paper-list | MARL | 429 | 2022-09 | コード付きMARL論文を手法別に整理 |
| 🔴 | [apexrl/Imitation-Learning-Paper-Lists](https://github.com/apexrl/Imitation-Learning-Paper-Lists) | paper-list | imitation learning | 157 | 2022-03 | 模倣学習の論文を簡潔な紹介付きで収集 |
| 🔴 | [dit7ya/awesome-irl](https://github.com/dit7ya/awesome-irl) | awesome | inverse RL | 44 | 2022-02 | 逆強化学習の論文・コード・動画・チュートリアル集 |
| 🔴 | [metarl/awesome-metarl](https://github.com/metarl/awesome-metarl) | paper-list | meta RL | 33 | 2020-05 | メタ強化学習のキュレーションリスト |

### 🔀 マルチモーダル / VLM / MLLM  (30件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [BradyFU/Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) | survey | MLLM | 17840 | 2026-05 | MLLM分野の最有名サーベイ。アーキテクチャ・学習・評価を網羅追跡 |
| 🟢 | [yunlong10/Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) | paper-list | 動画理解LLM | 3188 | 2026-03 | 動画理解向けVid-LLMの最新論文・コード・データセット |
| 🟢 | [jingyi0000/VLM_survey](https://github.com/jingyi0000/VLM_survey) | survey | VLM | 3123 | 2025-10 | 視覚タスク向けVision-Languageモデルの系統的レビュー |
| 🟢 | [ActiveVisionLab/Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) | awesome | 3D-LLM | 2210 | 2026-04 | 3D世界における多モーダルLLM資源の網羅リスト |
| 🟢 | [AIDC-AI/Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) | survey | 統合マルチモーダル | 1268 | 2026-03 | 理解と生成を統合する多モーダルモデルの網羅集(活発) |
| 🟢 | [gokayfem/awesome-vlm-architectures](https://github.com/gokayfem/awesome-vlm-architectures) | paper-list | VLM | 1259 | 2026-01 | 著名なVLMとそのアーキテクチャを解説したコレクション |
| 🟢 | [showlab/Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) | awesome | MLLM幻覚 | 1022 | 2025-09 | マルチモーダルLLMの幻覚(hallucination)に関する資源の厳選リスト |
| 🟢 | [zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) | paper-list | VLM(prompt/adapter) | 778 | 2026-05 | CLIP等のVLM向けプロンプト/アダプタ学習手法の厳選リスト |
| 🟢 | [mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM](https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM) | paper-list | 空間知能(VLM) | 747 | 2026-01 | VLMの空間推論に関する論文・ベンチマーク約200本(非常に活発) |
| 🟢 | [Paranioar/Awesome_Matching_Pretraining_Transfering](https://github.com/Paranioar/Awesome_Matching_Pretraining_Transfering) | paper-list | 画像テキストマッチング | 445 | 2025-09 | 画像テキストマッチング・VL事前学習・マルチモーダルモデルの大規模論文リスト |
| 🟢 | [friedrichor/Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) | awesome | マルチモーダル全般 | 335 | 2026-05 | マルチモーダル研究全般の厳選論文集 |
| 🟢 | [khuangaf/Awesome-Chart-Understanding](https://github.com/khuangaf/Awesome-Chart-Understanding) | survey | チャート理解 | 240 | 2025-12 | IEEE TKDEサーベイ準拠のチャート理解(QA/captioning/fact-checking)論文集 |
| 🟢 | [harrytea/Awesome-Document-Understanding](https://github.com/harrytea/Awesome-Document-Understanding) | paper-list | マルチモーダル文書理解 | 201 | 2025-09 | MLLM/OCR-free等のマルチモーダル文書AI論文・コード・データセット集 |
| 🟢 | [swordlidev/Evaluation-Multimodal-LLMs-Survey](https://github.com/swordlidev/Evaluation-Multimodal-LLMs-Survey) | survey | MLLM評価 | 149 | 2026-05 | MLLMのベンチマーク200件以上をレビューした評価サーベイ |
| 🟢 | [InfiMM/Awesome-Multimodal-LLM-for-Math-STEM](https://github.com/InfiMM/Awesome-Multimodal-LLM-for-Math-STEM) | awesome | マルチモーダル数学推論 | 143 | 2026-05 | Math/STEM/Code向けマルチモーダルLLMの論文集 |
| 🟢 | [WenkeHuang/Awesome-MLLM-Tuning](https://github.com/WenkeHuang/Awesome-MLLM-Tuning) | paper-list | MLLMチューニング | 98 | 2025-08 | MLLMの下流タスク向けチューニング手法サーベイ |
| 🟢 | [kkzhang95/Awesome-Composed-Multi-modal-Retrieval](https://github.com/kkzhang95/Awesome-Composed-Multi-modal-Retrieval) | survey | 合成マルチモーダル検索 | 89 | 2026-01 | 合成画像検索(CIR)・合成動画検索(CVR)を含むCMRサーベイ |
| 🟢 | [JarvisUSTC/Awesome-Multimodal-RAG](https://github.com/JarvisUSTC/Awesome-Multimodal-RAG) | paper-list | マルチモーダルRAG | 53 | 2025-11 | テキスト/画像/動画/音声を跨ぐマルチモーダルRAGの論文・ツール集 |
| 🟢 | [SuperBruceJia/Awesome-Large-Vision-Language-Model](https://github.com/SuperBruceJia/Awesome-Large-Vision-Language-Model) | awesome | VLM | 47 | 2025-07 | 大規模VLMと医療基盤モデルの論文・リソース集 |
| 📑 | [swordlidev/Efficient-Multimodal-LLMs-Survey](https://github.com/swordlidev/Efficient-Multimodal-LLMs-Survey) | survey | 効率的MLLM | 385 | 2025-04 | 効率的MLLM(軽量構造・戦略)の体系的レビュー |
| 🟡 | [krantiparida/awesome-audio-visual](https://github.com/krantiparida/awesome-audio-visual) | awesome | audio-visual | 771 | 2024-01 | 音声・視覚処理の各領域の論文・データセット集 |
| 🟡 | [cv-small-snails/Awesome-Table-Recognition](https://github.com/cv-small-snails/Awesome-Table-Recognition) | awesome | 表認識 | 404 | 2024-12 | 表認識の論文・データセット・コンペ解法を整理 |
| 🟡 | [declare-lab/awesome-emotion-recognition-in-conversations](https://github.com/declare-lab/awesome-emotion-recognition-in-conversations) | paper-list | 会話感情認識 | 278 | 2024-02 | 会話における感情認識(ERC)の網羅的リーディングリスト |
| 🟡 | [Tan-Junwen/awesome-table-structure-recognition](https://github.com/Tan-Junwen/awesome-table-structure-recognition) | awesome | 表構造認識 | 228 | 2024-09 | 表構造認識(TSR)のモデル・論文・データセット・コード集 |
| 🟡 | [Event-AHU/Prompt_Learning_Paper_List](https://github.com/Event-AHU/Prompt_Learning_Paper_List) | paper-list | プロンプト学習 | 19 | 2024-11 | (視覚言語)プロンプト学習の論文リスト |
| 🔴 | [tstanislawek/awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) | awesome | 文書理解 | 1518 | 2023-06 | KIE・レイアウト解析・DocQA・OCR等を網羅した定番リスト |
| 🔴 | [danieljf24/awesome-video-text-retrieval](https://github.com/danieljf24/awesome-video-text-retrieval) | awesome | 動画テキスト検索 | 645 | 2023-10 | 動画テキスト検索の深層学習リソース集 |
| 🔴 | [AmrMKayid/awesome-affective-computing](https://github.com/AmrMKayid/awesome-affective-computing) | awesome | 感情コンピューティング | 192 | 2019-11 | 感情コンピューティングの論文・ソフト・OSS・リソース集 |
| 🔴 | [EvelynFan/AWESOME-MER](https://github.com/EvelynFan/AWESOME-MER) | paper-list | マルチモーダル感情認識 | 127 | 2020-10 | マルチモーダル感情認識(MER)のリーディングリスト |
| 🔴 | [Lab-LVM/awesome-VLM](https://github.com/Lab-LVM/awesome-VLM) | paper-list | VLM | 7 | 2023-06 | 対照学習・PrefixLM・融合など手法別に整理したVLM論文集 |

### 🔊 音声 / オーディオ  (28件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [wq2012/awesome-diarization](https://github.com/wq2012/awesome-diarization) | awesome | 話者ダイアライゼーション | 1872 | 2025-07 | 話者ダイアライゼーションの論文・ライブラリ・データセット・評価ツールを網羅した定番リスト |
| 🟢 | [ga642381/speech-trident](https://github.com/ga642381/speech-trident) | paper-list | 音声LLM | 1231 | 2026-04 | 音声/オーディオLLM・表現学習・codecモデルの論文集 |
| 🟢 | [BinWang28/audio-ai-hub](https://github.com/BinWang28/audio-ai-hub) | awesome | 音声LLM | 921 | 2026-05 | オーディオ大規模言語モデルの論文・リソース集 |
| 🟢 | [EmulationAI/awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) | awesome | 音声LLM | 729 | 2026-05 | LLMのAudio AI応用に関するリソース集 |
| 🟢 | [DmitryRyumin/ICASSP-2023-24-Papers](https://github.com/DmitryRyumin/ICASSP-2023-24-Papers) | paper-list | 会議論文(ICASSP) | 527 | 2025-05 | ICASSP 2023-2024の論文を網羅したコレクション |
| 🟢 | [DongKeon/Awesome-Speaker-Diarization](https://github.com/DongKeon/Awesome-Speaker-Diarization) | paper-list | 話者ダイアライゼーション | 358 | 2026-03 | End-to-End/クラスタリング/マルチモーダル等を体系化した論文集(活発) |
| 🟢 | [wildminder/awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) | model | 音声生成 | 334 | 2026-04 | OSSのTTS・音声クローン・音楽生成モデル集 |
| 🟢 | [JeffC0628/awesome-voice-conversion](https://github.com/JeffC0628/awesome-voice-conversion) | awesome | voice conversion | 267 | 2025-11 | voice conversion(声質変換)のプロジェクト・コミュニティ集 |
| 🟢 | [VIPL-SLP/Awesome-Sign-Language-Processing](https://github.com/VIPL-SLP/Awesome-Sign-Language-Processing) | awesome | 手話処理 | 248 | 2026-05 | 手話処理(認識/翻訳/生成)の包括リソース集 |
| 🟢 | [ZechengLi19/Awesome-Sign-Language](https://github.com/ZechengLi19/Awesome-Sign-Language) | paper-list | 手話 | 220 | 2025-11 | 手話認識(SLR)・翻訳(SLT)等の論文リスト(活発) |
| 🟢 | [01Zhangbw/Speech-and-audio-papers-Top-Conference](https://github.com/01Zhangbw/Speech-and-audio-papers-Top-Conference) | paper-list | 会議論文(音声・音響) | 139 | 2026-01 | トップ会議(INTERSPEECH/ICASSP等)の音声・音響論文を集約 |
| 🟢 | [tleyden/awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech) | awesome | speech-to-speech | 56 | 2025-11 | LLMベースのspeech-to-speechモデル/フレームワーク集 |
| 🟢 | [huangcanan/Awesome-Large-Speech-Model](https://github.com/huangcanan/Awesome-Large-Speech-Model) | awesome | 大規模音声モデル | 28 | 2025-11 | 大規模音声/オーディオモデルの論文・データ・応用・ツール集 |
| 🟡 | [ybayle/awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) | paper-list | 音楽深層学習 | 2959 | 2023-12 | 音楽に応用された深層学習の論文・学位論文集 |
| 🟡 | [WenzheLiu-Speech/awesome-speech-enhancement](https://github.com/WenzheLiu-Speech/awesome-speech-enhancement) | paper-list | 音声強調 | 1240 | 2023-11 | speech enhancement・音源分離・定位の論文/コード/ツール集 |
| 🟡 | [DmitryRyumin/INTERSPEECH-2023-24-Papers](https://github.com/DmitryRyumin/INTERSPEECH-2023-24-Papers) | paper-list | 会議論文(INTERSPEECH) | 689 | 2024-12 | INTERSPEECH 2023-2024の論文を網羅したコレクション |
| 🟡 | [soham97/awesome-sound_event_detection](https://github.com/soham97/awesome-sound_event_detection) | paper-list | 音響イベント検出 | 197 | 2024-08 | Sound AI(音響イベント検出、音声キャプショニング等)の研究リーディングリスト |
| 🟡 | [abikaki/awesome-speech-emotion-recognition](https://github.com/abikaki/awesome-speech-emotion-recognition) | awesome | 音声感情認識 | 101 | 2024-12 | 音声感情認識(SER)の論文・データセット・ツールの厳選リスト |
| 🟡 | [bigcash/awesome-vad](https://github.com/bigcash/awesome-vad) | awesome | 音声区間検出(VAD) | 74 | 2024-11 | VADの実装・ツール・研究を集めたリスト |
| 🟡 | [DmitryRyumin/Awesome-Speech-Enhancement](https://github.com/DmitryRyumin/Awesome-Speech-Enhancement) | paper-list | 音声強調 | 27 | 2024-04 | 音声強調の論文・効果指標を整理したインタラクティブなリスト |
| 📦 | [seungwonpark/awesome-tts-samples](https://github.com/seungwonpark/awesome-tts-samples) | paper-list | TTS | 61 | 2020-08 | 音声サンプル付きTTS論文リスト |
| 🔴 | [zzw922cn/awesome-speech-recognition-speech-synthesis-papers](https://github.com/zzw922cn/awesome-speech-recognition-speech-synthesis-papers) | paper-list | 音声全般 | 3129 | 2023-10 | ASR・話者認証・TTS・音声合成・VCを網羅した論文リスト |
| 🔴 | [wenet-e2e/speech-synthesis-paper](https://github.com/wenet-e2e/speech-synthesis-paper) | paper-list | TTS | 1072 | 2023-07 | 音声合成(TTS)論文の体系的リスト |
| 🔴 | [guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion](https://github.com/guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion) | paper-list | 歌声合成/変換 | 482 | 2022-09 | 歌声合成(SVS)・歌声変換(SVC)・自動採譜の論文/プロジェクト集 |
| 🔴 | [zycv/awesome-keyword-spotting](https://github.com/zycv/awesome-keyword-spotting) | awesome | キーワードスポッティング | 287 | 2022-05 | 音声キーワード検出/ウェイクワード検出の論文・実装・データセット集 |
| 🔴 | [yamathcy/awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) | awesome | 音楽情報学 | 192 | 2023-07 | 音楽情報学の論文・チュートリアル・ライブラリ・ツールの厳選リスト |
| 🔴 | [dqqcasia/awesome-speech-translation](https://github.com/dqqcasia/awesome-speech-translation) | paper-list | 音声翻訳 | 179 | 2021-11 | 音声翻訳(パイプライン/E2E/ストリーミング/多言語)の論文リスト |
| 🔴 | [Rongjiehuang/awesome-speech-to-speech-translation](https://github.com/Rongjiehuang/awesome-speech-to-speech-translation) | paper-list | 音声間翻訳 | 39 | 2023-01 | 直接音声間翻訳(S2ST)の論文リスト |

### 🤖 ロボティクス / Embodied AI  (17件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [jonyzhang2023/awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) | paper-list | VLA/VLN | 3185 | 2026-05 | embodied AIのVLA・VLN・マルチモーダル学習の最先端研究集 |
| 🟢 | [YanjieZe/awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) | paper-list | ヒューマノイド | 2369 | 2026-05 | ヒューマノイドロボット学習の論文リスト |
| 🟢 | [HCPLab-SYSU/Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) | survey | 身体性AI | 2067 | 2026-05 | 身体性AIの知覚・相互作用・エージェント・sim-to-realを網羅(IEEE/ASME ToM 2025) |
| 🟢 | [zchoi/Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) | awesome | embodied AI | 1803 | 2026-05 | LLMを用いたembodied AI/ロボット研究のキュレーション |
| 🟢 | [curieuxjy/Awesome_Quadrupedal_Robots](https://github.com/curieuxjy/Awesome_Quadrupedal_Robots) | paper-list | 四足歩行 | 1100 | 2026-05 | 四足歩行ロボットの論文・リソース集 |
| 🟢 | [BaiShuanghao/Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) | paper-list | manipulation | 988 | 2026-05 | ロボットマニピュレーションの論文・コード集 |
| 🟢 | [Songwxuan/Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) | paper-list | 会議論文(Embodied AI) | 654 | 2026-05 | トップ会議採択のEmbodied AI論文を継続収集(2026会議まで反映、活発) |
| 🟢 | [DravenALG/awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam) | awesome | VLA/WAM | 626 | 2026-05 | VLAとWorld Action Model(WAM)研究のキュレーション |
| 🟢 | [yueen-ma/Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) | survey | VLA | 576 | 2026-02 | embodied AI向けVLAモデルのサーベイ論文付きリスト |
| 🟢 | [Jiaaqiliu/Awesome-VLA-Robotics](https://github.com/Jiaaqiliu/Awesome-VLA-Robotics) | paper-list | VLA | 477 | 2026-03 | ロボティクスのVLAモデル論文・モデル・データセット集 |
| 🟢 | [showlab/Awesome-Robotics-Diffusion](https://github.com/showlab/Awesome-Robotics-Diffusion) | paper-list | ロボティクス拡散 | 335 | 2026-05 | ロボット学習に拡散モデルを取り入れた最新論文の厳選リスト |
| 🟢 | [wadeKeith/Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI) | awesome | embodied AI | 210 | 2026-04 | embodied AIのサーベイ・VLA・データセット・シミュレータ等を網羅 |
| 🟢 | [KwanWaiPang/Awesome-VLN](https://github.com/KwanWaiPang/Awesome-VLN) | survey | 視覚言語ナビゲーション | 136 | 2026-05 | 視覚言語ナビゲーション(VLN)のサーベイ用論文集 |
| 🟢 | [KwanWaiPang/Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) | survey | VLA | 79 | 2026-02 | Vision-Language-Action(VLA)のサーベイ用論文集 |
| 🟢 | [KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping](https://github.com/KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping) | survey | 脚式ロボットSLAM | 63 | 2026-04 | 脚式ロボットのSLAMに関するサーベイ用論文集 |
| 🟡 | [RayYoh/Awesome-Robot-Learning](https://github.com/RayYoh/Awesome-Robot-Learning) | awesome | robot learning | 202 | 2024-08 | ロボット学習(主にマニピュレーション)のリソース集 |
| 🔴 | [gaiyi7788/awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning) | awesome | 脚式ロコモーション | 477 | 2023-07 | 脚式ロコモーション学習のリソース集 |

### 🕸️ グラフ学習(GNN) / 知識グラフ  (35件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [safe-graph/graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) | paper-list | グラフ不正検知 | 1839 | 2026-05 | グラフ/Transformerベースの不正・異常・外れ値検知論文集 |
| 🟢 | [LIANGKE23/Awesome-Knowledge-Graph-Reasoning](https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning) | paper-list | KG推論 | 1452 | 2025-11 | 知識グラフ推論の論文・コード・データセット集 |
| 🟢 | [yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) | survey | 時空間拡散モデル | 986 | 2026-02 | 時系列・時空間データ向け拡散モデルのサーベイ＆論文集(活発) |
| 🟢 | [SpaceLearner/Awesome-DynamicGraphLearning](https://github.com/SpaceLearner/Awesome-DynamicGraphLearning) | paper-list | 動的グラフ | 709 | 2025-06 | 動的(時系列)グラフ・知識グラフ上の機械学習論文集 |
| 🟢 | [amorehead/awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation) | paper-list | 分子生成 | 343 | 2025-07 | 生成的な分子モデリング・設計の論文集 |
| 🟢 | [ch-wan/awesome-gnn-systems](https://github.com/ch-wan/awesome-gnn-systems) | awesome | GNNシステム | 342 | 2026-05 | GNNシステム・高速化に関するリソース集 |
| 🟢 | [mala-lab/Awesome-Deep-Graph-Anomaly-Detection](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection) | survey | グラフ異常検知 | 212 | 2026-05 | 2025年TKDEサーベイ公式リポジトリ。GNNベースのグラフ異常検知論文・データセット |
| 🟢 | [jiapuwang/Awesome-TKGC](https://github.com/jiapuwang/Awesome-TKGC) | paper-list | 時系列KG補完 | 115 | 2025-10 | 時系列知識グラフ補完(TKGC)の論文・資源を5段階分類で網羅 |
| 🟢 | [AzureLeon1/awesome-molecular-diffusion-models](https://github.com/AzureLeon1/awesome-molecular-diffusion-models) | paper-list | 分子拡散モデル | 100 | 2026-04 | 分子拡散モデル関連論文の厳選リスト(活発) |
| 🟢 | [MGitHubL/Awesome-Temporal-Graph-Learning](https://github.com/MGitHubL/Awesome-Temporal-Graph-Learning) | paper-list | temporal graph | 92 | 2025-05 | temporal graph learning手法(論文・コード・データセット)集 |
| 📑 | [LirongWu/awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) | survey | グラフ自己教師あり | 1435 | 2024-08 | TKDE論文(対照/生成/予測型)の付随リスト |
| 📑 | [KimMeen/Awesome-GNN4TS](https://github.com/KimMeen/Awesome-GNN4TS) | survey | 時系列GNN | 858 | 2024-08 | 時系列解析向けGNN(TPAMI 2024)のリソース集 |
| 📑 | [junxia97/awesome-pretrain-on-molecules](https://github.com/junxia97/awesome-pretrain-on-molecules) | survey | 分子事前学習 | 539 | 2023-06 | 化学事前学習モデル(IJCAI 2023 survey)の論文リスト |
| 📑 | [zjunlp/Generative_KG_Construction_Papers](https://github.com/zjunlp/Generative_KG_Construction_Papers) | survey | 生成的KG構築 | 113 | 2023-07 | 生成的知識グラフ構築のレビュー(EMNLP 2022)の論文集 |
| 📑 | [Radical3-HeZhang/Awesome-Trustworthy-GNNs](https://github.com/Radical3-HeZhang/Awesome-Trustworthy-GNNs) | survey | 信頼できるGNN | 98 | 2024-07 | 信頼できるGNN(プライバシ/頑健性/公平性/説明性)サーベイ(Proc. IEEE 2024) |
| 🟡 | [thunlp/GNNPapers](https://github.com/thunlp/GNNPapers) | paper-list | GNN必読論文 | 16786 | 2023-12 | グラフニューラルネットワーク(GNN)の必読論文集(定番) |
| 🟡 | [TrustAGI-Lab/Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) | paper-list | GNN | 2302 | 2023-12 | グラフニューラルネットワークの論文リスト |
| 🟡 | [ChandlerBang/awesome-self-supervised-gnn](https://github.com/ChandlerBang/awesome-self-supervised-gnn) | paper-list | 自己教師ありGNN | 1725 | 2024-02 | GNNの事前学習・自己教師あり学習の論文集 |
| 🟡 | [jwwthu/GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) | paper-list | 交通予測GNN | 1206 | 2024-08 | 交通予測向けGNN論文・コードの大規模コレクション |
| 🟡 | [wehos/awesome-graph-transformer](https://github.com/wehos/awesome-graph-transformer) | paper-list | graph transformer | 929 | 2025-03 | グラフトランスフォーマーの論文集 |
| 🟡 | [zjunlp/PromptKG](https://github.com/zjunlp/PromptKG) | paper-list | プロンプト×KG | 734 | 2024-03 | プロンプト学習・知識グラフ関連の研究・ツール・論文ギャラリー |
| 🟡 | [yuanqidu/awesome-graph-generation](https://github.com/yuanqidu/awesome-graph-generation) | paper-list | グラフ生成 | 360 | 2025-01 | グラフ・分子生成の論文を網羅した最新リスト |
| 🟡 | [gzcsudo/Awesome-Hypergraph-Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network) | awesome | ハイパーグラフ | 331 | 2025-02 | ハイパーグラフ学習・理論・データ・ツールの厳選集 |
| 🟡 | [benb111/awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) | awesome | 低分子創薬ML | 241 | 2023-11 | 低分子創薬向け機械学習リソースの厳選集 |
| 🟡 | [EdisonLeeeee/Awesome-Fair-Graph-Learning](https://github.com/EdisonLeeeee/Awesome-Fair-Graph-Learning) | paper-list | 公平なグラフ学習 | 144 | 2024-09 | 公平なグラフ学習(FairGL)の論文リスト |
| 🟡 | [mengliu1998/awesome-expressive-gnn](https://github.com/mengliu1998/awesome-expressive-gnn) | paper-list | GNN表現力 | 124 | 2023-11 | GNNの表現力に関する研究・改善論文集 |
| 🟡 | [kaize0409/Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) | paper-list | グラフOOD | 85 | 2024-10 | グラフOOD(汎化・訓練時/テスト時適応)の論文リスト |
| 🟡 | [gozsari/Awesome-GNN-based-drug-discovery](https://github.com/gozsari/Awesome-GNN-based-drug-discovery) | awesome | 創薬GNN | 63 | 2024-04 | GNNによる創薬(論文・データセット・ツール)の厳選リスト |
| 🟡 | [PolarisRisingWar/HGNN_Collection](https://github.com/PolarisRisingWar/HGNN_Collection) | paper-list | 異種グラフNN | 61 | 2024-05 | 異種グラフNNのデータセット・アルゴリズム集 |
| 🟡 | [claws-lab/awesome-GNN-social-recsys](https://github.com/claws-lab/awesome-GNN-social-recsys) | paper-list | GNN推薦 | 53 | 2024-05 | GNNベースのソーシャル推薦論文集 |
| 🔴 | [benedekrozemberczki/awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification) | paper-list | グラフ分類/埋め込み | 4802 | 2023-03 | グラフ埋め込み・分類・表現学習の重要論文集(実装付) |
| 🔴 | [chihming/awesome-network-embedding](https://github.com/chihming/awesome-network-embedding) | awesome | ネットワーク埋め込み | 2626 | 2020-12 | ネットワーク埋め込み手法の定番厳選リスト |
| 🔴 | [shaoxiongji/knowledge-graphs](https://github.com/shaoxiongji/knowledge-graphs) | paper-list | knowledge graph | 1791 | 2022-10 | 知識グラフ研究(埋め込み・補完・時系列KG・応用)の論文集 |
| 🔴 | [XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection](https://github.com/XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection) | awesome | グラフ異常検知 | 384 | 2023-07 | 深層学習によるグラフ異常検知の論文・データセット・実装集 |
| 🔴 | [THUMNLab/awesome-graph-ood](https://github.com/THUMNLab/awesome-graph-ood) | paper-list | グラフOOD | 169 | 2023-06 | グラフのOOD汎化に関する論文集 |

### 🛒 推薦システム(RecSys)  (9件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [hongleizhang/RSPapers](https://github.com/hongleizhang/RSPapers) | awesome | 推薦必読論文 | 6495 | 2026-03 | 推薦システム必読論文を17カテゴリで整理、毎週更新(LLM/Agentic RS等も追加) |
| 🟢 | [guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) | paper-list | 検索・推薦・広告 | 2507 | 2026-04 | 検索・推薦・広告向け深層学習論文集 |
| 🟢 | [CHIANGEL/Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys) | survey | LLM推薦 | 1537 | 2026-01 | LLM関連の推薦システム論文集(TOIS採録サーベイ付き) |
| 🟢 | [nancheng58/Awesome-LLM4RS-Papers](https://github.com/nancheng58/Awesome-LLM4RS-Papers) | paper-list | LLM推薦 | 762 | 2026-03 | LLM強化推薦システムの論文集 |
| 🟢 | [YuanchenBei/Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) | survey | コールドスタート | 283 | 2026-03 | コールドスタート推薦のリソース集(LLM時代のサーベイ付き) |
| 📑 | [WLiK/LLM4Rec-Awesome-Papers](https://github.com/WLiK/LLM4Rec-Awesome-Papers) | survey | LLM推薦 | 2285 | 2025-03 | LLMを用いた推薦システムの論文・リソース集(サーベイ付き) |
| 🟡 | [AiHubCN/Awesome-Sequence-Modeling-for-Recommendation](https://github.com/AiHubCN/Awesome-Sequence-Modeling-for-Recommendation) | paper-list | 系列推薦 | 39 | 2023-11 | 系列推薦・系列モデリングの論文集 |
| 🔴 | [RUCAIBox/Awesome-RSPapers](https://github.com/RUCAIBox/Awesome-RSPapers) | paper-list | 推薦全般 | 989 | 2022-10 | 推薦システム論文の網羅的リスト |
| 🔴 | [RUCAIBox/CRSPapers](https://github.com/RUCAIBox/CRSPapers) | paper-list | 対話型推薦 | 80 | 2022-11 | 対話型推薦システム(CRS)の論文リスト |

### 📈 時系列(Time Series)  (11件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [TSCenter/awesome-time-series-papers](https://github.com/TSCenter/awesome-time-series-papers) | paper-list | 時系列全般 | 994 | 2026-04 | トップAI会議の最新時系列論文・コード集 |
| 🟢 | [WenjieDu/Awesome_Imputation](https://github.com/WenjieDu/Awesome_Imputation) | survey | 時系列補完 | 420 | 2026-03 | 時系列の欠損値補完(imputation)の論文・手法を集めたサーベイリポジトリ |
| 🟢 | [TongjiFinLab/awesome-time-series-forecasting](https://github.com/TongjiFinLab/awesome-time-series-forecasting) | paper-list | 時系列予測 | 262 | 2026-04 | 時系列予測の論文・コード集 |
| 🟢 | [mala-lab/Awesome-Anomaly-Detection-Foundation-Models](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) | paper-list | 異常検知 | 194 | 2026-05 | 基盤モデルによる異常検知の論文集 |
| 🟢 | [lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms](https://github.com/lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms) | paper-list | 異常検知 | 76 | 2025-09 | 多変量時系列異常検知の論文リスト |
| 🟢 | [qhliu26/awesome-time-series-analysis](https://github.com/qhliu26/awesome-time-series-analysis) | awesome | 時系列全般 | 65 | 2025-09 | 時系列の論文・ベンチマーク・データセット・チュートリアル集 |
| 📑 | [qingsongedu/time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) | survey | 時系列Transformer | 2984 | 2024-08 | 時系列向けTransformerのリソース(論文・コード・データ)を専門的にまとめたレビュー |
| 🟡 | [qingsongedu/awesome-AI-for-time-series-papers](https://github.com/qingsongedu/awesome-AI-for-time-series-papers) | paper-list | 時系列全般 | 1614 | 2024-04 | トップ会議・ジャーナルの時系列AI論文・チュートリアル・サーベイ集 |
| 🟡 | [qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) | paper-list | 時系列LLM | 1218 | 2024-12 | 時系列・時空間・イベントデータ向けLLM/基盤モデルの論文集 |
| 🟡 | [start2020/Awesome-TimeSeries-LLM-FM](https://github.com/start2020/Awesome-TimeSeries-LLM-FM) | paper-list | 時系列LLM | 154 | 2024-06 | 時系列タスク向けLLM・基盤モデルのリソース集 |
| 🟡 | [SJTU-DMTai/Awesome-Large-Models-for-Time-Series](https://github.com/SJTU-DMTai/Awesome-Large-Models-for-Time-Series) | paper-list | 時系列LLM | 47 | 2024-10 | 時系列解析向けLLM・基盤モデルの論文集 |

### 🦾 AIエージェント / LLM Agents  (19件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) | survey | LLMエージェント | 8134 | 2025-09 | 86ページのサーベイ「The Rise and Potential of LLM Based Agents」の論文リスト |
| 🟢 | [zjunlp/LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) | paper-list | LLMエージェント | 3019 | 2026-04 | LLMエージェントの必読論文集 |
| 🟢 | [luo-junyu/Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) | survey | LLMエージェント | 2720 | 2025-11 | LLMエージェントの手法・応用・課題サーベイの論文集 |
| 🟢 | [AGI-Edgerunners/LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) | paper-list | LLMエージェント | 2302 | 2025-07 | LLMベースエージェント関連論文のリスト |
| 🟢 | [kyegomez/awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) | awesome | マルチエージェント | 1504 | 2026-05 | マルチエージェント論文のキュレーション集(Swarms team) |
| 🟢 | [kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) | awesome | LLMエージェント | 1497 | 2026-05 | LLMエージェントフレームワークの厳選リスト |
| 🟢 | [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) | paper-list | GUIエージェント | 1192 | 2025-08 | マルチモーダルGUIエージェントの論文・リソース集 |
| 🟢 | [Jenqyang/Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) | awesome | AIエージェント | 1138 | 2026-05 | LLM駆動の自律エージェントコレクション |
| 🟢 | [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) | paper-list | AIエージェント | 897 | 2026-05 | AIエージェント研究論文集(工学・メモリ・評価・ワークフロー) |
| 🟢 | [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | paper-list | GUIエージェント | 803 | 2026-05 | GUIエージェント論文の厳選リスト |
| 🟢 | [ranpox/awesome-computer-use](https://github.com/ranpox/awesome-computer-use) | awesome | computer use | 557 | 2026-04 | Computer-use GUIエージェントの動画・ブログ・論文・プロジェクト集 |
| 🟢 | [TsinghuaC3I/Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) | paper-list | エージェント記憶 | 518 | 2026-05 | 言語エージェントの記憶(ユーザプロファイル・対話履歴)に関する論文集 |
| 🟢 | [opendilab/awesome-ui-agents](https://github.com/opendilab/awesome-ui-agents) | awesome | UIエージェント | 300 | 2026-05 | Web/App/OSを横断するUIエージェント資源の継続更新リスト |
| 🟢 | [DEEP-PolyU/Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) | survey | グラフエージェント記憶 | 277 | 2026-04 | グラフベースのエージェント記憶のサーベイ・論文・ベンチマーク集 |
| 🟡 | [hyp1231/awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) | awesome | LLMエージェント | 2233 | 2025-04 | LLM駆動エージェントの論文・リポジトリ・ブログ集 |
| 🟡 | [AGI-Edgerunners/LLM-Planning-Papers](https://github.com/AGI-Edgerunners/LLM-Planning-Papers) | paper-list | LLMプランニング | 440 | 2024-07 | LLMのプランニング(planning)に関する必読論文集 |
| 🟡 | [junhua/awesome-llm-agents](https://github.com/junhua/awesome-llm-agents) | paper-list | LLMエージェント | 84 | 2024-11 | LLMエージェントの高品質論文・OSSプロジェクト集 |
| 🟡 | [shizhl/Multi-Agent-Papers](https://github.com/shizhl/Multi-Agent-Papers) | paper-list | マルチエージェント | 72 | 2023-11 | 複雑タスク向けマルチエージェント協調の必読論文集 |
| 🟡 | [Andrewzh112/Awesome-LLM-based-MultiAgents](https://github.com/Andrewzh112/Awesome-LLM-based-MultiAgents) | paper-list | マルチエージェント | 27 | 2024-10 | LLMベースのマルチエージェント論文集 |

### 🔬 医療AI / AI for Science  (41件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [AI-in-Health/MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) | survey | 医療LLM | 2015 | 2025-09 | 医療LLM実践ガイド(Nature Reviews Bioengineering掲載) |
| 🟢 | [ai-boost/awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) | awesome | AI for Science | 1603 | 2026-05 | 物理・化学・生物・材料など科学的発見を加速するAIツール・論文集 |
| 🟢 | [Awesome-Image-Registration-Organization/awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration) | awesome | 画像レジストレーション | 1526 | 2026-05 | 画像レジストレーション全般の書籍・論文・ツールボックス集 |
| 🟢 | [richard-peng-xia/awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) | awesome | 医用マルチモーダル | 960 | 2026-02 | 医用画像へのマルチモーダル学習応用のリソース集 |
| 🟢 | [Jianing-Qiu/Awesome-Healthcare-Foundation-Models](https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models) | paper-list | ヘルスケア基盤モデル | 515 | 2026-04 | ヘルスケア基盤モデルの論文コレクション |
| 🟢 | [OmicsML/awesome-foundation-model-single-cell-papers](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) | paper-list | シングルセル基盤モデル | 449 | 2026-01 | シングルセル基盤モデルに特化した論文リスト |
| 🟢 | [mk-runner/Awesome-Radiology-Report-Generation](https://github.com/mk-runner/Awesome-Radiology-Report-Generation) | paper-list | 放射線レポート生成 | 436 | 2026-05 | 放射線レポート生成の論文・データセット・ツール集(非常に活発) |
| 🟢 | [burglarhobbit/Awesome-Medical-Large-Language-Models](https://github.com/burglarhobbit/Awesome-Medical-Large-Language-Models) | paper-list | 医療LLM | 392 | 2025-05 | 医療・ヘルスケア領域のLLM論文を厳選したコレクション |
| 🟢 | [jaychempan/Awesome-LWMs](https://github.com/jaychempan/Awesome-LWMs) | awesome | 気象気候 | 360 | 2025-06 | 大規模気象モデル(LWMs)コレクション(AI4Earth) |
| 🟢 | [AspirinCode/awesome-AI4MolConformation-MD](https://github.com/AspirinCode/awesome-AI4MolConformation-MD) | paper-list | 分子動力学 | 295 | 2026-05 | 生成AI/深層学習による分子コンフォメーション・分子動力学の論文集 |
| 🟢 | [ESIPFed/Awesome-Earth-Artificial-Intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) | awesome | 地球科学AI | 244 | 2026-05 | 地球科学AIのチュートリアル・ソフト・データセット・論文集 |
| 🟢 | [willxxy/awesome-mmps](https://github.com/willxxy/awesome-mmps) | awesome | マルチモーダル生理信号 | 159 | 2026-02 | EEG/ECG/EMG等の生理信号×機械学習の資源・データセット集(活発) |
| 🟢 | [LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis](https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis) | survey | 医用能動学習 | 134 | 2025-06 | 医用画像解析の能動学習サーベイ論文・コード |
| 🟢 | [JHU-MedImage-Reg/MedImgReg_Survey](https://github.com/JHU-MedImage-Reg/MedImgReg_Survey) | survey | 医用画像レジストレーション | 121 | 2025-05 | 学習ベース医用画像レジストレーションの論文集+損失関数/評価指標の実装 |
| 🟢 | [open-pathology/awesome-pathology](https://github.com/open-pathology/awesome-pathology) | awesome | 計算病理 | 119 | 2026-02 | デジタル/計算病理の資源(自己教師あり・特徴抽出・データセット等)を網羅 |
| 🟢 | [yboulaamane/awesome-drug-discovery](https://github.com/yboulaamane/awesome-drug-discovery) | awesome | 創薬 | 112 | 2026-05 | 計算創薬手法に特化した厳選リソースリスト |
| 🟢 | [shi-ang/SurvivalAnalysisPapers](https://github.com/shi-ang/SurvivalAnalysisPapers) | paper-list | 生存時間解析 | 90 | 2026-05 | 生存時間解析の論文・資源をカテゴリ別に整理(活発) |
| 🟢 | [faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation](https://github.com/faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation) | paper-list | 医用画像セグメンテーション | 66 | 2026-02 | 医用画像セグメンテーションの深層学習論文集 |
| 🟢 | [okbalefthanded/awesome-bci-reviews](https://github.com/okbalefthanded/awesome-bci-reviews) | survey | BCI | 47 | 2025-08 | BCIの査読済みレビュー・サーベイを年代順に整理(活発) |
| 🟢 | [BearCleverProud/AwesomeWSI](https://github.com/BearCleverProud/AwesomeWSI) | survey | 病理WSI | 35 | 2026-02 | WSI解析と病理基盤モデルの包括的コレクション(IJCAI 2025サーベイ準拠、活発) |
| 🟢 | [yuanzhang7/Awesome-Generative-Models-in-Pathology](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology) | survey | 病理生成モデル | 27 | 2025-10 | 病理における生成モデル(画像合成・レポート生成・クロスモーダル)150本超のサーベイ |
| 🟢 | [AIM-Research-Lab/Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) | paper-list | 医療AIエージェント | 23 | 2026-03 | 医療向けエージェントAIの最新サーベイ集 |
| 🟢 | [ambicuity/Awesome-MICCAI-2026](https://github.com/ambicuity/Awesome-MICCAI-2026) | paper-list | 会議論文(MICCAI) | 20 | 2026-05 | MICCAI 2026論文をarXivから自動収集しbotが毎日更新、分野別分類 |
| 🟢 | [Deepak-Mewada/Awesome-AI4BCI](https://github.com/Deepak-Mewada/Awesome-AI4BCI) | paper-list | BCI/脳信号 | 17 | 2025-09 | 脳信号エンコーディング/デコーディングの深層学習モデル資源集 |
| 📑 | [xmindflow/Awesome-Foundation-Models-in-Medical-Imaging](https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging) | survey | 医用画像基盤モデル | 301 | 2024-06 | 医用画像の視覚・言語基盤モデルの厳選リスト |
| 📑 | [shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate](https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate) | survey | 気象気候 | 293 | 2025-02 | 気象・気候データ理解向け基盤モデルの包括サーベイ |
| 📑 | [YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare](https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare) | survey | ヘルスケア基盤モデル | 251 | 2024-12 | ヘルスケア基盤モデル(HFM)の課題・機会・将来展望の包括レビュー |
| 📑 | [hsd1503/DL-ECG-Review](https://github.com/hsd1503/DL-ECG-Review) | survey | ECG深層学習 | 250 | 2020-10 | ECGの深層学習手法レビューと論文サマリ表 |
| 🟡 | [JunMa11/MICCAI-OpenSourcePapers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) | paper-list | 会議論文(MICCAI) | 1293 | 2023-11 | MICCAI 2019-2023のオープンソース論文をコードリンク付き表で整理 |
| 🟡 | [OmicsML/awesome-deep-learning-single-cell-papers](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) | paper-list | シングルセル | 856 | 2025-04 | シングルセル解析×深層学習の最新論文を30以上のタスク別に整理 |
| 🟡 | [LirongWu/awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning) | paper-list | タンパク質表現学習 | 685 | 2024-11 | タンパク質表現学習(AlphaFold含む)の論文集 |
| 🟡 | [opendilab/awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design) | paper-list | AIタンパク質設計 | 306 | 2024-05 | AIベースのタンパク質設計の研究論文集 |
| 🟡 | [mingze-yuan/Awesome-LLM-Healthcare](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) | paper-list | 医療LLM | 268 | 2023-12 | 医療分野のLLMレビュー論文に対応した論文リスト |
| 🟡 | [subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images](https://github.com/subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images) | awesome | EM画像神経セグメンテーション | 57 | 2024-03 | 電子顕微鏡(EM)画像における神経突起の3Dセグメンテーション資源集 |
| 🟡 | [OmicsML/awesome-molecule-protein-pretrain-papers](https://github.com/OmicsML/awesome-molecule-protein-pretrain-papers) | paper-list | 分子・タンパク質事前学習 | 47 | 2024-03 | 分子・タンパク質の事前学習論文集(創薬・ドッキング) |
| 🟡 | [taohan10200/Awesome_AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) | paper-list | AI4Earth | 14 | 2023-12 | 地球システム(特に気象・気候)の機械学習論文集 |
| 🔴 | [hurcy/awesome-ehr-deeplearning](https://github.com/hurcy/awesome-ehr-deeplearning) | awesome | EHR深層学習 | 428 | 2022-10 | EHRマイニング・機械学習・深層学習論文集 |
| 🔴 | [ziyujia/Physiological-Signal-Classification-Papers](https://github.com/ziyujia/Physiological-Signal-Classification-Papers) | paper-list | 生理信号分類 | 249 | 2022-07 | EEG/ECG/EMG/EOGの分類論文をタスク別に整理 |
| 🔴 | [zhjohnchan/awesome-radiology-report-generation](https://github.com/zhjohnchan/awesome-radiology-report-generation) | awesome | 医療レポート生成 | 180 | 2022-05 | 放射線/医療レポート生成と関連領域のキュレーションリスト |
| 🔴 | [twoXes/awesome-structural-bioinformatics](https://github.com/twoXes/awesome-structural-bioinformatics) | awesome | 構造バイオインフォマティクス | 79 | 2023-05 | 構造バイオインフォマティクスのリソース集 |
| 🔴 | [OmicsML/awesome-bio-chatgpt](https://github.com/OmicsML/awesome-bio-chatgpt) | paper-list | バイオ×ChatGPT | 22 | 2023-04 | 生物学・医療分野へのChatGPT/LLM応用の論文・資源集 |

### 🌍 AI応用ドメイン(Code / Math / Finance / Law / 科学)  (28件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [satellite-image-deep-learning/techniques](https://github.com/satellite-image-deep-learning/techniques) | awesome | 衛星画像 | 10158 | 2026-05 | 衛星・航空画像の深層学習手法の超大規模リファレンス |
| 🟢 | [georgezouq/awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) | awesome | AI for Finance | 5994 | 2026-05 | 金融市場のLLM・深層学習戦略・ツールの定番リスト |
| 🟢 | [codefuse-ai/Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) | paper-list | AI for Code | 3364 | 2026-05 | コード向け言語モデル研究とデータセットの網羅的キュレーション |
| 🟢 | [wenhwu/awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) | awesome | リモートセンシング変化検出 | 2236 | 2026-04 | RS変化検出のデータセット・手法・サーベイ集 |
| 🟢 | [Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) | paper-list | リモートセンシング基盤モデル | 1830 | 2026-05 | RSFMの論文・データセット・ベンチ・事前学習重みを網羅(活発) |
| 🟢 | [brycejohnston/awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) | awesome | 農業AI | 1771 | 2026-01 | 農業・農場・園芸向けOSS技術(ML・GIS・リモセン・ロボティクス含む)の定番リスト |
| 🟢 | [frutik/awesome-search](https://github.com/frutik/awesome-search) | awesome | 検索/EC | 1544 | 2026-05 | EC検索を中心にセマンティック検索・LTR・クエリ理解・検索品質を網羅 |
| 🟢 | [JuDFTteam/best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) | awesome | 原子論的ML/材料 | 690 | 2026-05 | 原子論的機械学習プロジェクト約510件をスコア付きランキング(活発) |
| 🟢 | [yuzhimanhua/Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) | survey | 科学LLM | 660 | 2025-06 | 数学・物理・化学・材料・生物・地球科学等の科学ドメイン事前学習モデルの包括サーベイ |
| 🟢 | [tilde-lab/awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) | awesome | 材料インフォマティクス | 515 | 2026-03 | 現代材料科学におけるマテリアルズ・インフォマティクスの取り組み集 |
| 🟢 | [iSEngLab/AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) | survey | LLM for SE | 329 | 2026-04 | 要件・開発・テスト・保守までSE全領域のLLM論文を整理 |
| 🟢 | [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) | awesome | 法務NLP | 325 | 2025-10 | 判決予測・契約分類・判例検索・法務QA等のLegalNLPリソース集 |
| 🟢 | [zhaoyu-li/DL4TP](https://github.com/zhaoyu-li/DL4TP) | survey | 自動定理証明 | 224 | 2025-05 | 定理証明への深層学習の調査。autoformalization・proof search等で分類 |
| 🟢 | [GeminiLight/awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) | paper-list | 教育AI | 186 | 2026-04 | トップ会議・ジャーナルの教育向けAI/LLM論文を収集 |
| 🟢 | [AI-in-Transportation-Lab/awesome-pinns](https://github.com/AI-in-Transportation-Lab/awesome-pinns) | awesome | PINN/SciML | 110 | 2026-05 | PINN/物理情報機械学習のライブラリ・論文・チュートリアル厳選集 |
| 🟢 | [Event-AHU/PINN_Paper_List](https://github.com/Event-AHU/PINN_Paper_List) | paper-list | PINN | 77 | 2026-04 | 物理情報ニューラルネットワーク(PINN)の論文リスト |
| 📑 | [adlnlp/FinLLMs](https://github.com/adlnlp/FinLLMs) | survey | LLM for Finance | 370 | 2025-04 | 論文「Large Language Models in Finance」の関連研究・ベンチ・データセット集 |
| 📑 | [xiaoaoran/awesome-RSFMs](https://github.com/xiaoaoran/awesome-RSFMs) | survey | リモートセンシング | 50 | 2024-11 | サーベイ「Foundation Models for Remote Sensing and Earth Observation」公式リポジトリ |
| 🟡 | [idrl-lab/PINNpapers](https://github.com/idrl-lab/PINNpapers) | paper-list | PINN | 1497 | 2023-12 | PINNの必読論文集。並列化・加速・転移学習・不確実性定量化・応用で整理 |
| 🟡 | [Thinklab-SJTU/awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) | paper-list | AI for EDA | 208 | 2023-12 | 電子設計自動化(EDA・チップ設計)へのAI応用論文集 |
| 🟡 | [AI4LAM/awesome-ai4lam](https://github.com/AI4LAM/awesome-ai4lam) | awesome | AI for 図書館・文書館・博物館 | 178 | 2024-06 | 図書館・文書館・博物館(GLAM/LAM)向けAIのプロジェクト・事例・リソース集(AI4LAMコミュニティ運営) |
| 🟡 | [tongyx361/Awesome-LLM4Math](https://github.com/tongyx361/Awesome-LLM4Math) | paper-list | 数学推論 | 157 | 2024-07 | LLM数学推論の高品質厳選リスト。学習データ・SFT・RL・ベンチを整理 |
| 🟡 | [Geralt-Targaryen/Awesome-Education-LLM](https://github.com/Geralt-Targaryen/Awesome-Education-LLM) | paper-list | 教育LLM | 77 | 2024-09 | 教育向けLLM研究・応用(教授支援・問題生成・自動採点等)の整理 |
| 🟡 | [czyssrs/LLM_X_papers](https://github.com/czyssrs/LLM_X_papers) | paper-list | ドメインLLM横断 | 54 | 2025-02 | 金融・医療・法務のLLM論文を継続更新する読書リスト |
| 🔴 | [CSHaitao/Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) | awesome | 司法AI | 303 | 2023-07 | 司法AI向けのコーパス・ベンチ・QA・要約データセットを集約 |
| 🔴 | [shaohua0116/awesome-program](https://github.com/shaohua0116/awesome-program) | paper-list | プログラム合成 | 168 | 2021-10 | プログラム合成・帰納・実行・修復・programmatic RLの論文集 |
| 🔴 | [px39n/Awesome-Precision-Agriculture](https://github.com/px39n/Awesome-Precision-Agriculture) | paper-list | 精密農業 | 137 | 2020-09 | UAV・深層学習による収量予測・作物検出・雑草検出等の論文集 |
| 🔴 | [sherrylixuecheng/awesome-ai4chem](https://github.com/sherrylixuecheng/awesome-ai4chem) | paper-list | AI for Chemistry | 49 | 2023-05 | 化学向けAI論文のキュレーション |

### 🚗 自動運転(Autonomous Driving)  (18件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [OpenDriveLab/Birds-eye-view-Perception](https://github.com/OpenDriveLab/Birds-eye-view-Perception) | survey | BEV知覚 | 1374 | 2025-07 | BEV知覚研究とクックブック(IEEE T-PAMI 2023) |
| 🟢 | [colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers](https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers) | paper-list | 軌道・運動予測 | 1103 | 2026-01 | 軌道・運動予測の包括的論文集 |
| 📑 | [LincanLi-X/Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) | survey | データ中心自動運転 | 180 | 2024-03 | データ中心の自動運転サーベイの公式リポジトリ |
| 🟡 | [amusi/awesome-lane-detection](https://github.com/amusi/awesome-lane-detection) | paper-list | 車線検出 | 3045 | 2024-08 | 車線検出(lane detection)の論文リスト |
| 🟡 | [jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction) | paper-list | 軌道予測 | 1682 | 2024-09 | 相互作用を考慮した軌道予測の最先端研究資料集 |
| 🟡 | [autodriving-heart/Awesome-Autonomous-Driving](https://github.com/autodriving-heart/Awesome-Autonomous-Driving) | awesome | 自動運転全般 | 1129 | 2024-08 | 自動運転全般のawesomeリスト |
| 🟡 | [PJLab-ADG/awesome-knowledge-driven-AD](https://github.com/PJLab-ADG/awesome-knowledge-driven-AD) | paper-list | 知識駆動自動運転 | 501 | 2024-06 | 知識駆動型自動運転の厳選論文集 |
| 🟡 | [PeterJaq/Awesome-Autonomous-Driving](https://github.com/PeterJaq/Awesome-Autonomous-Driving) | awesome | 自動運転全般 | 353 | 2024-08 | 自動運転全般の広範なリスト |
| 🟡 | [autodriving-heart/Awesome-occupancy-perception](https://github.com/autodriving-heart/Awesome-occupancy-perception) | paper-list | 占有知覚 | 308 | 2024-08 | 占有知覚(Occupancy)論文コレクション |
| 🟡 | [autodriving-heart/CVPR-2024-Papers-Autonomous-Driving](https://github.com/autodriving-heart/CVPR-2024-Papers-Autonomous-Driving) | paper-list | 会議論文(CVPR/AD) | 257 | 2024-08 | CVPR 2024の自動運転関連論文リスト |
| 🟡 | [autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI](https://github.com/autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI) | paper-list | 会議論文(CVPR/AD+Embodied) | 29 | 2025-04 | CVPR 2025の自動運転・身体性AI関連論文リスト |
| 🟡 | [autodriving-heart/Awesome-4D-Radar](https://github.com/autodriving-heart/Awesome-4D-Radar) | paper-list | 4Dレーダ | 12 | 2024-02 | 4Dレーダ知覚に関する論文・リソース集 |
| 🔴 | [opendilab/awesome-end-to-end-autonomous-driving](https://github.com/opendilab/awesome-end-to-end-autonomous-driving) | awesome | End-to-End自動運転 | 493 | 2023-08 | End-to-End自動運転の資源を継続更新するリスト |
| 🔴 | [chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving](https://github.com/chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving) | paper-list | 占有予測 | 263 | 2023-07 | マルチカメラ意味的占有予測論文(Occ3D等) |
| 🔴 | [opendilab/awesome-driving-behavior-prediction](https://github.com/opendilab/awesome-driving-behavior-prediction) | paper-list | 運転行動予測 | 83 | 2022-12 | 運転行動予測の研究論文集 |
| 🔴 | [autodriving-heart/Awesome-BEV-Perception](https://github.com/autodriving-heart/Awesome-BEV-Perception) | paper-list | BEV知覚 | 32 | 2023-06 | BEV知覚の厳選論文コレクション |
| 🔴 | [autodriving-heart/Awesome-Trajectory-Prediction](https://github.com/autodriving-heart/Awesome-Trajectory-Prediction) | paper-list | 軌道予測 | 27 | 2023-06 | 軌道予測の論文コレクション |
| 🔴 | [ylhua/Awesome-BEV-Perception](https://github.com/ylhua/Awesome-BEV-Perception) | paper-list | BEV知覚 | 5 | 2022-08 | BEV知覚関連論文(BEVFormer, PETRv2, FIERY等) |

### 🛡️ AI安全性 / Alignment / 解釈性  (37件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) | awesome | 解釈性 | 4034 | 2026-05 | 責任あるML・解釈性の総合リソースリスト |
| 🟢 | [ydyjya/Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) | awesome | LLM安全性 | 1856 | 2026-05 | LLM安全性の論文・記事・データセット・ベンチマーク集 |
| 🟢 | [benedekrozemberczki/awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) | paper-list | 不正検知 | 1798 | 2026-01 | ICDM/KDD/SDM等の不正検知データマイニング論文の定番リスト |
| 🟢 | [wangyongjie-ntu/Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) | paper-list | XAI | 1641 | 2026-03 | 説明可能AI/MLの研究資料集 |
| 🟢 | [corca-ai/awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) | awesome | LLMセキュリティ | 1598 | 2025-08 | LLMセキュリティのツール・文献・プロジェクト集 |
| 🟢 | [thunlp/TAADpapers](https://github.com/thunlp/TAADpapers) | paper-list | テキスト敵対的攻撃 | 1574 | 2025-06 | テキストの敵対的攻撃・防御(TAAD)の必読論文集 |
| 🟢 | [yueliu1999/Awesome-Jailbreak-on-LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) | paper-list | LLMジェイルブレイク | 1390 | 2026-05 | LLMジェイルブレイク手法の論文・コード・データセット・評価集(非常に活発) |
| 🟢 | [tamlhp/awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) | awesome | 機械アンラーニング | 950 | 2026-05 | 機械unラーニングのサーベイ公式リスト。手法・データセット・評価指標を網羅 |
| 🟢 | [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) | paper-list | LLMアンラーニング | 591 | 2026-05 | LLMの機械unラーニング論文・サーベイ・ベンチマーク集 |
| 🟢 | [MinghuiChen43/awesome-trustworthy-deep-learning](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning) | paper-list | 信頼性 | 386 | 2026-05 | OOD汎化・敵対的サンプル・バックドア等の信頼性論文(毎日更新) |
| 🟢 | [HongshengHu/membership-inference-machine-learning-literature](https://github.com/HongshengHu/membership-inference-machine-learning-literature) | paper-list | メンバーシップ推論 | 371 | 2026-04 | メンバーシップ推論攻撃に特化した文献集 |
| 🟢 | [Billy1900/Awesome-AI-for-cybersecurity](https://github.com/Billy1900/Awesome-AI-for-cybersecurity) | awesome | サイバーセキュリティAI | 254 | 2026-05 | ネットワーク侵入検知・アンチマルウェア・WAF・不正対策を網羅したAIリスト |
| 🟢 | [AndrewZhou924/Awesome-model-inversion-attack](https://github.com/AndrewZhou924/Awesome-model-inversion-attack) | paper-list | モデル反転攻撃 | 221 | 2026-04 | モデル反転攻撃サーベイの公式リスト。CV/グラフ/NLP別に整理 |
| 🟢 | [itsqyh/Awesome-LMMs-Mechanistic-Interpretability](https://github.com/itsqyh/Awesome-LMMs-Mechanistic-Interpretability) | survey | マルチモーダル機械的解釈性 | 203 | 2026-03 | 大規模多モーダルモデルの内部表現を扱う機械的解釈性資源集(活発) |
| 🟢 | [franciscoliu/Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) | paper-list | 生成AIアンラーニング | 188 | 2026-04 | 生成AIのunラーニング論文をモダリティ・用途別に整理 |
| 🟢 | [Libr-AI/OpenRedTeaming](https://github.com/Libr-AI/OpenRedTeaming) | paper-list | LLMレッドチーミング | 165 | 2025-05 | LLM/マルチモーダルのレッドチーミング論文集(30+手法実装) |
| 🟢 | [and-mill/Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) | awesome | 生成AI電子透かし | 140 | 2026-05 | 生成AIモデル向け電子透かし手法を画像・音声・テキスト別に整理(活発) |
| 🟢 | [AI-in-Transportation-Lab/awesome-mechanistic-interpretability](https://github.com/AI-in-Transportation-Lab/awesome-mechanistic-interpretability) | awesome | 機械的解釈性 | 97 | 2026-05 | ニューラルネットを理解可能な計算要素へ逆解析する機械的解釈性のリソース集 |
| 🟢 | [AI4Risk/awesome-fraud-detection](https://github.com/AI4Risk/awesome-fraud-detection) | paper-list | 金融不正検知 | 43 | 2026-05 | GNNによる金融不正検知のサーベイ付き論文・コード集(活発) |
| 📑 | [tjunlp-lab/Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers) | survey | LLM安全性 | 56 | 2024-12 | LLM安全性のサーベイ論文リスト |
| 🟡 | [jivoi/awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) | awesome | サイバーセキュリティML | 8776 | 2024-08 | マルウェア・侵入検知等にMLを使うツール・論文・教材の定番リスト |
| 🟡 | [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) | awesome | プロンプトインジェクション防御 | 696 | 2025-02 | プロンプトインジェクションに対する実用・提案済み防御策を網羅 |
| 🟡 | [stratosphereips/awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) | awesome | MLプライバシー攻撃 | 639 | 2024-03 | メンバーシップ推論・モデル反転・属性推論・モデル抽出を網羅した論文リスト |
| 🟡 | [zihao-ai/Awesome-Backdoor-in-Deep-Learning](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning) | paper-list | バックドア攻撃 | 238 | 2024-03 | 深層学習のバックドア攻撃と防御を攻撃種別・防御段階で整理した論文集(活発) |
| 🟡 | [Giskard-AI/awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) | paper-list | AI安全性 | 215 | 2025-04 | AI品質・安全性に関する論文と技術記事のキュレーションリスト |
| 🟡 | [usnistgov/trojai-literature](https://github.com/usnistgov/trojai-literature) | paper-list | トロイの木馬攻撃 | 149 | 2024-10 | NISTが運営するAIトロイの木馬攻撃研究文献の総覧 |
| 🟡 | [TracyCuiq/Learning-Deep-Hiding](https://github.com/TracyCuiq/Learning-Deep-Hiding) | paper-list | 深層情報秘匿 | 67 | 2024-06 | 画像ステガノグラフィと電子透かしを含む「deep hiding」論文を体系整理 |
| 🟡 | [minbeomkim/Constitutional-AI-awesome-papers](https://github.com/minbeomkim/Constitutional-AI-awesome-papers) | paper-list | Constitutional AI | 13 | 2024-03 | Constitutional AI/倫理指針下のAIに関する論文リスト |
| 🔴 | [yenchenlin/awesome-adversarial-machine-learning](https://github.com/yenchenlin/awesome-adversarial-machine-learning) | awesome | 敵対的攻撃 | 1906 | 2020-11 | 敵対的機械学習の論文・ブログ・講演を集めた古典的キュレーション |
| 🔴 | [lopusz/awesome-interpretable-machine-learning](https://github.com/lopusz/awesome-interpretable-machine-learning) | awesome | 解釈性 | 916 | 2023-03 | 解釈可能機械学習のリソースリスト |
| 🔴 | [datamllab/awesome-fairness-in-ai](https://github.com/datamllab/awesome-fairness-in-ai) | awesome | ML公平性 | 334 | 2023-09 | AIにおける公平性リソースの厳選集 |
| 🔴 | [altamiracorp/awesome-xai](https://github.com/altamiracorp/awesome-xai) | awesome | XAI | 188 | 2021-05 | 説明可能AI(XAI)・解釈可能MLの論文とリソース |
| 🔴 | [dit7ya/awesome-ai-alignment](https://github.com/dit7ya/awesome-ai-alignment) | awesome | alignment | 81 | 2023-07 | AIアライメント研究の優れたリソースのキュレーションリスト |
| 🔴 | [brandeis-machine-learning/awesome-ml-fairness](https://github.com/brandeis-machine-learning/awesome-ml-fairness) | paper-list | ML公平性 | 74 | 2023-05 | 機械学習の公平性に関する論文・リソース集 |
| 🔴 | [hari-sikchi/awesome-ai-safety](https://github.com/hari-sikchi/awesome-ai-safety) | awesome | AI安全性 | 64 | 2020-02 | AI安全性の論文・プロジェクト・コミュニティのリスト |
| 🔴 | [ch-shin/awesome-data-poisoning](https://github.com/ch-shin/awesome-data-poisoning) | awesome | データポイズニング | 25 | 2022-09 | トップ会議のデータポイズニング攻撃・防御論文集 |
| 🔴 | [KululuMi/Awesome-Adversarial-Training](https://github.com/KululuMi/Awesome-Adversarial-Training) | paper-list | 敵対的学習 | 6 | 2022-04 | FGSM/PGD/TRADES/AutoAttack等の敵対的訓練論文リスト |

### ⚖️ AI倫理 / ガバナンス / 規制 / Human-AI Interaction  (7件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [EthicalML/awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) | awesome | AI規制/政策 | 1438 | 2026-05 | 各国のAI規制・ガイドライン・倫理規範・標準を地域別に網羅 |
| 🟢 | [gesiscss/awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) | awesome | 計算社会科学 | 890 | 2026-05 | 計算社会科学の書籍・講座・OSS資源の網羅リスト(GESIS運営) |
| 🟢 | [ValueByte-AI/Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science) | paper-list | LLM×社会科学 | 622 | 2026-02 | 社会科学にLLMを応用する論文集 |
| 🟢 | [AthenaCore/AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI) | awesome | 責任あるAI | 129 | 2026-05 | 責任あるAIの研究・書籍・規制・成熟度モデル・ツールを17分野で集約 |
| 🟢 | [ValueByte-AI/Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) | survey | LLM心理測定 | 109 | 2025-11 | LLMの人格・価値観・心の理論・認知能力を心理測定の観点で扱う論文集 |
| 🔴 | [zhijing-jin/NLP4SocialGood_Papers](https://github.com/zhijing-jin/NLP4SocialGood_Papers) | paper-list | NLP for Social Good | 310 | 2023-09 | 社会善のためのNLP論文の読解リスト(救命・QoL・公平性等) |
| 🔴 | [bwang514/awesome-HAI](https://github.com/bwang514/awesome-HAI) | awesome | Human-AI Interaction | 297 | 2021-05 | HCI視点での人間とAIのインタラクション設計に関する学術資料集 |

### ⚡ 効率化(圧縮 / 量子化 / NAS / AutoML)  (21件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [Efficient-ML/Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) | paper-list | 量子化 | 2383 | 2026-05 | モデル量子化の論文・コード・ドキュメントのリスト |
| 🟢 | [horseee/Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) | awesome | 効率的LLM | 2016 | 2025-06 | 効率的LLM(枝刈り・量子化・蒸留等)のキュレーションリスト |
| 🟢 | [HuangOwen/Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) | awesome | LLM圧縮 | 1837 | 2026-02 | 量子化・枝刈り・蒸留などLLM圧縮の論文とツール集 |
| 🟢 | [gigwegbe/tinyml-papers-and-projects](https://github.com/gigwegbe/tinyml-papers-and-projects) | paper-list | TinyML | 1010 | 2025-12 | TinyMLの論文・プロジェクト集(活発に更新) |
| 🟢 | [windmaple/awesome-AutoML](https://github.com/windmaple/awesome-AutoML) | awesome | AutoML | 936 | 2026-03 | AutoMLのキュレーションリスト |
| 🟢 | [PrunaAI/awesome-ai-efficiency](https://github.com/PrunaAI/awesome-ai-efficiency) | awesome | AI効率化 | 222 | 2026-02 | AIモデルの高速化・小型化・省エネ手法のリスト |
| 🟢 | [jeho-lee/Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) | awesome | オンデバイスAIシステム | 156 | 2026-05 | オンデバイスAIシステム(推論エンジン/ベンチ/論文)、活発 |
| 🟢 | [samuelrince/awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) | awesome | Green AI | 114 | 2026-05 | AIの環境影響を評価・削減するGreen AIツール/論文の定番リスト |
| 📑 | [Tebmer/Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) | survey | LLM知識蒸留 | 1281 | 2025-03 | LLMの知識蒸留サーベイ連動の論文集 |
| 🟡 | [cedrickchee/awesome-ml-model-compression](https://github.com/cedrickchee/awesome-ml-model-compression) | awesome | モデル圧縮 | 543 | 2024-09 | モデル圧縮・量子化のリサーチ論文・ツール・学習資料 |
| 🟡 | [jackguagua/awesome-nas-papers](https://github.com/jackguagua/awesome-nas-papers) | paper-list | NAS | 405 | 2024-01 | Neural Architecture Search論文の集約リスト |
| 🔴 | [FLHonker/Awesome-Knowledge-Distillation](https://github.com/FLHonker/Awesome-Knowledge-Distillation) | paper-list | 知識蒸留 | 2665 | 2023-05 | 知識蒸留の論文を分類整理(2014-2021) |
| 🔴 | [D-X-Y/Awesome-AutoDL](https://github.com/D-X-Y/Awesome-AutoDL) | awesome | AutoML | 2337 | 2022-09 | 自動深層学習(AutoDL)のリソースと詳細分析 |
| 🔴 | [csarron/awesome-emdl](https://github.com/csarron/awesome-emdl) | awesome | 組込み/モバイルDL | 768 | 2023-03 | 組込み・モバイル深層学習の論文/ライブラリ/ツール集 |
| 🔴 | [Bisonai/awesome-edge-machine-learning](https://github.com/Bisonai/awesome-edge-machine-learning) | awesome | エッジML | 280 | 2023-02 | エッジ機械学習の論文・推論エンジン・課題・書籍を網羅 |
| 🔴 | [automl/awesome-transformer-search](https://github.com/automl/awesome-transformer-search) | awesome | NAS | 270 | 2023-06 | TransformerとNASを組み合わせたリソースのリスト |
| 🔴 | [ChanChiChoi/awesome-model-compression](https://github.com/ChanChiChoi/awesome-model-compression) | paper-list | モデル圧縮 | 166 | 2023-02 | モデル圧縮(構造・蒸留・二値化・量子化・枝刈り)論文集 |
| 🔴 | [NiuTrans/NASPapers](https://github.com/NiuTrans/NASPapers) | paper-list | NAS | 135 | 2021-09 | ニューラルアーキテクチャ探索(NAS)の論文リスト |
| 🔴 | [chenbong/awesome-compression-papers](https://github.com/chenbong/awesome-compression-papers) | paper-list | 圧縮 | 25 | 2020-10 | 圧縮・高速化(枝刈り・量子化・蒸留・低ランク分解)の論文集 |
| 🔴 | [chenyaofo/awesome-architecture-search](https://github.com/chenyaofo/awesome-architecture-search) | paper-list | NAS | 9 | 2022-05 | NASの進展を最新追跡する論文リスト |
| 🔴 | [Openning07/Awesome-NAS](https://github.com/Openning07/Awesome-NAS) | awesome | NAS | 1 | 2020-04 | ニューラルアーキテクチャ探索(NAS)リソースのキュレーション |

### 🔐 連合学習 / プライバシー  (7件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning](https://github.com/JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning) | paper-list | 差分プライバシー | 388 | 2025-09 | 差分プライバシーを用いた連合学習・MLの論文と実装 |
| 🟢 | [gnipping/Awesome-ML-SP-Papers](https://github.com/gnipping/Awesome-ML-SP-Papers) | paper-list | MLセキュリティ | 347 | 2025-11 | セキュリティトップ4会議のML Security & Privacy論文集 |
| 🟡 | [poga/awesome-federated-learning](https://github.com/poga/awesome-federated-learning) | awesome | 連合学習 | 547 | 2024-06 | 連合学習とMLにおけるプライバシーのリソース集 |
| 🟡 | [AmberLJC/FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper) | paper-list | 連合学習システム | 75 | 2024-02 | 連合学習システム・フレームワークの論文リスト |
| 🔴 | [chaoyanghe/Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning) | paper-list | 連合学習 | 2016 | 2022-09 | FedML連携の連合学習研究・プロダクション統合リスト |
| 🔴 | [csl-cqu/awesome-secure-federated-learning-papers](https://github.com/csl-cqu/awesome-secure-federated-learning-papers) | paper-list | 安全な連合学習 | 26 | 2023-03 | 安全な連合学習(攻撃・防御・勾配反転)の論文集 |
| 🔴 | [Willjay5991/awesome-federated-learning](https://github.com/Willjay5991/awesome-federated-learning) | awesome | 連合学習 | 2 | 2020-08 | 連合学習の論文・記事・フレームワーク・講義資料 |

### ♻️ 継続学習(Continual Learning)  (7件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [xialeiliu/Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning) | paper-list | 継続学習 | 4469 | 2026-05 | 増分学習・継続学習・破滅的忘却の主要会議論文集 |
| 🟢 | [zzz47zzz/awesome-lifelong-learning-methods-for-llm](https://github.com/zzz47zzz/awesome-lifelong-learning-methods-for-llm) | survey | LLM生涯学習 | 162 | 2025-05 | LLMの生涯学習に関するサーベイ・論文集 |
| 🟡 | [Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning](https://github.com/Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning) | paper-list | 増分学習 | 607 | 2024-05 | 増分・継続・生涯学習のリポジトリ |
| 🟡 | [feifeiobama/Awesome-Continual-Learning](https://github.com/feifeiobama/Awesome-Continual-Learning) | paper-list | 継続学習 | 203 | 2024-10 | 継続学習論文とBibTeXエントリのキュレーションリスト |
| 🟡 | [AGI-Edgerunners/LLM-Continual-Learning-Papers](https://github.com/AGI-Edgerunners/LLM-Continual-Learning-Papers) | paper-list | LLM継続学習 | 149 | 2023-11 | LLMの継続学習(continual learning)の必読論文集 |
| 🟡 | [lywang3081/Awesome-Continual-Learning](https://github.com/lywang3081/Awesome-Continual-Learning) | paper-list | 継続学習 | 108 | 2024-02 | 継続学習サーベイ連動の論文リストと有用なリソース |
| 🔴 | [prprbr/awesome-lifelong-continual-learning](https://github.com/prprbr/awesome-lifelong-continual-learning) | awesome | 生涯学習 | 298 | 2021-03 | 生涯/継続学習の論文・ブログ・データセット・ソフトウェアのリスト |

### 🖥️ MLシステム / 学習・推論インフラ / データ基盤  (16件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [HuaizhengZhang/AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) | awesome | MLシステム | 4047 | 2025-07 | AIシステム論文と産業実践(OSDI/NSDI/MLSys等、LLM・GenAI含む)を集めた定番 |
| 🟢 | [wasiahmad/Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) | paper-list | 合成データ | 1537 | 2025-06 | LLMによる合成データ生成のリーディングリスト(活発) |
| 🟢 | [yandex-research/rtdl](https://github.com/yandex-research/rtdl) | paper-list | テーブル深層学習 | 1139 | 2026-04 | テーブルデータ深層学習の論文とパッケージ集(Yandex Research) |
| 🟢 | [byungsoo-oh/ml-systems-papers](https://github.com/byungsoo-oh/ml-systems-papers) | paper-list | MLシステム | 556 | 2026-02 | MLシステム分野の論文を体系的に集めたコレクション |
| 🟢 | [lambda7xx/awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) | paper-list | AIシステム | 362 | 2026-05 | AIシステムの論文とそのコードをまとめたリスト |
| 🟢 | [dangkhoasdc/awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) | awesome | ベクトルDB | 353 | 2026-05 | 高次元ベクトル検索・データベース関連の厳選リスト(活発) |
| 🟢 | [sihyeong/Awesome-LLM-Inference-Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) | survey | LLM推論エンジン | 210 | 2026-04 | LLM推論最適化手法をレイテンシ/スループット/メモリ別に分類した網羅的まとめ |
| 🟢 | [LAMDA-Tabular/Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) | survey | テーブル深層学習 | 123 | 2026-05 | 「Representation Learning for Tabular Data」サーベイ付随リスト |
| 🟡 | [AgaMiko/data-augmentation-review](https://github.com/AgaMiko/data-augmentation-review) | awesome | データ拡張 | 1637 | 2024-08 | データ拡張の手法・ライブラリ・論文を幅広く集めたレビュー |
| 🟡 | [currentslab/awesome-vector-search](https://github.com/currentslab/awesome-vector-search) | awesome | ベクトル検索 | 1563 | 2024-08 | ベクトル検索のライブラリ・サービス・論文集(Faiss, Annoy等) |
| 🟡 | [Shenggan/awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) | awesome | 分散学習 | 279 | 2024-10 | 大規模モデルの分散学習・推論に関するプロジェクトと論文の厳選リスト |
| 🟡 | [statice/awesome-synthetic-data](https://github.com/statice/awesome-synthetic-data) | awesome | 合成データ | 257 | 2024-01 | OSS/商用の合成データツール厳選リスト(SDV等) |
| 🟡 | [DefTruth/Awesome-LLM-Inference](https://github.com/DefTruth/Awesome-LLM-Inference) | paper-list | LLM推論 | 16 | 2025-03 | LLM/VLM推論最適化(FlashAttention,PagedAttention,MLA等)の論文+コード集 |
| 🔴 | [CrazyVertigo/awesome-data-augmentation](https://github.com/CrazyVertigo/awesome-data-augmentation) | awesome | データ拡張 | 797 | 2021-03 | データ拡張手法(AugMix, CutMix等)の厳選リスト |
| 🔴 | [RaviVijay/awesome-dl-hw-resources](https://github.com/RaviVijay/awesome-dl-hw-resources) | awesome | DLハードウェア | 58 | 2018-05 | 深層学習向けハードウェア/チップ設計リソースの厳選リスト |
| 🔴 | [dujiangsu/Awesome-MLSys](https://github.com/dujiangsu/Awesome-MLSys) | paper-list | MLSys | 6 | 2023-09 | 大規模モデル推論を中心としたMLSys分野の学術論文集 |

### 🛠️ MLOps / データ中心AI  (10件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | awesome | MLシステム | 20573 | 2026-05 | MLのデプロイ・監視・スケーリング用OSSライブラリのリスト |
| 🟢 | [kelvins/awesome-mlops](https://github.com/kelvins/awesome-mlops) | awesome | MLOps | 5155 | 2026-04 | MLOpsツールのキュレーションリスト |
| 🟢 | [Guang000/Awesome-Dataset-Distillation](https://github.com/Guang000/Awesome-Dataset-Distillation) | awesome | データセット蒸留 | 1936 | 2026-05 | 勾配/分布マッチング・生成手法・応用を網羅した定番リスト(非常に活発) |
| 🟢 | [Data-Centric-AI-Community/awesome-data-centric-ai](https://github.com/Data-Centric-AI-Community/awesome-data-centric-ai) | awesome | データ中心AI | 350 | 2026-04 | データ中心AIのOSS・チュートリアル・研究 |
| 🟢 | [SJTU-DMTai/awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) | paper-list | データ品質/評価 | 120 | 2026-05 | データ評価・データ帰属・データ選定/プルーニング/コアセットを網羅 |
| 🟡 | [visenger/awesome-mlops](https://github.com/visenger/awesome-mlops) | awesome | MLOps | 13924 | 2024-11 | MLOpsの参考文献・リソース集 |
| 🟡 | [daochenzha/data-centric-AI](https://github.com/daochenzha/data-centric-AI) | awesome | データ中心AI | 1150 | 2024-06 | データ中心AIのリソースキュレーションリスト |
| 🟡 | [HazyResearch/data-centric-ai](https://github.com/HazyResearch/data-centric-ai) | awesome | データ中心AI | 1142 | 2023-12 | データ中心AIのリソース集(Stanford HazyResearch) |
| 🟡 | [Renumics/awesome-open-data-centric-ai](https://github.com/Renumics/awesome-open-data-centric-ai) | awesome | データ中心AI | 732 | 2023-11 | 非構造化データ向けデータ中心AIのOSSツール集 |
| 🟡 | [PatrickZH/Awesome-Coreset-Selection](https://github.com/PatrickZH/Awesome-Coreset-Selection) | awesome | コアセット選択 | 183 | 2024-06 | コアセット/サブセット選択・data pruningの論文集 |

### 📊 データセット / ベンチマーク  (5件)

| 鮮度 | リポジトリ | 種別 | サブ分野 | ⭐ | 最終更新 | 説明 |
|:--:|:--|:--|:--|--:|:--:|:--|
| 🟢 | [onejune2018/Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) | awesome | LLM評価 | 637 | 2025-11 | LLM評価のツール・ベンチマーク・リーダーボード・論文の厳選リスト |
| 🟢 | [ahammadmejbah/Awesome-Datasets-Hub](https://github.com/ahammadmejbah/Awesome-Datasets-Hub) | awesome | データセット | 132 | 2026-05 | 医療AI・NLP・マルチモーダル等のLLM向けデータセット集 |
| 🟢 | [SihyeongPark/Awesome-LLM-Benchmark](https://github.com/SihyeongPark/Awesome-LLM-Benchmark) | awesome | LLMベンチマーク | 11 | 2026-04 | 大規模言語モデル向けベンチマーク一覧 |
| 🟢 | [BenchGecko/awesome-llm-benchmarks](https://github.com/BenchGecko/awesome-llm-benchmarks) | awesome | LLMベンチマーク | 1 | 2026-03 | LLM/AIモデルのベンチマーク・データセット・リーダーボード集 |
| 🟡 | [leobeeson/llm_benchmarks](https://github.com/leobeeson/llm_benchmarks) | awesome | LLMベンチマーク | 569 | 2024-07 | LLM評価用ベンチマーク・データセットのコレクション |

---

## 調査メモ

- 各分野は専任の調査エージェントがWebSearch/WebFetchおよびGitHub APIで実在確認のうえ収集。
- 重複(複数分野に該当するリスト)は代表分野に正規化して1件に集約。
- HTTP 404 のリポジトリ(例: `steve-zeyu-zhang/Awesome-3D-Medical-Imaging-Segmentation`)は除外済み。
- リダイレクト(リネーム/移管)されたリポジトリは正規 full_name に解決済み。
