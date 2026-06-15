# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

**語言:** [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-lightgrey)](README.md) [![English](https://img.shields.io/badge/English-lightgrey)](README.en.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey)](README.ko.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-blue)](README.zh-Hant.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-lightgrey)](README.zh-Hans.md)

> 一份「清單的清單(awesome-of-awesome)」：橫跨 AI 研究各領域，彙整並分類 **awesome 清單、survey 倉庫、會議論文清單與特定模型合集**。

涵蓋 CV / CG / NLP / RL 等所有領域，也納入未冠 `awesome-` 的 survey 倉庫(例如 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))與 `awesome-nanobanana-pro` 之類的特定模型範例集。

**共 902 筆** / 33 個領域 — 🟢 活躍 446 筆、🟡 中等 202 筆(依 2026-06-15 的 GitHub 中繼資料自動生成)。

## 圖例 / 收錄標準

每筆條目皆標註 **⭐star 數**與 **📅最後更新(年-月)**及新鮮度標記。除歷史資料彙整外，皆以更新時間與頻率為重收錄與排序。

| 標記 | 意義 |
|:--:|:--|
| 🟢 | 活躍(近 12 個月內更新) |
| 🟡 | 中等(13〜30 個月) |
| 🔴 | 停滯(逾 30 個月未更新) |
| 📑 | 以同行評審 survey 論文為基礎的彙整(涵蓋性與權威性勝於更新頻率，雖舊仍有用) |
| 📚 | 歷史・經典合集(本即停止更新，不計新鮮度) |
| 📦 | 已封存(read-only) |

類型: `awesome`=精選清單 / `survey`=survey 論文附屬 / `paper-list`=論文清單 / `model`=特定模型範例

> 詳細中繼資料、完整結果與統計見 [docs/research-notes.md](docs/research-notes.md)；製作方法見 [docs/best-practices.md](docs/best-practices.md)(日文)。

## 目錄

- [🧠 機器學習通用 / 深度學習](#-機器學習通用--深度學習) (24)
- [📐 ML 理論 / 最佳化](#-ml-理論--最佳化) (12)
- [🎲 機率模型 / 貝氏 / 因果 / 不確定性](#-機率模型--貝氏--因果--不確定性) (17)
- [🏗️ 新架構 (SSM・Mamba・KAN・SNN・量子 ML)](#-新架構-ssmmambakansnn量子-ml) (24)
- [🌱 自監督 / 表徵學習 / 基礎模型](#-自監督--表徵學習--基礎模型) (6)
- [🎓 學習範式 (元學習/遷移/少樣本/OOD/半監督)](#-學習範式-元學習遷移少樣本ood半監督) (27)
- [👁️ 電腦視覺 (Computer Vision)](#-電腦視覺-computer-vision) (111)
- [🎨 電腦圖學 / 3D / 渲染](#-電腦圖學--3d--渲染) (65)
- [🖌️ 低階影像處理 / 復原 / 壓縮](#-低階影像處理--復原--壓縮) (22)
- [🎬 動漫・動畫・插畫・字型](#-動漫動畫插畫字型) (8)
- [💬 NLP / 大型語言模型(LLM)](#-nlp--大型語言模型llm) (98)
- [🖼️ 生成式 AI / Diffusion / 影像・影片生成](#-生成式-ai--diffusion--影像影片生成) (42)
- [🍌 特定模型的提示詞・範例集](#-特定模型的提示詞範例集) (21)
- [🧰 模型生態系 / 維運工具 (MCP・LLMOps・LLM 應用)](#-模型生態系--維運工具-mcpllmopsllm-應用) (25)
- [🎮 強化學習(RL)](#-強化學習rl) (35)
- [🔀 多模態 / VLM / MLLM](#-多模態--vlm--mllm) (30)
- [🔊 語音 / 音訊](#-語音--音訊) (28)
- [🤖 機器人學 / Embodied AI](#-機器人學--embodied-ai) (19)
- [🕸️ 圖學習(GNN) / 知識圖譜](#-圖學習gnn--知識圖譜) (35)
- [🛒 推薦系統(RecSys)](#-推薦系統recsys) (12)
- [📈 時間序列(Time Series)](#-時間序列time-series) (12)
- [🦾 AI 代理 / LLM Agents](#-ai-代理--llm-agents) (20)
- [🔬 醫療 AI / AI for Science](#-醫療-ai--ai-for-science) (41)
- [🌍 應用領域 (Code/Math/Finance/Law/科學)](#-應用領域-codemathfinancelaw科學) (33)
- [🚗 自動駕駛(Autonomous Driving)](#-自動駕駛autonomous-driving) (18)
- [🛡️ AI 安全 / Alignment / 可解釋性](#-ai-安全--alignment--可解釋性) (37)
- [⚖️ AI 倫理 / 治理 / 法規 / Human-AI Interaction](#-ai-倫理--治理--法規--human-ai-interaction) (7)
- [⚡ 高效化 (壓縮/量化/NAS/AutoML)](#-高效化-壓縮量化nasautoml) (23)
- [🔐 聯邦學習 / 隱私](#-聯邦學習--隱私) (7)
- [♻️ 持續學習(Continual Learning)](#-持續學習continual-learning) (7)
- [🖥️ ML 系統 / 訓練・推論基礎設施 / 資料](#-ml-系統--訓練推論基礎設施--資料) (19)
- [🛠️ MLOps / 資料中心 AI](#-mlops--資料中心-ai) (12)
- [📊 資料集 / 基準測試](#-資料集--基準測試) (5)


## 🧠 機器學習通用 / 深度學習

- 🟢 [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) — 依語言分類的ML框架與函式庫經典精選清單 `awesome` ⭐72.8k · 📅2026-06
- 🟢 [awesome-datascience](https://github.com/academic/awesome-datascience) — 學習資料科學並應用於實際問題的經典資源集 `awesome` ⭐29.4k · 📅2026-06
- 🟢 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) — 支援AI研究論文撰寫與潤飾的工具與資源集 `awesome` ⭐28.4k · 📅2026-05
- 🟢 [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources) — 涵蓋異常偵測書籍、論文、影片與工具箱的經典清單 `awesome` ⭐9.3k · 📅2026-03
- 🟢 [kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) — 彙整Kaggle競賽解法與構想的集合 `awesome` ⭐6.4k · 📅2026-06
- 🟢 [awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) — 精選Python資料科學軟體的清單 `awesome` ⭐3.5k · 📅2026-04
- 🟢 [awesome-deeplearning-resources](https://github.com/endymecy/awesome-deeplearning-resources) — 依時序整理DL與深度強化學習的論文與程式碼 `paper-list` ⭐3k · 📅2026-01
- 🟢 [paperlists](https://github.com/papercopilot/paperlists) — Paper Copilot的整理資料，依年度以JSON橫跨涵蓋主要會議並持續更新（大型） `paper-list` ⭐937 · 📅2026-02
- 🟢 [ai-deadlines](https://github.com/huggingface/ai-deadlines) — 主要AI會議的截止倒數（paperswithcode版後繼，現行主流） `awesome` ⭐343 · 📅2026-06
- 🟢 [ai_papers_scrapper](https://github.com/george-gca/ai_papers_scrapper) — 依會議×年度取得主要AI會議（2017起）PDF、作者與摘要等的爬蟲 `paper-list` ⭐52 · 📅2026-06
- 🟢 [ICML-2025-Papers](https://github.com/DmitryRyumin/ICML-2025-Papers) — 附程式碼實作連結體系化ICML 2025錄取論文 `paper-list` ⭐39 · 📅2025-10
- 📑 [awesome-AI-tutorials-surveys](https://github.com/qingsongedu/awesome-AI-tutorials-surveys) — 頂級AI會議的DL/ML/DM/CV/NLP/語音教學與綜述集 `survey` ⭐165 · 📅2023-02
- 🟡 [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) — 彙整DL教學、專案與社群的經典清單 `awesome` ⭐28.4k · 📅2025-05
- 🟡 [Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) — 機器學習與深度學習的教學、文章與資源大規模集 `awesome` ⭐17.9k · 📅2024-06
- 🟡 [Conference-Accepted-Paper-List](https://github.com/Lionelsy/Conference-Accepted-Paper-List) — 彙整主要AI/ML/機器人會議2015-2025錄取論文連結與截止資訊（活躍） `paper-list` ⭐1.3k · 📅2025-01
- 🟡 [AAAI-2024-Papers](https://github.com/DmitryRyumin/AAAI-2024-Papers) — 涵蓋AAAI 2024創新研究論文的集合 `paper-list` ⭐591 · 📅2025-01
- 🟡 [AI-Conference-Info](https://github.com/tranhungnghiep/AI-Conference-Info) — 橫跨年度彙整40+主要AI會議的錄取率、投稿統計與截止 `awesome` ⭐165 · 📅2024-07
- 🟡 [Conference-Paper](https://github.com/hzxwonder/Conference-Paper) — 整理CCF-A會議錄取論文，附標題、作者、URL與摘要 `paper-list` ⭐8 · 📅2024-04
- 📚 [Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) — 依學習順序整理深度學習主要論文的經典路線圖 `paper-list` ⭐39.5k · 📅2022-11
- 📚 [awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) — 2012〜2016年最常被引用的重要DL論文Top100 `paper-list` ⭐26.2k · 📅2024-01
- 🔴 [awesome-project-ideas](https://github.com/NirantK/awesome-project-ideas) — 彙整ML/NLP/Vision/推薦專案構想的清單 `awesome` ⭐9.1k · 📅2023-03
- 🔴 [awesome-ai-awesomeness](https://github.com/amusi/awesome-ai-awesomeness) — 彙整AI相關awesome清單的『awesome的awesome』 `awesome` ⭐978 · 📅2023-08
- 🔴 [Awesome-Paper-List](https://github.com/Doragd/Awesome-Paper-List) — 彙整NLP/CV/ML眾多論文清單與相關資源的元清單 `awesome` ⭐195 · 📅2022-04
- 🔴 [awesome-machine-learning-papers](https://github.com/solaris33/awesome-machine-learning-papers) — 重要ML論文與儲存庫的精選清單 `paper-list` ⭐78 · 📅2017-06

## 📐 ML 理論 / 最佳化

- 🟢 [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) — 於36個以上領域涵蓋將機器學習應用於組合最佳化的論文（活躍） `paper-list` ⭐2.1k · 📅2026-06
- 🟢 [awesome-neuro-ai-papers](https://github.com/CYHSM/awesome-neuro-ai-papers) — 深度學習與神經科學交叉領域的論文與綜述集（活躍） `paper-list` ⭐443 · 📅2026-01
- 🟢 [awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) — grokking、雙重下降、樂透假說等DL經驗現象與理論論文清單 `paper-list` ⭐398 · 📅2026-05
- 🟢 [awesome-language-model-analysis](https://github.com/Furyton/awesome-language-model-analysis) — 語言模型的理論與實證分析（湧現能力、scaling law、ICL理論、grokking） `paper-list` ⭐100 · 📅2026-06
- 🟡 [awesome-automl-papers](https://github.com/hibayesian/awesome-automl-papers) — AutoML論文、文章、教學與專案的經典大規模清單 `paper-list` ⭐4.1k · 📅2024-06
- 🟡 [must-read-papers-for-ml](https://github.com/hurshd0/must-read-papers-for-ml) — 資料科學與ML/DL工程師用必讀論文集（含經典） `paper-list` ⭐1.4k · 📅2023-12
- 🟡 [NeuralTangentKernel-Papers](https://github.com/kwignb/NeuralTangentKernel-Papers) — Neural Tangent Kernel（NTK）相關論文彙整清單 `paper-list` ⭐122 · 📅2025-01
- 🟡 [awesome-bayesian-optimization](https://github.com/materials-data-facility/awesome-bayesian-optimization) — 材料科學與化學用貝氏最佳化的軟體/論文/教學集 `awesome` ⭐51 · 📅2024-04
- 🔴 [Open-L2O](https://github.com/VITA-Group/Open-L2O) — L2O方法首個全面的基準兼論文整理儲存庫 `paper-list` ⭐299 · 📅2023-06
- 🔴 [awesome-deep-neuroevolution](https://github.com/Alro10/awesome-deep-neuroevolution) — 將演化計算應用於深度學習的Deep Neuroevolution資源集 `awesome` ⭐227 · 📅2021-04
- 🔴 [Awesome-ScalingLaws](https://github.com/RZFan525/Awesome-ScalingLaws) — 專注於LLM scaling law的資源集 `awesome` ⭐84 · 📅2023-04
- 🔴 [MLT-Papers](https://github.com/guoji-fu/MLT-Papers) — 機器學習理論（泛化界、最佳化、深度學習數學）論文清單 `paper-list` ⭐10 · 📅2022-02

## 🎲 機率模型 / 貝氏 / 因果 / 不確定性

- 🟢 [Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) — 對應ACM CSUR刊載綜述的diffusion/score-based/SDE生成模型論文分類 `survey` ⭐3.3k · 📅2025-09
- 🟢 [awesome-normalizing-flows](https://github.com/janosh/awesome-normalizing-flows) — 彙整normalizing flow論文、實作（PyTorch/JAX/Julia）與影片的代表性清單 `awesome` ⭐1.6k · 📅2026-03
- 🟢 [awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) — 彙整分布無關不確定性量化（CP）影片、論文與函式庫的充實清單 `awesome` ⭐1.2k · 📅2026-05
- 🟢 [awesome-uncertainty-deeplearning](https://github.com/ENSTA-U2IS-AI/awesome-uncertainty-deeplearning) — 涵蓋深度學習預測性不確定性估計的綜述、論文與程式碼的活躍清單 `awesome` ⭐814 · 📅2026-05
- 🟢 [awesome-flow-matching](https://github.com/dongzhuoyao/awesome-flow-matching) — 彙整flow matching與隨機插值相關研究的活躍清單 `awesome` ⭐681 · 📅2026-04
- 🟢 [awesome-ebm](https://github.com/yataobian/awesome-ebm) — 依年代整理EBM論文、函式庫與教學的活躍清單 `awesome` ⭐392 · 📅2026-04
- 🟡 [awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms) — 可重現因果推論與因果ML方法的索引（附綜述論文） `awesome` ⭐3.3k · 📅2025-01
- 🟡 [awesome-neural-ode](https://github.com/Zymrael/awesome-neural-ode) — 涵蓋Neural ODE/SDE/CDE、動力系統、控制與數值解法的交叉領域 `awesome` ⭐1.5k · 📅2024-09
- 🟡 [Awesome-GFlowNets](https://github.com/zdhNarsil/Awesome-GFlowNets) — 彙整GFlowNet基礎論文、應用與教學的核心清單 `awesome` ⭐499 · 📅2024-10
- 🟡 [Awesome-Optimal-Transport-in-Deep-Learning](https://github.com/changwxx/Awesome-Optimal-Transport-in-Deep-Learning) — 彙整深度學習中最佳傳輸的論文、程式碼與資料 `awesome` ⭐350 · 📅2024-05
- 🟡 [Awesome-VQVAE](https://github.com/wenhaochai/Awesome-VQVAE) — Vector Quantized VAE（VQ-VAE）及其應用相關論文與資源集 `awesome` ⭐331 · 📅2025-01
- 🔴 [Awesome-VAEs](https://github.com/matthewvowels1/Awesome-VAEs) — 彙整約900篇VAE、disentanglement、表示學習與生成模型論文 `paper-list` ⭐843 · 📅2021-07
- 🔴 [awesome-bayesian-deep-learning](https://github.com/robi56/awesome-bayesian-deep-learning) — 依年代整理貝氏深度學習論文與學位論文的經典清單 `awesome` ⭐416 · 📅2017-05
- 🔴 [awesome-optimal-transport](https://github.com/kilianFatras/awesome-optimal-transport) — 機器學習用最佳傳輸（OT）的論文、教學、函式庫與書籍集 `awesome` ⭐246 · 📅2021-05
- 🔴 [Awesome-Causal-Inference](https://github.com/matthewvowels1/Awesome-Causal-Inference) — 依年代彙整偏機器學習的因果推論與因果發現論文的文獻清單 `paper-list` ⭐115 · 📅2021-05
- 🔴 [awesome-gaussian-processes](https://github.com/RaulPL/awesome-gaussian-processes) — 彙整學習Gaussian process的書籍、影片、軟體與論文 `awesome` ⭐42 · 📅2021-07
- 🔴 [Awesome-Causal-Discovery](https://github.com/CharonWangg/Awesome-Causal-Discovery) — 聚焦因果發現與因果表示學習的論文與書籍清單 `awesome` ⭐12 · 📅2023-11

## 🏗️ 新架構 (SSM・Mamba・KAN・SNN・量子 ML)

- 🟢 [awesome-kan](https://github.com/mintisan/awesome-kan) — 涵蓋KAN函式庫、實作、論文與教學的事實標準清單 `awesome` ⭐3.2k · 📅2026-06
- 🟢 [Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) — 持續更新頂會與期刊的SNN論文與程式碼 `paper-list` ⭐787 · 📅2026-03
- 🟢 [Mamba_State_Space_Model_Paper_List](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) — Mamba綜述附帶的依應用分類論文清單 `paper-list` ⭐753 · 📅2025-06
- 🟢 [Awesome-Mamba-Collection](https://github.com/XiudingCai/Awesome-Mamba-Collection) — 跨領域涵蓋Mamba論文、教學與實作的代表性精選 `paper-list` ⭐740 · 📅2026-06
- 🟢 [Awesome-state-space-models](https://github.com/radarFudan/Awesome-state-space-models) — 彙整從S4到Mamba的狀態空間模型偏理論論文清單 `paper-list` ⭐621 · 📅2025-11
- 🟢 [Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) — 活躍更新雙曲嵌入、雙曲模型與應用的最新論文 `paper-list` ⭐600 · 📅2026-06
- 🟢 [awesome-snn-conference-paper](https://github.com/AXYZdong/awesome-snn-conference-paper) — 彙整SNN領域頂尖會議與期刊論文及程式碼實作的清單 `paper-list` ⭐454 · 📅2026-05
- 🟢 [Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) — LLM用高效架構（線性注意力、SSM、RWKV等）的大規模綜述 `survey` ⭐409 · 📅2025-11
- 🟢 [Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy) — 追蹤LLM時代神經符號學習最新動向的清單 `paper-list` ⭐307 · 📅2025-06
- 🟢 [Efficient_Attention_Survey](https://github.com/attention-survey/Efficient_Attention_Survey) — 依硬體效率、稀疏、線性等分類高效注意力機制的綜述 `survey` ⭐298 · 📅2025-12
- 🟢 [Awesome_Mamba](https://github.com/xmindflow/Awesome_Mamba) — 對應醫療影像分析SSM全面綜述的清單 `survey` ⭐268 · 📅2025-07
- 🟢 [Awesome-RWKV-in-Vision](https://github.com/Yaziwel/Awesome-RWKV-in-Vision) — 彙整RWKV電腦視覺應用論文的清單 `paper-list` ⭐245 · 📅2025-06
- 🟢 [Awesome-Mamba-in-Vision](https://github.com/vgthengane/Awesome-Mamba-in-Vision) — 彙整電腦視覺領域Mamba論文 `paper-list` ⭐36 · 📅2026-03
- 🟢 [Awesome_Modern_Hopfield_Networks](https://github.com/Event-AHU/Awesome_Modern_Hopfield_Networks) — 現代Hopfield network的論文清單 `paper-list` ⭐27 · 📅2026-03
- 🟢 [Awesome-Linear-Attention-Survey](https://github.com/btzyd/Awesome-Linear-Attention-Survey) — 涵蓋線性注意力演算法、理論、應用與基礎設施的綜述附帶清單 `survey` ⭐12 · 📅2026-02
- 🟢 [KAN-Papers](https://github.com/RamtinMoslemi/KAN-Papers) — 從arXiv擷取的KAN論文完整清單 `paper-list` ⭐6 · 📅2026-05
- 🟡 [awesome-quantum-machine-learning](https://github.com/krishnakumarsekar/awesome-quantum-machine-learning) — 大規模收集QML基礎、演算法、教材與專案 `awesome` ⭐3.6k · 📅2024-05
- 🟡 [awesome-quantum-ml](https://github.com/artix41/awesome-quantum-ml) — 在量子裝置上運行的ML演算法論文與資料精選 `paper-list` ⭐528 · 📅2024-06
- 🟡 [awesome-deeplogic](https://github.com/ccclyu/awesome-deeplogic) — 以NLP應用為主的神經符號AI論文集 `paper-list` ⭐302 · 📅2024-08
- 🟡 [awesome-snn](https://github.com/coderonion/awesome-snn) — Spike-Driven-Transformer等公開SNN實作集 `model` ⭐235 · 📅2024-10
- 📦 [awesome-fast-attention](https://github.com/Separius/awesome-fast-attention) — 高效注意力模組的經典全面清單 `awesome` ⭐1k · 📅2021-08
- 🔴 [awesome-capsule-networks](https://github.com/sekwiatkowski/awesome-capsule-networks) — Dynamic Routing/EM Routing等capsule network主要論文與實作集 `awesome` ⭐976 · 📅2020-02
- 🔴 [awesome-neuromorphic-hw](https://github.com/open-neuromorphic/awesome-neuromorphic-hw) — SNN的ASIC/FPGA等神經形態硬體論文集 `paper-list` ⭐211 · 📅2023-11
- 🔴 [Neural-Symbolic-and-Probabilistic-Logic-Papers](https://github.com/thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers) — 神經符號與機率邏輯論文精選 `paper-list` ⭐137 · 📅2023-09

## 🌱 自監督 / 表徵學習 / 基礎模型

- 🟢 [awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning) — 自監督學習方法的經典精選清單 `awesome` ⭐6.4k · 📅2026-02
- 🟢 [Awesome-Foundation-Models](https://github.com/uncbiag/Awesome-Foundation-Models) — 視覺與語言任務用基礎模型的精選清單 `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-LLM-VLM-Foundation-Models](https://github.com/srebroa/Awesome-LLM-VLM-Foundation-Models) — LLM、VLM與基礎模型的精選清單 `awesome` ⭐6 · 📅2026-02
- 🟡 [awesome-contrastive-self-supervised-learning](https://github.com/asheeshcric/awesome-contrastive-self-supervised-learning) — 對比式自監督學習（SimCLR/VICReg等）論文集 `paper-list` ⭐1.3k · 📅2024-09
- 🟡 [Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) — 時序用自監督學習（SSL4TS）的論文、程式碼與資料集 `paper-list` ⭐379 · 📅2024-04
- 🟡 [awesome-self-supervised-multimodal-learning](https://github.com/ys-zong/awesome-self-supervised-multimodal-learning) — 自監督多模態學習資源（與T-PAMI連動） `paper-list` ⭐278 · 📅2024-08

## 🎓 學習範式 (元學習/遷移/少樣本/OOD/半監督)

- 🟢 [awesome-domain-adaptation](https://github.com/zhaoxin94/awesome-domain-adaptation) — 彙整領域自適應相關論文與程式碼的經典清單 `awesome` ⭐5.4k · 📅2025-12
- 🟢 [awesome-imbalanced-learning](https://github.com/ZhiningLiu1998/awesome-imbalanced-learning) — 總覽類別不平衡/長尾學習的論文、程式碼、框架與函式庫 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) — 涵蓋SFDA/TTBA/TTIA/OTTA等的測試時自適應經典清單 `awesome` ⭐1.3k · 📅2025-11
- 🟢 [Awesome-LongTailed-Learning](https://github.com/Vanint/Awesome-LongTailed-Learning) — 對應TPAMI2023綜述，依類別重平衡/資訊增強/模組改善分類 `survey` ⭐1k · 📅2025-11
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) — 涵蓋OOD偵測與泛化的基準、論文與函式庫 `awesome` ⭐1k · 📅2026-04
- 🟢 [awesome-multi-task-learning](https://github.com/thuml/awesome-multi-task-learning) — 彙整MTL資料集、程式庫與論文（清華THUML） `awesome` ⭐838 · 📅2026-03
- 🟢 [awesome-active-learning](https://github.com/baifanxxx/awesome-active-learning) — 彙整主動學習的論文、工具與基準的清單 `awesome` ⭐802 · 📅2026-03
- 🟢 [Awesome-Multi-Task-Learning](https://github.com/WeihongLi-ac/Awesome-Multi-Task-Learning) — 依時序整理多任務學習最新論文 `paper-list` ⭐378 · 📅2026-03
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/shuolucs/Awesome-Out-Of-Distribution-Detection) — 對應ACM CSUR 2025錄取任務導向OOD偵測綜述的論文清單 `survey` ⭐166 · 📅2026-01
- 🟢 [Awesome-OOD-VLM](https://github.com/AtsuMiyai/Awesome-OOD-VLM) — 對應視覺語言模型時代通用OOD偵測綜述（TMLR2025）的清單 `survey` ⭐102 · 📅2025-06
- 📑 [Awesome-Noisy-Labels](https://github.com/songhwanjun/Awesome-Noisy-Labels) — 對應雜訊標籤學習綜述的論文清單 `survey` ⭐573 · 📅2023-02
- 🟡 [transferlearning](https://github.com/jindongwang/transferlearning) — 遷移學習領域最大規模之一的儲存庫，涵蓋論文、程式碼與資料集 `paper-list` ⭐14.3k · 📅2025-02
- 🟡 [Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise) — 涵蓋雜訊標籤學習論文、程式碼與綜述的最大規模清單 `awesome` ⭐2.7k · 📅2025-05
- 🟡 [awesome-semi-supervised-learning](https://github.com/yassouali/awesome-semi-supervised-learning) — 依CV/NLP/生成/圖整理半監督學習論文與方法 `awesome` ⭐1.9k · 📅2024-05
- 🟡 [awesome_OpenSetRecognition_list](https://github.com/gary23ai/awesome_OpenSetRecognition_list) — 彙整開放集辨識、OOD與開放世界辨識論文的經典清單 `paper-list` ⭐1.2k · 📅2024-03
- 🟡 [awesome-source-free-test-time-adaptation](https://github.com/YuejiangLIU/awesome-source-free-test-time-adaptation) — 測試時自適應、測試時訓練與source-free領域自適應論文清單 `paper-list` ⭐549 · 📅2024-06
- 🟡 [Awesome-Domain-Generalization](https://github.com/junkunyuan/Awesome-Domain-Generalization) — 彙整領域泛化的論文、程式碼與資料集的清單 `awesome` ⭐537 · 📅2025-04
- 🔴 [Awesome-Meta-Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning) — 涵蓋元學習論文、程式碼、書籍、影片與資料集的經典清單 `awesome` ⭐1.6k · 📅2020-11
- 🔴 [awesome-zero-shot-learning](https://github.com/sbharadwajj/awesome-zero-shot-learning) — 彙整零樣本學習論文、程式碼與資源的精選 `awesome` ⭐933 · 📅2021-07
- 🔴 [awesome-curriculum-learning](https://github.com/Openning07/awesome-curriculum-learning) — 依偵測/分割/分類/遷移/RL為課程學習論文加標籤 `awesome` ⭐248 · 📅2022-08
- 🔴 [Awesome-Weak-Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) — 程式化/規則式弱監督學習的論文與資源集 `awesome` ⭐195 · 📅2023-03
- 🔴 [awesome-distribution-shift](https://github.com/weitianxin/awesome-distribution-shift) — 分布偏移與基準的論文集 `awesome` ⭐128 · 📅2023-08
- 🔴 [awesome-few-shot-learning](https://github.com/indussky8/awesome-few-shot-learning) — 含標準資料集比較結果的few-shot學習論文精選 `paper-list` ⭐126 · 📅2021-10
- 🔴 [Awesome-Zero-Shot-Learning](https://github.com/WilliamYi96/Awesome-Zero-Shot-Learning) — 彙整零樣本學習最新論文與資料集進展的清單 `paper-list` ⭐85 · 📅2022-08
- 🔴 [Awesome-Failure-Detection](https://github.com/Impression2805/Awesome-Failure-Detection) — 整合處理OOD偵測與誤分類偵測（failure detection）的論文清單 `paper-list` ⭐53 · 📅2023-10
- 🔴 [Awesome-compositional-zero-shot-learning](https://github.com/uqzhichen/Awesome-compositional-zero-shot-learning) — 專注於組合式零樣本學習（屬性與物件組合泛化）的論文清單 `paper-list` ⭐11 · 📅2022-07
- 🔴 [awsome-domain-adaptation](https://github.com/cmhungsteve/awsome-domain-adaptation) — 分類整理領域自適應相關論文且廣被參考的一覽 `awesome` ⭐1 · 📅2019-09

## 👁️ 電腦視覺 (Computer Vision)

- 🟢 [CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) — 大規模彙整CVPR 2026論文與開源專案（經典） `paper-list` ⭐22.7k · 📅2026-03
- 🟢 [awesome-industrial-anomaly-detection](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) — 工業影像異常/瑕疵偵測的論文與資料集集（非常活躍） `awesome` ⭐3.6k · 📅2026-06
- 🟢 [awesome-hand-pose-estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation) — 手部姿態估計/追蹤（含3D）的經典清單 `awesome` ⭐3.4k · 📅2025-12
- 🟢 [Awesome-Super-Resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) — 彙整超解析度相關論文、資料與儲存庫 `awesome` ⭐3.1k · 📅2026-06
- 🟢 [Awesome-Deblurring](https://github.com/subeeshvasu/Awesome-Deblurring) — 彙整影像與影片去模糊資源的清單 `awesome` ⭐2.9k · 📅2025-06
- 🟢 [ICCV2025-Papers-with-Code](https://github.com/amusi/ICCV2025-Papers-with-Code) — ICCV 2025論文與開源專案集 `paper-list` ⭐2.9k · 📅2025-07
- 🟢 [Awesome-Crowd-Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) — 群眾計數的經典清單，附資料集與程式碼且活躍 `awesome` ⭐2.6k · 📅2026-01
- 🟢 [awesome-multiple-object-tracking](https://github.com/luanshiyinyang/awesome-multiple-object-tracking) — 整理MOT綜述論文、依年份分類的演算法與資料集 `awesome` ⭐1.5k · 📅2025-10
- 🟢 [awesome-grounding](https://github.com/TheShadow29/awesome-grounding) — 影像/影片/3D的指代表達與grounding論文集 `paper-list` ⭐1.1k · 📅2025-09
- 🟢 [SAM4MIS](https://github.com/YichiZhang98/SAM4MIS) — SAM應用於醫療影像分割的論文與OSS摘要 `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary](https://github.com/jianzongwu/Awesome-Open-Vocabulary) — TPAMI 2024《Towards Open Vocabulary Learning: A Survey》的companion `survey` ⭐997 · 📅2026-05
- 🟢 [ICCV-2023-25-Papers](https://github.com/DmitryRyumin/ICCV-2023-25-Papers) — ICCV 2023-2025錄取論文精選集 `paper-list` ⭐968 · 📅2025-11
- 🟢 [top-cvpr-2025-papers](https://github.com/SkalskiP/top-cvpr-2025-papers) — 精選CVPR 2025重點論文的集合 `paper-list` ⭐886 · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary-Semantic-Segmentation](https://github.com/Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation) — 開放詞彙/零樣本語意分割論文清單 `paper-list` ⭐878 · 📅2026-05
- 🟢 [Awesome-Referring-Image-Segmentation](https://github.com/MarkMoHR/Awesome-Referring-Image-Segmentation) — 指代影像分割的論文與資料集集 `awesome` ⭐825 · 📅2026-01
- 🟢 [Awesome-Skeleton-based-Action-Recognition](https://github.com/firework8/Awesome-Skeleton-based-Action-Recognition) — 每月更新的骨架式動作辨識論文清單 `paper-list` ⭐713 · 📅2026-06
- 🟢 [HOI-Learning-List](https://github.com/DirtyHarryLYL/HOI-Learning-List) — 涵蓋資料集、基準與論文的HOI學習清單（活躍） `awesome` ⭐711 · 📅2025-10
- 🟢 [Awesome-Scene-Graph-Generation](https://github.com/ChocoWu/Awesome-Scene-Graph-Generation) — 涵蓋LLM/非LLM方法、2D/3D/影片的活躍場景圖生成清單 `awesome` ⭐677 · 📅2026-06
- 🟢 [Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC](https://github.com/Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC) — 彙整主要會議AIGC相關論文與程式碼 `paper-list` ⭐667 · 📅2026-06
- 🟢 [Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation](https://github.com/zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation) — 橫跨收集時序動作偵測、提案生成與弱監督 `paper-list` ⭐589 · 📅2026-05
- 🟢 [Awesome-Gaze-Estimation](https://github.com/cvlab-uob/Awesome-Gaze-Estimation) — 視線估計論文的精選清單 `awesome` ⭐536 · 📅2025-06
- 🟢 [Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization) — 影像和諧化的論文、程式碼與資源集（活躍） `awesome` ⭐533 · 📅2026-02
- 🟢 [Awesome-Video-Object-Segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation) — VOS最新論文、資料集與專案集 `awesome` ⭐502 · 📅2026-06
- 🟢 [Awesome-Face-Restoration](https://github.com/TaoWangzj/Awesome-Face-Restoration) — 彙整人臉復原方法論文與儲存庫的清單 `paper-list` ⭐493 · 📅2026-03
- 🟢 [awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) — 偽裝/隱蔽物件偵測的精選資源集 `awesome` ⭐477 · 📅2025-12
- 🟢 [Awesome-Object-Pose-Estimation](https://github.com/CNJianLiu/Awesome-Object-Pose-Estimation) — IJCV2026綜述《Deep Learning-Based Object Pose Estimation》專案頁 `survey` ⭐425 · 📅2026-01
- 🟢 [Awesome_Long_Form_Video_Understanding](https://github.com/ttengwang/Awesome_Long_Form_Video_Understanding) — 專注於長片的論文與資料集集 `paper-list` ⭐378 · 📅2025-10
- 🟢 [awesome-described-object-detection](https://github.com/Charles-Xie/awesome-described-object-detection) — Described/Open-Vocabulary物件偵測與指代表達理解論文集 `paper-list` ⭐353 · 📅2025-11
- 🟢 [awesome-concealed-object-segmentation](https://github.com/ChunmingHe/awesome-concealed-object-segmentation) — 隱蔽物件分割的資源集 `awesome` ⭐343 · 📅2026-01
- 🟢 [Awesome-Visual-Grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) — TPAMI 2025綜述，涵蓋REC/phrase grounding/grounding MLLM（活躍） `survey` ⭐317 · 📅2025-11
- 🟢 [Awesome-3D-Visual-Grounding](https://github.com/liudaizong/Awesome-3D-Visual-Grounding) — 專注於3D視覺grounding論文（活躍） `paper-list` ⭐281 · 📅2026-01
- 🟢 [Awesome-Multimodal-Referring-Segmentation](https://github.com/henghuiding/Awesome-Multimodal-Referring-Segmentation) — 多模態指代分割清單 `awesome` ⭐249 · 📅2026-05
- 🟢 [awesome-micro-expression-recognition](https://github.com/Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition) — 微表情（micro-expression）辨識、偵測與spotting的論文集 `paper-list` ⭐180 · 📅2025-08
- 🟢 [awesome-video-self-supervised-learning](https://github.com/Malitha123/awesome-video-self-supervised-learning) — 影片自監督學習方法論文集 `paper-list` ⭐172 · 📅2026-03
- 🟢 [Awesome-SAM2](https://github.com/GuoleiSun/Awesome-SAM2) — 影像與影片用SAM2的論文與程式碼集 `paper-list` ⭐151 · 📅2025-10
- 🟢 [awesome-3d-anomaly-detection](https://github.com/M-3LAB/awesome-3d-anomaly-detection) — 點雲與多模態3D異常偵測綜述儲存庫 `awesome` ⭐120 · 📅2026-06
- 🟢 [Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference) — 頂尖國際會議刊載的事件/脈衝相機論文集 `paper-list` ⭐119 · 📅2026-04
- 🟢 [awesome-3D-scene-graphs](https://github.com/DennisRotondi/awesome-3D-scene-graphs) — 含機器人應用的3D場景圖專門清單 `awesome` ⭐109 · 📅2026-06
- 🟢 [TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding](https://github.com/iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding) — 以MLLM進行影片時序grounding（VTG-LLM）的最新論文、程式碼與資料集 `paper-list` ⭐93 · 📅2026-06
- 🟢 [Awesome-MultiModal-Visual-Object-Tracking](https://github.com/Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking) — RGBT/RGBD/RGBE等多模態視覺物件追蹤綜述 `survey` ⭐84 · 📅2026-04
- 🟢 [Awesome-Temporal-Video-Grounding](https://github.com/Tangkfan/Awesome-Temporal-Video-Grounding) — VMR/TVG/TSGV的論文清單 `paper-list` ⭐41 · 📅2025-12
- 🟢 [awesome-captioning-evaluation](https://github.com/aimagelab/awesome-captioning-evaluation) — MLLM時代影像描述評估相關論文集 `paper-list` ⭐35 · 📅2025-11
- 📑 [Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) — IJCV 2023綜述，體系化LiDAR/相機/多模態3D偵測 `survey` ⭐609 · 📅2023-05
- 📑 [Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) — 深度影像復原/增強中先驗分布的綜述 `survey` ⭐87 · 📅2025-05
- 📑 [360_Survey](https://github.com/vlislab22/360_Survey) — 全方位視覺（深度估計、3D重建、分割）的全面綜述 `survey` ⭐23 · 📅2024-12
- 🟡 [Awesome-Transformer-Attention](https://github.com/cmhungsteve/Awesome-Transformer-Attention) — 涵蓋ViT/Attention極為全面的論文清單 `paper-list` ⭐5k · 📅2024-07
- 🟡 [Awesome-Visual-Transformer](https://github.com/dk-liang/Awesome-Visual-Transformer) — 彙整CV用Transformer論文的集合 `awesome` ⭐3.6k · 📅2025-01
- 🟡 [awesome-ocr](https://github.com/kba/awesome-ocr) — OCR與手寫文字辨識（HTR）的軟體、函式庫與文獻集（歷史文件數位化核心） `awesome` ⭐3.1k · 📅2024-07
- 🟡 [ECCV2024-Papers-with-Code](https://github.com/amusi/ECCV2024-Papers-with-Code) — ECCV 2024論文與開源專案集 `paper-list` ⭐2.3k · 📅2024-08
- 🟡 [SOTA-MedSeg](https://github.com/JunMa11/SOTA-MedSeg) — 基於各類挑戰賽的SOTA醫療影像分割方法集 `paper-list` ⭐1.7k · 📅2023-12
- 🟡 [Awesome-Edge-Detection-Papers](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers) — 邊緣/輪廓/邊界偵測論文與工具箱集 `paper-list` ⭐1.6k · 📅2024-12
- 🟡 [Awesome-person-re-identification](https://github.com/bismex/Awesome-person-re-identification) — 涵蓋監督/非監督/跨模態ReID的大規模論文清單 `awesome` ⭐1.3k · 📅2024-06
- 🟡 [awesome-point-cloud-registration](https://github.com/XuyangBai/awesome-point-cloud-registration) — 依匹配策略整理的點雲配準論文集 `paper-list` ⭐948 · 📅2024-07
- 🟡 [Awesome-Computer-Vision-Paper-List](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List) — 可跨頂會檢索錄取論文的論文清單 `paper-list` ⭐760 · 📅2024-04
- 🟡 [Awesome-Optical-Flow](https://github.com/hzwer/Awesome-Optical-Flow) — 光流與相關研究的論文清單 `awesome` ⭐650 · 📅2024-11
- 🟡 [awesome-diffusion-models-in-low-level-vision](https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision) — 超解析度/修復等低階視覺用diffusion model論文集 `paper-list` ⭐555 · 📅2025-02
- 🟡 [CVPR-2023-24-Papers](https://github.com/DmitryRyumin/CVPR-2023-24-Papers) — 依主題整理CVPR 2023/2024錄取論文 `paper-list` ⭐451 · 📅2024-07
- 🟡 [awesome-ocr-resources](https://github.com/ZumingHuang/awesome-ocr-resources) — 彙整OCR論文與資料集的資源集 `awesome` ⭐431 · 📅2025-01
- 🟡 [Awesome-Segment-Anything](https://github.com/Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything) — Segment Anything Model（SAM）相關論文與專案集 `paper-list` ⭐371 · 📅2024-12
- 🟡 [awesome-temporal-action-segmentation](https://github.com/nus-cvml/awesome-temporal-action-segmentation) — 時序動作分割的論文與資料集集（活躍） `paper-list` ⭐250 · 📅2024-04
- 🟡 [Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — 聚焦於2020年後單眼深度估計論文的清單 `paper-list` ⭐209 · 📅2024-10
- 🟡 [Awesome-Gait-Recognition](https://github.com/BNU-IVC/Awesome-Gait-Recognition) — 步態辨識的論文與資料集集（收錄CVPR'25等，活躍） `paper-list` ⭐187 · 📅2025-05
- 🟡 [awesome-salient-object-detection](https://github.com/visionxiang/awesome-salient-object-detection) — 含RGB-D等的顯著性物件偵測資源集 `awesome` ⭐147 · 📅2024-09
- 🟡 [WACV-2024-Papers](https://github.com/DmitryRyumin/WACV-2024-Papers) — 系統性整理WACV 2024論文的集合 `paper-list` ⭐97 · 📅2024-09
- 🟡 [awesome-human-visual-attention](https://github.com/aimagelab/awesome-human-visual-attention) — saliency、scanpath、視線預測與視覺注意力的論文/資源集 `paper-list` ⭐66 · 📅2025-05
- 📚 [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) — 涵蓋CV全領域書籍、講義、論文、工具與資料集的經典清單 `awesome` ⭐23.3k · 📅2024-05
- 📚 [really-awesome-semantic-segmentation](https://github.com/nightrome/really-awesome-semantic-segmentation) — 語意分割論文清單（2018年停止更新） `paper-list` ⭐404 · 📅2018-03
- 🔴 [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) — 語意分割的經典資源集 `awesome` ⭐10.8k · 📅2021-05
- 🔴 [awesome-object-detection](https://github.com/amusi/awesome-object-detection) — 彙整R-CNN系列、YOLO、SSD等物件偵測論文與實作的經典清單 `awesome` ⭐7.5k · 📅2022-12
- 🔴 [awesome-Face_Recognition](https://github.com/ChanChiChoi/awesome-Face_Recognition) — 涵蓋人臉偵測/辨識/重建/生成等的大規模論文集 `paper-list` ⭐4.7k · 📅2023-02
- 🔴 [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition) — 涵蓋動作辨識與相關領域資源的經典清單 `awesome` ⭐4k · 📅2023-05
- 🔴 [awesome-image-classification](https://github.com/weiaicunzai/awesome-image-classification) — 2014年以後的深度學習影像分類論文與實作清單 `paper-list` ⭐3.1k · 📅2022-04
- 🔴 [awesome-deep-text-detection-recognition](https://github.com/hwalsuklee/awesome-deep-text-detection-recognition) — 整理基於深度學習的文字偵測/辨識論文 `paper-list` ⭐2.5k · 📅2021-08
- 🔴 [awesome-human-pose-estimation](https://github.com/cbsudux/awesome-human-pose-estimation) — 人體姿態估計論文與資源集 `awesome` ⭐2.5k · 📅2022-10
- 🔴 [awesome-cbir-papers](https://github.com/willard-yuan/awesome-cbir-papers) — 經典與代表性的內容式影像檢索（CBIR）論文集 `paper-list` ⭐1.8k · 📅2023-10
- 🔴 [multi-object-tracking-paper-list](https://github.com/SpyderXu/multi-object-tracking-paper-list) — 多物件追蹤的論文清單與原始碼集 `paper-list` ⭐1.7k · 📅2020-04
- 🔴 [Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) — 專注於場景文字定位與辨識的資源集 `awesome` ⭐1.7k · 📅2018-07
- 🔴 [awesome-tiny-object-detection](https://github.com/kuanhungchen/awesome-tiny-object-detection) — Tiny Object Detection（微小物件偵測）論文與資源集 `paper-list` ⭐1.6k · 📅2023-10
- 🔴 [awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation) — 2D/3D人體姿態估計相關論文集 `paper-list` ⭐1.4k · 📅2020-08
- 🔴 [awesome-image-captioning](https://github.com/zhjohnchan/awesome-image-captioning) — 依年份整理的影像描述與相關領域資源 `awesome` ⭐1.1k · 📅2023-03
- 🔴 [activityrecognition](https://github.com/jindongwang/activityrecognition) — 動作辨識（activity recognition）的資料、程式碼與資料集集 `paper-list` ⭐929 · 📅2019-08
- 🔴 [awesome-face](https://github.com/polarisZhao/awesome-face) — 人臉相關演算法、資料集與論文的精選集 `awesome` ⭐916 · 📅2019-08
- 🔴 [Awesome-Face-Forgery-Generation-and-Detection](https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection) — 人臉偽造生成與偵測相關論文與程式碼集 `paper-list` ⭐780 · 📅2022-11
- 🔴 [Awesome-Temporal-Action-Localization](https://github.com/Alvin-Zeng/Awesome-Temporal-Action-Localization) — temporal action localization/detection/proposal論文與基準彙整 `paper-list` ⭐589 · 📅2022-09
- 🔴 [awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) — 實用metric learning及其應用的精選 `awesome` ⭐520 · 📅2023-04
- 🔴 [Awesome-Image-Matting](https://github.com/wchstrife/Awesome-Image-Matting) — 基於深度學習的matting論文與程式碼精選清單 `awesome` ⭐439 · 📅2023-11
- 🔴 [Awesome-Visual-Captioning](https://github.com/forence/Awesome-Visual-Captioning) — 聚焦影像/影片描述與Seq2Seq學習的論文集 `paper-list` ⭐410 · 📅2022-11
- 🔴 [Awesome-3D-Detectors](https://github.com/Hub-Tian/Awesome-3D-Detectors) — 以LiDAR為主的3D偵測方法論文與程式碼集 `paper-list` ⭐398 · 📅2022-02
- 🔴 [Awesome-Super-Resolution](https://github.com/ptkin/Awesome-Super-Resolution) — 超解析度資源精選集 `awesome` ⭐386 · 📅2019-09
- 🔴 [Awesome-FAS](https://github.com/RizhaoCai/Awesome-FAS) — 人臉防偽/PAD/liveness論文的全面集合 `paper-list` ⭐383 · 📅2022-08
- 🔴 [awesome-depth](https://github.com/scott89/awesome-depth) — 彙整深度估計出版物的精選清單 `paper-list` ⭐337 · 📅2020-09
- 🔴 [Awesome-generalizable-6D-object-pose](https://github.com/liuyuan-pal/Awesome-generalizable-6D-object-pose) — 可泛化6DoF物件姿態估計的最新論文集 `paper-list` ⭐328 · 📅2023-04
- 🔴 [Awesome-Vision-Transformer-Collection](https://github.com/GuanRunwei/Awesome-Vision-Transformer-Collection) — 彙整ViT衍生與下游任務的集合 `awesome` ⭐256 · 📅2022-07
- 🔴 [Awesome-Fine-grained-Visual-Classification](https://github.com/haoweiz23/Awesome-Fine-grained-Visual-Classification) — 細粒度視覺分類（FGVC）論文集 `paper-list` ⭐241 · 📅2023-09
- 🔴 [Awesome-Person-Re-Identification](https://github.com/FDU-VTS/Awesome-Person-Re-Identification) — 含資料集與綜述的人物再辨識清單 `awesome` ⭐205 · 📅2021-12
- 🔴 [6d-object-pose-estimation](https://github.com/GeorgeDu/6d-object-pose-estimation) — 6D物件姿態估計的論文與程式碼彙整 `paper-list` ⭐205 · 📅2023-06
- 🔴 [awesome-optical-flow-algorithm](https://github.com/antran89/awesome-optical-flow-algorithm) — 從經典方法到RAFT等深度學習的光流演算法集 `awesome` ⭐160 · 📅2022-10
- 🔴 [awesome-video-understanding](https://github.com/sujiongming/awesome-video-understanding) — 影片分類、動作辨識與影片資料集的資源集 `awesome` ⭐143 · 📅2017-12
- 🔴 [Awesome-Video-Captioning](https://github.com/tgc1997/Awesome-Video-Captioning) — 影片描述生成的論文集 `paper-list` ⭐121 · 📅2021-01
- 🔴 [awesome-360-vision](https://github.com/hsientzucheng/awesome-360-vision) — 360度視覺整體的論文集 `paper-list` ⭐121 · 📅2019-01
- 🔴 [Awesome-3D-Semantic-Segmentation](https://github.com/vvincenttttt/Awesome-3D-Semantic-Segmentation) — 3D語意分割的論文與程式碼集 `paper-list` ⭐75 · 📅2022-09
- 🔴 [Awesome-Events-Deep-Learning](https://github.com/vlislab2022/Awesome-Events-Deep-Learning) — 事件相機用深度學習資源集 `awesome` ⭐62 · 📅2023-09
- 🔴 [awesome-vqa-latest](https://github.com/Taaccoo/awesome-vqa-latest) — 持續更新VQA論文的閱讀清單 `paper-list` ⭐52 · 📅2022-08
- 🔴 [awesome-rec](https://github.com/daqingliu/awesome-rec) — Referring Expression Comprehension（REC）專用論文清單 `paper-list` ⭐47 · 📅2021-05
- 🔴 [awesome-image-retrieval-papers](https://github.com/lgbwust/awesome-image-retrieval-papers) — 影像檢索論文與實作的全面集合 `paper-list` ⭐36 · 📅2018-12
- 🔴 [TSGV-Learning-List](https://github.com/Huntersxsx/TSGV-Learning-List) — TSGV/NLVL/VMR的相關研究彙整 `paper-list` ⭐31 · 📅2022-03
- 🔴 [awesome-computer-vision-papers](https://github.com/tzxiang/awesome-computer-vision-papers) — CV與深度學習相關論文與資源清單 `awesome` ⭐26 · 📅2020-09
- 🔴 [awesome-hyperspectral-image-classification](https://github.com/immortal13/awesome-hyperspectral-image-classification) — 超光譜影像分類的論文與程式碼集 `paper-list` ⭐20 · 📅2023-07
- 🔴 [Awesome-image-captioning](https://github.com/luo3300612/Awesome-image-captioning) — ICCV/ECCV/CVPR等的影像描述論文清單 `paper-list` ⭐8 · 📅2019-09
- 🔴 [Awesome-3D-Human-Pose-Estimation](https://github.com/bsridatta/Awesome-3D-Human-Pose-Estimation) — 專注於3D人體姿態估計的論文集 `paper-list` ⭐5 · 📅2021-04
- 🔴 [Awesome-Human-Object-Interaction-Detection](https://github.com/KainingYing/Awesome-Human-Object-Interaction-Detection) — 依會議與年份分類的HOI偵測論文集 `paper-list` ⭐3 · 📅2021-08

## 🎨 電腦圖學 / 3D / 渲染

- 🟢 [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) — 彙整3DGS論文、實作、檢視器與工具的全面清單 `awesome` ⭐8.7k · 📅2026-06
- 🟢 [awesome-neural-rendering](https://github.com/weihaox/awesome-neural-rendering) — 神經渲染與可微渲染的資料集 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — 運用隱式表示、NeRF與3DGS的SLAM論文集 `paper-list` ⭐2k · 📅2026-06
- 🟢 [awesome-digital-human](https://github.com/weihaox/awesome-digital-human) — 2D/3D/4D人體建模與虛擬人生成綜合集 `awesome` ⭐2k · 📅2026-04
- 🟢 [Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis) — talking face合成的廣泛資源集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion) — 3D生成用diffusion model論文集 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing) — 點雲處理的函式庫、軟體與資料集 `awesome` ⭐799 · 📅2025-11
- 🟢 [awesome-dust3r](https://github.com/ruili3/awesome-dust3r) — DUSt3R系列幾何基礎模型論文與資源追蹤 `model` ⭐797 · 📅2025-11
- 🟢 [Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D) — AIGC 3D（生成、紋理、材質）論文集 `awesome` ⭐778 · 📅2026-05
- 🟢 [awesome-ray-tracing](https://github.com/dannyfritz/awesome-ray-tracing) — 光線追蹤的論文、課程與實作清單 `awesome` ⭐659 · 📅2025-10
- 🟢 [Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — Text-to-3D/Diffusion-to-3D研究精選 `paper-list` ⭐591 · 📅2026-06
- 🟢 [awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) — 3D繪圖函式庫精選集 `awesome` ⭐525 · 📅2026-05
- 🟢 [Awesome-4D-Spatial-Intelligence](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) — 從影片重建4D空間智慧的綜述 `survey` ⭐507 · 📅2026-06
- 🟢 [awesome-simulation](https://github.com/Housz/awesome-simulation) — CG物理模擬資源整理 `awesome` ⭐389 · 📅2026-06
- 🟢 [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) — 每日從arXiv自動更新的3DGS論文追蹤 `paper-list` ⭐297 · 📅2026-06
- 🟢 [Awesome-Transformer-based-SLAM](https://github.com/KwanWaiPang/Awesome-Transformer-based-SLAM) — Transformer式SLAM的綜述用論文集 `survey` ⭐271 · 📅2026-06
- 🟢 [Awesome-3DGS-SLAM](https://github.com/KwanWaiPang/Awesome-3DGS-SLAM) — 3DGS SLAM綜述用論文集 `survey` ⭐267 · 📅2026-02
- 🟢 [Awesome-Learning-based-VO-VIO](https://github.com/KwanWaiPang/Awesome-Learning-based-VO-VIO) — 學習式視覺里程計（VO/VIO）的綜述用論文集 `survey` ⭐198 · 📅2026-04
- 🟢 [awesome-geometry-processing](https://github.com/zishun/awesome-geometry-processing) — 幾何處理的函式庫、工具與資料集 `awesome` ⭐174 · 📅2026-03
- 🟢 [Awesome-SIGGRAPH-Computational-Optics](https://github.com/zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics) — SIGGRAPH刊載計算光學論文的閱讀清單 `paper-list` ⭐106 · 📅2026-06
- 🟢 [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation) — 3D重建與生成的論文與資料集集 `paper-list` ⭐80 · 📅2026-03
- 🟢 [awesome-dynamic-NeRF](https://github.com/pdaicode/awesome-dynamic-NeRF) — 動態場景用NeRF的論文集 `paper-list` ⭐68 · 📅2026-04
- 🟢 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey) — 四邊形網格化相關論文、程式碼與專案集 `survey` ⭐41 · 📅2026-06
- 🟢 [Awesome-Diffusion-based-SLAM](https://github.com/KwanWaiPang/Awesome-Diffusion-based-SLAM) — diffusion model式SLAM的綜述用論文集 `survey` ⭐34 · 📅2026-05
- 🟢 [awesome-brep-reconstruction](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) — B-rep（邊界表示）重建的論文與OSS專案集，定期更新 `survey` ⭐29 · 📅2026-01
- 🟢 [Awesome-Event-based-SLAM](https://github.com/KwanWaiPang/Awesome-Event-based-SLAM) — 事件式SLAM的綜述用論文集 `survey` ⭐22 · 📅2026-01
- 🟢 [offset-mesh-survey](https://github.com/Bigger-and-Stronger/offset-mesh-survey) — 偏移網格生成相關論文、專案與程式碼的持續更新綜述 `survey` ⭐13 · 📅2026-06
- 🟢 [awesome-3d-medial-axis](https://github.com/Bigger-and-Stronger/awesome-3d-medial-axis) — 中軸（medial axis）/骨架及其應用的論文與OSS集，定期更新 `survey` ⭐5 · 📅2025-10
- 🟢 [direction-field-survey](https://github.com/Bigger-and-Stronger/direction-field-survey) — 方向場（direction field）相關論文、專案與程式碼的持續更新綜述 `survey` ⭐4 · 📅2026-06
- 🟢 [parameterization-survey](https://github.com/Bigger-and-Stronger/parameterization-survey) — 網格參數化相關論文、專案與程式碼的持續更新綜述 `survey` ⭐2 · 📅2026-06
- 📑 [Gen3D](https://github.com/weihaox/Gen3D) — 深度生成式3D-aware影像合成綜述（CSUR 2023） `survey` ⭐164 · 📅2025-02
- 📑 [boundary-layer-generation-survey](https://github.com/Bigger-and-Stronger/boundary-layer-generation-survey) — 邊界層網格生成相關論文、專案與程式碼的持續更新綜述 `survey` ⭐3 · 📅2025-02
- 🟡 [3D-Machine-Learning](https://github.com/timzhang642/3D-Machine-Learning) — 3D機器學習（點雲/網格/體素/SDF等）的資源儲存庫 `awesome` ⭐10.2k · 📅2024-07
- 🟡 [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) — Neural Radiance Fields論文的經典精選清單 `awesome` ⭐6.8k · 📅2025-01
- 🟡 [awesome-implicit-representations](https://github.com/vsitzmann/awesome-implicit-representations) — DeepSDF等隱式神經表示的資料集 `awesome` ⭐2.6k · 📅2024-02
- 🟡 [awesome-point-cloud-analysis-2023](https://github.com/NUAAXQ/awesome-point-cloud-analysis-2023) — 每日更新2017年後點雲分析論文的清單 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-Talking-Face](https://github.com/JosephPai/Awesome-Talking-Face) — 專注於talking face的精選集 `awesome` ⭐1.5k · 📅2024-12
- 🟡 [awesome-3d-reconstruction-papers](https://github.com/bluestyle97/awesome-3d-reconstruction-papers) — 深度學習時代的3D重建論文集 `paper-list` ⭐910 · 📅2023-12
- 🟡 [awesome-taichi](https://github.com/taichi-dev/awesome-taichi) — 以Taichi製作的模擬（流體、布料等）應用集 `awesome` ⭐683 · 📅2024-06
- 🟡 [awesome-3dbody-papers](https://github.com/3DFaceBody/awesome-3dbody-papers) — 3D人體（SMPL等）論文集 `paper-list` ⭐661 · 📅2024-01
- 🟡 [awesome-4d-generation](https://github.com/cwchenwang/awesome-4d-generation) — 4D生成（text-to-4D等）論文清單 `paper-list` ⭐331 · 📅2024-10
- 🟡 [Awesome-Avatars](https://github.com/pansanity666/Awesome-Avatars) — 人體虛擬人的生成、重建與編輯最新進展 `paper-list` ⭐276 · 📅2024-04
- 🟡 [Awesome-Inverse-Rendering](https://github.com/ingra14m/Awesome-Inverse-Rendering) — 基於neural field的逆渲染論文集 `paper-list` ⭐259 · 📅2024-12
- 🟡 [Awesome-InverseRendering](https://github.com/tkuri/Awesome-InverseRendering) — 本質分解與逆渲染論文清單 `paper-list` ⭐234 · 📅2025-04
- 🟡 [awesome-3dgs](https://github.com/pdaicode/awesome-3dgs) — 3DGS相關論文精選集 `paper-list` ⭐123 · 📅2024-08
- 🟡 [awesome-avatar](https://github.com/Jason-cs18/awesome-avatar) — talking-face/talking-body相關資源集 `awesome` ⭐61 · 📅2024-11
- 🟡 [Awesome-3D-Human-Motion-Generation](https://github.com/Run542968/Awesome-3D-Human-Motion-Generation) — 以Text-to-Motion為主的人體動作生成論文集 `paper-list` ⭐25 · 📅2024-07
- 🟡 [awesome-dynamic-scene-representations](https://github.com/yklcs/awesome-dynamic-scene-representations) — 動態場景表示的資料集 `paper-list` ⭐8 · 📅2024-04
- 🟡 [awesome-visualization](https://github.com/Bigger-and-Stronger/awesome-visualization) — 記錄CG相關資料視覺化方法與渲染案例的儲存庫 `awesome` ⭐1 · 📅2025-03
- 🔴 [awesome_3DReconstruction_list](https://github.com/openMVG/awesome_3DReconstruction_list) — 影像3D重建的經典論文與資料集 `awesome` ⭐4.4k · 📅2021-10
- 🔴 [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis) — 點雲分析與處理相關論文與資料集清單 `awesome` ⭐4.2k · 📅2023-05
- 🔴 [awesome-visual-slam](https://github.com/tzutalin/awesome-visual-slam) — 視覺SLAM/視覺里程計的OSS與論文集 `awesome` ⭐2.4k · 📅2022-05
- 🔴 [awesome-slam](https://github.com/kanster/awesome-slam) — SLAM的教學、專案與社群集 `awesome` ⭐1.7k · 📅2020-07
- 🔴 [awesome-3D-generation](https://github.com/justimyhxu/awesome-3D-generation) — 3D生成論文精選清單 `awesome` ⭐1.2k · 📅2023-03
- 🔴 [awesome-graphics](https://github.com/ericjang/awesome-graphics) — CG教學與論文的綜合清單 `awesome` ⭐1.1k · 📅2020-02
- 🔴 [Awesome-SLAM](https://github.com/SilenceOverflow/Awesome-SLAM) — 持續更新的SLAM論文清單 `paper-list` ⭐1.1k · 📅2023-10
- 🔴 [3D-Reconstruction-with-Deep-Learning-Methods](https://github.com/natowi/3D-Reconstruction-with-Deep-Learning-Methods) — 以深度學習進行3D重建的專案一覽 `paper-list` ⭐1k · 📅2023-05
- 🔴 [awesome-computer-graphics](https://github.com/luisdnsantos/awesome-computer-graphics) — CG學習用書籍、課程與資料集 `awesome` ⭐1k · 📅2021-07
- 🔴 [Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) — 基於學習的MVS論文清單 `paper-list` ⭐634 · 📅2023-11
- 🔴 [Awsome_Deep_Geometry_Learning](https://github.com/subeeshvasu/Awsome_Deep_Geometry_Learning) — 3D形狀深度學習解決方案資料集 `paper-list` ⭐361 · 📅2021-08
- 🔴 [awesome-mvs](https://github.com/krahets/awesome-mvs) — MVS的教學、論文與軟體集 `awesome` ⭐277 · 📅2022-08
- 🔴 [awesome-pbr](https://github.com/neil3d/awesome-pbr) — PBR的資料、簡報與論文綜合集 `awesome` ⭐118 · 📅2021-01
- 🔴 [Awesome-BRDF](https://github.com/tkuri/Awesome-BRDF) — 依表示方式整理BRDF表示相關論文 `paper-list` ⭐32 · 📅2021-06
- 🔴 [awesome-Implicit-NeRF-SLAM](https://github.com/Taeyoung96/awesome-Implicit-NeRF-SLAM) — 隱式表示與NeRF的SLAM/機器人應用論文集 `paper-list` ⭐13 · 📅2023-11
- 🔴 [texture-synthesis-papers](https://github.com/lzhbrian/texture-synthesis-papers) — 紋理合成論文（附程式碼）集 `paper-list` ⭐4 · 📅2019-03

## 🖌️ 低階影像處理 / 復原 / 壓縮

- 🟢 [awesome-low-light-image-enhancement](https://github.com/zhihongz/awesome-low-light-image-enhancement) — 涵蓋低光影像增強資料集/方法/論文/評估指標（活躍） `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment) — IQA論文/資料集/程式碼的全面集（非常活躍） `awesome` ⭐1.5k · 📅2026-04
- 🟢 [Image-Fusion](https://github.com/Linfeng-Tang/Image-Fusion) — 《Deep Learning-based Image Fusion》綜述，橫跨紅外-可見光/醫療/多曝光等 `survey` ⭐1.2k · 📅2026-06
- 🟢 [Awesome-Image-Colorization](https://github.com/MarkMoHR/Awesome-Image-Colorization) — 基於深度學習的影像/影片上色論文（至2025-2026仍活躍） `awesome` ⭐1.2k · 📅2026-06
- 🟢 [Awesome-Deep-Learning-Based-Video-Compression](https://github.com/ppingzhang/Awesome-Deep-Learning-Based-Video-Compression) — 基於深度學習的影片壓縮論文清單 `paper-list` ⭐294 · 📅2025-09
- 🟢 [Awesome-High-Dynamic-Range-Imaging](https://github.com/rebeccaeexu/Awesome-High-Dynamic-Range-Imaging) — HDR論文集（多/單影格、HDRTV、HDR影片、色調映射） `awesome` ⭐238 · 📅2026-02
- 🟢 [awesome-computational-photography](https://github.com/visionxiang/awesome-computational-photography) — 以深度學習進行計算攝影（影像匹配、對齊、拼接、穩定化） `paper-list` ⭐180 · 📅2025-07
- 🟢 [Awesome-Video-Frame-Interpolation](https://github.com/CMLab-Korea/Awesome-Video-Frame-Interpolation) — IEEE TCSVT'26錄取的VFI綜述，體系化250+論文（活躍） `survey` ⭐150 · 📅2026-04
- 🟢 [Awesome-Image-Restoration](https://github.com/TaoWangzj/Awesome-Image-Restoration) — 綜述《Deep Image Restoration》附帶，橫跨denoise/deblur/SR/dehaze/derain等 `survey` ⭐14 · 📅2025-11
- 🟡 [Awesome-Denoise](https://github.com/oneTaken/Awesome-Denoise) — 依色彩空間與雜訊模型整理影像/連拍/影片去噪論文 `awesome` ⭐503 · 📅2024-04
- 🟡 [Awesome-Shadow-Removal](https://github.com/GuoLanqing/Awesome-Shadow-Removal) — 去陰影的論文/程式碼/資料集/指標集（活躍） `awesome` ⭐395 · 📅2025-04
- 🟡 [awesome-reflection-removal](https://github.com/ChenyangLEI/awesome-reflection-removal) — 去反光方法集（單張影像/閃光/偏光/互動式） `awesome` ⭐157 · 📅2024-12
- 🟡 [awesome-video-enhancement](https://github.com/liuzhen03/awesome-video-enhancement) — 橫跨影片超解析度、插補、去噪、去模糊與修復的論文集 `paper-list` ⭐157 · 📅2024-08
- 🟡 [UIE](https://github.com/YuZhao1999/UIE) — 水下影像增強的資源清單 `paper-list` ⭐117 · 📅2024-05
- 🟡 [Awesome-Neural-Compression](https://github.com/Xinjie-Q/Awesome-Neural-Compression) — 涵蓋影像、影片、點雲、NeRF與3DGS的神經壓縮論文/資源集 `awesome` ⭐83 · 📅2024-08
- 🟡 [Awesome-Deblurring-Resources](https://github.com/kawchar85/Awesome-Deblurring-Resources) — 依年份整理的影像與影片去模糊論文/資料集（活躍） `paper-list` ⭐13 · 📅2024-08
- 🔴 [Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers) — 綜述《Neural Style Transfer: A Review》附帶的代表論文與程式碼集 `paper-list` ⭐1.6k · 📅2022-02
- 🔴 [DerainZoo](https://github.com/nnUyi/DerainZoo) — 去雨的方法、資料集與程式碼集（單張影像/影片） `paper-list` ⭐516 · 📅2022-05
- 🔴 [awesome-image-alignment-and-stitching](https://github.com/tzxiang/awesome-image-alignment-and-stitching) — 影像對齊與拼接的精選 `paper-list` ⭐462 · 📅2022-08
- 🔴 [Awesome-Image-Distortion-Correction](https://github.com/subeeshvasu/Awesome-Image-Distortion-Correction) — 捲簾快門效應與徑向畸變校正相關資源集 `awesome` ⭐282 · 📅2023-07
- 🔴 [awesome-dehazing](https://github.com/youngguncho/awesome-dehazing) — 分類整理單張/多張影像去霧、水下增強與資料集的論文集 `awesome` ⭐202 · 📅2020-08
- 🔴 [Video-Frame-Interpolation-Collections](https://github.com/lyh-18/Video-Frame-Interpolation-Collections) — SOTA VFI方法的集合 `paper-list` ⭐65 · 📅2021-11

## 🎬 動漫・動畫・插畫・字型

- 🟢 [AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) — 動畫/漫畫研究的論文與資料集集（生成、上色、角色動畫等） `awesome` ⭐1.2k · 📅2025-12
- 🟢 [Awesome-Sketch-Based-Applications](https://github.com/MarkMoHR/Awesome-Sketch-Based-Applications) — 基於草圖的應用論文集 `paper-list` ⭐707 · 📅2026-06
- 🟢 [Awesome-Sketch-Synthesis](https://github.com/MarkMoHR/Awesome-Sketch-Synthesis) — 草圖合成(生成)論文集 `paper-list` ⭐566 · 📅2026-06
- 🟢 [Awesome-Animation-Research](https://github.com/zhenglinpan/Awesome-Animation-Research) — 收集動畫(2D/卡通等)研究論文與資料集的清單 `paper-list` ⭐205 · 📅2026-04
- 🟢 [Awesome-AI4Animation](https://github.com/yunlong10/Awesome-AI4Animation) — AI 動畫生成、插補、上色與製作輔助的論文集 `paper-list` ⭐204 · 📅2026-01
- 🟢 [TypographyResearchCollection](https://github.com/IShengFang/TypographyResearchCollection) — 字體排印相關的CG/CV/ML研究收集（含字型生成、動畫） `paper-list` ⭐162 · 📅2025-08
- 🟢 [Awesome-2D-Animation](https://github.com/MarkMoHR/Awesome-2D-Animation) — 中間影格(inbetweening)與 2D 動畫的工具、資料集與論文集 `paper-list` ⭐38 · 📅2026-06
- 🔴 [Sketch-Based-Deep-Learning](https://github.com/qyzdao/Sketch-Based-Deep-Learning) — 草圖式深度學習論文集（線稿上色、向量化等） `paper-list` ⭐179 · 📅2021-05

## 💬 NLP / 大型語言模型(LLM)

- 🟢 [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — 涵蓋LLM論文、模型、工具與課程最大規模之一的清單 `awesome` ⭐26.9k · 📅2025-07
- 🟢 [Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM) — 整理開源中文大型語言模型（底座/領域微調/資料/教程） `awesome` ⭐22.6k · 📅2026-05
- 🟢 [awesome-nlp](https://github.com/keon/awesome-nlp) — 彙整NLP全領域函式庫、資料與教學的經典清單 `awesome` ⭐18.7k · 📅2026-06
- 🟢 [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) — 彙整LLM演化譜系樹與實務應用指南的綜述集 `survey` ⭐10.2k · 📅2026-04
- 🟢 [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) — 彙整多模態生成、Agent、輔助編程、資料處理、訓練與推理等的LLM資料總整理 `awesome` ⭐8.5k · 📅2026-06
- 🟢 [awesome-prompts](https://github.com/ai-boost/awesome-prompts) — 高評價GPTs提示與前沿提示工程論文集 `awesome` ⭐8.2k · 📅2026-06
- 🟢 [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) — 聚焦OpenAI o1與推理技法的論文與部落格集 `paper-list` ⭐6.9k · 📅2025-12
- 🟢 [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) — 彙整GPT/ChatGPT提示技法論文與工具的清單 `awesome` ⭐6k · 📅2026-06
- 🟢 [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) — FlashAttention、PagedAttention等推理加速論文集 `paper-list` ⭐5.3k · 📅2026-04
- 🟢 [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) — Text2SQL/Text2DSL等的教學與資源集 `awesome` ⭐3.7k · 📅2026-01
- 🟢 [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — 從CoT到o1/DeepSeek-R1的LLM推理論文集（非常活躍） `awesome` ⭐3.6k · 📅2026-04
- 🟢 [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) — 從提示工程到正式AI系統的context engineering綜述 `survey` ⭐3.2k · 📅2026-05
- 🟢 [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) — 基於圖的RAG綜述、論文與基準集 `awesome` ⭐2.5k · 📅2026-06
- 🟢 [Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) — 彙整圖相關LLM資源的精選集 `awesome` ⭐2.4k · 📅2025-11
- 🟢 [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) — 持續更新ICL與提示工程最新資源的論文清單 `paper-list` ⭐2.2k · 📅2026-05
- 🟢 [KG-LLM-Papers](https://github.com/zjukg/KG-LLM-Papers) — 整合知識圖譜與LLM的論文清單 `paper-list` ⭐2.2k · 📅2026-03
- 🟢 [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) — 長文脈建模（高效注意力、KV快取、位置編碼等）論文集 `paper-list` ⭐2.1k · 📅2026-06
- 🟢 [Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets) — 以5個面向整理預訓練語料、指令/偏好/評估資料集 `awesome` ⭐1.5k · 📅2026-03
- 🟢 [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) — 基於TKDE2025綜述的LLM Text-to-SQL論文與基準集 `survey` ⭐1.3k · 📅2026-05
- 🟢 [SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) — speculative decoding的必讀論文與部落格集（與綜述連動） `survey` ⭐1.3k · 📅2026-06
- 🟢 [KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) — LLM知識編輯相關論文清單 `paper-list` ⭐1.2k · 📅2025-07
- 🟢 [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) — 依模型整理LLM幻覺偵測論文的清單 `paper-list` ⭐1.1k · 📅2026-06
- 🟢 [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) — 《Siren's Song in the AI Ocean》幻覺綜述的閱讀清單 `survey` ⭐1.1k · 📅2025-09
- 🟢 [Paper-Reading-ConvAI](https://github.com/iwangjian/Paper-Reading-ConvAI) — 以對話系統與NLG為主的會話AI論文清單 `paper-list` ⭐1k · 📅2026-05
- 🟢 [awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) — 《LLM × DATA》綜述官方儲存庫 `survey` ⭐790 · 📅2026-03
- 🟢 [Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) — 《Stop Overthinking》高效推理綜述（TMLR2025）論文集 `survey` ⭐774 · 📅2026-02
- 🟢 [Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) — 《LLMs-as-Judges》評估方法綜述官方論文集 `survey` ⭐590 · 📅2025-07
- 🟢 [A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) — TKDE錄取《MoE in LLMs》綜述官方論文集 `survey` ⭐504 · 📅2026-06
- 🟢 [LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) — 工具學習綜述官方儲存庫，依task planning/tool selection等分類 `survey` ⭐484 · 📅2025-08
- 🟢 [Awesome-LLM-Quantization](https://github.com/pprp/Awesome-LLM-Quantization) — 專注於LLM量化的論文清單 `awesome` ⭐428 · 📅2026-04
- 🟢 [awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference) — 彙整MoE模型推理最佳化論文的清單 `paper-list` ⭐399 · 📅2026-03
- 🟢 [Awesome-Inference-Time-Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling) — 推理時/測試時擴展的論文清單（活躍） `awesome` ⭐389 · 📅2026-05
- 🟢 [Awesome_papers_on_LLMs_detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) — LLM生成文字與程式碼偵測的論文清單 `paper-list` ⭐289 · 📅2025-06
- 🟢 [Awesome-Fake-News-Detection](https://github.com/wangbing1416/Awesome-Fake-News-Detection) — 假新聞與謠言偵測的論文清單 `awesome` ⭐164 · 📅2026-04
- 🟢 [GEC-Info](https://github.com/gotutiyan/GEC-Info) — 收集並分類GEC論文的儲存庫 `paper-list` ⭐128 · 📅2026-01
- 🟢 [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) — LLM self-correction論文清單（依綜述） `paper-list` ⭐81 · 📅2026-05
- 🟢 [Awesome-Function-Callings](https://github.com/Applied-Machine-Learning-Lab/Awesome-Function-Callings) — 專注於LLM function calling的論文清單 `paper-list` ⭐72 · 📅2026-04
- 🟢 [Awesome-Personalized-LLMs](https://github.com/VanillaCreamer/Awesome-Personalized-LLMs) — 個人化LLM（偏好建模、persona控制、記憶式）最新論文集 `paper-list` ⭐48 · 📅2026-06
- 🟢 [awesome-lora-adapter](https://github.com/marlin-codes/awesome-lora-adapter) — 彙整LoRA與adapter系方法的論文清單 `paper-list` ⭐22 · 📅2026-05
- 🟢 [Awesome-PEFT](https://github.com/XiaoshuangJi/Awesome-PEFT) — 以LoRA各種衍生為主的PEFT論文、函式庫與實作集 `awesome` ⭐7 · 📅2026-06
- 🟢 [Awesome-Text-Generation-Evaluation](https://github.com/SuperBruceJia/Awesome-Text-Generation-Evaluation) — NLG評估指標（有/無參考）的精選清單 `awesome` ⭐4 · 📅2026-05
- 📑 [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) — 《A Survey of Large Language Models》官方儲存庫 `survey` ⭐12.2k · 📅2025-03
- 📑 [ABigSurvey](https://github.com/NiuTrans/ABigSurvey) — 彙整NLP與ML數百篇綜述論文的綜述之綜述 `survey` ⭐2k · 📅2024-03
- 📑 [RAG-Survey](https://github.com/hymie122/RAG-Survey) — 《RAG for AI-Generated Content》綜述的分類體系與論文集 `survey` ⭐1.8k · 📅2024-08
- 📑 [Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) — 《LLMs on Graphs》TKDE綜述的論文與資源集 `survey` ⭐993 · 📅2025-03
- 📑 [Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) — 《Evaluating LLMs: A Comprehensive Survey》論文集 `survey` ⭐803 · 📅2024-05
- 📑 [CNSurvey](https://github.com/NiuTrans/CNSurvey) — NLP與機器學習的中文綜述文章清單 `survey` ⭐580 · 📅2023-05
- 📑 [ABigSurveyOfLLMs](https://github.com/NiuTrans/ABigSurveyOfLLMs) — 彙整150篇以上LLM相關綜述的集合 `survey` ⭐352 · 📅2025-02
- 📑 [Semantic-Retrieval-Models](https://github.com/caiyinqiong/Semantic-Retrieval-Models) — 涵蓋語意檢索模型（DPR、RAG、RepBERT等）的TOIS錄取綜述論文清單 `survey` ⭐340 · 📅2023-06
- 📑 [CTGSurvey](https://github.com/IAAR-Shanghai/CTGSurvey) — LLM用可控文字生成綜述論文清單（分類訓練時/推理時方法） `survey` ⭐204 · 📅2024-08
- 📑 [Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models](https://github.com/THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models) — 系統性彙整基礎模型用PEFT方法的綜述兼論文清單 `survey` ⭐112 · 📅2025-03
- 📑 [llm-alignment-survey](https://github.com/Magnetic2014/llm-alignment-survey) — 《LLM Alignment: A Survey》的對齊閱讀清單 `survey` ⭐82 · 📅2023-09
- 📑 [Awesome_Information_Extraction](https://github.com/wutong8023/Awesome_Information_Extraction) — 含RE、EE、slot filling的IE文獻綜述 `survey` ⭐72 · 📅2023-01
- 📑 [Awesome-Data-Efficient-LLM](https://github.com/luo-junyu/Awesome-Data-Efficient-LLM) — 資料高效與資料中心的LLM論文集（附綜述） `survey` ⭐60 · 📅2025-02
- 🟡 [Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) — 程式碼生成LLM研究的精選清單 `awesome` ⭐1.3k · 📅2024-12
- 🟡 [Awesome-LLM4IE-Papers](https://github.com/quqxui/Awesome-LLM4IE-Papers) — 以LLM進行生成式資訊抽取（NER/RE/EE）的論文集 `paper-list` ⭐1.1k · 📅2024-11
- 🟡 [Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers) — ACL2023綜述《Reasoning with LM Prompting》論文清單 `paper-list` ⭐1k · 📅2025-05
- 🟡 [ToolLearningPapers](https://github.com/thunlp/ToolLearningPapers) — 基礎模型工具學習（tool learning）的必讀論文集 `paper-list` ⭐922 · 📅2024-07
- 🟡 [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) — 基於In-Context Learning綜述的論文清單 `paper-list` ⭐877 · 📅2024-10
- 🟡 [awesome-pretrained-models-for-information-retrieval](https://github.com/ict-bigdatalab/awesome-pretrained-models-for-information-retrieval) — IR用預訓練模型（pretraining for IR）論文集 `awesome` ⭐676 · 📅2024-01
- 🟡 [Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) — MoE研究閱讀清單 `paper-list` ⭐667 · 📅2024-10
- 🟡 [EventExtractionPapers](https://github.com/BaptisteBlouin/EventExtractionPapers) — 以事件抽取任務為主的NLP資源清單 `paper-list` ⭐580 · 📅2024-03
- 🟡 [awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning) — Instruction Tuning/Following論文與資料集集 `paper-list` ⭐510 · 📅2024-04
- 🟡 [awesome-llm-pretraining](https://github.com/RUCAIBox/awesome-llm-pretraining) — LLM預訓練的資料、框架與方法資源集 `awesome` ⭐383 · 📅2025-04
- 🟡 [Awesome-LLM-Watermark](https://github.com/hzy312/Awesome-LLM-Watermark) — 持續更新最新LLM浮水印論文的清單 `paper-list` ⭐374 · 📅2024-12
- 🟡 [ABSAPapers](https://github.com/ZhengZixiang/ABSAPapers) — 面向aspect的情感分析（ABSA）論文與資源集 `paper-list` ⭐363 · 📅2024-03
- 🟡 [Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) — LLM幻覺相關論文清單 `paper-list` ⭐336 · 📅2024-03
- 🟡 [LLM-Optimizers-Papers](https://github.com/AGI-Edgerunners/LLM-Optimizers-Papers) — 將LLM用作最佳化器/提示自動最佳化的必讀論文集 `paper-list` ⭐252 · 📅2024-03
- 🟡 [awesome-tool-llm](https://github.com/zorazrw/awesome-tool-llm) — 彙整工具增強LLM（ToRA、MINT等）的精選清單 `awesome` ⭐245 · 📅2024-08
- 🟡 [Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) — 《Evaluation of RAG: A Survey》官方評估論文清單 `paper-list` ⭐198 · 📅2025-04
- 🟡 [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) — 測試時LLM（含self-correction/refine）論文集 `awesome` ⭐153 · 📅2025-03
- 🟡 [Low-resource-KEPapers](https://github.com/zjunlp/Low-resource-KEPapers) — 低資源資訊抽取（NER/RE/EE）的論文、工具與資料集集 `paper-list` ⭐136 · 📅2024-11
- 🟡 [EMNLP-2023-Papers](https://github.com/DmitryRyumin/EMNLP-2023-Papers) — 系統性整理EMNLP 2023論文的集合 `paper-list` ⭐111 · 📅2024-05
- 🟡 [Paper-Neural-Topic-Models](https://github.com/bobxwu/Paper-Neural-Topic-Models) — 神經主題模型（NTM）的論文集 `paper-list` ⭐96 · 📅2024-07
- 🟡 [Awesome-Papers-Retrieval-Augmented-Generation](https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation) — 基於知識導向RAG綜述的論文分類清單 `paper-list` ⭐89 · 📅2025-03
- 🟡 [Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers) — 多語言LLM論文清單 `paper-list` ⭐34 · 📅2025-01
- 🟡 [awesome-llm-tool-learning](https://github.com/AngxiaoYue/awesome-llm-tool-learning) — LLM工具學習論文（Gorilla、HuggingGPT、ART等）清單 `paper-list` ⭐28 · 📅2024-07
- 🟡 [Awesome-LLM-Reasoning-Techniques](https://github.com/Junting-Lu/Awesome-LLM-Reasoning-Techniques) — 含CoT與o1的LLM推理技法論文與資源集 `paper-list` ⭐18 · 📅2024-10
- 📦 [Fact-Checking-Survey](https://github.com/neemakot/Fact-Checking-Survey) — COLING2020《Explainable Automated Fact-Checking》綜述論文集 `survey` ⭐51 · 📅2021-01
- 🔴 [PromptPapers](https://github.com/thunlp/PromptPapers) — 預訓練模型提示式調校的必讀論文集 `paper-list` ⭐4.3k · 📅2023-07
- 🔴 [Top-AI-Conferences-Paper-with-Code](https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code) — ACL/EMNLP/NAACL/COLING等頂會附程式碼的論文集 `paper-list` ⭐2.7k · 📅2022-10
- 🔴 [Style-Transfer-in-Text](https://github.com/fuzhenxin/Style-Transfer-in-Text) — 文字風格轉換的經典論文清單（分類監督/非監督/評估） `paper-list` ⭐1.6k · 📅2023-03
- 🔴 [awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization) — 文字摘要的論文、工具與資料集集 `awesome` ⭐1.5k · 📅2023-01
- 🔴 [awesome-relation-extraction](https://github.com/roomylee/awesome-relation-extraction) — 專注於關係抽取的資源清單 `awesome` ⭐1.2k · 📅2022-01
- 🔴 [awesome-qa](https://github.com/seriousran/awesome-qa) — 問答的資料集、論文與資源集 `awesome` ⭐769 · 📅2022-01
- 🔴 [awesome-sentiment-analysis](https://github.com/declare-lab/awesome-sentiment-analysis) — 情感分析論文的閱讀清單 `paper-list` ⭐538 · 📅2023-03
- 🔴 [awesome-nlg](https://github.com/accelerated-text/awesome-nlg) — NLG整體的資源集（工具/論文/資料） `awesome` ⭐483 · 📅2023-09
- 🔴 [Named-Entity-Recognition-NER-Papers](https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers) — 涵蓋7個會議NER論文的清單 `paper-list` ⭐390 · 📅2022-02
- 🔴 [Awesome-Sentence-Embedding](https://github.com/Doragd/Awesome-Sentence-Embedding) — 收錄句子表示學習論文與STS排行榜（SimCSE等） `awesome` ⭐314 · 📅2023-10
- 🔴 [DeltaPapers](https://github.com/thunlp/DeltaPapers) — 預訓練模型參數高效調校（Delta Tuning）的必讀論文集 `paper-list` ⭐284 · 📅2023-06
- 🔴 [Awesome-KBQA](https://github.com/RUCAIBox/Awesome-KBQA) — 知識庫QA（KBQA）的論文、工具與排行榜集 `paper-list` ⭐182 · 📅2022-04
- 🔴 [Accepted-Papers-Lists](https://github.com/audreycs/Accepted-Papers-Lists) — 彙整主要期刊與會議錄取論文清單的儲存庫 `paper-list` ⭐147 · 📅2022-12
- 🔴 [MT-paper-lists](https://github.com/NiuTrans/MT-paper-lists) — 依會議整理機器翻譯論文的清單 `paper-list` ⭐124 · 📅2020-12
- 🔴 [Data-to-Text-Generation](https://github.com/liang8qi/Data-to-Text-Generation) — data-to-text生成的論文與資料集集 `paper-list` ⭐108 · 📅2023-05
- 🔴 [awesome-NLP-Machine-Learning](https://github.com/tjunlp-lab/awesome-NLP-Machine-Learning) — NLP研究用機器學習技法（RL/自監督等）的論文與程式碼集 `paper-list` ⭐35 · 📅2020-03
- 🔴 [AWESOME-Dialogue](https://github.com/thuiar/AWESOME-Dialogue) — 對話與互動系統的論文清單 `paper-list` ⭐15 · 📅2020-06
- 🔴 [awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp) — 以英語以外語言為對象的多語言NLP研究精選 `awesome` ⭐8 · 📅2023-07
- 🔴 [AwesomeSemanticParsing](https://github.com/aarsri/AwesomeSemanticParsing) — 語意剖析的論文與資源集 `awesome` ⭐0 · 📅2020-11

## 🖼️ 生成式 AI / Diffusion / 影像・影片生成

- 🟢 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) — 彙整影片生成與編輯diffusion model的經典清單 `awesome` ⭐5.7k · 📅2026-05
- 🟢 [gans-awesome-applications](https://github.com/nashory/gans-awesome-applications) — 彙整GAN應用與demo的精選清單 `awesome` ⭐5.1k · 📅2026-06
- 🟢 [really-awesome-gan](https://github.com/nightrome/really-awesome-gan) — 彙整GAN論文的全面清單 `paper-list` ⭐3.8k · 📅2025-08
- 🟢 [awesome-virtual-try-on](https://github.com/minar09/awesome-virtual-try-on) — 虛擬試穿的論文/程式碼/資料集經典清單 `awesome` ⭐3.1k · 📅2026-06
- 🟢 [Awesome-Text-to-Image](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image) — 文字生成影像的綜述式論文清單 `survey` ⭐2.4k · 📅2026-02
- 🟢 [Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) — Video Diffusion Model綜述（CSUR） `survey` ⭐2.3k · 📅2026-04
- 🟢 [awesome-diffusion-categorized](https://github.com/wangkai930418/awesome-diffusion-categorized) — 依子領域分類diffusion論文的實用集合 `awesome` ⭐2.2k · 📅2026-03
- 🟢 [awesome-talking-head-generation](https://github.com/harlanhong/awesome-talking-head-generation) — talking head生成論文清單 `paper-list` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) — Deepfake偵測的工具/論文/程式碼 `awesome` ⭐1.8k · 📅2025-09
- 🟢 [awesome-image-translation](https://github.com/weihaox/awesome-image-translation) — image-to-image translation相關優良資源的集合 `awesome` ⭐1.2k · 📅2025-09
- 🟢 [Awesome-diffusion-model-for-image-processing](https://github.com/lixinustc/Awesome-diffusion-model-for-image-processing) — 整理復原/增強/編碼/品質評估的diffusion model `survey` ⭐947 · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/showlab/Awesome-Unified-Multimodal-Models) — 統一理解與生成的模型論文集 `paper-list` ⭐826 · 📅2025-10
- 🟢 [Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) — 視覺autoregressive model綜述（TMLR 2025） `survey` ⭐796 · 📅2026-05
- 🟢 [awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) — 彙整影片生成研究的集合 `awesome` ⭐770 · 📅2026-03
- 🟢 [awesome-text-to-image-studies](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) — 彙整text-to-image研究的持續更新清單 `awesome` ⭐759 · 📅2026-04
- 🟢 [Awesome-Deepfake-Generation-and-Detection](https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection) — Deepfake生成與偵測綜述 `survey` ⭐639 · 📅2026-05
- 🟢 [Awesome-Video-World-Models-with-AR-Diffusion](https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion) — AR+diffusion的影片世界模型（演算法/應用/基礎） `awesome` ⭐600 · 📅2026-06
- 🟢 [awesome-discrete-diffusion-models](https://github.com/kuleshov-group/awesome-discrete-diffusion-models) — 專注於離散diffusion model的資源清單 `awesome` ⭐563 · 📅2025-09
- 🟢 [Awesome-Controllable-Diffusion](https://github.com/atfortes/Awesome-Controllable-Diffusion) — ControlNet、DreamBooth、IP-Adapter等可控生成資源 `awesome` ⭐507 · 📅2025-06
- 🟢 [Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model) — 整理從影片生成到世界模型的脈絡 `paper-list` ⭐496 · 📅2026-03
- 🟢 [Awesome-Image-Editing](https://github.com/FudanCVL/Awesome-Image-Editing) — 以T2I模型進行影像編輯的綜述 `survey` ⭐472 · 📅2025-08
- 🟢 [Awesome-Evaluation-of-Visual-Generation](https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation) — 視覺生成的評估指標/模型/系統集 `paper-list` ⭐452 · 📅2026-05
- 🟢 [Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation) — autoregressive視覺生成最新論文追蹤 `paper-list` ⭐430 · 📅2025-06
- 🟢 [Awesome-Try-On-Models](https://github.com/Zheng-Chong/Awesome-Try-On-Models) — 整理虛擬試穿模型（含2025） `paper-list` ⭐423 · 📅2026-05
- 🟢 [Awesome-AIGC-Image-Video-Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) — AI生成影像/影片偵測的最新研究集 `paper-list` ⭐414 · 📅2026-06
- 🟢 [awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) — 影像修復研究的集合 `awesome` ⭐389 · 📅2026-02
- 🟢 [Awesome-Comprehensive-Deepfake-Detection](https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection) — Deepfake偵測的全面論文清單 `paper-list` ⭐315 · 📅2026-04
- 🟢 [awesome-diffusion-v2v](https://github.com/wenhao728/awesome-diffusion-v2v) — 基於diffusion的Video-to-Video編輯論文與基準 `paper-list` ⭐288 · 📅2026-04
- 🟢 [Awesome-Text-to-Video-Generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation) — 依Sora綜述整理的T2V/I2V論文清單 `survey` ⭐258 · 📅2026-03
- 🟢 [Awesome-Consistency-Models](https://github.com/G-U-N/Awesome-Consistency-Models) — Consistency Model資源清單 `awesome` ⭐131 · 📅2025-12
- 📑 [GAN-Inversion](https://github.com/weihaox/GAN-Inversion) — GAN Inversion綜述（TPAMI 2022）附帶儲存庫 `survey` ⭐1.1k · 📅2025-02
- 📑 [awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) — Text-to-Video生成綜述 `survey` ⭐731 · 📅2024-07
- 🟡 [Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) — 涵蓋diffusion model論文與資源最大規模之一的清單 `awesome` ⭐12.3k · 📅2024-08
- 🟡 [Awesome-High-Resolution-Diffusion](https://github.com/GuoLanqing/Awesome-High-Resolution-Diffusion) — 高解析度影像/影片合成的diffusion論文 `paper-list` ⭐169 · 📅2024-12
- 🟡 [Awesome-Music-Generation](https://github.com/shaopengw/Awesome-Music-Generation) — 音樂生成模型MG²的資源 `model` ⭐165 · 📅2025-03
- 🟡 [awesome-diffusion-iclr-2025](https://github.com/moatifbutt/awesome-diffusion-iclr-2025) — ICLR 2025 diffusion相關投稿清單 `paper-list` ⭐61 · 📅2024-10
- 📚 [the-gan-zoo](https://github.com/hindupuravinash/the-gan-zoo) — 列出所有具名GAN的經典清單 `paper-list` ⭐14.7k · 📅2023-10
- 🔴 [awesome-ai-art-image-synthesis](https://github.com/altryne/awesome-ai-art-image-synthesis) — DALL·E2/MidJourney/SD等工具與提示集 `awesome` ⭐1.8k · 📅2022-12
- 🔴 [awesome-diffusion-low-level-vision](https://github.com/yulunzhang/awesome-diffusion-low-level-vision) — 低階視覺diffusion model清單 `paper-list` ⭐186 · 📅2023-09
- 🔴 [awesome-controlnet](https://github.com/cobanov/awesome-controlnet) — ControlNet相關資源清單 `awesome` ⭐97 · 📅2023-03
- 🔴 [awesome-few-shot-generation](https://github.com/kobeshegu/awesome-few-shot-generation) — 少量影像生成的論文清單 `paper-list` ⭐87 · 📅2023-08
- 🔴 [Awsome-GAN-Training](https://github.com/subeeshvasu/Awsome-GAN-Training) — 彙整GAN訓練（training）相關資源的清單 `awesome` ⭐30 · 📅2020-10

## 🍌 特定模型的提示詞・範例集

- 🟢 [Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) — Gemini系Nano Banana生成範例與提示集（公開資料集） `model` ⭐23k · 📅2025-12
- 🟢 [awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) — GPT-Image-2的API與提示及範例集 `model` ⭐16.7k · 📅2026-06
- 🟢 [awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) — 世界最大規模之一的Nano Banana Pro提示集10,000+/16語言（每日更新） `model` ⭐12.5k · 📅2026-06
- 🟢 [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) — Nano Banana Pro（Nano Banana 2）的提示與範例集 `model` ⭐10.1k · 📅2026-05
- 🟢 [awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) — Gemini-2.5-Flash-Image（Nano Banana）範例/提示集 `model` ⭐8.8k · 📅2025-09
- 🟢 [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) — Seedance 2.0影片生成提示2000+（每日更新） `model` ⭐1.4k · 📅2026-06
- 🟢 [awesome-nano-banana-pro](https://github.com/muset-ai/awesome-nano-banana-pro) — Nano Banana Pro的影像與提示範例集 `model` ⭐1.1k · 📅2025-11
- 🟢 [awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) — Veo3/Kling/Hailuo用影片提示集 `model` ⭐546 · 📅2025-10
- 🟢 [Awesome-Chinese-Stable-Diffusion](https://github.com/leeguandong/Awesome-Chinese-Stable-Diffusion) — 中文文生圖SD模型集（含Kolors/HunyuanDiT等） `model` ⭐431 · 📅2026-05
- 🟢 [awesome-qwen-prompt-insight](https://github.com/XiaomingX/awesome-qwen-prompt-insight) — Qwen用優質提示的大規模集合 `model` ⭐401 · 📅2026-02
- 🟢 [awesome-nano-banana-images](https://github.com/githubssg/awesome-nano-banana-images) — GPT-4o/gpt-image-1的影像與提示集 `model` ⭐305 · 📅2025-09
- 🟢 [Awesome-Open-AI-Sora](https://github.com/Curated-Awesome-Lists/Awesome-Open-AI-Sora) — Sora相關文章/影片/新聞的資源中心 `model` ⭐260 · 📅2026-05
- 🟢 [awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) — 橫跨多個影片模型的提示/技法集 `model` ⭐61 · 📅2026-01
- 🟢 [awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts) — Grok Imagine（xAI）影片生成提示集 `model` ⭐21 · 📅2026-06
- 🟢 [awesome-qwen-image-2512](https://github.com/shauray8/awesome-qwen-image-2512) — qwen-image-2512範例/提示集 `model` ⭐0 · 📅2025-12
- 🟡 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) — GPT-4o與gpt-image-1的影像與提示範例集 `model` ⭐8.1k · 📅2025-05
- 🟡 [Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) — 彙整GPT Store刊載GPT的精選 `model` ⭐3.4k · 📅2024-11
- 🟡 [Awesome-GPT4o-Image-Prompts](https://github.com/ImgEdify/Awesome-GPT4o-Image-Prompts) — GPT-4o影像生成提示辭典 `model` ⭐570 · 📅2025-05
- 🟡 [awesome-grok-prompts](https://github.com/langgptai/awesome-grok-prompts) — Grok（xAI）用進階提示與範本集 `model` ⭐505 · 📅2025-05
- 🟡 [awesome-llama-prompts](https://github.com/langgptai/awesome-llama-prompts) — Llama2/Llama3用提示集 `model` ⭐270 · 📅2024-08
- 🟡 [awesome-flux](https://github.com/Eris2025/awesome-flux) — FLUX生態系（LoRA/ControlNet/量化）資源集 `model` ⭐105 · 📅2024-08

## 🧰 模型生態系 / 維運工具 (MCP・LLMOps・LLM 應用)

- 🟢 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — 可執行的LLM應用/RAG/agent集合 `awesome` ⭐114.6k · 📅2026-06
- 🟢 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 最大規模的MCP（Model Context Protocol）伺服器集合 `awesome` ⭐89.2k · 📅2026-06
- 🟢 [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Claude Skill/工具的精選 `awesome` ⭐64.6k · 📅2026-05
- 🟢 [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code用skill/hook/slash-command/外掛集 `awesome` ⭐46.5k · 📅2026-04
- 🟢 [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) — 將DeepSeek API整合至各類軟體的官方精選 `model` ⭐37.9k · 📅2026-02
- 🟢 [Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) — 涵蓋PyTorch相關模型、實作與函式庫的大規模清單 `awesome` ⭐16.5k · 📅2026-02
- 🟢 [awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) — 精選現代生成AI專案與服務的清單 `awesome` ⭐12.1k · 📅2026-06
- 🟢 [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) — LangChain框架的工具與專案清單 `awesome` ⭐9.4k · 📅2026-04
- 🟢 [ai-collection](https://github.com/ai-collection/ai-collection) — 彙整生成AI應用的全景圖 `awesome` ⭐9k · 📅2026-06
- 🟢 [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) — ChatGPT用awesome清單（sindresorhus系列） `awesome` ⭐6.3k · 📅2026-02
- 🟢 [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) — 收集AI相關實用工具的集合（中英並列） `awesome` ⭐6k · 📅2026-06
- 🟢 [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) — LLM開發與運維用工具（訓練/服務/監控）的精選清單 `awesome` ⭐5.8k · 📅2026-05
- 🟢 [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) — MCP伺服器的精選 `awesome` ⭐5.6k · 📅2026-05
- 🟢 [awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools) — 精選AI頂尖工具的清單 `awesome` ⭐5.5k · 📅2025-12
- 🟢 [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) — 真正開源的AI專案、模型、工具與基礎的精選清單 `awesome` ⭐3.9k · 📅2026-06
- 🟢 [awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) — ChatGPT的函式庫/SDK/API精選 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-claude](https://github.com/webfuse-com/awesome-claude) — Anthropic Claude整體的精選清單 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) — 生成AI中RAG應用的awesome清單 `awesome` ⭐1.2k · 📅2026-06
- 🟢 [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) — 彙整DeepSeek Coder相關OSS專案的官方清單 `model` ⭐791 · 📅2025-11
- 🟢 [awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) — ComfyUI自訂節點的大規模集合 `awesome` ⭐707 · 📅2025-07
- 🟢 [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) — Gemini CLI用工具/擴充/資源集 `awesome` ⭐470 · 📅2026-06
- 🟢 [awesome-stable-diffusion](https://github.com/doanbactam/awesome-stable-diffusion) — Stable Diffusion資源的精選 `awesome` ⭐78 · 📅2026-03
- 🟢 [awesome-mistral](https://github.com/samouraiworld/awesome-mistral) — Mistral AI生態系的資源/工具/專案集 `awesome` ⭐42 · 📅2026-06
- 🟡 [awesome-gpt](https://github.com/formulahendry/awesome-gpt) — GPT/ChatGPT/OpenAI相關專案與資源集 `awesome` ⭐1k · 📅2024-05
- 🟡 [awesome-flux-ai](https://github.com/AINativeLab/awesome-flux-ai) — Flux AI的工具/函式庫/應用收錄 `awesome` ⭐111 · 📅2025-05

## 🎮 強化學習(RL)

- 🟢 [MARL-Papers](https://github.com/LantaoYu/MARL-Papers) — 多智能體RL的研究與綜述論文清單（經典） `paper-list` ⭐4.8k · 📅2026-02
- 🟢 [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) — 彙整LLM與多模態應用於機器人/RL的論文集 `paper-list` ⭐4.4k · 📅2026-04
- 🟢 [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — 持續更新人類回饋RL的論文與資源 `paper-list` ⭐4.4k · 📅2026-05
- 🟢 [Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) — 大型推理模型用RL的綜述論文儲存庫 `survey` ⭐2.5k · 📅2025-11
- 🟢 [Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) — 世界模型（影片生成、Embodied AI、自動駕駛）論文全面收錄 `paper-list` ⭐1.8k · 📅2026-06
- 🟢 [awesome-diffusion-model-in-rl](https://github.com/opendilab/awesome-diffusion-model-in-rl) — 持續更新強化學習中diffusion model資源的清單 `awesome` ⭐1.6k · 📅2026-05
- 🟢 [awesome-model-based-RL](https://github.com/opendilab/awesome-model-based-RL) — 持續更新收集model-based RL論文 `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-decision-transformer](https://github.com/opendilab/awesome-decision-transformer) — Decision Transformer資源的持續更新清單 `awesome` ⭐903 · 📅2026-05
- 🟢 [awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) — 整理Deep RL函式庫、環境與基準的清單 `awesome` ⭐891 · 📅2025-07
- 🟢 [Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) — 彙整Safe RL的baseline與論文的儲存庫 `paper-list` ⭐798 · 📅2026-03
- 🟢 [World-Model](https://github.com/tsinghua-fib-lab/World-Model) — 世界模型的全面綜述（ACM CSUR 2025錄取） `survey` ⭐753 · 📅2025-11
- 🟢 [awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl) — 專注於exploration的RL論文清單 `paper-list` ⭐694 · 📅2026-05
- 🟢 [awesome-multi-modal-reinforcement-learning](https://github.com/opendilab/awesome-multi-modal-reinforcement-learning) — 持續更新多模態RL資源 `paper-list` ⭐608 · 📅2026-05
- 🟢 [Reinforcement-Learning-Papers](https://github.com/yingchengyang/Reinforcement-Learning-Papers) — 依年份整理ICLR/ICML/NeurIPS經典與最新論文 `paper-list` ⭐573 · 📅2026-02
- 🟢 [Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) — 整理視覺RL與多模態基礎模型用RL論文 `paper-list` ⭐449 · 📅2026-04
- 🟢 [Reinforcement-Learning-Papers](https://github.com/Allenpandas/Reinforcement-Learning-Papers) — 涵蓋NeurIPS/ICML/ICLR/AAAI/IJCAI/AAMAS/ICRA的論文 `paper-list` ⭐367 · 📅2025-11
- 🟢 [awesome-in-context-rl](https://github.com/dunnolab/awesome-in-context-rl) — In-Context RL論文精選 `paper-list` ⭐302 · 📅2025-09
- 🟢 [Awesome-Causal-Reinforcement-Learning](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) — 因果RL綜述（TNNLS 2024）官方儲存庫 `survey` ⭐221 · 📅2026-06
- 🟢 [awesome-deep-reinforcement-learning](https://github.com/jgvictores/awesome-deep-reinforcement-learning) — 收錄框架、模型、資料集、gym與baseline `awesome` ⭐206 · 📅2026-03
- 🟢 [awesome-RLVR](https://github.com/opendilab/awesome-RLVR) — 持續更新可驗證獎勵RL（RLVR）論文 `paper-list` ⭐194 · 📅2026-06
- 🟢 [AwesomeSim2Real](https://github.com/LongchaoDa/AwesomeSim2Real) — 綜述《A Survey of Sim-to-Real Methods in RL》的companion `survey` ⭐174 · 📅2025-09
- 🟢 [awesome-world-models-for-robots](https://github.com/operator22th/awesome-world-models-for-robots) — 機器人用世界模型論文集 `paper-list` ⭐137 · 📅2026-03
- 🟢 [Awesome-Embodied-World-Model](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) — 專注於具身agent用世界模型的論文集 `survey` ⭐120 · 📅2026-05
- 🟡 [awesome-deep-rl](https://github.com/tigerneil/awesome-deep-rl) — 廣泛收集面向Deep RL與AI未來的資源清單 `awesome` ⭐1.5k · 📅2024-03
- 🟡 [awesome-rl-envs](https://github.com/clvrai/awesome-rl-envs) — 涵蓋RL用環境與模擬器的清單 `awesome` ⭐1.3k · 📅2024-05
- 🟡 [awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl) — offline RL的演算法索引（持續更新） `paper-list` ⭐1.1k · 📅2024-05
- 🟡 [awesome-game-ai](https://github.com/datamllab/awesome-game-ai) — 以多智能體學習為主的遊戲AI資源集 `awesome` ⭐969 · 📅2024-06
- 🟡 [Awesome-Imitation-Learning](https://github.com/kristery/Awesome-Imitation-Learning) — 彙整模仿學習論文與資源的清單 `paper-list` ⭐607 · 📅2024-02
- 📚 [deep-reinforcement-learning-papers](https://github.com/junhyukoh/deep-reinforcement-learning-papers) — 依主題彙整Deep RL主要論文的經典清單 `paper-list` ⭐2.2k · 📅2016-06
- 🔴 [awesome-rl](https://github.com/aikorea/awesome-rl) — 彙整RL全領域程式碼、講義、論文與環境的經典精選 `awesome` ⭐9.8k · 📅2023-05
- 🔴 [awesome-real-world-rl](https://github.com/ugurkanates/awesome-real-world-rl) — 在真實世界運行強化學習的論文與專案集（含sim2real） `awesome` ⭐457 · 📅2022-10
- 🔴 [MARL-papers-with-code](https://github.com/TimeBreaker/MARL-papers-with-code) — 依方法整理附程式碼的MARL論文 `paper-list` ⭐428 · 📅2022-09
- 🔴 [Imitation-Learning-Paper-Lists](https://github.com/apexrl/Imitation-Learning-Paper-Lists) — 附簡介收集模仿學習論文 `paper-list` ⭐157 · 📅2022-03
- 🔴 [awesome-irl](https://github.com/dit7ya/awesome-irl) — 逆強化學習的論文、程式碼、影片與教學集 `awesome` ⭐44 · 📅2022-02
- 🔴 [awesome-metarl](https://github.com/metarl/awesome-metarl) — 元強化學習精選清單 `paper-list` ⭐33 · 📅2020-05

## 🔀 多模態 / VLM / MLLM

- 🟢 [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) — MLLM領域最知名綜述，全面追蹤架構、訓練與評估 `survey` ⭐17.9k · 📅2026-05
- 🟢 [Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) — 影片理解用Vid-LLM最新論文、程式碼與資料集 `paper-list` ⭐3.2k · 📅2026-06
- 🟢 [VLM_survey](https://github.com/jingyi0000/VLM_survey) — 視覺任務用Vision-Language模型的系統性綜述 `survey` ⭐3.1k · 📅2025-10
- 🟢 [Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) — 3D世界中多模態LLM資源的全面清單 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) — 整合理解與生成的多模態模型全面集（活躍） `survey` ⭐1.3k · 📅2026-03
- 🟢 [awesome-vlm-architectures](https://github.com/gokayfem/awesome-vlm-architectures) — 解說知名VLM及其架構的集合 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) — 多模態LLM幻覺（hallucination）相關資源的精選清單 `awesome` ⭐1k · 📅2025-09
- 🟢 [Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) — CLIP等VLM用提示/adapter學習方法的精選清單 `paper-list` ⭐781 · 📅2026-06
- 🟢 [Awesome-Spatial-Intelligence-in-VLM](https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM) — VLM空間推理相關論文與基準約200篇（非常活躍） `paper-list` ⭐754 · 📅2026-01
- 🟢 [Awesome_Matching_Pretraining_Transfering](https://github.com/Paranioar/Awesome_Matching_Pretraining_Transfering) — 影像文字匹配、VL預訓練與多模態模型的大規模論文清單 `paper-list` ⭐445 · 📅2025-09
- 🟢 [Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) — 多模態研究整體的精選論文集 `awesome` ⭐339 · 📅2026-06
- 🟢 [Awesome-Chart-Understanding](https://github.com/khuangaf/Awesome-Chart-Understanding) — 依IEEE TKDE綜述整理的圖表理解（QA/captioning/fact-checking）論文集 `survey` ⭐240 · 📅2025-12
- 🟢 [Awesome-Document-Understanding](https://github.com/harrytea/Awesome-Document-Understanding) — MLLM/OCR-free等多模態文件AI論文、程式碼與資料集集 `paper-list` ⭐201 · 📅2025-09
- 🟢 [Evaluation-Multimodal-LLMs-Survey](https://github.com/swordlidev/Evaluation-Multimodal-LLMs-Survey) — 綜述200多個MLLM基準的評估綜述 `survey` ⭐154 · 📅2026-06
- 🟢 [Awesome-Multimodal-LLM-for-Math-STEM](https://github.com/InfiMM/Awesome-Multimodal-LLM-for-Math-STEM) — Math/STEM/Code用多模態LLM論文集 `awesome` ⭐143 · 📅2026-05
- 🟢 [Awesome-MLLM-Tuning](https://github.com/WenkeHuang/Awesome-MLLM-Tuning) — MLLM下游任務調校方法綜述 `paper-list` ⭐99 · 📅2025-08
- 🟢 [Awesome-Composed-Multi-modal-Retrieval](https://github.com/kkzhang95/Awesome-Composed-Multi-modal-Retrieval) — 含合成影像檢索（CIR）與合成影片檢索（CVR）的CMR綜述 `survey` ⭐89 · 📅2026-01
- 🟢 [Awesome-Multimodal-RAG](https://github.com/JarvisUSTC/Awesome-Multimodal-RAG) — 橫跨文字/影像/影片/音訊的多模態RAG論文與工具集 `paper-list` ⭐53 · 📅2025-11
- 🟢 [Awesome-Large-Vision-Language-Model](https://github.com/SuperBruceJia/Awesome-Large-Vision-Language-Model) — 大規模VLM與醫療基礎模型的論文與資源集 `awesome` ⭐49 · 📅2025-07
- 📑 [Efficient-Multimodal-LLMs-Survey](https://github.com/swordlidev/Efficient-Multimodal-LLMs-Survey) — 高效MLLM（輕量結構、策略）的系統性綜述 `survey` ⭐385 · 📅2025-04
- 🟡 [awesome-audio-visual](https://github.com/krantiparida/awesome-audio-visual) — 語音與視覺處理各領域的論文與資料集集 `awesome` ⭐772 · 📅2024-01
- 🟡 [Awesome-Table-Recognition](https://github.com/cv-small-snails/Awesome-Table-Recognition) — 整理表格辨識的論文、資料集與競賽解法 `awesome` ⭐404 · 📅2024-12
- 🟡 [awesome-emotion-recognition-in-conversations](https://github.com/declare-lab/awesome-emotion-recognition-in-conversations) — 會話情緒辨識（ERC）的全面閱讀清單 `paper-list` ⭐279 · 📅2024-02
- 🟡 [awesome-table-structure-recognition](https://github.com/Tan-Junwen/awesome-table-structure-recognition) — 表格結構辨識（TSR）的模型、論文、資料集與程式碼集 `awesome` ⭐230 · 📅2024-09
- 🟡 [Prompt_Learning_Paper_List](https://github.com/Event-AHU/Prompt_Learning_Paper_List) — （視覺語言）提示學習的論文清單 `paper-list` ⭐19 · 📅2024-11
- 🔴 [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) — 涵蓋KIE、版面分析、DocQA、OCR等的經典清單 `awesome` ⭐1.5k · 📅2023-06
- 🔴 [awesome-video-text-retrieval](https://github.com/danieljf24/awesome-video-text-retrieval) — 影片文字檢索的深度學習資源集 `awesome` ⭐645 · 📅2023-10
- 🔴 [awesome-affective-computing](https://github.com/AmrMKayid/awesome-affective-computing) — 情感運算的論文、軟體、OSS與資源集 `awesome` ⭐192 · 📅2019-11
- 🔴 [AWESOME-MER](https://github.com/EvelynFan/AWESOME-MER) — 多模態情緒辨識（MER）的閱讀清單 `paper-list` ⭐126 · 📅2020-10
- 🔴 [awesome-VLM](https://github.com/Lab-LVM/awesome-VLM) — 依對比學習、PrefixLM、融合等方法整理的VLM論文集 `paper-list` ⭐7 · 📅2023-06

## 🔊 語音 / 音訊

- 🟢 [awesome-diarization](https://github.com/wq2012/awesome-diarization) — 涵蓋語者分段的論文、函式庫、資料集與評估工具的經典清單 `awesome` ⭐1.9k · 📅2026-06
- 🟢 [speech-trident](https://github.com/ga642381/speech-trident) — 語音/音訊LLM、表示學習與codec模型論文集 `paper-list` ⭐1.2k · 📅2026-06
- 🟢 [audio-ai-hub](https://github.com/BinWang28/audio-ai-hub) — 音訊大型語言模型的論文與資源集 `awesome` ⭐932 · 📅2026-06
- 🟢 [awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) — LLM應用於Audio AI的資源集 `awesome` ⭐732 · 📅2026-06
- 🟢 [Awesome-Speaker-Diarization](https://github.com/DongKeon/Awesome-Speaker-Diarization) — 體系化End-to-End/聚類/多模態等的論文集（活躍） `paper-list` ⭐362 · 📅2026-03
- 🟢 [awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) — OSS的TTS、語音複製與音樂生成模型集 `model` ⭐345 · 📅2026-04
- 🟢 [awesome-voice-conversion](https://github.com/JeffC0628/awesome-voice-conversion) — voice conversion（音質轉換）的專案與社群集 `awesome` ⭐267 · 📅2025-11
- 🟢 [Awesome-Sign-Language-Processing](https://github.com/VIPL-SLP/Awesome-Sign-Language-Processing) — 手語處理（辨識/翻譯/生成）的全面資源集 `awesome` ⭐250 · 📅2026-05
- 🟢 [Awesome-Sign-Language](https://github.com/ZechengLi19/Awesome-Sign-Language) — 手語辨識（SLR）、翻譯（SLT）等的論文清單（活躍） `paper-list` ⭐220 · 📅2025-11
- 🟢 [Speech-and-audio-papers-Top-Conference](https://github.com/01Zhangbw/Speech-and-audio-papers-Top-Conference) — 彙整頂會（INTERSPEECH/ICASSP等）的語音與音訊論文 `paper-list` ⭐140 · 📅2026-01
- 🟢 [awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech) — 基於LLM的speech-to-speech模型/框架集 `awesome` ⭐58 · 📅2025-11
- 🟢 [Awesome-Large-Speech-Model](https://github.com/huangcanan/Awesome-Large-Speech-Model) — 大規模語音/音訊模型的論文、資料、應用與工具集 `awesome` ⭐28 · 📅2025-11
- 🟡 [awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) — 應用於音樂的深度學習論文與學位論文集 `paper-list` ⭐3k · 📅2023-12
- 🟡 [INTERSPEECH-2023-24-Papers](https://github.com/DmitryRyumin/INTERSPEECH-2023-24-Papers) — 涵蓋INTERSPEECH 2023-2024論文的集合 `paper-list` ⭐687 · 📅2024-12
- 🟡 [ICASSP-2023-24-Papers](https://github.com/DmitryRyumin/ICASSP-2023-24-Papers) — 涵蓋ICASSP 2023-2024論文的集合 `paper-list` ⭐526 · 📅2025-05
- 🟡 [awesome-sound_event_detection](https://github.com/soham97/awesome-sound_event_detection) — Sound AI（音訊事件偵測、音訊描述等）的研究閱讀清單 `paper-list` ⭐198 · 📅2024-08
- 🟡 [awesome-speech-emotion-recognition](https://github.com/abikaki/awesome-speech-emotion-recognition) — 語音情緒辨識（SER）的論文、資料集與工具精選清單 `awesome` ⭐101 · 📅2024-12
- 🟡 [awesome-vad](https://github.com/bigcash/awesome-vad) — 彙整VAD的實作、工具與研究的清單 `awesome` ⭐75 · 📅2024-11
- 🟡 [Awesome-Speech-Enhancement](https://github.com/DmitryRyumin/Awesome-Speech-Enhancement) — 整理語音增強論文與效果指標的互動式清單 `paper-list` ⭐27 · 📅2024-04
- 📦 [awesome-tts-samples](https://github.com/seungwonpark/awesome-tts-samples) — 附語音樣本的TTS論文清單 `paper-list` ⭐61 · 📅2020-08
- 🔴 [awesome-speech-recognition-speech-synthesis-papers](https://github.com/zzw922cn/awesome-speech-recognition-speech-synthesis-papers) — 涵蓋ASR、語者驗證、TTS、語音合成與VC的論文清單 `paper-list` ⭐3.1k · 📅2023-10
- 🔴 [awesome-speech-enhancement](https://github.com/WenzheLiu-Speech/awesome-speech-enhancement) — speech enhancement、音源分離與定位的論文/程式碼/工具集 `paper-list` ⭐1.2k · 📅2023-11
- 🔴 [speech-synthesis-paper](https://github.com/wenet-e2e/speech-synthesis-paper) — 語音合成（TTS）論文的系統性清單 `paper-list` ⭐1.1k · 📅2023-07
- 🔴 [Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion](https://github.com/guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion) — 歌聲合成（SVS）、歌聲轉換（SVC）與自動採譜的論文/專案集 `paper-list` ⭐483 · 📅2022-09
- 🔴 [awesome-keyword-spotting](https://github.com/zycv/awesome-keyword-spotting) — 語音關鍵字偵測/喚醒詞偵測的論文、實作與資料集集 `awesome` ⭐287 · 📅2022-05
- 🔴 [awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) — 音樂資訊學的論文、教學、函式庫與工具精選清單 `awesome` ⭐193 · 📅2023-07
- 🔴 [awesome-speech-translation](https://github.com/dqqcasia/awesome-speech-translation) — 語音翻譯（管線/E2E/串流/多語言）的論文清單 `paper-list` ⭐179 · 📅2021-11
- 🔴 [awesome-speech-to-speech-translation](https://github.com/Rongjiehuang/awesome-speech-to-speech-translation) — 直接語音間翻譯（S2ST）論文清單 `paper-list` ⭐39 · 📅2023-01

## 🤖 機器人學 / Embodied AI

- 🟢 [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — embodied AI的VLA、VLN與多模態學習前沿研究集 `paper-list` ⭐3.3k · 📅2026-06
- 🟢 [awesome-robotics-libraries](https://github.com/jslee02/awesome-robotics-libraries) — 精選機器人函式庫與軟體的清單 `awesome` ⭐3k · 📅2026-06
- 🟢 [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — 人形機器人學習論文清單 `paper-list` ⭐2.5k · 📅2026-06
- 🟢 [Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — 涵蓋具身AI的感知、互動、agent與sim-to-real（IEEE/ASME ToM 2025） `survey` ⭐2.1k · 📅2026-06
- 🟢 [Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) — 運用LLM的embodied AI/機器人研究精選 `awesome` ⭐1.8k · 📅2026-06
- 🟢 [Awesome_Quadrupedal_Robots](https://github.com/curieuxjy/Awesome_Quadrupedal_Robots) — 四足機器人的論文與資源集 `paper-list` ⭐1.1k · 📅2026-06
- 🟢 [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) — 機器人操作的論文與程式碼集 `paper-list` ⭐1k · 📅2026-06
- 🟢 [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam) — VLA與World Action Model（WAM）研究精選 `awesome` ⭐743 · 📅2026-06
- 🟢 [Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) — 持續收集頂會錄取的Embodied AI論文（反映至2026會議，活躍） `paper-list` ⭐679 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) — embodied AI用VLA模型附綜述論文的清單 `survey` ⭐588 · 📅2026-06
- 🟢 [Awesome-VLA-Robotics](https://github.com/Jiaaqiliu/Awesome-VLA-Robotics) — 機器人VLA模型的論文、模型與資料集集 `paper-list` ⭐478 · 📅2026-03
- 🟢 [Awesome-Robotics-Diffusion](https://github.com/showlab/Awesome-Robotics-Diffusion) — 將diffusion model引入機器人學習的最新論文精選清單 `paper-list` ⭐340 · 📅2026-05
- 🟢 [Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI) — 涵蓋embodied AI綜述、VLA、資料集與模擬器等 `awesome` ⭐215 · 📅2026-06
- 🟢 [Awesome-VLN](https://github.com/KwanWaiPang/Awesome-VLN) — 視覺語言導航（VLN）綜述用論文集 `survey` ⭐146 · 📅2026-06
- 🟢 [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) — Vision-Language-Action（VLA）綜述用論文集 `survey` ⭐81 · 📅2026-02
- 🟢 [Awesome-Legged-Robot-Localization-and-Mapping](https://github.com/KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping) — 足式機器人SLAM相關綜述用論文集 `survey` ⭐64 · 📅2026-06
- 🟡 [Awesome-Robot-Learning](https://github.com/RayYoh/Awesome-Robot-Learning) — 機器人學習（主要為操作）的資源集 `awesome` ⭐203 · 📅2024-08
- 🔴 [awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling) — 彙整以C++/Python/ROS進行專業機器人開發工具的集合 `awesome` ⭐3.8k · 📅2023-11
- 🔴 [awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning) — 足式運動學習的資源集 `awesome` ⭐481 · 📅2023-07

## 🕸️ 圖學習(GNN) / 知識圖譜

- 🟢 [graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) — 圖/Transformer式詐欺、異常與離群偵測論文集 `paper-list` ⭐1.9k · 📅2026-05
- 🟢 [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) — 時序與時空資料用diffusion model的綜述與論文集（活躍） `survey` ⭐992 · 📅2026-02
- 🟢 [Awesome-DynamicGraphLearning](https://github.com/SpaceLearner/Awesome-DynamicGraphLearning) — 動態（時序）圖與知識圖譜上的機器學習論文集 `paper-list` ⭐710 · 📅2025-06
- 🟢 [awesome-gnn-systems](https://github.com/ch-wan/awesome-gnn-systems) — GNN系統與加速相關資源集 `awesome` ⭐344 · 📅2026-06
- 🟢 [awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation) — 生成式分子建模與設計的論文集 `paper-list` ⭐343 · 📅2026-06
- 🟢 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection) — 2025年TKDE綜述官方儲存庫，GNN式圖異常偵測論文與資料集 `survey` ⭐218 · 📅2026-06
- 🟢 [Awesome-TKGC](https://github.com/jiapuwang/Awesome-TKGC) — 以5階段分類涵蓋時序知識圖譜補全（TKGC）的論文與資源 `paper-list` ⭐116 · 📅2025-10
- 🟢 [awesome-molecular-diffusion-models](https://github.com/AzureLeon1/awesome-molecular-diffusion-models) — 分子diffusion model相關論文的精選清單（活躍） `paper-list` ⭐101 · 📅2026-04
- 🟢 [Awesome-Knowledge-Graph-Reasoning](https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning) — 知識圖譜推理的論文、程式碼與資料集集 `paper-list` ⭐4 · 📅2025-11
- 📑 [awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) — TKDE論文（對比/生成/預測型）的附帶清單 `survey` ⭐1.4k · 📅2024-08
- 📑 [Awesome-GNN4TS](https://github.com/KimMeen/Awesome-GNN4TS) — 時序分析用GNN（TPAMI 2024）的資源集 `survey` ⭐859 · 📅2024-08
- 📑 [awesome-pretrain-on-molecules](https://github.com/junxia97/awesome-pretrain-on-molecules) — 化學預訓練模型（IJCAI 2023 survey）的論文清單 `survey` ⭐539 · 📅2023-06
- 📑 [Generative_KG_Construction_Papers](https://github.com/zjunlp/Generative_KG_Construction_Papers) — 生成式知識圖譜構建綜述（EMNLP 2022）的論文集 `survey` ⭐113 · 📅2023-07
- 📑 [Awesome-Trustworthy-GNNs](https://github.com/Radical3-HeZhang/Awesome-Trustworthy-GNNs) — 可信賴GNN（隱私/穩健性/公平性/可解釋性）綜述（Proc. IEEE 2024） `survey` ⭐98 · 📅2024-07
- 🟡 [GNNPapers](https://github.com/thunlp/GNNPapers) — 圖神經網路（GNN）的必讀論文集（經典） `paper-list` ⭐16.8k · 📅2023-12
- 🟡 [Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) — 圖神經網路論文清單 `paper-list` ⭐2.3k · 📅2023-12
- 🟡 [awesome-self-supervised-gnn](https://github.com/ChandlerBang/awesome-self-supervised-gnn) — GNN預訓練與自監督學習論文集 `paper-list` ⭐1.7k · 📅2024-02
- 🟡 [GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) — 交通預測用GNN論文與程式碼的大規模集合 `paper-list` ⭐1.2k · 📅2024-08
- 🟡 [awesome-graph-transformer](https://github.com/wehos/awesome-graph-transformer) — graph transformer論文集 `paper-list` ⭐930 · 📅2025-03
- 🟡 [PromptKG](https://github.com/zjunlp/PromptKG) — 提示學習與知識圖譜相關的研究、工具與論文集 `paper-list` ⭐735 · 📅2024-03
- 🟡 [awesome-graph-generation](https://github.com/yuanqidu/awesome-graph-generation) — 涵蓋圖與分子生成論文的最新清單 `paper-list` ⭐360 · 📅2025-01
- 🟡 [Awesome-Hypergraph-Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network) — 超圖學習、理論、資料與工具的精選集 `awesome` ⭐332 · 📅2025-02
- 🟡 [Awesome-Fair-Graph-Learning](https://github.com/EdisonLeeeee/Awesome-Fair-Graph-Learning) — 公平圖學習（FairGL）的論文清單 `paper-list` ⭐144 · 📅2024-09
- 🟡 [Awesome-Temporal-Graph-Learning](https://github.com/MGitHubL/Awesome-Temporal-Graph-Learning) — temporal graph learning方法（論文、程式碼、資料集）集 `paper-list` ⭐92 · 📅2025-05
- 🟡 [Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) — 圖OOD（泛化、訓練時/測試時自適應）論文清單 `paper-list` ⭐85 · 📅2024-10
- 🟡 [Awesome-GNN-based-drug-discovery](https://github.com/gozsari/Awesome-GNN-based-drug-discovery) — 以GNN進行藥物開發（論文、資料集、工具）的精選清單 `awesome` ⭐64 · 📅2024-04
- 🟡 [HGNN_Collection](https://github.com/PolarisRisingWar/HGNN_Collection) — 異質圖NN的資料集與演算法集 `paper-list` ⭐62 · 📅2024-05
- 🟡 [awesome-GNN-social-recsys](https://github.com/claws-lab/awesome-GNN-social-recsys) — 基於GNN的社交推薦論文集 `paper-list` ⭐53 · 📅2024-05
- 🔴 [awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification) — 圖嵌入、分類與表示學習的重要論文集（附實作） `paper-list` ⭐4.8k · 📅2023-03
- 🔴 [awesome-network-embedding](https://github.com/chihming/awesome-network-embedding) — 網路嵌入方法的經典精選清單 `awesome` ⭐2.6k · 📅2020-12
- 🔴 [knowledge-graphs](https://github.com/shaoxiongji/knowledge-graphs) — 知識圖譜研究（嵌入、補全、時序KG、應用）論文集 `paper-list` ⭐1.8k · 📅2022-10
- 🔴 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection) — 以深度學習進行圖異常偵測的論文、資料集與實作集 `awesome` ⭐384 · 📅2023-07
- 🔴 [awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) — 小分子藥物開發用機器學習資源的精選集 `awesome` ⭐241 · 📅2023-11
- 🔴 [awesome-graph-ood](https://github.com/THUMNLab/awesome-graph-ood) — 圖OOD泛化相關論文集 `paper-list` ⭐169 · 📅2023-06
- 🔴 [awesome-expressive-gnn](https://github.com/mengliu1998/awesome-expressive-gnn) — GNN表達力相關研究與改善論文集 `paper-list` ⭐124 · 📅2023-11

## 🛒 推薦系統(RecSys)

- 🟢 [RSPapers](https://github.com/hongleizhang/RSPapers) — 以17個類別整理推薦系統必讀論文，每週更新（亦新增LLM/Agentic RS等） `awesome` ⭐6.5k · 📅2026-03
- 🟢 [Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) — 搜尋、推薦與廣告用深度學習論文集 `paper-list` ⭐2.5k · 📅2026-04
- 🟢 [Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys) — LLM相關推薦系統論文集（附TOIS錄取綜述） `survey` ⭐1.5k · 📅2026-01
- 🟢 [Awesome-LLM4RS-Papers](https://github.com/nancheng58/Awesome-LLM4RS-Papers) — LLM增強推薦系統論文集 `paper-list` ⭐764 · 📅2026-03
- 🟢 [Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) — 冷啟動推薦資源集（附LLM時代綜述） `survey` ⭐284 · 📅2026-03
- 📑 [LLM4Rec-Awesome-Papers](https://github.com/WLiK/LLM4Rec-Awesome-Papers) — 運用LLM的推薦系統論文與資源集（附綜述） `survey` ⭐2.3k · 📅2025-03
- 📑 [RecDebiasing](https://github.com/jiawei-chen/RecDebiasing) — TOIS 2023《Bias and Debias in Recommender System: A Survey》的去偏方法集 `survey` ⭐462 · 📅2024-02
- 📑 [Awesome-SSLRec-Papers](https://github.com/HKUDS/Awesome-SSLRec-Papers) — ACM CSUR《Self-Supervised Learning for Recommendation》綜述的companion `survey` ⭐123 · 📅2024-08
- 🔴 [Awesome-RSPapers](https://github.com/RUCAIBox/Awesome-RSPapers) — 推薦系統論文的全面清單 `paper-list` ⭐988 · 📅2022-10
- 🔴 [CRSPapers](https://github.com/RUCAIBox/CRSPapers) — 對話式推薦系統（CRS）的論文清單 `paper-list` ⭐80 · 📅2022-11
- 🔴 [Awesome-Sequence-Modeling-for-Recommendation](https://github.com/AiHubCN/Awesome-Sequence-Modeling-for-Recommendation) — 序列推薦與序列建模論文集 `paper-list` ⭐39 · 📅2023-11
- 🔴 [Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems](https://github.com/YuyingZhao/Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems) — 全面整理推薦系統的公平性與多樣性研究 `paper-list` ⭐25 · 📅2023-06

## 📈 時間序列(Time Series)

- 🟢 [awesome-time-series-papers](https://github.com/TSCenter/awesome-time-series-papers) — 頂級AI會議最新時序論文與程式碼集 `paper-list` ⭐1k · 📅2026-06
- 🟢 [Awesome_Imputation](https://github.com/WenjieDu/Awesome_Imputation) — 彙整時序缺失值補全（imputation）論文與方法的綜述儲存庫 `survey` ⭐421 · 📅2026-03
- 🟢 [awesome-time-series-forecasting](https://github.com/TongjiFinLab/awesome-time-series-forecasting) — 時序預測的論文與程式碼集 `paper-list` ⭐277 · 📅2026-06
- 🟢 [Awesome-Anomaly-Detection-Foundation-Models](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) — 以基礎模型進行異常偵測的論文集 `paper-list` ⭐199 · 📅2026-05
- 🟢 [awesome-multivariate-time-series-anomaly-detection-algorithms](https://github.com/lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms) — 多變量時序異常偵測論文清單 `paper-list` ⭐77 · 📅2025-09
- 🟢 [awesome-time-series-analysis](https://github.com/qhliu26/awesome-time-series-analysis) — 時序的論文、基準、資料集與教學集 `awesome` ⭐66 · 📅2025-09
- 📑 [time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) — 專門彙整時序用Transformer資源（論文、程式碼、資料）的綜述 `survey` ⭐3k · 📅2024-08
- 🟡 [awesome-TS-anomaly-detection](https://github.com/rob-med/awesome-TS-anomaly-detection) — 時序資料異常偵測工具與資料集的清單 `awesome` ⭐3.2k · 📅2024-10
- 🟡 [awesome-AI-for-time-series-papers](https://github.com/qingsongedu/awesome-AI-for-time-series-papers) — 頂會與期刊的時序AI論文、教學與綜述集 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) — 時序、時空與事件資料用LLM/基礎模型論文集 `paper-list` ⭐1.2k · 📅2024-12
- 🟡 [Awesome-TimeSeries-LLM-FM](https://github.com/start2020/Awesome-TimeSeries-LLM-FM) — 時序任務用LLM與基礎模型的資源集 `paper-list` ⭐154 · 📅2024-06
- 🟡 [Awesome-Large-Models-for-Time-Series](https://github.com/SJTU-DMTai/Awesome-Large-Models-for-Time-Series) — 時序分析用LLM與基礎模型論文集 `paper-list` ⭐47 · 📅2024-10

## 🦾 AI 代理 / LLM Agents

- 🟢 [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) — 86頁綜述《The Rise and Potential of LLM Based Agents》論文清單 `survey` ⭐8.2k · 📅2025-09
- 🟢 [LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) — LLM agent的必讀論文集 `paper-list` ⭐3k · 📅2026-06
- 🟢 [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) — LLM agent方法、應用與課題綜述論文集 `survey` ⭐2.8k · 📅2025-11
- 🟢 [LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) — LLM式agent相關論文清單 `paper-list` ⭐2.3k · 📅2025-07
- 🟢 [awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) — 多agent論文的精選集（Swarms team） `awesome` ⭐1.6k · 📅2026-06
- 🟢 [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — LLM agent框架的精選清單 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — AI agent研究論文集（工程、記憶、評估、工作流程） `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) — 多模態GUI agent的論文與資源集 `paper-list` ⭐1.2k · 📅2025-08
- 🟢 [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) — LLM驅動的自主agent集合 `awesome` ⭐1.2k · 📅2026-06
- 🟢 [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) — GUI agent論文的精選清單 `paper-list` ⭐818 · 📅2026-06
- 🟢 [Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) — 語言agent記憶（使用者檔案、對話歷史）相關論文集 `paper-list` ⭐569 · 📅2026-06
- 🟢 [awesome-computer-use](https://github.com/ranpox/awesome-computer-use) — Computer-use GUI agent的影片、部落格、論文與專案集 `awesome` ⭐563 · 📅2026-04
- 🟢 [awesome-ui-agents](https://github.com/opendilab/awesome-ui-agents) — 橫跨Web/App/OS的UI agent資源持續更新清單 `awesome` ⭐302 · 📅2026-06
- 🟢 [Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) — 圖式agent記憶的綜述、論文與基準集 `survey` ⭐294 · 📅2026-06
- 🟡 [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI自主agent（專案/框架）的大規模清單 `awesome` ⭐28.3k · 📅2025-02
- 🟡 [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) — LLM驅動agent的論文、儲存庫與部落格集 `awesome` ⭐2.2k · 📅2025-04
- 🟡 [LLM-Planning-Papers](https://github.com/AGI-Edgerunners/LLM-Planning-Papers) — LLM planning相關的必讀論文集 `paper-list` ⭐441 · 📅2024-07
- 🟡 [awesome-llm-agents](https://github.com/junhua/awesome-llm-agents) — LLM agent的高品質論文與OSS專案集 `paper-list` ⭐85 · 📅2024-11
- 🟡 [Awesome-LLM-based-MultiAgents](https://github.com/Andrewzh112/Awesome-LLM-based-MultiAgents) — LLM式多agent論文集 `paper-list` ⭐28 · 📅2024-10
- 🔴 [Multi-Agent-Papers](https://github.com/shizhl/Multi-Agent-Papers) — 複雜任務用多agent協作的必讀論文集 `paper-list` ⭐71 · 📅2023-11

## 🔬 醫療 AI / AI for Science

- 🟢 [MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) — 醫療LLM實務指南（刊於Nature Reviews Bioengineering） `survey` ⭐2k · 📅2025-09
- 🟢 [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) — 加速物理、化學、生物、材料等科學發現的AI工具與論文集 `awesome` ⭐1.6k · 📅2026-06
- 🟢 [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration) — 影像配準整體的書籍、論文與工具箱集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — 多模態學習應用於醫療影像的資源集 `awesome` ⭐966 · 📅2026-06
- 🟢 [Awesome-Healthcare-Foundation-Models](https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models) — 健康照護基礎模型的論文集合 `paper-list` ⭐517 · 📅2026-04
- 🟢 [awesome-foundation-model-single-cell-papers](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) — 專注於單細胞基礎模型的論文清單 `paper-list` ⭐470 · 📅2026-06
- 🟢 [Awesome-Radiology-Report-Generation](https://github.com/mk-runner/Awesome-Radiology-Report-Generation) — 放射報告生成的論文、資料集與工具集（非常活躍） `paper-list` ⭐445 · 📅2026-06
- 🟢 [Awesome-LWMs](https://github.com/jaychempan/Awesome-LWMs) — 大型氣象模型（LWMs）集合（AI4Earth） `awesome` ⭐361 · 📅2025-06
- 🟢 [awesome-AI4MolConformation-MD](https://github.com/AspirinCode/awesome-AI4MolConformation-MD) — 以生成AI/深度學習進行分子構型與分子動力學的論文集 `paper-list` ⭐296 · 📅2026-06
- 🟢 [Awesome-Earth-Artificial-Intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) — 地球科學AI的教學、軟體、資料集與論文集 `awesome` ⭐244 · 📅2026-05
- 🟢 [awesome-mmps](https://github.com/willxxy/awesome-mmps) — EEG/ECG/EMG等生理訊號×機器學習的資源與資料集集（活躍） `awesome` ⭐160 · 📅2026-02
- 🟢 [Awesome-Active-Learning-for-Medical-Image-Analysis](https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis) — 醫療影像分析主動學習綜述論文與程式碼 `survey` ⭐135 · 📅2025-06
- 🟢 [awesome-pathology](https://github.com/open-pathology/awesome-pathology) — 涵蓋數位/計算病理資源（自監督、特徵抽取、資料集等） `awesome` ⭐120 · 📅2026-02
- 🟢 [awesome-drug-discovery](https://github.com/yboulaamane/awesome-drug-discovery) — 專注於計算藥物開發方法的精選資源清單 `awesome` ⭐116 · 📅2026-05
- 🟢 [SurvivalAnalysisPapers](https://github.com/shi-ang/SurvivalAnalysisPapers) — 依類別整理存活分析的論文與資源（活躍） `paper-list` ⭐91 · 📅2026-06
- 🟢 [Awesome-DL-for-Medical-Imaging-Segmentation](https://github.com/faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation) — 醫療影像分割的深度學習論文集 `paper-list` ⭐66 · 📅2026-02
- 🟢 [awesome-bci-reviews](https://github.com/okbalefthanded/awesome-bci-reviews) — 依年代整理BCI經同儕審查的綜述（活躍） `survey` ⭐47 · 📅2025-08
- 🟢 [AwesomeWSI](https://github.com/BearCleverProud/AwesomeWSI) — WSI分析與病理基礎模型的全面集合（依IJCAI 2025綜述，活躍） `survey` ⭐34 · 📅2026-06
- 🟢 [Awesome-Generative-Models-in-Pathology](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology) — 病理中生成模型（影像合成、報告生成、跨模態）超過150篇的綜述 `survey` ⭐26 · 📅2026-06
- 🟢 [Awesome-MICCAI-2026](https://github.com/ambicuity/Awesome-MICCAI-2026) — 從arXiv自動收集MICCAI 2026論文由bot每日更新並依領域分類 `paper-list` ⭐25 · 📅2026-06
- 🟢 [Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) — 醫療用agentic AI最新綜述集 `paper-list` ⭐24 · 📅2026-03
- 🟢 [Awesome-AI4BCI](https://github.com/Deepak-Mewada/Awesome-AI4BCI) — 腦訊號編碼/解碼的深度學習模型資源集 `paper-list` ⭐17 · 📅2025-09
- 📑 [Awesome-Foundation-Models-in-Medical-Imaging](https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging) — 醫療影像視覺與語言基礎模型的精選清單 `survey` ⭐302 · 📅2024-06
- 📑 [Awesome-Foundation-Models-for-Weather-and-Climate](https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate) — 氣象與氣候資料理解用基礎模型的全面綜述 `survey` ⭐293 · 📅2025-02
- 📑 [Awesome-Foundation-Models-for-Advancing-Healthcare](https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare) — 健康照護基礎模型（HFM）課題、機會與未來展望的全面綜述 `survey` ⭐252 · 📅2024-12
- 📑 [DL-ECG-Review](https://github.com/hsd1503/DL-ECG-Review) — ECG深度學習方法綜述與論文摘要表 `survey` ⭐250 · 📅2020-10
- 📑 [MedImgReg_Survey](https://github.com/JHU-MedImage-Reg/MedImgReg_Survey) — 學習式醫療影像配準論文集，附損失函數/評估指標實作 `survey` ⭐121 · 📅2025-05
- 🟡 [awesome-deep-learning-single-cell-papers](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) — 依30多種任務整理單細胞分析×深度學習最新論文 `paper-list` ⭐858 · 📅2025-04
- 🟡 [awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning) — 蛋白質表示學習（含AlphaFold）論文集 `paper-list` ⭐684 · 📅2024-11
- 🟡 [Awesome-Medical-Large-Language-Models](https://github.com/burglarhobbit/Awesome-Medical-Large-Language-Models) — 精選醫療與健康照護領域LLM論文的集合 `paper-list` ⭐393 · 📅2025-05
- 🟡 [awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design) — AI式蛋白質設計的研究論文集 `paper-list` ⭐307 · 📅2024-05
- 🟡 [Awesome-LLM-Healthcare](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) — 對應醫療領域LLM綜述論文的論文清單 `paper-list` ⭐269 · 📅2023-12
- 🟡 [Awesome-Neuron-Segmentation-in-EM-Images](https://github.com/subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images) — 電子顯微鏡（EM）影像中神經突起3D分割資源集 `awesome` ⭐57 · 📅2024-03
- 🟡 [awesome-molecule-protein-pretrain-papers](https://github.com/OmicsML/awesome-molecule-protein-pretrain-papers) — 分子與蛋白質的預訓練論文集（藥物開發、docking） `paper-list` ⭐47 · 📅2024-03
- 🟡 [Awesome_AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) — 地球系統（特別是氣象與氣候）的機器學習論文集 `paper-list` ⭐14 · 📅2023-12
- 🔴 [MICCAI-OpenSourcePapers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) — 以附程式碼連結的表格整理MICCAI 2019-2023開源論文 `paper-list` ⭐1.3k · 📅2023-11
- 🔴 [awesome-ehr-deeplearning](https://github.com/hurcy/awesome-ehr-deeplearning) — EHR挖掘、機器學習與深度學習論文集 `awesome` ⭐430 · 📅2022-10
- 🔴 [Physiological-Signal-Classification-Papers](https://github.com/ziyujia/Physiological-Signal-Classification-Papers) — 依任務整理EEG/ECG/EMG/EOG的分類論文 `paper-list` ⭐250 · 📅2022-07
- 🔴 [awesome-radiology-report-generation](https://github.com/zhjohnchan/awesome-radiology-report-generation) — 放射/醫療報告生成與相關領域的精選清單 `awesome` ⭐180 · 📅2022-05
- 🔴 [awesome-structural-bioinformatics](https://github.com/twoXes/awesome-structural-bioinformatics) — 結構生物資訊學的資源集 `awesome` ⭐79 · 📅2023-05
- 🔴 [awesome-bio-chatgpt](https://github.com/OmicsML/awesome-bio-chatgpt) — ChatGPT/LLM應用於生物學與醫療領域的論文與資源集 `paper-list` ⭐22 · 📅2023-04

## 🌍 應用領域 (Code/Math/Finance/Law/科學)

- 🟢 [techniques](https://github.com/satellite-image-deep-learning/techniques) — 衛星與航空影像深度學習方法的超大規模參考資料 `awesome` ⭐10.2k · 📅2026-06
- 🟢 [awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) — 金融市場LLM、深度學習策略與工具的經典清單 `awesome` ⭐6.1k · 📅2026-06
- 🟢 [Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) — 程式碼用語言模型研究與資料集的全面精選 `paper-list` ⭐3.4k · 📅2026-05
- 🟢 [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) — RS變化偵測的資料集、方法與綜述集 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Remote-Sensing-Foundation-Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) — 涵蓋RSFM論文、資料集、基準與預訓練權重（活躍） `paper-list` ⭐1.9k · 📅2026-05
- 🟢 [awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) — 農業、農場與園藝用OSS技術（含ML、GIS、遙測、機器人）的經典清單 `awesome` ⭐1.8k · 📅2026-01
- 🟢 [awesome-search](https://github.com/frutik/awesome-search) — 以電商搜尋為主，涵蓋語意搜尋、LTR、查詢理解與搜尋品質 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) — 為約510個原子論機器學習專案評分排名（活躍） `awesome` ⭐692 · 📅2026-06
- 🟢 [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) — 數學、物理、化學、材料、生物、地球科學等科學領域預訓練模型的全面綜述 `survey` ⭐660 · 📅2025-06
- 🟢 [awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) — 現代材料科學中材料資訊學的相關工作集 `awesome` ⭐517 · 📅2026-03
- 🟢 [awesome-digital-humanities](https://github.com/dh-tech/awesome-digital-humanities) — 為人文學者提供的量化與計算方法軟體集（NLP、主題模型、文本分析） `awesome` ⭐387 · 📅2026-05
- 🟢 [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) — 整理從需求、開發、測試到維護全SE領域的LLM論文 `survey` ⭐330 · 📅2026-04
- 🟢 [awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) — 判決預測、合約分類、判例檢索、法務QA等LegalNLP資源集 `awesome` ⭐327 · 📅2025-10
- 🟢 [awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) — 收集頂會與期刊的教育用AI/LLM論文 `paper-list` ⭐191 · 📅2026-06
- 🟢 [awesome-pinns](https://github.com/AI-in-Transportation-Lab/awesome-pinns) — PINN/物理資訊機器學習的函式庫、論文與教學精選集 `awesome` ⭐120 · 📅2026-06
- 🟢 [PINN_Paper_List](https://github.com/Event-AHU/PINN_Paper_List) — 物理資訊神經網路（PINN）的論文清單 `paper-list` ⭐81 · 📅2026-04
- 📑 [FinLLMs](https://github.com/adlnlp/FinLLMs) — 論文《Large Language Models in Finance》的相關研究、基準與資料集集 `survey` ⭐373 · 📅2025-04
- 📑 [DL4TP](https://github.com/zhaoyu-li/DL4TP) — 深度學習應用於定理證明的調查，依autoformalization、proof search等分類 `survey` ⭐225 · 📅2025-05
- 📑 [awesome-RSFMs](https://github.com/xiaoaoran/awesome-RSFMs) — 綜述《Foundation Models for Remote Sensing and Earth Observation》官方儲存庫 `survey` ⭐51 · 📅2024-11
- 🟡 [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — 著重機器學習的量化/演算法交易資源集 `awesome` ⭐3.7k · 📅2025-05
- 🟡 [PINNpapers](https://github.com/idrl-lab/PINNpapers) — PINN必讀論文集，依並行化、加速、遷移學習、不確定性量化與應用整理 `paper-list` ⭐1.5k · 📅2023-12
- 🟡 [LLM4SoftwareTesting](https://github.com/LLM-Testing/LLM4SoftwareTesting) — 運用LLM進行測試生成、測試補全等的論文集 `paper-list` ⭐530 · 📅2024-01
- 🟡 [awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) — 將AI應用於電子設計自動化（EDA、晶片設計）的論文集 `paper-list` ⭐212 · 📅2023-12
- 🟡 [awesome-ai4lam](https://github.com/AI4LAM/awesome-ai4lam) — 圖書館、檔案館與博物館（GLAM/LAM）用AI的專案、案例與資源集（AI4LAM社群營運） `awesome` ⭐178 · 📅2024-06
- 🟡 [Awesome-LLM4Math](https://github.com/tongyx361/Awesome-LLM4Math) — LLM數學推理的高品質精選清單，整理訓練資料、SFT、RL與基準 `paper-list` ⭐157 · 📅2024-07
- 🟡 [Awesome-Education-LLM](https://github.com/Geralt-Targaryen/Awesome-Education-LLM) — 整理教育用LLM研究與應用（教學輔助、題目生成、自動評分等） `paper-list` ⭐77 · 📅2024-09
- 🟡 [LLM_X_papers](https://github.com/czyssrs/LLM_X_papers) — 持續更新金融、醫療、法務LLM論文的閱讀清單 `paper-list` ⭐54 · 📅2025-02
- 🔴 [awesome-machine-learning-on-source-code](https://github.com/src-d/awesome-machine-learning-on-source-code) — 將機器學習應用於原始碼（MLonCode）的論文與連結集 `awesome` ⭐6.6k · 📅2020-12
- 🔴 [Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) — 彙整司法AI用語料、基準、QA與摘要資料集 `awesome` ⭐304 · 📅2023-07
- 🔴 [awesome-program](https://github.com/shaohua0116/awesome-program) — 程式合成、歸納、執行、修復與programmatic RL的論文集 `paper-list` ⭐168 · 📅2021-10
- 🔴 [Awesome-Precision-Agriculture](https://github.com/px39n/Awesome-Precision-Agriculture) — 以UAV與深度學習進行產量預測、作物偵測、雜草偵測等的論文集 `paper-list` ⭐139 · 📅2020-09
- 🔴 [awesome-ai4chem](https://github.com/sherrylixuecheng/awesome-ai4chem) — 化學用AI論文的精選 `paper-list` ⭐49 · 📅2023-05
- 🔴 [Awesome-Sports-Analytics](https://github.com/wywyWang/Awesome-Sports-Analytics) — 足球、籃球、羽球等運動分析論文與程式碼集 `paper-list` ⭐20 · 📅2023-03

## 🚗 自動駕駛(Autonomous Driving)

- 🟢 [Birds-eye-view-Perception](https://github.com/OpenDriveLab/Birds-eye-view-Perception) — BEV感知研究與cookbook（IEEE T-PAMI 2023） `survey` ⭐1.4k · 📅2025-07
- 🟢 [Awesome-Trajectory-Motion-Prediction-Papers](https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers) — 軌跡與運動預測的全面論文集 `paper-list` ⭐1.1k · 📅2026-01
- 🟢 [awesome-end-to-end-autonomous-driving](https://github.com/opendilab/awesome-end-to-end-autonomous-driving) — 持續更新End-to-End自動駕駛資源的清單 `awesome` ⭐493 · 📅2026-06
- 📑 [Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) — 資料中心自動駕駛綜述官方儲存庫 `survey` ⭐179 · 📅2024-03
- 🟡 [awesome-lane-detection](https://github.com/amusi/awesome-lane-detection) — 車道偵測（lane detection）的論文清單 `paper-list` ⭐3.1k · 📅2024-08
- 🟡 [Awesome-Interaction-Aware-Trajectory-Prediction](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction) — 考量互動的軌跡預測前沿研究資料集 `paper-list` ⭐1.7k · 📅2024-09
- 🟡 [Awesome-Autonomous-Driving](https://github.com/autodriving-heart/Awesome-Autonomous-Driving) — 自動駕駛整體的awesome清單 `awesome` ⭐1.1k · 📅2024-08
- 🟡 [awesome-knowledge-driven-AD](https://github.com/PJLab-ADG/awesome-knowledge-driven-AD) — 知識驅動型自動駕駛的精選論文集 `paper-list` ⭐501 · 📅2024-06
- 🟡 [Awesome-Autonomous-Driving](https://github.com/PeterJaq/Awesome-Autonomous-Driving) — 自動駕駛整體的廣泛清單 `awesome` ⭐353 · 📅2024-08
- 🟡 [Awesome-occupancy-perception](https://github.com/autodriving-heart/Awesome-occupancy-perception) — 佔據感知（Occupancy）論文集合 `paper-list` ⭐308 · 📅2024-08
- 🟡 [CVPR-2024-Papers-Autonomous-Driving](https://github.com/autodriving-heart/CVPR-2024-Papers-Autonomous-Driving) — CVPR 2024的自動駕駛相關論文清單 `paper-list` ⭐257 · 📅2024-08
- 🟡 [CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI](https://github.com/autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI) — CVPR 2025的自動駕駛與具身AI相關論文清單 `paper-list` ⭐30 · 📅2025-04
- 🟡 [Awesome-4D-Radar](https://github.com/autodriving-heart/Awesome-4D-Radar) — 4D雷達感知相關論文與資源集 `paper-list` ⭐12 · 📅2024-02
- 🔴 [Awesome-Occupancy-Prediction-Autonomous-Driving](https://github.com/chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving) — 多相機語意佔據預測論文（Occ3D等） `paper-list` ⭐263 · 📅2023-07
- 🔴 [awesome-driving-behavior-prediction](https://github.com/opendilab/awesome-driving-behavior-prediction) — 駕駛行為預測的研究論文集 `paper-list` ⭐83 · 📅2022-12
- 🔴 [Awesome-BEV-Perception](https://github.com/autodriving-heart/Awesome-BEV-Perception) — BEV感知的精選論文集合 `paper-list` ⭐32 · 📅2023-06
- 🔴 [Awesome-Trajectory-Prediction](https://github.com/autodriving-heart/Awesome-Trajectory-Prediction) — 軌跡預測的論文集合 `paper-list` ⭐27 · 📅2023-06
- 🔴 [Awesome-BEV-Perception](https://github.com/ylhua/Awesome-BEV-Perception) — BEV感知相關論文（BEVFormer、PETRv2、FIERY等） `paper-list` ⭐5 · 📅2022-08

## 🛡️ AI 安全 / Alignment / 可解釋性

- 🟢 [awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) — 負責任ML與可解釋性的綜合資源清單 `awesome` ⭐4k · 📅2026-06
- 🟢 [Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) — LLM安全性的論文、文章、資料集與基準集 `awesome` ⭐1.9k · 📅2026-05
- 🟢 [awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) — ICDM/KDD/SDM等詐欺偵測資料探勘論文的經典清單 `paper-list` ⭐1.8k · 📅2026-01
- 🟢 [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) — 可解釋AI/ML的研究資料集 `paper-list` ⭐1.6k · 📅2026-03
- 🟢 [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) — LLM安全性的工具、文獻與專案集 `awesome` ⭐1.6k · 📅2025-08
- 🟢 [TAADpapers](https://github.com/thunlp/TAADpapers) — 文字對抗攻擊與防禦（TAAD）的必讀論文集 `paper-list` ⭐1.6k · 📅2025-06
- 🟢 [Awesome-Jailbreak-on-LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) — LLM越獄方法的論文、程式碼、資料集與評估集（非常活躍） `paper-list` ⭐1.4k · 📅2026-06
- 🟢 [awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) — machine unlearning綜述官方清單，涵蓋方法、資料集與評估指標 `awesome` ⭐955 · 📅2026-05
- 🟢 [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) — LLM machine unlearning的論文、綜述與基準集 `paper-list` ⭐598 · 📅2026-06
- 🟢 [awesome-trustworthy-deep-learning](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning) — OOD泛化、對抗樣本、後門等可信賴性論文（每日更新） `paper-list` ⭐387 · 📅2026-05
- 🟢 [membership-inference-machine-learning-literature](https://github.com/HongshengHu/membership-inference-machine-learning-literature) — 專注於成員推論攻擊的文獻集 `paper-list` ⭐372 · 📅2026-04
- 🟢 [Awesome-AI-for-cybersecurity](https://github.com/Billy1900/Awesome-AI-for-cybersecurity) — 涵蓋網路入侵偵測、防惡意軟體、WAF與防詐的AI清單 `awesome` ⭐256 · 📅2026-06
- 🟢 [Awesome-model-inversion-attack](https://github.com/AndrewZhou924/Awesome-model-inversion-attack) — 模型反演攻擊綜述官方清單，依CV/圖/NLP整理 `paper-list` ⭐221 · 📅2026-04
- 🟢 [Awesome-LMMs-Mechanistic-Interpretability](https://github.com/itsqyh/Awesome-LMMs-Mechanistic-Interpretability) — 探討大型多模態模型內部表示的mechanistic interpretability資源集（活躍） `survey` ⭐205 · 📅2026-03
- 🟢 [Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) — 依模態與用途整理生成AI的unlearning論文 `paper-list` ⭐188 · 📅2026-04
- 🟢 [Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) — 依影像、音訊、文字整理生成AI模型用浮水印方法（活躍） `awesome` ⭐142 · 📅2026-05
- 🟢 [awesome-mechanistic-interpretability](https://github.com/AI-in-Transportation-Lab/awesome-mechanistic-interpretability) — 將神經網路逆解析為可理解計算元素的mechanistic interpretability資源集 `awesome` ⭐110 · 📅2026-06
- 🟢 [awesome-fraud-detection](https://github.com/AI4Risk/awesome-fraud-detection) — 以GNN進行金融詐欺偵測的附綜述論文與程式碼集（活躍） `paper-list` ⭐44 · 📅2026-05
- 📑 [Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers) — LLM安全性綜述論文清單 `survey` ⭐55 · 📅2024-12
- 🟡 [awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) — 將ML用於惡意軟體、入侵偵測等的工具、論文與教材經典清單 `awesome` ⭐8.9k · 📅2024-08
- 🟡 [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) — 涵蓋prompt injection的實用與已提出防禦對策 `awesome` ⭐705 · 📅2025-02
- 🟡 [awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) — 涵蓋成員推論、模型反演、屬性推論與模型抽取的論文清單 `awesome` ⭐639 · 📅2024-03
- 🟡 [Awesome-Backdoor-in-Deep-Learning](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning) — 依攻擊類型與防禦階段整理深度學習後門攻擊與防禦的論文集（活躍） `paper-list` ⭐239 · 📅2024-03
- 🟡 [awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) — AI品質與安全性相關論文與技術文章的精選清單 `paper-list` ⭐216 · 📅2025-04
- 🟡 [OpenRedTeaming](https://github.com/Libr-AI/OpenRedTeaming) — LLM/多模態red teaming論文集（30+方法實作） `paper-list` ⭐167 · 📅2025-05
- 🟡 [trojai-literature](https://github.com/usnistgov/trojai-literature) — NIST營運的AI木馬攻擊研究文獻總覽 `paper-list` ⭐151 · 📅2024-10
- 🟡 [Learning-Deep-Hiding](https://github.com/TracyCuiq/Learning-Deep-Hiding) — 體系化整理含影像隱寫術與浮水印的「deep hiding」論文 `paper-list` ⭐67 · 📅2024-06
- 🟡 [Constitutional-AI-awesome-papers](https://github.com/minbeomkim/Constitutional-AI-awesome-papers) — Constitutional AI/倫理準則下AI的相關論文清單 `paper-list` ⭐13 · 📅2024-03
- 🔴 [awesome-adversarial-machine-learning](https://github.com/yenchenlin/awesome-adversarial-machine-learning) — 彙整對抗式機器學習論文、部落格與演講的經典精選 `awesome` ⭐1.9k · 📅2020-11
- 🔴 [awesome-interpretable-machine-learning](https://github.com/lopusz/awesome-interpretable-machine-learning) — 可解釋機器學習的資源清單 `awesome` ⭐917 · 📅2023-03
- 🔴 [awesome-fairness-in-ai](https://github.com/datamllab/awesome-fairness-in-ai) — AI公平性資源的精選集 `awesome` ⭐334 · 📅2023-09
- 🔴 [awesome-xai](https://github.com/altamiracorp/awesome-xai) — 可解釋AI（XAI）與可解釋ML的論文與資源 `awesome` ⭐190 · 📅2021-05
- 🔴 [awesome-ai-alignment](https://github.com/dit7ya/awesome-ai-alignment) — AI對齊研究優良資源的精選清單 `awesome` ⭐81 · 📅2023-07
- 🔴 [awesome-ml-fairness](https://github.com/brandeis-machine-learning/awesome-ml-fairness) — 機器學習公平性相關論文與資源集 `paper-list` ⭐74 · 📅2023-05
- 🔴 [awesome-ai-safety](https://github.com/hari-sikchi/awesome-ai-safety) — AI安全性的論文、專案與社群清單 `awesome` ⭐65 · 📅2020-02
- 🔴 [awesome-data-poisoning](https://github.com/ch-shin/awesome-data-poisoning) — 頂會的資料投毒攻擊與防禦論文集 `awesome` ⭐25 · 📅2022-09
- 🔴 [Awesome-Adversarial-Training](https://github.com/KululuMi/Awesome-Adversarial-Training) — FGSM/PGD/TRADES/AutoAttack等對抗訓練論文清單 `paper-list` ⭐6 · 📅2022-04

## ⚖️ AI 倫理 / 治理 / 法規 / Human-AI Interaction

- 🟢 [awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) — 依地區涵蓋各國AI法規、指引、倫理規範與標準 `awesome` ⭐1.4k · 📅2026-06
- 🟢 [awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) — 計算社會科學的書籍、課程與OSS資源全面清單（GESIS營運） `awesome` ⭐901 · 📅2026-05
- 🟢 [Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science) — 將LLM應用於社會科學的論文集 `paper-list` ⭐630 · 📅2026-06
- 🟢 [AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI) — 於17個領域彙整負責任AI的研究、書籍、法規、成熟度模型與工具 `awesome` ⭐130 · 📅2026-05
- 🟢 [Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) — 以心理測量觀點探討LLM人格、價值觀、心智理論與認知能力的論文集 `survey` ⭐115 · 📅2025-11
- 🔴 [NLP4SocialGood_Papers](https://github.com/zhijing-jin/NLP4SocialGood_Papers) — 社會公益用NLP論文的閱讀清單（救命、QoL、公平性等） `paper-list` ⭐310 · 📅2023-09
- 🔴 [awesome-HAI](https://github.com/bwang514/awesome-HAI) — 從HCI視角探討人類與AI互動設計的學術資料集 `awesome` ⭐297 · 📅2021-05

## ⚡ 高效化 (壓縮/量化/NAS/AutoML)

- 🟢 [Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) — iOS用Core ML模型的最大規模清單 `model` ⭐7k · 📅2025-06
- 🟢 [Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) — 模型量化的論文、程式碼與文件清單 `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) — 高效LLM（剪枝、量化、蒸餾等）的精選清單 `awesome` ⭐2k · 📅2025-06
- 🟢 [Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) — 量化、剪枝、蒸餾等LLM壓縮的論文與工具集 `awesome` ⭐1.8k · 📅2026-02
- 🟢 [tinyml-papers-and-projects](https://github.com/gigwegbe/tinyml-papers-and-projects) — TinyML的論文與專案集（活躍更新） `paper-list` ⭐1k · 📅2025-12
- 🟢 [awesome-AutoML](https://github.com/windmaple/awesome-AutoML) — AutoML精選清單 `awesome` ⭐938 · 📅2026-03
- 🟢 [awesome-ai-efficiency](https://github.com/PrunaAI/awesome-ai-efficiency) — AI模型加速、小型化與節能方法清單 `awesome` ⭐221 · 📅2026-06
- 🟢 [Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) — 裝置端AI系統（推理引擎/基準/論文），活躍 `awesome` ⭐159 · 📅2026-06
- 🟢 [awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) — 評估與減少AI環境影響的Green AI工具/論文經典清單 `awesome` ⭐114 · 📅2026-05
- 📑 [Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) — 與LLM知識蒸餾綜述連動的論文集 `survey` ⭐1.3k · 📅2025-03
- 🟡 [awesome-ml-model-compression](https://github.com/cedrickchee/awesome-ml-model-compression) — 模型壓縮與量化的研究論文、工具與學習資料 `awesome` ⭐545 · 📅2024-09
- 🟡 [awesome-nas-papers](https://github.com/jackguagua/awesome-nas-papers) — Neural Architecture Search論文彙整清單 `paper-list` ⭐405 · 📅2024-01
- 🔴 [deep-learning-model-convertor](https://github.com/ysh329/deep-learning-model-convertor) — 不同深度學習框架間模型轉換工具的一覽 `awesome` ⭐3.2k · 📅2023-06
- 🔴 [Awesome-Knowledge-Distillation](https://github.com/FLHonker/Awesome-Knowledge-Distillation) — 分類整理知識蒸餾論文（2014-2021） `paper-list` ⭐2.7k · 📅2023-05
- 🔴 [Awesome-AutoDL](https://github.com/D-X-Y/Awesome-AutoDL) — 自動深度學習（AutoDL）的資源與詳細分析 `awesome` ⭐2.3k · 📅2022-09
- 🔴 [awesome-emdl](https://github.com/csarron/awesome-emdl) — 嵌入式與行動深度學習的論文/函式庫/工具集 `awesome` ⭐769 · 📅2023-03
- 🔴 [awesome-edge-machine-learning](https://github.com/Bisonai/awesome-edge-machine-learning) — 涵蓋邊緣機器學習的論文、推理引擎、課題與書籍 `awesome` ⭐280 · 📅2023-02
- 🔴 [awesome-transformer-search](https://github.com/automl/awesome-transformer-search) — 結合Transformer與NAS的資源清單 `awesome` ⭐270 · 📅2023-06
- 🔴 [awesome-model-compression](https://github.com/ChanChiChoi/awesome-model-compression) — 模型壓縮（結構、蒸餾、二值化、量化、剪枝）論文集 `paper-list` ⭐166 · 📅2023-02
- 🔴 [NASPapers](https://github.com/NiuTrans/NASPapers) — 神經架構搜尋（NAS）的論文清單 `paper-list` ⭐135 · 📅2021-09
- 🔴 [awesome-compression-papers](https://github.com/chenbong/awesome-compression-papers) — 壓縮與加速（剪枝、量化、蒸餾、低秩分解）論文集 `paper-list` ⭐25 · 📅2020-10
- 🔴 [awesome-architecture-search](https://github.com/chenyaofo/awesome-architecture-search) — 最新追蹤NAS進展的論文清單 `paper-list` ⭐9 · 📅2022-05
- 🔴 [Awesome-NAS](https://github.com/Openning07/Awesome-NAS) — 神經架構搜尋（NAS）資源的精選 `awesome` ⭐1 · 📅2020-04

## 🔐 聯邦學習 / 隱私

- 🟢 [Awesome-Differential-Privacy-and-Meachine-Learning](https://github.com/JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning) — 運用差分隱私的聯邦學習與ML論文與實作 `paper-list` ⭐386 · 📅2025-09
- 🟢 [Awesome-ML-SP-Papers](https://github.com/gnipping/Awesome-ML-SP-Papers) — 安全四大頂會的ML Security & Privacy論文集 `paper-list` ⭐354 · 📅2025-11
- 🟡 [awesome-federated-learning](https://github.com/poga/awesome-federated-learning) — 聯邦學習與ML隱私的資源集 `awesome` ⭐547 · 📅2024-06
- 🟡 [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper) — 聯邦學習系統與框架的論文清單 `paper-list` ⭐75 · 📅2024-02
- 🔴 [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning) — 與FedML連動的聯邦學習研究與生產整合清單 `paper-list` ⭐2k · 📅2022-09
- 🔴 [awesome-secure-federated-learning-papers](https://github.com/csl-cqu/awesome-secure-federated-learning-papers) — 安全聯邦學習（攻擊、防禦、梯度反演）論文集 `paper-list` ⭐26 · 📅2023-03
- 🔴 [awesome-federated-learning](https://github.com/Willjay5991/awesome-federated-learning) — 聯邦學習的論文、文章、框架與講義資料 `awesome` ⭐2 · 📅2020-08

## ♻️ 持續學習(Continual Learning)

- 🟢 [Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning) — 增量學習、持續學習與災難性遺忘的主要會議論文集 `paper-list` ⭐4.5k · 📅2026-06
- 📑 [awesome-lifelong-learning-methods-for-llm](https://github.com/zzz47zzz/awesome-lifelong-learning-methods-for-llm) — LLM終身學習相關綜述與論文集 `survey` ⭐164 · 📅2025-05
- 🟡 [Best-Incremental-Learning](https://github.com/Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning) — 增量、持續與終身學習的儲存庫 `paper-list` ⭐608 · 📅2024-05
- 🟡 [Awesome-Continual-Learning](https://github.com/feifeiobama/Awesome-Continual-Learning) — 持續學習論文與BibTeX條目的精選清單 `paper-list` ⭐204 · 📅2024-10
- 🟡 [Awesome-Continual-Learning](https://github.com/lywang3081/Awesome-Continual-Learning) — 與持續學習綜述連動的論文清單與實用資源 `paper-list` ⭐108 · 📅2024-02
- 🔴 [awesome-lifelong-continual-learning](https://github.com/prprbr/awesome-lifelong-continual-learning) — 終身/持續學習的論文、部落格、資料集與軟體清單 `awesome` ⭐298 · 📅2021-03
- 🔴 [LLM-Continual-Learning-Papers](https://github.com/AGI-Edgerunners/LLM-Continual-Learning-Papers) — LLM持續學習（continual learning）的必讀論文集 `paper-list` ⭐150 · 📅2023-11

## 🖥️ ML 系統 / 訓練・推論基礎設施 / 資料

- 🟢 [AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) — 彙整AI系統論文與業界實務（OSDI/NSDI/MLSys等，含LLM與GenAI）的經典 `awesome` ⭐4.1k · 📅2025-07
- 🟢 [Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) — 以LLM進行合成資料生成的閱讀清單（活躍） `paper-list` ⭐1.5k · 📅2025-06
- 🟢 [rtdl](https://github.com/yandex-research/rtdl) — 表格資料深度學習的論文與套件集（Yandex Research） `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [ML4DB-paper-list](https://github.com/LumingSun/ML4DB-paper-list) — 以AI強化DB系統的論文集（學習式索引、查詢最佳化） `paper-list` ⭐774 · 📅2026-04
- 🟢 [ml-systems-papers](https://github.com/byungsoo-oh/ml-systems-papers) — 系統性收集ML系統領域論文的集合 `paper-list` ⭐619 · 📅2026-02
- 🟢 [awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) — 彙整AI系統論文及其程式碼的清單 `paper-list` ⭐365 · 📅2026-05
- 🟢 [awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) — 高維向量檢索與資料庫相關的精選清單（活躍） `awesome` ⭐353 · 📅2026-06
- 🟢 [Awesome-LLM-Inference-Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) — 依延遲/吞吐量/記憶體分類LLM推理最佳化方法的全面整理 `survey` ⭐213 · 📅2026-04
- 🟢 [Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) — 《Representation Learning for Tabular Data》綜述附帶清單 `survey` ⭐127 · 📅2026-06
- 🟢 [awesome-ai4db-paper](https://github.com/Wind-Gone/awesome-ai4db-paper) — AI4DB論文集（學習式索引、基數估計、學習式查詢最佳化、LLM×DB） `paper-list` ⭐112 · 📅2026-04
- 🟡 [data-augmentation-review](https://github.com/AgaMiko/data-augmentation-review) — 廣泛收集資料增強方法、函式庫與論文的綜述 `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-vector-search](https://github.com/currentslab/awesome-vector-search) — 向量檢索的函式庫、服務與論文集（Faiss、Annoy等） `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) — 大規模模型分散式訓練與推理相關專案與論文的精選清單 `awesome` ⭐279 · 📅2024-10
- 🟡 [awesome-synthetic-data](https://github.com/statice/awesome-synthetic-data) — OSS/商用合成資料工具精選清單（SDV等） `awesome` ⭐259 · 📅2024-01
- 🟡 [Awesome-LLM-Inference](https://github.com/DefTruth/Awesome-LLM-Inference) — LLM/VLM推理最佳化（FlashAttention、PagedAttention、MLA等）的論文與程式碼集 `paper-list` ⭐16 · 📅2025-03
- 🔴 [awesome-data-augmentation](https://github.com/CrazyVertigo/awesome-data-augmentation) — 資料增強方法（AugMix、CutMix等）的精選清單 `awesome` ⭐797 · 📅2021-03
- 🔴 [awesome-dl-hw-resources](https://github.com/RaviVijay/awesome-dl-hw-resources) — 深度學習用硬體/晶片設計資源的精選清單 `awesome` ⭐59 · 📅2018-05
- 🔴 [awesome-ml-testing](https://github.com/yqtian-se/awesome-ml-testing) — ML/深度學習系統測試相關的論文與工具集 `paper-list` ⭐47 · 📅2021-10
- 🔴 [Awesome-MLSys](https://github.com/dujiangsu/Awesome-MLSys) — 以大規模模型推理為主的MLSys領域學術論文集 `paper-list` ⭐6 · 📅2023-09

## 🛠️ MLOps / 資料中心 AI

- 🟢 [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) — ML部署、監控與擴展用OSS函式庫清單 `awesome` ⭐20.6k · 📅2026-06
- 🟢 [awesome-mlops](https://github.com/kelvins/awesome-mlops) — MLOps工具的精選清單 `awesome` ⭐5.2k · 📅2026-04
- 🟢 [Awesome-Dataset-Distillation](https://github.com/Guang000/Awesome-Dataset-Distillation) — 涵蓋梯度/分布匹配、生成方法與應用的經典清單（非常活躍） `awesome` ⭐1.9k · 📅2026-06
- 🟢 [awesome-data-centric-ai](https://github.com/Data-Centric-AI-Community/awesome-data-centric-ai) — 資料中心AI的OSS、教學與研究 `awesome` ⭐351 · 📅2026-04
- 🟢 [awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) — 涵蓋資料評估、資料歸因與資料選擇/剪枝/coreset `paper-list` ⭐120 · 📅2026-06
- 🟡 [awesome-mlops](https://github.com/visenger/awesome-mlops) — MLOps的參考文獻與資源集 `awesome` ⭐13.9k · 📅2024-11
- 🟡 [awesome-data-labeling](https://github.com/HumanSignal/awesome-data-labeling) — 精選資料標註工具的清單 `awesome` ⭐4.3k · 📅2024-06
- 🟡 [data-centric-AI](https://github.com/daochenzha/data-centric-AI) — 資料中心AI的資源精選清單 `awesome` ⭐1.1k · 📅2024-06
- 🟡 [data-centric-ai](https://github.com/HazyResearch/data-centric-ai) — 資料中心AI的資源集（Stanford HazyResearch） `awesome` ⭐1.1k · 📅2023-12
- 🟡 [Awesome-Coreset-Selection](https://github.com/PatrickZH/Awesome-Coreset-Selection) — coreset/子集選擇與data pruning的論文集 `awesome` ⭐184 · 📅2024-06
- 🔴 [releasing-research-code](https://github.com/paperswithcode/releasing-research-code) — ML研究程式碼公開的最佳實務（NeurIPS 2020官方推薦） `awesome` ⭐2.9k · 📅2023-05
- 🔴 [awesome-open-data-centric-ai](https://github.com/Renumics/awesome-open-data-centric-ai) — 非結構化資料用資料中心AI的OSS工具集 `awesome` ⭐732 · 📅2023-11

## 📊 資料集 / 基準測試

- 🟢 [Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) — LLM評估的工具、基準、排行榜與論文精選清單 `awesome` ⭐642 · 📅2025-11
- 🟢 [Awesome-Datasets-Hub](https://github.com/ahammadmejbah/Awesome-Datasets-Hub) — 醫療AI、NLP、多模態等LLM用資料集集 `awesome` ⭐138 · 📅2026-06
- 🟢 [Awesome-LLM-Benchmark](https://github.com/SihyeongPark/Awesome-LLM-Benchmark) — 大型語言模型用基準一覽 `awesome` ⭐12 · 📅2026-06
- 🟢 [awesome-llm-benchmarks](https://github.com/BenchGecko/awesome-llm-benchmarks) — LLM/AI模型的基準、資料集與排行榜集 `awesome` ⭐1 · 📅2026-03
- 🟡 [llm_benchmarks](https://github.com/leobeeson/llm_benchmarks) — LLM評估用基準與資料集的集合 `awesome` ⭐569 · 📅2024-07

## 官方論文集・論文入口(非 GitHub)

因非 GitHub 倉庫而未納入主清單，但作為一手來源十分有用的官方論文入口。

- [CVF Open Access](https://openaccess.thecvf.com/menu) — CVPR/ICCV/WACV 官方開放取用論文
- [ECVA / ECCV Papers](https://www.ecva.net/papers.php) — ECCV 官方論文(ECVA 開放取用)
- [Ke-Sen Huang's Home Page](https://kesen.realtimerendering.com/) — SIGGRAPH 等圖學論文連結的經典彙整
- [OpenReview](https://openreview.net/) — ICLR/NeurIPS 等審稿與錄取論文
- [ACL Anthology](https://aclanthology.org/) — NLP(ACL/EMNLP/NAACL 等)官方論文典藏
- [PMLR](https://proceedings.mlr.press/) — ICML/AISTATS/CoLT 等官方論文集
- [NeurIPS Proceedings](https://papers.nips.cc/) — NeurIPS 官方論文集
- [Papers with Code](https://paperswithcode.com/) — 論文 + 程式碼 + SOTA 排行榜
- [DBLP](https://dblp.org/) — 電腦科學論文書目資料庫
- [arXiv](https://arxiv.org/) — 預印本伺服器(cs.LG/cs.CV/cs.CL 等)

---

## 關於本倉庫

- 由各領域分工的調查代理橫跨 GitHub 蒐集，僅收錄確認存在的倉庫。
- star 數與最後更新為生成當下 GitHub API 的實際值；新鮮度標記可判別是否過時。
- 所有連結皆解析重新導向後統一為正規 URL。
- ⭐star・📅更新可透過 `./scripts/refresh.sh` 或 GitHub Actions(每週)重新生成與自動更新。

## 授權

本清單(彙整本身)以 [CC0 1.0](LICENSE)(公眾領域)釋出。各連結倉庫依其各自授權。

Generated with Claude Code
