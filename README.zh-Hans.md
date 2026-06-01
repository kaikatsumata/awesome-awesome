# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

**语言:** [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-lightgrey)](README.md) [![English](https://img.shields.io/badge/English-lightgrey)](README.en.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey)](README.ko.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-lightgrey)](README.zh-Hant.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-blue)](README.zh-Hans.md)

> 一份「列表的列表(awesome-of-awesome)」：横跨 AI 研究各领域，汇整并分类 **awesome 列表、survey 仓库、会议论文列表与特定模型合集**。

涵盖 CV / CG / NLP / RL 等所有领域，也纳入未冠 `awesome-` 的 survey 仓库(例如 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))与 `awesome-nanobanana-pro` 之类的特定模型范例集。

**共 902 条** / 33 个领域 — 🟢 活跃 441 条、🟡 中等 205 条(依 2026-06-01 的 GitHub 元数据自动生成)。

## 图例 / 收录标准

每条目均标注 **⭐star 数**与 **📅最后更新(年-月)**及新鲜度标记。除历史资料汇整外，均以更新时间与频率为重收录与排序。

| 标记 | 含义 |
|:--:|:--|
| 🟢 | 活跃(近 12 个月内更新) |
| 🟡 | 中等(13〜30 个月) |
| 🔴 | 停滞(超 30 个月未更新) |
| 📑 | 以同行评审 survey 论文为基础的汇整(覆盖性与权威性胜于更新频率，虽旧仍有用) |
| 📚 | 历史・经典合集(本即停止更新，不计新鲜度) |
| 📦 | 已归档(read-only) |

类型: `awesome`=精选列表 / `survey`=survey 论文附属 / `paper-list`=论文列表 / `model`=特定模型范例

> 详细元数据、完整结果与统计见 [docs/research-notes.md](docs/research-notes.md);制作方法见 [docs/best-practices.md](docs/best-practices.md)(日文)。

## 目录

- [🧠 机器学习通用 / 深度学习](#-机器学习通用--深度学习) (24)
- [📐 ML 理论 / 优化](#-ml-理论--优化) (12)
- [🎲 概率模型 / 贝叶斯 / 因果 / 不确定性](#-概率模型--贝叶斯--因果--不确定性) (17)
- [🏗️ 新架构 (SSM・Mamba・KAN・SNN・量子 ML)](#-新架构-ssmmambakansnn量子-ml) (24)
- [🌱 自监督 / 表征学习 / 基础模型](#-自监督--表征学习--基础模型) (6)
- [🎓 学习范式 (元学习/迁移/少样本/OOD/半监督)](#-学习范式-元学习迁移少样本ood半监督) (27)
- [👁️ 计算机视觉 (Computer Vision)](#-计算机视觉-computer-vision) (111)
- [🎨 计算机图形学 / 3D / 渲染](#-计算机图形学--3d--渲染) (65)
- [🖌️ 低层图像处理 / 复原 / 压缩](#-低层图像处理--复原--压缩) (22)
- [🎬 动漫・动画・插画・字体](#-动漫动画插画字体) (8)
- [💬 NLP / 大语言模型(LLM)](#-nlp--大语言模型llm) (98)
- [🖼️ 生成式 AI / Diffusion / 图像・视频生成](#-生成式-ai--diffusion--图像视频生成) (42)
- [🍌 特定模型的提示词・范例集](#-特定模型的提示词范例集) (21)
- [🧰 模型生态 / 运维工具 (MCP・LLMOps・LLM 应用)](#-模型生态--运维工具-mcpllmopsllm-应用) (25)
- [🎮 强化学习(RL)](#-强化学习rl) (35)
- [🔀 多模态 / VLM / MLLM](#-多模态--vlm--mllm) (30)
- [🔊 语音 / 音频](#-语音--音频) (28)
- [🤖 机器人学 / Embodied AI](#-机器人学--embodied-ai) (19)
- [🕸️ 图学习(GNN) / 知识图谱](#-图学习gnn--知识图谱) (35)
- [🛒 推荐系统(RecSys)](#-推荐系统recsys) (12)
- [📈 时间序列(Time Series)](#-时间序列time-series) (12)
- [🦾 AI 智能体 / LLM Agents](#-ai-智能体--llm-agents) (20)
- [🔬 医疗 AI / AI for Science](#-医疗-ai--ai-for-science) (41)
- [🌍 应用领域 (Code/Math/Finance/Law/科学)](#-应用领域-codemathfinancelaw科学) (33)
- [🚗 自动驾驶(Autonomous Driving)](#-自动驾驶autonomous-driving) (18)
- [🛡️ AI 安全 / Alignment / 可解释性](#-ai-安全--alignment--可解释性) (37)
- [⚖️ AI 伦理 / 治理 / 监管 / Human-AI Interaction](#-ai-伦理--治理--监管--human-ai-interaction) (7)
- [⚡ 高效化 (压缩/量化/NAS/AutoML)](#-高效化-压缩量化nasautoml) (23)
- [🔐 联邦学习 / 隐私](#-联邦学习--隐私) (7)
- [♻️ 持续学习(Continual Learning)](#-持续学习continual-learning) (7)
- [🖥️ ML 系统 / 训练・推理基础设施 / 数据](#-ml-系统--训练推理基础设施--数据) (19)
- [🛠️ MLOps / 数据中心 AI](#-mlops--数据中心-ai) (12)
- [📊 数据集 / 基准测试](#-数据集--基准测试) (5)


## 🧠 机器学习通用 / 深度学习

- 🟢 [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) — 按语言分类ML框架与库的经典精选列表 `awesome` ⭐72.6k · 📅2026-05
- 🟢 [awesome-datascience](https://github.com/academic/awesome-datascience) — 用于学习数据科学并应用于实际问题的经典资源集 `awesome` ⭐29.3k · 📅2026-05
- 🟢 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) — 辅助AI研究论文写作与润色的工具与资源集 `awesome` ⭐26.6k · 📅2026-05
- 🟢 [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources) — 涵盖异常检测的书籍、论文、视频与工具箱的经典列表 `awesome` ⭐9.3k · 📅2026-03
- 🟢 [kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) — 汇集Kaggle竞赛解法与思路的合集 `awesome` ⭐6.4k · 📅2026-05
- 🟢 [awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) — 精选Python数据科学软件的列表 `awesome` ⭐3.4k · 📅2026-04
- 🟢 [awesome-deeplearning-resources](https://github.com/endymecy/awesome-deeplearning-resources) — 按时间整理DL与深度强化学习的论文与代码 `paper-list` ⭐3k · 📅2026-01
- 🟢 [paperlists](https://github.com/papercopilot/paperlists) — Paper Copilot的整理数据,按年度JSON跨主要会议全面覆盖并持续更新(大型) `paper-list` ⭐933 · 📅2026-02
- 🟢 [ai-deadlines](https://github.com/huggingface/ai-deadlines) — 主要AI会议截止倒计时(paperswithcode版的后继,当前主流) `awesome` ⭐342 · 📅2026-05
- 🟢 [ai_papers_scrapper](https://github.com/george-gca/ai_papers_scrapper) — 按会议×年度获取主要AI会议(2017-)PDF、作者、摘要等的爬虫 `paper-list` ⭐52 · 📅2026-03
- 🟢 [ICML-2025-Papers](https://github.com/DmitryRyumin/ICML-2025-Papers) — 系统化ICML 2025录用论文并附代码实现链接 `paper-list` ⭐37 · 📅2025-10
- 📑 [awesome-AI-tutorials-surveys](https://github.com/qingsongedu/awesome-AI-tutorials-surveys) — 顶级AI会议的DL/ML/DM/CV/NLP/语音教程与综述集 `survey` ⭐165 · 📅2023-02
- 🟡 [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) — 汇集DL教程、项目与社区的经典列表 `awesome` ⭐28.3k · 📅2025-05
- 🟡 [Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) — 机器学习与深度学习的教程、文章与资源大规模集 `awesome` ⭐17.9k · 📅2024-06
- 🟡 [Conference-Accepted-Paper-List](https://github.com/Lionelsy/Conference-Accepted-Paper-List) — 汇集主要AI/ML/机器人会议2015-2025录用论文链接与截止信息(活跃) `paper-list` ⭐1.3k · 📅2025-01
- 🟡 [AAAI-2024-Papers](https://github.com/DmitryRyumin/AAAI-2024-Papers) — 涵盖AAAI 2024创新研究论文的合集 `paper-list` ⭐591 · 📅2025-01
- 🟡 [AI-Conference-Info](https://github.com/tranhungnghiep/AI-Conference-Info) — 跨年度汇集40余个主要AI会议录用率、投稿统计与截止信息 `awesome` ⭐165 · 📅2024-07
- 🟡 [Conference-Paper](https://github.com/hzxwonder/Conference-Paper) — 整理CCF-A会议录用论文,附标题、作者、URL与摘要 `paper-list` ⭐8 · 📅2024-04
- 📚 [Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) — 按学习顺序整理深度学习主要论文的经典路线图 `paper-list` ⭐39.5k · 📅2022-11
- 📚 [awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) — 2012-2016年引用最高的重要DL论文Top100 `paper-list` ⭐26.1k · 📅2024-01
- 🔴 [awesome-project-ideas](https://github.com/NirantK/awesome-project-ideas) — 汇集ML/NLP/Vision/推荐项目创意的列表 `awesome` ⭐9.1k · 📅2023-03
- 🔴 [awesome-ai-awesomeness](https://github.com/amusi/awesome-ai-awesomeness) — 汇集AI相关awesome列表的『awesome之awesome』 `awesome` ⭐979 · 📅2023-08
- 🔴 [Awesome-Paper-List](https://github.com/Doragd/Awesome-Paper-List) — 汇集NLP/CV/ML众多论文列表与相关资源的元列表 `awesome` ⭐194 · 📅2022-04
- 🔴 [awesome-machine-learning-papers](https://github.com/solaris33/awesome-machine-learning-papers) — 重要ML论文与仓库的精选列表 `paper-list` ⭐78 · 📅2017-06

## 📐 ML 理论 / 优化

- 🟢 [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) — 在36余个领域涵盖机器学习用于组合优化的论文(活跃) `paper-list` ⭐2.1k · 📅2026-05
- 🟢 [awesome-neuro-ai-papers](https://github.com/CYHSM/awesome-neuro-ai-papers) — 深度学习与神经科学交叉领域的论文与综述集(活跃) `paper-list` ⭐444 · 📅2026-01
- 🟢 [awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) — grokking、双下降、彩票假设等DL经验现象与理论论文列表 `paper-list` ⭐401 · 📅2026-05
- 🟡 [awesome-automl-papers](https://github.com/hibayesian/awesome-automl-papers) — AutoML论文、文章、教程与项目的经典大规模列表 `paper-list` ⭐4.1k · 📅2024-06
- 🟡 [must-read-papers-for-ml](https://github.com/hurshd0/must-read-papers-for-ml) — 面向数据科学与ML/DL工程师的必读论文集(含经典) `paper-list` ⭐1.4k · 📅2023-12
- 🟡 [NeuralTangentKernel-Papers](https://github.com/kwignb/NeuralTangentKernel-Papers) — Neural Tangent Kernel(NTK)相关论文汇集列表 `paper-list` ⭐122 · 📅2025-01
- 🟡 [awesome-language-model-analysis](https://github.com/Furyton/awesome-language-model-analysis) — 语言模型的理论与实证分析(涌现能力、scaling law、ICL理论、grokking) `paper-list` ⭐100 · 📅2024-12
- 🟡 [awesome-bayesian-optimization](https://github.com/materials-data-facility/awesome-bayesian-optimization) — 面向材料科学与化学的贝叶斯优化软件/论文/教程集 `awesome` ⭐50 · 📅2024-04
- 🔴 [Open-L2O](https://github.com/VITA-Group/Open-L2O) — 首个全面的L2O方法基准兼论文整理仓库 `paper-list` ⭐299 · 📅2023-06
- 🔴 [awesome-deep-neuroevolution](https://github.com/Alro10/awesome-deep-neuroevolution) — 将进化计算应用于深度学习的Deep Neuroevolution资源集 `awesome` ⭐227 · 📅2021-04
- 🔴 [Awesome-ScalingLaws](https://github.com/RZFan525/Awesome-ScalingLaws) — 专注LLM scaling law的资源集 `awesome` ⭐84 · 📅2023-04
- 🔴 [MLT-Papers](https://github.com/guoji-fu/MLT-Papers) — 机器学习理论(泛化界、优化、深度学习数学)论文列表 `paper-list` ⭐10 · 📅2022-02

## 🎲 概率模型 / 贝叶斯 / 因果 / 不确定性

- 🟢 [Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) — 对应ACM CSUR综述的diffusion、score-based与SDE生成模型论文分类 `survey` ⭐3.3k · 📅2025-09
- 🟢 [awesome-normalizing-flows](https://github.com/janosh/awesome-normalizing-flows) — 汇集normalizing flow论文、实现(PyTorch/JAX/Julia)与视频的代表性列表 `awesome` ⭐1.6k · 📅2026-03
- 🟢 [awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) — 汇集无分布不确定性量化(CP)视频、论文与库的充实列表 `awesome` ⭐1.2k · 📅2026-05
- 🟢 [awesome-uncertainty-deeplearning](https://github.com/ENSTA-U2IS-AI/awesome-uncertainty-deeplearning) — 涵盖深度学习预测不确定性估计综述、论文与代码的活跃列表 `awesome` ⭐811 · 📅2026-05
- 🟢 [awesome-flow-matching](https://github.com/dongzhuoyao/awesome-flow-matching) — 汇总flow matching与随机插值相关研究的活跃列表 `awesome` ⭐675 · 📅2026-04
- 🟢 [awesome-ebm](https://github.com/yataobian/awesome-ebm) — 按年代整理EBM论文、库与教程的活跃列表 `awesome` ⭐387 · 📅2026-04
- 🟡 [awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms) — 可复现因果推断与因果ML方法索引(含综述论文) `awesome` ⭐3.3k · 📅2025-01
- 🟡 [awesome-neural-ode](https://github.com/Zymrael/awesome-neural-ode) — 涵盖Neural ODE/SDE/CDE、动力系统、控制与数值解法交叉领域 `awesome` ⭐1.5k · 📅2024-09
- 🟡 [Awesome-GFlowNets](https://github.com/zdhNarsil/Awesome-GFlowNets) — 汇集GFlowNet基础论文、应用与教程的核心列表 `awesome` ⭐500 · 📅2024-10
- 🟡 [Awesome-Optimal-Transport-in-Deep-Learning](https://github.com/changwxx/Awesome-Optimal-Transport-in-Deep-Learning) — 汇集深度学习中最优传输的论文、代码与资料 `awesome` ⭐349 · 📅2024-05
- 🟡 [Awesome-VQVAE](https://github.com/wenhaochai/Awesome-VQVAE) — Vector Quantized VAE(VQ-VAE)及其应用相关论文与资源集 `awesome` ⭐330 · 📅2025-01
- 🔴 [Awesome-VAEs](https://github.com/matthewvowels1/Awesome-VAEs) — 汇集VAE、解耦、表示学习与生成模型约900篇论文 `paper-list` ⭐842 · 📅2021-07
- 🔴 [awesome-bayesian-deep-learning](https://github.com/robi56/awesome-bayesian-deep-learning) — 按年代整理贝叶斯深度学习论文与学位论文的经典列表 `awesome` ⭐416 · 📅2017-05
- 🔴 [awesome-optimal-transport](https://github.com/kilianFatras/awesome-optimal-transport) — 面向机器学习的最优传输(OT)论文、教程、库与书籍集 `awesome` ⭐246 · 📅2021-05
- 🔴 [Awesome-Causal-Inference](https://github.com/matthewvowels1/Awesome-Causal-Inference) — 按年代整理偏机器学习的因果推断与因果发现论文的文献列表 `paper-list` ⭐113 · 📅2021-05
- 🔴 [awesome-gaussian-processes](https://github.com/RaulPL/awesome-gaussian-processes) — 汇集学习高斯过程的书籍、视频、软件与论文 `awesome` ⭐42 · 📅2021-07
- 🔴 [Awesome-Causal-Discovery](https://github.com/CharonWangg/Awesome-Causal-Discovery) — 聚焦因果发现与因果表示学习的论文与书籍列表 `awesome` ⭐12 · 📅2023-11

## 🏗️ 新架构 (SSM・Mamba・KAN・SNN・量子 ML)

- 🟢 [awesome-kan](https://github.com/mintisan/awesome-kan) — 涵盖KAN库、实现、论文与教程的事实标准列表 `awesome` ⭐3.2k · 📅2026-06
- 🟢 [Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) — 持续更新顶会与期刊的SNN论文与代码 `paper-list` ⭐776 · 📅2026-03
- 🟢 [Mamba_State_Space_Model_Paper_List](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) — Mamba综述配套的按应用领域分类论文列表 `paper-list` ⭐752 · 📅2025-06
- 🟢 [Awesome-Mamba-Collection](https://github.com/XiudingCai/Awesome-Mamba-Collection) — 跨领域涵盖Mamba论文、教程与实现的代表性精选 `paper-list` ⭐734 · 📅2026-04
- 🟢 [Awesome-state-space-models](https://github.com/radarFudan/Awesome-state-space-models) — 汇集从S4到Mamba的状态空间模型偏理论论文的列表 `paper-list` ⭐621 · 📅2025-11
- 🟢 [Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) — 活跃更新双曲嵌入、双曲模型与应用的最新论文 `paper-list` ⭐595 · 📅2026-05
- 🟢 [awesome-snn-conference-paper](https://github.com/AXYZdong/awesome-snn-conference-paper) — 汇集SNN领域顶级会议与期刊论文及代码实现的列表 `paper-list` ⭐451 · 📅2026-05
- 🟢 [Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) — 面向LLM的高效架构(线性注意力、SSM、RWKV等)大规模综述 `survey` ⭐408 · 📅2025-11
- 🟢 [Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy) — 追踪LLM时代神经符号学习最新动向的列表 `paper-list` ⭐299 · 📅2025-06
- 🟢 [Efficient_Attention_Survey](https://github.com/attention-survey/Efficient_Attention_Survey) — 将高效注意力机制按硬件效率、稀疏、线性等分类的综述 `survey` ⭐298 · 📅2025-12
- 🟢 [Awesome_Mamba](https://github.com/xmindflow/Awesome_Mamba) — 医学图像分析中SSM综合综述对应列表 `survey` ⭐267 · 📅2025-07
- 🟢 [Awesome-RWKV-in-Vision](https://github.com/Yaziwel/Awesome-RWKV-in-Vision) — 汇集RWKV计算机视觉应用论文的列表 `paper-list` ⭐244 · 📅2025-06
- 🟢 [Awesome-Mamba-in-Vision](https://github.com/vgthengane/Awesome-Mamba-in-Vision) — 汇集计算机视觉领域的Mamba论文 `paper-list` ⭐36 · 📅2026-03
- 🟢 [Awesome_Modern_Hopfield_Networks](https://github.com/Event-AHU/Awesome_Modern_Hopfield_Networks) — 现代Hopfield网络的论文列表 `paper-list` ⭐27 · 📅2026-03
- 🟢 [Awesome-Linear-Attention-Survey](https://github.com/btzyd/Awesome-Linear-Attention-Survey) — 涉及线性注意力算法、理论、应用与基础设施的综述配套列表 `survey` ⭐12 · 📅2026-02
- 🟢 [KAN-Papers](https://github.com/RamtinMoslemi/KAN-Papers) — 从arXiv抽取的KAN论文完整列表 `paper-list` ⭐5 · 📅2026-05
- 🟡 [awesome-quantum-machine-learning](https://github.com/krishnakumarsekar/awesome-quantum-machine-learning) — 大规模收集QML的基础、算法、教材与项目 `awesome` ⭐3.6k · 📅2024-05
- 🟡 [awesome-quantum-ml](https://github.com/artix41/awesome-quantum-ml) — 在量子设备上运行的ML算法论文与资料精选 `paper-list` ⭐526 · 📅2024-06
- 🟡 [awesome-deeplogic](https://github.com/ccclyu/awesome-deeplogic) — 以NLP应用为中心的神经符号AI论文集 `paper-list` ⭐302 · 📅2024-08
- 🟡 [awesome-snn](https://github.com/coderonion/awesome-snn) — Spike-Driven-Transformer等公开SNN实现集 `model` ⭐233 · 📅2024-10
- 📦 [awesome-fast-attention](https://github.com/Separius/awesome-fast-attention) — 高效注意力模块的经典全面列表 `awesome` ⭐1k · 📅2021-08
- 🔴 [awesome-capsule-networks](https://github.com/sekwiatkowski/awesome-capsule-networks) — Dynamic Routing/EM Routing等胶囊网络主要论文与实现集 `awesome` ⭐975 · 📅2020-02
- 🔴 [awesome-neuromorphic-hw](https://github.com/open-neuromorphic/awesome-neuromorphic-hw) — SNN的ASIC/FPGA等神经形态硬件论文集 `paper-list` ⭐210 · 📅2023-11
- 🔴 [Neural-Symbolic-and-Probabilistic-Logic-Papers](https://github.com/thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers) — 神经符号与概率逻辑的论文精选 `paper-list` ⭐135 · 📅2023-09

## 🌱 自监督 / 表征学习 / 基础模型

- 🟢 [awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning) — 自监督学习方法的经典精选列表 `awesome` ⭐6.4k · 📅2026-02
- 🟢 [Awesome-Foundation-Models](https://github.com/uncbiag/Awesome-Foundation-Models) — 面向视觉与语言任务的基础模型精选列表 `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-LLM-VLM-Foundation-Models](https://github.com/srebroa/Awesome-LLM-VLM-Foundation-Models) — LLM、VLM与基础模型的精选列表 `awesome` ⭐6 · 📅2026-02
- 🟡 [awesome-contrastive-self-supervised-learning](https://github.com/asheeshcric/awesome-contrastive-self-supervised-learning) — 对比型自监督学习(SimCLR/VICReg等)论文集 `paper-list` ⭐1.3k · 📅2024-09
- 🟡 [Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) — 面向时间序列的自监督学习(SSL4TS)论文、代码与数据集 `paper-list` ⭐377 · 📅2024-04
- 🟡 [awesome-self-supervised-multimodal-learning](https://github.com/ys-zong/awesome-self-supervised-multimodal-learning) — 自监督多模态学习资源(与T-PAMI联动) `paper-list` ⭐278 · 📅2024-08

## 🎓 学习范式 (元学习/迁移/少样本/OOD/半监督)

- 🟢 [awesome-domain-adaptation](https://github.com/zhaoxin94/awesome-domain-adaptation) — 汇集域适应相关论文与代码的经典列表 `awesome` ⭐5.4k · 📅2025-12
- 🟢 [awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) — 涵盖SFDA/TTBA/TTIA/OTTA等测试时适应的经典列表 `awesome` ⭐1.3k · 📅2025-11
- 🟢 [Awesome-LongTailed-Learning](https://github.com/Vanint/Awesome-LongTailed-Learning) — 对应TPAMI2023综述,按类别再平衡/信息增强/模块改进分类 `survey` ⭐1k · 📅2025-11
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) — 涵盖OOD检测与泛化的基准、论文与库 `awesome` ⭐1k · 📅2026-04
- 🟢 [awesome-multi-task-learning](https://github.com/thuml/awesome-multi-task-learning) — 汇集MTL的数据集、代码库与论文(清华THUML) `awesome` ⭐837 · 📅2026-03
- 🟢 [awesome-active-learning](https://github.com/baifanxxx/awesome-active-learning) — 汇集主动学习论文、工具与基准的列表 `awesome` ⭐800 · 📅2026-03
- 🟢 [Awesome-Multi-Task-Learning](https://github.com/WeihongLi-ac/Awesome-Multi-Task-Learning) — 按时间整理多任务学习的最新论文 `paper-list` ⭐378 · 📅2026-03
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/shuolucs/Awesome-Out-Of-Distribution-Detection) — 对应ACM CSUR 2025录用任务导向OOD检测综述的论文列表 `survey` ⭐166 · 📅2026-01
- 🟢 [Awesome-OOD-VLM](https://github.com/AtsuMiyai/Awesome-OOD-VLM) — 对应视觉语言模型时代广义OOD检测综述(TMLR2025)的列表 `survey` ⭐101 · 📅2025-06
- 📑 [Awesome-Noisy-Labels](https://github.com/songhwanjun/Awesome-Noisy-Labels) — 对应噪声标签学习综述的论文列表 `survey` ⭐572 · 📅2023-02
- 🟡 [transferlearning](https://github.com/jindongwang/transferlearning) — 迁移学习领域最大规模仓库之一,涵盖论文、代码与数据集 `paper-list` ⭐14.3k · 📅2025-02
- 🟡 [Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise) — 涵盖噪声标签学习论文、代码与综述的最大规模列表 `awesome` ⭐2.7k · 📅2025-05
- 🟡 [awesome-semi-supervised-learning](https://github.com/yassouali/awesome-semi-supervised-learning) — 按CV/NLP/生成/图整理半监督学习论文与方法 `awesome` ⭐1.9k · 📅2024-05
- 🟡 [awesome-imbalanced-learning](https://github.com/ZhiningLiu1998/awesome-imbalanced-learning) — 综览类别不平衡/长尾学习论文、代码、框架与库 `awesome` ⭐1.5k · 📅2025-02
- 🟡 [awesome_OpenSetRecognition_list](https://github.com/gary23ai/awesome_OpenSetRecognition_list) — 汇集开放集识别、OOD与开放世界识别论文的经典列表 `paper-list` ⭐1.2k · 📅2024-03
- 🟡 [awesome-source-free-test-time-adaptation](https://github.com/YuejiangLIU/awesome-source-free-test-time-adaptation) — 测试时适应、测试时训练与无源域适应的论文列表 `paper-list` ⭐548 · 📅2024-06
- 🟡 [Awesome-Domain-Generalization](https://github.com/junkunyuan/Awesome-Domain-Generalization) — 汇集域泛化论文、代码与数据集的列表 `awesome` ⭐532 · 📅2025-04
- 🔴 [Awesome-Meta-Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning) — 涵盖元学习论文、代码、书籍、视频与数据集的经典列表 `awesome` ⭐1.6k · 📅2020-11
- 🔴 [awesome-zero-shot-learning](https://github.com/sbharadwajj/awesome-zero-shot-learning) — 汇集零样本学习论文、代码与资源的精选 `awesome` ⭐933 · 📅2021-07
- 🔴 [awesome-curriculum-learning](https://github.com/Openning07/awesome-curriculum-learning) — 按检测/分割/分类/迁移/RL对课程学习论文打标签 `awesome` ⭐247 · 📅2022-08
- 🔴 [Awesome-Weak-Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) — 程序化/规则化弱监督学习的论文与资源集 `awesome` ⭐194 · 📅2023-03
- 🔴 [awesome-distribution-shift](https://github.com/weitianxin/awesome-distribution-shift) — 分布偏移与基准的论文集 `awesome` ⭐128 · 📅2023-08
- 🔴 [awesome-few-shot-learning](https://github.com/indussky8/awesome-few-shot-learning) — 含标准数据集上对比结果的few-shot学习论文精选 `paper-list` ⭐126 · 📅2021-10
- 🔴 [Awesome-Zero-Shot-Learning](https://github.com/WilliamYi96/Awesome-Zero-Shot-Learning) — 汇总零样本学习最新论文与数据集进展的列表 `paper-list` ⭐85 · 📅2022-08
- 🔴 [Awesome-Failure-Detection](https://github.com/Impression2805/Awesome-Failure-Detection) — 统一处理OOD检测与误分类检测(failure detection)的论文列表 `paper-list` ⭐53 · 📅2023-10
- 🔴 [Awesome-compositional-zero-shot-learning](https://github.com/uqzhichen/Awesome-compositional-zero-shot-learning) — 专注组合零样本学习(属性与物体组合泛化)的论文列表 `paper-list` ⭐11 · 📅2022-07
- 🔴 [awsome-domain-adaptation](https://github.com/cmhungsteve/awsome-domain-adaptation) — 对域适应相关论文分类整理的广泛引用列表 `awesome` ⭐1 · 📅2019-09

## 👁️ 计算机视觉 (Computer Vision)

- 🟢 [CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) — CVPR 2026论文与开源项目的大规模汇集(经典) `paper-list` ⭐22.6k · 📅2026-03
- 🟢 [awesome-industrial-anomaly-detection](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) — 工业图像异常/缺陷检测的论文与数据集集(非常活跃) `awesome` ⭐3.6k · 📅2026-05
- 🟢 [awesome-hand-pose-estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation) — 手部姿态估计/跟踪(含3D)的经典列表 `awesome` ⭐3.4k · 📅2025-12
- 🟢 [Awesome-Super-Resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) — 汇集超分辨率相关论文、数据与代码库 `awesome` ⭐3.1k · 📅2026-04
- 🟢 [Awesome-Deblurring](https://github.com/subeeshvasu/Awesome-Deblurring) — 汇集图像与视频去模糊资源的列表 `awesome` ⭐2.9k · 📅2025-06
- 🟢 [ICCV2025-Papers-with-Code](https://github.com/amusi/ICCV2025-Papers-with-Code) — ICCV 2025论文与开源项目集 `paper-list` ⭐2.9k · 📅2025-07
- 🟢 [Awesome-Crowd-Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) — 人群计数的经典列表,含数据集与代码且活跃 `awesome` ⭐2.6k · 📅2026-01
- 🟢 [awesome-multiple-object-tracking](https://github.com/luanshiyinyang/awesome-multiple-object-tracking) — 整理MOT综述论文、按年算法与数据集 `awesome` ⭐1.5k · 📅2025-10
- 🟢 [awesome-grounding](https://github.com/TheShadow29/awesome-grounding) — 图像/视频/3D的指代表达与grounding论文集 `paper-list` ⭐1.1k · 📅2025-09
- 🟢 [SAM4MIS](https://github.com/YichiZhang98/SAM4MIS) — SAM应用于医学图像分割的论文与开源项目摘要 `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary](https://github.com/jianzongwu/Awesome-Open-Vocabulary) — TPAMI 2024《Towards Open Vocabulary Learning: A Survey》的配套 `survey` ⭐998 · 📅2026-05
- 🟢 [ICCV-2023-25-Papers](https://github.com/DmitryRyumin/ICCV-2023-25-Papers) — ICCV 2023-2025录用论文精选 `paper-list` ⭐964 · 📅2025-11
- 🟢 [top-cvpr-2025-papers](https://github.com/SkalskiP/top-cvpr-2025-papers) — 精选CVPR 2025重点论文的合集 `paper-list` ⭐878 · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary-Semantic-Segmentation](https://github.com/Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation) — 开放词汇/零样本语义分割论文列表 `paper-list` ⭐877 · 📅2026-05
- 🟢 [Awesome-Referring-Image-Segmentation](https://github.com/MarkMoHR/Awesome-Referring-Image-Segmentation) — 指代图像分割的论文与数据集集 `awesome` ⭐822 · 📅2026-01
- 🟢 [Awesome-Skeleton-based-Action-Recognition](https://github.com/firework8/Awesome-Skeleton-based-Action-Recognition) — 每月更新的基于骨架的行为识别论文列表 `paper-list` ⭐711 · 📅2026-05
- 🟢 [HOI-Learning-List](https://github.com/DirtyHarryLYL/HOI-Learning-List) — 涵盖数据集、基准与论文的HOI学习列表(活跃) `awesome` ⭐710 · 📅2025-10
- 🟢 [Awesome-Scene-Graph-Generation](https://github.com/ChocoWu/Awesome-Scene-Graph-Generation) — 涵盖LLM/非LLM方法、2D/3D/视频的活跃场景图生成列表 `awesome` ⭐671 · 📅2026-05
- 🟢 [Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC](https://github.com/Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC) — 汇集主要会议AIGC相关论文与代码 `paper-list` ⭐664 · 📅2026-05
- 🟢 [Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation](https://github.com/zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation) — 跨时序行为检测、提案生成与弱监督收集 `paper-list` ⭐587 · 📅2026-05
- 🟢 [Awesome-Gaze-Estimation](https://github.com/cvlab-uob/Awesome-Gaze-Estimation) — 视线估计论文的精选列表 `awesome` ⭐535 · 📅2025-06
- 🟢 [Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization) — 图像协调化的论文、代码与资源集(活跃) `awesome` ⭐532 · 📅2026-02
- 🟢 [Awesome-Video-Object-Segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation) — VOS的最新论文、数据集与项目集 `awesome` ⭐498 · 📅2026-05
- 🟢 [Awesome-Face-Restoration](https://github.com/TaoWangzj/Awesome-Face-Restoration) — 汇集人脸修复方法论文与代码库的列表 `paper-list` ⭐491 · 📅2026-03
- 🟢 [awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) — 伪装/隐蔽目标检测的精选资源集 `awesome` ⭐477 · 📅2025-12
- 🟢 [Awesome-Object-Pose-Estimation](https://github.com/CNJianLiu/Awesome-Object-Pose-Estimation) — IJCV2026综述《Deep Learning-Based Object Pose Estimation》的项目主页 `survey` ⭐421 · 📅2026-01
- 🟢 [Awesome_Long_Form_Video_Understanding](https://github.com/ttengwang/Awesome_Long_Form_Video_Understanding) — 专注长视频的论文与数据集集 `paper-list` ⭐377 · 📅2025-10
- 🟢 [awesome-described-object-detection](https://github.com/Charles-Xie/awesome-described-object-detection) — Described/Open-Vocabulary目标检测与指代表达理解的论文集 `paper-list` ⭐354 · 📅2025-11
- 🟢 [awesome-concealed-object-segmentation](https://github.com/ChunmingHe/awesome-concealed-object-segmentation) — 隐蔽物体分割的资源集 `awesome` ⭐340 · 📅2026-01
- 🟢 [Awesome-Visual-Grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) — TPAMI 2025综述,涵盖REC/phrase grounding/grounding MLLM(活跃) `survey` ⭐313 · 📅2025-11
- 🟢 [Awesome-3D-Visual-Grounding](https://github.com/liudaizong/Awesome-3D-Visual-Grounding) — 专注3D视觉grounding论文(活跃) `paper-list` ⭐281 · 📅2026-01
- 🟢 [Awesome-Multimodal-Referring-Segmentation](https://github.com/henghuiding/Awesome-Multimodal-Referring-Segmentation) — 多模态指代分割列表 `awesome` ⭐249 · 📅2026-05
- 🟢 [awesome-micro-expression-recognition](https://github.com/Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition) — 微表情(micro-expression)识别、检测与spotting的论文集 `paper-list` ⭐180 · 📅2025-08
- 🟢 [awesome-video-self-supervised-learning](https://github.com/Malitha123/awesome-video-self-supervised-learning) — 视频中自监督学习方法的论文集 `paper-list` ⭐171 · 📅2026-03
- 🟢 [Awesome-SAM2](https://github.com/GuoleiSun/Awesome-SAM2) — 面向图像与视频的SAM2论文与代码集 `paper-list` ⭐150 · 📅2025-10
- 🟢 [Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference) — 顶级国际会议发表的事件/脉冲相机论文集 `paper-list` ⭐118 · 📅2026-04
- 🟢 [awesome-3d-anomaly-detection](https://github.com/M-3LAB/awesome-3d-anomaly-detection) — 点云与多模态3D异常检测的综述仓库 `awesome` ⭐113 · 📅2026-06
- 🟢 [TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding](https://github.com/iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding) — 基于MLLM的视频时序grounding(VTG-LLM)的最新论文、代码与数据集 `paper-list` ⭐91 · 📅2025-11
- 🟢 [Awesome-MultiModal-Visual-Object-Tracking](https://github.com/Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking) — RGBT/RGBD/RGBE等多模态视觉目标跟踪综述 `survey` ⭐84 · 📅2026-04
- 🟢 [Awesome-Temporal-Video-Grounding](https://github.com/Tangkfan/Awesome-Temporal-Video-Grounding) — VMR/TVG/TSGV的论文列表 `paper-list` ⭐39 · 📅2025-12
- 🟢 [awesome-captioning-evaluation](https://github.com/aimagelab/awesome-captioning-evaluation) — MLLM时代图像描述评估相关论文集 `paper-list` ⭐34 · 📅2025-11
- 📑 [Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) — IJCV 2023综述,系统化LiDAR/相机/多模态3D检测 `survey` ⭐609 · 📅2023-05
- 📑 [Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) — 深度图像复原/增强中先验的综述 `survey` ⭐87 · 📅2025-05
- 📑 [360_Survey](https://github.com/vlislab22/360_Survey) — 全方位视觉(深度估计、3D重建、分割)的综合综述 `survey` ⭐23 · 📅2024-12
- 🟡 [Awesome-Transformer-Attention](https://github.com/cmhungsteve/Awesome-Transformer-Attention) — 涵盖ViT/Attention的极其全面的论文列表 `paper-list` ⭐5k · 📅2024-07
- 🟡 [Awesome-Visual-Transformer](https://github.com/dk-liang/Awesome-Visual-Transformer) — 汇集面向CV的Transformer论文的合集 `awesome` ⭐3.6k · 📅2025-01
- 🟡 [awesome-ocr](https://github.com/kba/awesome-ocr) — OCR与手写文字识别(HTR)的软件、库与文献集(历史文献数字化核心) `awesome` ⭐3.1k · 📅2024-07
- 🟡 [ECCV2024-Papers-with-Code](https://github.com/amusi/ECCV2024-Papers-with-Code) — ECCV 2024论文与开源项目集 `paper-list` ⭐2.3k · 📅2024-08
- 🟡 [SOTA-MedSeg](https://github.com/JunMa11/SOTA-MedSeg) — 基于各类挑战赛的SOTA医学图像分割方法集 `paper-list` ⭐1.7k · 📅2023-12
- 🟡 [Awesome-Edge-Detection-Papers](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers) — 边缘/轮廓/边界检测论文与工具箱集 `paper-list` ⭐1.6k · 📅2024-12
- 🟡 [Awesome-person-re-identification](https://github.com/bismex/Awesome-person-re-identification) — 涵盖有监督/无监督/跨模态ReID的大规模论文列表 `awesome` ⭐1.3k · 📅2024-06
- 🟡 [awesome-point-cloud-registration](https://github.com/XuyangBai/awesome-point-cloud-registration) — 按匹配策略整理的点云配准论文集 `paper-list` ⭐948 · 📅2024-07
- 🟡 [Awesome-Computer-Vision-Paper-List](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List) — 可跨顶会检索已录用论文的论文列表 `paper-list` ⭐761 · 📅2024-04
- 🟡 [Awesome-Optical-Flow](https://github.com/hzwer/Awesome-Optical-Flow) — 光流及相关研究的论文列表 `awesome` ⭐648 · 📅2024-11
- 🟡 [awesome-diffusion-models-in-low-level-vision](https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision) — 面向超分/修复等低层视觉的diffusion model论文集 `paper-list` ⭐553 · 📅2025-02
- 🟡 [CVPR-2023-24-Papers](https://github.com/DmitryRyumin/CVPR-2023-24-Papers) — 按主题整理的CVPR 2023/2024录用论文 `paper-list` ⭐450 · 📅2024-07
- 🟡 [awesome-ocr-resources](https://github.com/ZumingHuang/awesome-ocr-resources) — 汇集OCR论文与数据集的资源集 `awesome` ⭐431 · 📅2025-01
- 🟡 [Awesome-Segment-Anything](https://github.com/Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything) — Segment Anything Model(SAM)相关论文与项目集 `paper-list` ⭐372 · 📅2024-12
- 🟡 [awesome-temporal-action-segmentation](https://github.com/nus-cvml/awesome-temporal-action-segmentation) — 时序行为分割的论文与数据集集(活跃) `paper-list` ⭐250 · 📅2024-04
- 🟡 [Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — 聚焦2020年以来单目深度估计论文的列表 `paper-list` ⭐210 · 📅2024-10
- 🟡 [Awesome-Gait-Recognition](https://github.com/BNU-IVC/Awesome-Gait-Recognition) — 步态识别的论文与数据集集(收录CVPR'25等,活跃) `paper-list` ⭐187 · 📅2025-05
- 🟡 [awesome-salient-object-detection](https://github.com/visionxiang/awesome-salient-object-detection) — 包含RGB-D等的显著性目标检测资源集 `awesome` ⭐148 · 📅2024-09
- 🟡 [awesome-3D-scene-graphs](https://github.com/DennisRotondi/awesome-3D-scene-graphs) — 含机器人应用的3D场景图专门列表 `awesome` ⭐109 · 📅2024-12
- 🟡 [WACV-2024-Papers](https://github.com/DmitryRyumin/WACV-2024-Papers) — 系统整理WACV 2024论文的合集 `paper-list` ⭐97 · 📅2024-09
- 🟡 [awesome-human-visual-attention](https://github.com/aimagelab/awesome-human-visual-attention) — saliency、scanpath、注视预测与视觉注意力的论文/资源集 `paper-list` ⭐66 · 📅2025-05
- 📚 [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) — 汇集CV全领域的书籍、讲义、论文、工具与数据集的经典列表 `awesome` ⭐23.3k · 📅2024-05
- 📚 [really-awesome-semantic-segmentation](https://github.com/nightrome/really-awesome-semantic-segmentation) — 语义分割论文列表(2018年起停止更新) `paper-list` ⭐404 · 📅2018-03
- 🔴 [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) — 语义分割的经典资源集 `awesome` ⭐10.8k · 📅2021-05
- 🔴 [awesome-object-detection](https://github.com/amusi/awesome-object-detection) — 汇集R-CNN系列、YOLO、SSD等目标检测论文/实现的经典列表 `awesome` ⭐7.5k · 📅2022-12
- 🔴 [awesome-Face_Recognition](https://github.com/ChanChiChoi/awesome-Face_Recognition) — 涵盖人脸检测/识别/重建/生成等的大规模论文集 `paper-list` ⭐4.7k · 📅2023-02
- 🔴 [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition) — 涵盖行为识别及相关领域资源的经典列表 `awesome` ⭐4k · 📅2023-05
- 🔴 [awesome-image-classification](https://github.com/weiaicunzai/awesome-image-classification) — 2014年以来的深度学习图像分类论文/实现列表 `paper-list` ⭐3.1k · 📅2022-04
- 🔴 [awesome-deep-text-detection-recognition](https://github.com/hwalsuklee/awesome-deep-text-detection-recognition) — 整理基于深度学习的文本检测/识别论文 `paper-list` ⭐2.5k · 📅2021-08
- 🔴 [awesome-human-pose-estimation](https://github.com/cbsudux/awesome-human-pose-estimation) — 人体姿态估计的论文与资源集 `awesome` ⭐2.5k · 📅2022-10
- 🔴 [awesome-cbir-papers](https://github.com/willard-yuan/awesome-cbir-papers) — 经典与代表性的基于内容图像检索(CBIR)论文集 `paper-list` ⭐1.8k · 📅2023-10
- 🔴 [multi-object-tracking-paper-list](https://github.com/SpyderXu/multi-object-tracking-paper-list) — 多目标跟踪论文列表与源代码集 `paper-list` ⭐1.7k · 📅2020-04
- 🔴 [Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) — 专注场景文本定位与识别的资源集 `awesome` ⭐1.7k · 📅2018-07
- 🔴 [awesome-tiny-object-detection](https://github.com/kuanhungchen/awesome-tiny-object-detection) — Tiny Object Detection(微小目标检测)的论文与资源集 `paper-list` ⭐1.6k · 📅2023-10
- 🔴 [awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation) — 2D/3D人体姿态估计相关论文集 `paper-list` ⭐1.4k · 📅2020-08
- 🔴 [awesome-image-captioning](https://github.com/zhjohnchan/awesome-image-captioning) — 按年份整理的图像描述生成及相关领域资源 `awesome` ⭐1.1k · 📅2023-03
- 🔴 [activityrecognition](https://github.com/jindongwang/activityrecognition) — 行为识别(activity recognition)的资料、代码与数据集集 `paper-list` ⭐930 · 📅2019-08
- 🔴 [awesome-face](https://github.com/polarisZhao/awesome-face) — 人脸相关算法、数据集与论文的精选 `awesome` ⭐915 · 📅2019-08
- 🔴 [Awesome-Face-Forgery-Generation-and-Detection](https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection) — 人脸伪造的生成与检测相关论文与代码集 `paper-list` ⭐780 · 📅2022-11
- 🔴 [Awesome-Temporal-Action-Localization](https://github.com/Alvin-Zeng/Awesome-Temporal-Action-Localization) — temporal action localization/detection/proposal的论文与基准汇总 `paper-list` ⭐589 · 📅2022-09
- 🔴 [awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) — 实用度量学习及其应用的精选 `awesome` ⭐520 · 📅2023-04
- 🔴 [Awesome-Image-Matting](https://github.com/wchstrife/Awesome-Image-Matting) — 基于深度学习的抠图论文与代码精选列表 `awesome` ⭐438 · 📅2023-11
- 🔴 [Awesome-Visual-Captioning](https://github.com/forence/Awesome-Visual-Captioning) — 聚焦图像/视频描述与Seq2Seq学习的论文集 `paper-list` ⭐410 · 📅2022-11
- 🔴 [Awesome-3D-Detectors](https://github.com/Hub-Tian/Awesome-3D-Detectors) — 以LiDAR为中心的3D检测方法论文与代码集 `paper-list` ⭐398 · 📅2022-02
- 🔴 [Awesome-Super-Resolution](https://github.com/ptkin/Awesome-Super-Resolution) — 超分辨率资源精选 `awesome` ⭐386 · 📅2019-09
- 🔴 [Awesome-FAS](https://github.com/RizhaoCai/Awesome-FAS) — 人脸反欺骗/PAD/liveness论文的全面合集 `paper-list` ⭐383 · 📅2022-08
- 🔴 [awesome-depth](https://github.com/scott89/awesome-depth) — 汇集深度估计出版物的精选列表 `paper-list` ⭐337 · 📅2020-09
- 🔴 [Awesome-generalizable-6D-object-pose](https://github.com/liuyuan-pal/Awesome-generalizable-6D-object-pose) — 可泛化6DoF物体姿态估计的最新论文集 `paper-list` ⭐328 · 📅2023-04
- 🔴 [Awesome-Vision-Transformer-Collection](https://github.com/GuanRunwei/Awesome-Vision-Transformer-Collection) — 汇集ViT变体与下游任务的合集 `awesome` ⭐256 · 📅2022-07
- 🔴 [Awesome-Fine-grained-Visual-Classification](https://github.com/haoweiz23/Awesome-Fine-grained-Visual-Classification) — 细粒度视觉分类(FGVC)的论文合集 `paper-list` ⭐241 · 📅2023-09
- 🔴 [Awesome-Person-Re-Identification](https://github.com/FDU-VTS/Awesome-Person-Re-Identification) — 包含数据集与综述的行人重识别列表 `awesome` ⭐205 · 📅2021-12
- 🔴 [6d-object-pose-estimation](https://github.com/GeorgeDu/6d-object-pose-estimation) — 6D物体姿态估计的论文与代码汇总 `paper-list` ⭐204 · 📅2023-06
- 🔴 [awesome-optical-flow-algorithm](https://github.com/antran89/awesome-optical-flow-algorithm) — 从经典方法到RAFT等深度学习的光流算法集 `awesome` ⭐159 · 📅2022-10
- 🔴 [awesome-video-understanding](https://github.com/sujiongming/awesome-video-understanding) — 视频分类、行为识别与视频数据集资源集 `awesome` ⭐143 · 📅2017-12
- 🔴 [Awesome-Video-Captioning](https://github.com/tgc1997/Awesome-Video-Captioning) — 视频描述生成的论文集 `paper-list` ⭐121 · 📅2021-01
- 🔴 [awesome-360-vision](https://github.com/hsientzucheng/awesome-360-vision) — 360度视觉全领域论文集 `paper-list` ⭐121 · 📅2019-01
- 🔴 [Awesome-3D-Semantic-Segmentation](https://github.com/vvincenttttt/Awesome-3D-Semantic-Segmentation) — 3D语义分割的论文与代码集 `paper-list` ⭐74 · 📅2022-09
- 🔴 [Awesome-Events-Deep-Learning](https://github.com/vlislab2022/Awesome-Events-Deep-Learning) — 面向事件相机的深度学习资源集 `awesome` ⭐62 · 📅2023-09
- 🔴 [awesome-vqa-latest](https://github.com/Taaccoo/awesome-vqa-latest) — 持续更新VQA论文的阅读列表 `paper-list` ⭐52 · 📅2022-08
- 🔴 [awesome-rec](https://github.com/daqingliu/awesome-rec) — 专用于Referring Expression Comprehension(REC)的论文列表 `paper-list` ⭐46 · 📅2021-05
- 🔴 [awesome-image-retrieval-papers](https://github.com/lgbwust/awesome-image-retrieval-papers) — 图像检索论文与实现的全面合集 `paper-list` ⭐36 · 📅2018-12
- 🔴 [TSGV-Learning-List](https://github.com/Huntersxsx/TSGV-Learning-List) — TSGV/NLVL/VMR的相关研究汇总 `paper-list` ⭐31 · 📅2022-03
- 🔴 [awesome-computer-vision-papers](https://github.com/tzxiang/awesome-computer-vision-papers) — CV与深度学习相关论文及资源的列表 `awesome` ⭐26 · 📅2020-09
- 🔴 [awesome-hyperspectral-image-classification](https://github.com/immortal13/awesome-hyperspectral-image-classification) — 高光谱图像分类的论文与代码集 `paper-list` ⭐20 · 📅2023-07
- 🔴 [Awesome-image-captioning](https://github.com/luo3300612/Awesome-image-captioning) — ICCV/ECCV/CVPR等图像描述生成论文列表 `paper-list` ⭐8 · 📅2019-09
- 🔴 [Awesome-3D-Human-Pose-Estimation](https://github.com/bsridatta/Awesome-3D-Human-Pose-Estimation) — 专注于3D人体姿态估计的论文合集 `paper-list` ⭐5 · 📅2021-04
- 🔴 [Awesome-Human-Object-Interaction-Detection](https://github.com/KainingYing/Awesome-Human-Object-Interaction-Detection) — 按会议与年份整理的HOI检测论文集 `paper-list` ⭐3 · 📅2021-08

## 🎨 计算机图形学 / 3D / 渲染

- 🟢 [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) — 汇集3DGS论文、实现、查看器与工具的全面列表 `awesome` ⭐8.7k · 📅2026-05
- 🟢 [awesome-neural-rendering](https://github.com/weihaox/awesome-neural-rendering) — neural rendering与可微渲染的资料集 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — 使用隐式表示、NeRF与3DGS的SLAM论文集 `paper-list` ⭐2k · 📅2026-05
- 🟢 [awesome-digital-human](https://github.com/weihaox/awesome-digital-human) — 2D/3D/4D人体建模与虚拟形象生成综合集 `awesome` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis) — talking face合成的广泛资源集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion) — 面向3D生成的diffusion model论文集 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing) — 点云处理的库、软件与资料集 `awesome` ⭐798 · 📅2025-11
- 🟢 [awesome-dust3r](https://github.com/ruili3/awesome-dust3r) — DUSt3R系列几何基础模型论文与资源追踪 `model` ⭐792 · 📅2025-11
- 🟢 [Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D) — AIGC 3D(生成、纹理、材质)论文集 `awesome` ⭐776 · 📅2026-05
- 🟢 [awesome-ray-tracing](https://github.com/dannyfritz/awesome-ray-tracing) — ray tracing的论文、课程与实现列表 `awesome` ⭐657 · 📅2025-10
- 🟢 [Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — Text-to-3D/Diffusion-to-3D研究精选 `paper-list` ⭐587 · 📅2026-05
- 🟢 [awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) — 3D图形库精选 `awesome` ⭐524 · 📅2026-05
- 🟢 [Awesome-4D-Spatial-Intelligence](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) — 从视频重建4D空间智能的综述 `survey` ⭐497 · 📅2026-05
- 🟢 [awesome-simulation](https://github.com/Housz/awesome-simulation) — CG物理仿真资源整理 `awesome` ⭐388 · 📅2026-03
- 🟢 [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) — 从arXiv每日自动更新的3DGS论文追踪 `paper-list` ⭐287 · 📅2026-06
- 🟢 [Awesome-Transformer-based-SLAM](https://github.com/KwanWaiPang/Awesome-Transformer-based-SLAM) — 基于Transformer的SLAM的综述用论文集 `survey` ⭐270 · 📅2026-05
- 🟢 [Awesome-3DGS-SLAM](https://github.com/KwanWaiPang/Awesome-3DGS-SLAM) — 面向3DGS SLAM综述的论文集 `survey` ⭐261 · 📅2026-02
- 🟢 [Awesome-Learning-based-VO-VIO](https://github.com/KwanWaiPang/Awesome-Learning-based-VO-VIO) — 基于学习的视觉里程计(VO/VIO)的综述用论文集 `survey` ⭐195 · 📅2026-04
- 🟢 [awesome-geometry-processing](https://github.com/zishun/awesome-geometry-processing) — 几何处理的库、工具与资料集 `awesome` ⭐174 · 📅2026-03
- 🟢 [Awesome-SIGGRAPH-Computational-Optics](https://github.com/zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics) — SIGGRAPH计算光学论文的阅读列表 `paper-list` ⭐104 · 📅2026-04
- 🟢 [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation) — 3D重建与生成的论文与数据集集 `paper-list` ⭐78 · 📅2026-03
- 🟢 [awesome-dynamic-NeRF](https://github.com/pdaicode/awesome-dynamic-NeRF) — 面向动态场景的NeRF论文集 `paper-list` ⭐67 · 📅2026-04
- 🟢 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey) — 四边形网格剖分相关论文、代码与项目集 `survey` ⭐37 · 📅2026-05
- 🟢 [Awesome-Diffusion-based-SLAM](https://github.com/KwanWaiPang/Awesome-Diffusion-based-SLAM) — 基于diffusion model的SLAM的综述用论文集 `survey` ⭐34 · 📅2026-05
- 🟢 [awesome-brep-reconstruction](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) — B-rep(边界表示)重建的论文与开源项目集,定期更新 `survey` ⭐29 · 📅2026-01
- 🟢 [Awesome-Event-based-SLAM](https://github.com/KwanWaiPang/Awesome-Event-based-SLAM) — 基于事件的SLAM的综述用论文集 `survey` ⭐21 · 📅2026-01
- 🟢 [offset-mesh-survey](https://github.com/Bigger-and-Stronger/offset-mesh-survey) — 偏移网格生成相关论文、项目与代码的持续更新综述 `survey` ⭐13 · 📅2026-05
- 🟢 [awesome-3d-medial-axis](https://github.com/Bigger-and-Stronger/awesome-3d-medial-axis) — 中轴(medial axis)/骨架及其应用的论文与开源集,定期更新 `survey` ⭐5 · 📅2025-10
- 🟢 [direction-field-survey](https://github.com/Bigger-and-Stronger/direction-field-survey) — 方向场(direction field)相关论文、项目与代码的持续更新综述 `survey` ⭐4 · 📅2026-05
- 🟢 [parameterization-survey](https://github.com/Bigger-and-Stronger/parameterization-survey) — 网格参数化相关论文、项目与代码的持续更新综述 `survey` ⭐2 · 📅2026-05
- 📑 [Gen3D](https://github.com/weihaox/Gen3D) — 深度生成式3D-aware图像合成的综述(CSUR 2023) `survey` ⭐164 · 📅2025-02
- 📑 [boundary-layer-generation-survey](https://github.com/Bigger-and-Stronger/boundary-layer-generation-survey) — 边界层网格生成相关论文、项目与代码的持续更新综述 `survey` ⭐3 · 📅2025-02
- 🟡 [3D-Machine-Learning](https://github.com/timzhang642/3D-Machine-Learning) — 3D机器学习(点云/网格/体素/SDF等)的资源仓库 `awesome` ⭐10.2k · 📅2024-07
- 🟡 [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) — Neural Radiance Fields论文的经典精选列表 `awesome` ⭐6.8k · 📅2025-01
- 🟡 [awesome-implicit-representations](https://github.com/vsitzmann/awesome-implicit-representations) — DeepSDF等隐式神经表示的资料集 `awesome` ⭐2.6k · 📅2024-02
- 🟡 [awesome-point-cloud-analysis-2023](https://github.com/NUAAXQ/awesome-point-cloud-analysis-2023) — 每日更新2017年以来点云分析论文的列表 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-Talking-Face](https://github.com/JosephPai/Awesome-Talking-Face) — 专注talking face的精选 `awesome` ⭐1.5k · 📅2024-12
- 🟡 [awesome-3d-reconstruction-papers](https://github.com/bluestyle97/awesome-3d-reconstruction-papers) — 深度学习时代的3D重建论文集 `paper-list` ⭐910 · 📅2023-12
- 🟡 [awesome-taichi](https://github.com/taichi-dev/awesome-taichi) — 用Taichi制作的仿真(流体、布料等)应用集 `awesome` ⭐683 · 📅2024-06
- 🟡 [awesome-3dbody-papers](https://github.com/3DFaceBody/awesome-3dbody-papers) — 3D人体(SMPL等)的论文集 `paper-list` ⭐661 · 📅2024-01
- 🟡 [awesome-4d-generation](https://github.com/cwchenwang/awesome-4d-generation) — 4D生成(text-to-4D等)论文列表 `paper-list` ⭐331 · 📅2024-10
- 🟡 [Awesome-Avatars](https://github.com/pansanity666/Awesome-Avatars) — 人类虚拟形象的生成、重建与编辑最新进展 `paper-list` ⭐276 · 📅2024-04
- 🟡 [Awesome-Inverse-Rendering](https://github.com/ingra14m/Awesome-Inverse-Rendering) — 基于neural field的逆渲染论文集 `paper-list` ⭐258 · 📅2024-12
- 🟡 [Awesome-InverseRendering](https://github.com/tkuri/Awesome-InverseRendering) — 本征分解与逆渲染论文列表 `paper-list` ⭐234 · 📅2025-04
- 🟡 [awesome-3dgs](https://github.com/pdaicode/awesome-3dgs) — 3DGS相关论文精选 `paper-list` ⭐123 · 📅2024-08
- 🟡 [awesome-avatar](https://github.com/Jason-cs18/awesome-avatar) — talking-face/talking-body相关资源集 `awesome` ⭐59 · 📅2024-11
- 🟡 [Awesome-3D-Human-Motion-Generation](https://github.com/Run542968/Awesome-3D-Human-Motion-Generation) — 以Text-to-Motion为中心的人体动作生成论文集 `paper-list` ⭐25 · 📅2024-07
- 🟡 [awesome-dynamic-scene-representations](https://github.com/yklcs/awesome-dynamic-scene-representations) — 动态场景表示的资料集 `paper-list` ⭐8 · 📅2024-04
- 🟡 [awesome-visualization](https://github.com/Bigger-and-Stronger/awesome-visualization) — 记录CG相关数据可视化方法与渲染案例的仓库 `awesome` ⭐1 · 📅2025-03
- 🔴 [awesome_3DReconstruction_list](https://github.com/openMVG/awesome_3DReconstruction_list) — 从图像进行3D重建的经典论文与资料集 `awesome` ⭐4.4k · 📅2021-10
- 🔴 [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis) — 点云分析与处理相关论文及数据集列表 `awesome` ⭐4.2k · 📅2023-05
- 🔴 [awesome-visual-slam](https://github.com/tzutalin/awesome-visual-slam) — 视觉SLAM/视觉里程计的开源与论文集 `awesome` ⭐2.4k · 📅2022-05
- 🔴 [awesome-slam](https://github.com/kanster/awesome-slam) — SLAM的教程、项目与社区集 `awesome` ⭐1.7k · 📅2020-07
- 🔴 [awesome-3D-generation](https://github.com/justimyhxu/awesome-3D-generation) — 3D生成论文的精选列表 `awesome` ⭐1.2k · 📅2023-03
- 🔴 [awesome-graphics](https://github.com/ericjang/awesome-graphics) — CG教程与论文综合列表 `awesome` ⭐1.1k · 📅2020-02
- 🔴 [Awesome-SLAM](https://github.com/SilenceOverflow/Awesome-SLAM) — 持续更新的SLAM论文列表 `paper-list` ⭐1.1k · 📅2023-10
- 🔴 [3D-Reconstruction-with-Deep-Learning-Methods](https://github.com/natowi/3D-Reconstruction-with-Deep-Learning-Methods) — 基于深度学习的3D重建项目一览 `paper-list` ⭐1k · 📅2023-05
- 🔴 [awesome-computer-graphics](https://github.com/luisdnsantos/awesome-computer-graphics) — 用于CG学习的书籍、课程与资料集 `awesome` ⭐1k · 📅2021-07
- 🔴 [Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) — 基于学习的MVS论文列表 `paper-list` ⭐633 · 📅2023-11
- 🔴 [Awsome_Deep_Geometry_Learning](https://github.com/subeeshvasu/Awsome_Deep_Geometry_Learning) — 3D形状深度学习方案资料集 `paper-list` ⭐361 · 📅2021-08
- 🔴 [awesome-mvs](https://github.com/krahets/awesome-mvs) — MVS的教程、论文与软件集 `awesome` ⭐277 · 📅2022-08
- 🔴 [awesome-pbr](https://github.com/neil3d/awesome-pbr) — PBR的资料、幻灯片与论文综合合集 `awesome` ⭐118 · 📅2021-01
- 🔴 [Awesome-BRDF](https://github.com/tkuri/Awesome-BRDF) — 按表示方式整理的BRDF表示相关论文 `paper-list` ⭐29 · 📅2021-06
- 🔴 [awesome-Implicit-NeRF-SLAM](https://github.com/Taeyoung96/awesome-Implicit-NeRF-SLAM) — 隐式表示、NeRF在SLAM/机器人中应用的论文集 `paper-list` ⭐13 · 📅2023-11
- 🔴 [texture-synthesis-papers](https://github.com/lzhbrian/texture-synthesis-papers) — 纹理合成论文(含代码)的汇集 `paper-list` ⭐4 · 📅2019-03

## 🖌️ 低层图像处理 / 复原 / 压缩

- 🟢 [awesome-low-light-image-enhancement](https://github.com/zhihongz/awesome-low-light-image-enhancement) — 涵盖低光图像增强数据集/方法/论文/评估指标(活跃) `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment) — IQA论文/数据集/代码的全面集(非常活跃) `awesome` ⭐1.5k · 📅2026-04
- 🟢 [Image-Fusion](https://github.com/Linfeng-Tang/Image-Fusion) — 《Deep Learning-based Image Fusion》综述,跨红外-可见/医学/多曝光等 `survey` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-Image-Colorization](https://github.com/MarkMoHR/Awesome-Image-Colorization) — 基于深度学习的图像/视频上色论文(更新至2025-2026,活跃) `awesome` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-Deep-Learning-Based-Video-Compression](https://github.com/ppingzhang/Awesome-Deep-Learning-Based-Video-Compression) — 基于深度学习的视频压缩论文列表 `paper-list` ⭐292 · 📅2025-09
- 🟢 [Awesome-High-Dynamic-Range-Imaging](https://github.com/rebeccaeexu/Awesome-High-Dynamic-Range-Imaging) — HDR论文集(多帧/单帧、HDRTV、HDR视频、色调映射) `awesome` ⭐237 · 📅2026-02
- 🟢 [awesome-computational-photography](https://github.com/visionxiang/awesome-computational-photography) — 基于深度学习的计算摄影(图像匹配、对齐、拼接、稳定化) `paper-list` ⭐179 · 📅2025-07
- 🟢 [Awesome-Video-Frame-Interpolation](https://github.com/CMLab-Korea/Awesome-Video-Frame-Interpolation) — IEEE TCSVT'26录用VFI综述,系统化250+论文(活跃) `survey` ⭐147 · 📅2026-04
- 🟢 [Awesome-Image-Restoration](https://github.com/TaoWangzj/Awesome-Image-Restoration) — 综述《Deep Image Restoration》配套,跨denoise/deblur/SR/dehaze/derain等 `survey` ⭐13 · 📅2025-11
- 🟡 [Awesome-Denoise](https://github.com/oneTaken/Awesome-Denoise) — 按色彩空间与噪声模型整理图像/连拍/视频去噪论文 `awesome` ⭐503 · 📅2024-04
- 🟡 [Awesome-Shadow-Removal](https://github.com/GuoLanqing/Awesome-Shadow-Removal) — 去阴影的论文/代码/数据集/指标集(活跃) `awesome` ⭐395 · 📅2025-04
- 🟡 [awesome-reflection-removal](https://github.com/ChenyangLEI/awesome-reflection-removal) — 去反射方法集(单图/闪光/偏振/交互式) `awesome` ⭐158 · 📅2024-12
- 🟡 [awesome-video-enhancement](https://github.com/liuzhen03/awesome-video-enhancement) — 跨视频超分、插帧、去噪、去模糊与inpainting的论文集 `paper-list` ⭐156 · 📅2024-08
- 🟡 [UIE](https://github.com/YuZhao1999/UIE) — 水下图像增强的资源列表 `paper-list` ⭐117 · 📅2024-05
- 🟡 [Awesome-Neural-Compression](https://github.com/Xinjie-Q/Awesome-Neural-Compression) — 涵盖图像、视频、点云、NeRF、3DGS的神经压缩论文/资源集 `awesome` ⭐83 · 📅2024-08
- 🟡 [Awesome-Deblurring-Resources](https://github.com/kawchar85/Awesome-Deblurring-Resources) — 按年份整理的图像与视频去模糊论文/数据集(活跃) `paper-list` ⭐13 · 📅2024-08
- 🔴 [Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers) — 综述《Neural Style Transfer: A Review》配套的代表论文与代码集 `paper-list` ⭐1.6k · 📅2022-02
- 🔴 [DerainZoo](https://github.com/nnUyi/DerainZoo) — 去雨方法、数据集与代码集(单图/视频) `paper-list` ⭐516 · 📅2022-05
- 🔴 [awesome-image-alignment-and-stitching](https://github.com/tzxiang/awesome-image-alignment-and-stitching) — 图像对齐与拼接的精选 `paper-list` ⭐462 · 📅2022-08
- 🔴 [Awesome-Image-Distortion-Correction](https://github.com/subeeshvasu/Awesome-Image-Distortion-Correction) — 卷帘快门效应与径向畸变校正相关资源集 `awesome` ⭐281 · 📅2023-07
- 🔴 [awesome-dehazing](https://github.com/youngguncho/awesome-dehazing) — 对单图/多图去雾、水下增强与数据集分类的论文集 `awesome` ⭐202 · 📅2020-08
- 🔴 [Video-Frame-Interpolation-Collections](https://github.com/lyh-18/Video-Frame-Interpolation-Collections) — SOTA VFI方法的合集 `paper-list` ⭐65 · 📅2021-11

## 🎬 动漫・动画・插画・字体

- 🟢 [AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) — 动漫/漫画研究的论文与数据集集(生成、上色、角色动画等) `awesome` ⭐1.2k · 📅2025-12
- 🟢 [Awesome-Sketch-Based-Applications](https://github.com/MarkMoHR/Awesome-Sketch-Based-Applications) — 基于草图的应用论文集 `paper-list` ⭐707 · 📅2026-05
- 🟢 [Awesome-Sketch-Synthesis](https://github.com/MarkMoHR/Awesome-Sketch-Synthesis) — 草图合成(生成)论文集 `paper-list` ⭐566 · 📅2026-05
- 🟢 [Awesome-AI4Animation](https://github.com/yunlong10/Awesome-AI4Animation) — AI 动画生成、插值、上色与制作辅助的论文集 `paper-list` ⭐203 · 📅2026-01
- 🟢 [Awesome-Animation-Research](https://github.com/zhenglinpan/Awesome-Animation-Research) — 收集动画(2D/卡通等)研究论文与数据集的列表 `paper-list` ⭐202 · 📅2026-04
- 🟢 [TypographyResearchCollection](https://github.com/IShengFang/TypographyResearchCollection) — 排版相关CG/CV/ML研究收集(含字体生成与动画) `paper-list` ⭐159 · 📅2025-08
- 🟢 [Awesome-2D-Animation](https://github.com/MarkMoHR/Awesome-2D-Animation) — 中间帧(inbetweening)与 2D 动画的工具、数据集与论文集 `paper-list` ⭐38 · 📅2026-05
- 🔴 [Sketch-Based-Deep-Learning](https://github.com/qyzdao/Sketch-Based-Deep-Learning) — 基于草图的深度学习论文集(线稿上色、矢量化等) `paper-list` ⭐178 · 📅2021-05

## 💬 NLP / 大语言模型(LLM)

- 🟢 [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — 涵盖LLM论文、模型、工具与课程的最大规模列表之一 `awesome` ⭐26.9k · 📅2025-07
- 🟢 [Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM) — 整理开源中文大语言模型(底座/领域微调/数据/教程) `awesome` ⭐22.6k · 📅2026-05
- 🟢 [awesome-nlp](https://github.com/keon/awesome-nlp) — 汇集NLP全领域库、数据与教程的经典列表 `awesome` ⭐18.7k · 📅2026-05
- 🟢 [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) — 汇总LLM演化谱系树与实践应用指南的综述集 `survey` ⭐10.2k · 📅2026-04
- 🟢 [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) — 汇总多模态生成、Agent、辅助编码、数据处理、训练、推理等LLM资料 `awesome` ⭐8.5k · 📅2026-05
- 🟢 [awesome-prompts](https://github.com/ai-boost/awesome-prompts) — 高评分GPTs提示与前沿提示工程论文的合集 `awesome` ⭐8.1k · 📅2026-06
- 🟢 [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) — 聚焦OpenAI o1与推理技法的论文与博客集 `paper-list` ⭐6.9k · 📅2025-12
- 🟢 [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) — 汇集面向GPT/ChatGPT的提示技法论文与工具的列表 `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) — FlashAttention、PagedAttention等推理加速论文集 `paper-list` ⭐5.3k · 📅2026-04
- 🟢 [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) — Text2SQL/Text2DSL等教程与资源集 `awesome` ⭐3.7k · 📅2026-01
- 🟢 [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — 从CoT到o1/DeepSeek-R1的LLM推理论文集(非常活跃) `awesome` ⭐3.6k · 📅2026-04
- 🟢 [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) — 从提示工程到生产级AI系统的上下文工程综述 `survey` ⭐3.2k · 📅2026-05
- 🟢 [Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) — 汇集图相关LLM资源的精选 `awesome` ⭐2.4k · 📅2025-11
- 🟢 [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) — 基于图的RAG综述、论文与基准集 `awesome` ⭐2.4k · 📅2026-05
- 🟢 [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) — 持续更新ICL与提示工程最新资源的论文列表 `paper-list` ⭐2.2k · 📅2026-05
- 🟢 [KG-LLM-Papers](https://github.com/zjukg/KG-LLM-Papers) — 整合知识图谱与LLM的论文列表 `paper-list` ⭐2.2k · 📅2026-03
- 🟢 [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) — 长上下文建模(高效注意力、KV缓存、位置编码等)的论文集 `paper-list` ⭐2.1k · 📅2026-05
- 🟢 [Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets) — 从5个视角整理预训练语料、指令/偏好/评估数据集 `awesome` ⭐1.5k · 📅2026-03
- 🟢 [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) — 基于TKDE2025综述的LLM Text-to-SQL论文与基准集 `survey` ⭐1.3k · 📅2026-05
- 🟢 [SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) — 投机解码的必读论文与博客集(与综述联动) `survey` ⭐1.2k · 📅2026-05
- 🟢 [KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) — LLM知识编辑相关论文列表 `paper-list` ⭐1.2k · 📅2025-07
- 🟢 [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) — 按模型整理的LLM幻觉检测论文列表 `paper-list` ⭐1.1k · 📅2026-05
- 🟢 [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) — 《Siren's Song in the AI Ocean》幻觉综述阅读列表 `survey` ⭐1.1k · 📅2025-09
- 🟢 [Paper-Reading-ConvAI](https://github.com/iwangjian/Paper-Reading-ConvAI) — 以对话系统与NLG为中心的会话AI论文列表 `paper-list` ⭐1k · 📅2026-05
- 🟢 [awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) — 《LLM × DATA》综述官方仓库 `survey` ⭐781 · 📅2026-03
- 🟢 [Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) — 《Stop Overthinking》高效推理综述(TMLR2025)的论文集 `survey` ⭐769 · 📅2026-02
- 🟢 [Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) — 《LLMs-as-Judges》评估方法综述的官方论文集 `survey` ⭐584 · 📅2025-07
- 🟢 [A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) — TKDE录用《MoE in LLMs》综述的官方论文集 `survey` ⭐502 · 📅2025-07
- 🟢 [LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) — 工具学习综述的官方仓库,按task planning/tool selection等分类 `survey` ⭐484 · 📅2025-08
- 🟢 [Awesome-LLM-Quantization](https://github.com/pprp/Awesome-LLM-Quantization) — 专注LLM量化的论文列表 `awesome` ⭐423 · 📅2026-04
- 🟢 [awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference) — 汇集MoE模型推理优化论文的列表 `paper-list` ⭐394 · 📅2026-03
- 🟢 [Awesome-Inference-Time-Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling) — 推理时/测试时扩展的论文列表(活跃) `awesome` ⭐385 · 📅2026-05
- 🟢 [Awesome_papers_on_LLMs_detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) — LLM生成文本与代码检测的论文列表 `paper-list` ⭐288 · 📅2025-06
- 🟢 [Awesome-Fake-News-Detection](https://github.com/wangbing1416/Awesome-Fake-News-Detection) — 假新闻与谣言检测的论文列表 `awesome` ⭐164 · 📅2026-04
- 🟢 [GEC-Info](https://github.com/gotutiyan/GEC-Info) — 收集与分类GEC论文的仓库 `paper-list` ⭐128 · 📅2026-01
- 🟢 [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) — LLM自我修正的论文列表(遵循综述) `paper-list` ⭐81 · 📅2026-05
- 🟢 [Awesome-Function-Callings](https://github.com/Applied-Machine-Learning-Lab/Awesome-Function-Callings) — 专注LLM function calling的论文列表 `paper-list` ⭐71 · 📅2026-04
- 🟢 [Awesome-Personalized-LLMs](https://github.com/VanillaCreamer/Awesome-Personalized-LLMs) — 个性化LLM(偏好建模、persona控制、记忆驱动)的最新论文集 `paper-list` ⭐46 · 📅2026-05
- 🟢 [awesome-lora-adapter](https://github.com/marlin-codes/awesome-lora-adapter) — 汇集LoRA与适配器类方法的论文列表 `paper-list` ⭐22 · 📅2026-05
- 🟢 [Awesome-PEFT](https://github.com/XiaoshuangJi/Awesome-PEFT) — 以LoRA各类变体为中心的PEFT论文、库与实现集 `awesome` ⭐7 · 📅2026-03
- 🟢 [Awesome-Text-Generation-Evaluation](https://github.com/SuperBruceJia/Awesome-Text-Generation-Evaluation) — NLG评估指标(有参考/无参考)的精选列表 `awesome` ⭐4 · 📅2026-05
- 📑 [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) — 《A Survey of Large Language Models》官方仓库 `survey` ⭐12.2k · 📅2025-03
- 📑 [ABigSurvey](https://github.com/NiuTrans/ABigSurvey) — 将NLP与ML数百篇综述论文一览化的综述之综述 `survey` ⭐2k · 📅2024-03
- 📑 [RAG-Survey](https://github.com/hymie122/RAG-Survey) — 《RAG for AI-Generated Content》综述的分类体系与论文集 `survey` ⭐1.8k · 📅2024-08
- 📑 [Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) — 《LLMs on Graphs》TKDE综述的论文与资源集 `survey` ⭐991 · 📅2025-03
- 📑 [Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) — 《Evaluating LLMs: A Comprehensive Survey》的论文集 `survey` ⭐803 · 📅2024-05
- 📑 [CNSurvey](https://github.com/NiuTrans/CNSurvey) — NLP与机器学习的中文综述文章列表 `survey` ⭐580 · 📅2023-05
- 📑 [ABigSurveyOfLLMs](https://github.com/NiuTrans/ABigSurveyOfLLMs) — 汇集150余篇LLM相关综述的合集 `survey` ⭐349 · 📅2025-02
- 📑 [Semantic-Retrieval-Models](https://github.com/caiyinqiong/Semantic-Retrieval-Models) — 涵盖语义检索模型(DPR、RAG、RepBERT等)的TOIS录用综述论文列表 `survey` ⭐340 · 📅2023-06
- 📑 [CTGSurvey](https://github.com/IAAR-Shanghai/CTGSurvey) — 面向LLM的可控文本生成综述论文列表(分类训练时/推理时方法) `survey` ⭐205 · 📅2024-08
- 📑 [Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models](https://github.com/THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models) — 系统整理面向基础模型PEFT方法的综述兼论文列表 `survey` ⭐112 · 📅2025-03
- 📑 [llm-alignment-survey](https://github.com/Magnetic2014/llm-alignment-survey) — 《LLM Alignment: A Survey》的对齐阅读列表 `survey` ⭐82 · 📅2023-09
- 📑 [Awesome_Information_Extraction](https://github.com/wutong8023/Awesome_Information_Extraction) — 含RE、EE、slot filling的IE文献综述 `survey` ⭐72 · 📅2023-01
- 📑 [Awesome-Data-Efficient-LLM](https://github.com/luo-junyu/Awesome-Data-Efficient-LLM) — 数据高效与数据中心的LLM论文集(含综述) `survey` ⭐57 · 📅2025-02
- 🟡 [Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) — 代码生成LLM研究的精选列表 `awesome` ⭐1.3k · 📅2024-12
- 🟡 [Awesome-LLM4IE-Papers](https://github.com/quqxui/Awesome-LLM4IE-Papers) — 基于LLM的生成式信息抽取(NER/RE/EE)论文集 `paper-list` ⭐1.1k · 📅2024-11
- 🟡 [Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers) — ACL2023综述《Reasoning with LM Prompting》的论文列表 `paper-list` ⭐1k · 📅2025-05
- 🟡 [ToolLearningPapers](https://github.com/thunlp/ToolLearningPapers) — 基础模型工具学习(tool learning)的必读论文集 `paper-list` ⭐921 · 📅2024-07
- 🟡 [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) — 基于In-Context Learning综述的论文列表 `paper-list` ⭐876 · 📅2024-10
- 🟡 [awesome-pretrained-models-for-information-retrieval](https://github.com/ict-bigdatalab/awesome-pretrained-models-for-information-retrieval) — 面向IR的预训练模型(pretraining for IR)论文集 `awesome` ⭐676 · 📅2024-01
- 🟡 [Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) — MoE研究的阅读列表 `paper-list` ⭐666 · 📅2024-10
- 🟡 [EventExtractionPapers](https://github.com/BaptisteBlouin/EventExtractionPapers) — 以事件抽取任务为中心的NLP资源列表 `paper-list` ⭐580 · 📅2024-03
- 🟡 [awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning) — Instruction Tuning/Following论文与数据集集 `paper-list` ⭐510 · 📅2024-04
- 🟡 [awesome-llm-pretraining](https://github.com/RUCAIBox/awesome-llm-pretraining) — LLM预训练的数据、框架与方法资源集 `awesome` ⭐376 · 📅2025-04
- 🟡 [Awesome-LLM-Watermark](https://github.com/hzy312/Awesome-LLM-Watermark) — 持续更新最新LLM水印论文的列表 `paper-list` ⭐375 · 📅2024-12
- 🟡 [ABSAPapers](https://github.com/ZhengZixiang/ABSAPapers) — 方面级情感分析(ABSA)的论文与资源集 `paper-list` ⭐363 · 📅2024-03
- 🟡 [Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) — LLM幻觉相关论文列表 `paper-list` ⭐335 · 📅2024-03
- 🟡 [LLM-Optimizers-Papers](https://github.com/AGI-Edgerunners/LLM-Optimizers-Papers) — 将LLM用作优化器/提示自动优化的必读论文集 `paper-list` ⭐252 · 📅2024-03
- 🟡 [awesome-tool-llm](https://github.com/zorazrw/awesome-tool-llm) — 汇集工具增强LLM(ToRA、MINT等)的精选列表 `awesome` ⭐243 · 📅2024-08
- 🟡 [Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) — 《Evaluation of RAG: A Survey》官方评估论文列表 `paper-list` ⭐198 · 📅2025-04
- 🟡 [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) — 测试时LLM(含self-correction/refine)论文集 `awesome` ⭐152 · 📅2025-03
- 🟡 [Low-resource-KEPapers](https://github.com/zjunlp/Low-resource-KEPapers) — 低资源信息抽取(NER/RE/EE)的论文、工具与数据集集 `paper-list` ⭐135 · 📅2024-11
- 🟡 [EMNLP-2023-Papers](https://github.com/DmitryRyumin/EMNLP-2023-Papers) — 系统整理EMNLP 2023论文的合集 `paper-list` ⭐111 · 📅2024-05
- 🟡 [Paper-Neural-Topic-Models](https://github.com/bobxwu/Paper-Neural-Topic-Models) — 神经主题模型(NTM)的论文集 `paper-list` ⭐95 · 📅2024-07
- 🟡 [Awesome-Papers-Retrieval-Augmented-Generation](https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation) — 基于知识导向RAG综述的论文分类列表 `paper-list` ⭐89 · 📅2025-03
- 🟡 [Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers) — 多语言LLM论文列表 `paper-list` ⭐34 · 📅2025-01
- 🟡 [awesome-llm-tool-learning](https://github.com/AngxiaoYue/awesome-llm-tool-learning) — LLM工具学习论文(Gorilla、HuggingGPT、ART等)的列表 `paper-list` ⭐28 · 📅2024-07
- 🟡 [Awesome-LLM-Reasoning-Techniques](https://github.com/Junting-Lu/Awesome-LLM-Reasoning-Techniques) — 包含CoT与o1的LLM推理技法论文与资源集 `paper-list` ⭐18 · 📅2024-10
- 📦 [Fact-Checking-Survey](https://github.com/neemakot/Fact-Checking-Survey) — COLING2020《Explainable Automated Fact-Checking》综述的论文集 `survey` ⭐51 · 📅2021-01
- 🔴 [PromptPapers](https://github.com/thunlp/PromptPapers) — 预训练模型基于提示微调的必读论文集 `paper-list` ⭐4.3k · 📅2023-07
- 🔴 [Top-AI-Conferences-Paper-with-Code](https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code) — ACL/EMNLP/NAACL/COLING等顶会的带代码论文集 `paper-list` ⭐2.7k · 📅2022-10
- 🔴 [Style-Transfer-in-Text](https://github.com/fuzhenxin/Style-Transfer-in-Text) — 文本风格转换的经典论文列表(分类有监督/无监督/评估) `paper-list` ⭐1.6k · 📅2023-03
- 🔴 [awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization) — 文本摘要的论文、工具与数据集集 `awesome` ⭐1.5k · 📅2023-01
- 🔴 [awesome-relation-extraction](https://github.com/roomylee/awesome-relation-extraction) — 专注关系抽取的资源列表 `awesome` ⭐1.2k · 📅2022-01
- 🔴 [awesome-qa](https://github.com/seriousran/awesome-qa) — 问答的数据集、论文与资源集 `awesome` ⭐767 · 📅2022-01
- 🔴 [awesome-sentiment-analysis](https://github.com/declare-lab/awesome-sentiment-analysis) — 情感分析论文阅读列表 `paper-list` ⭐538 · 📅2023-03
- 🔴 [awesome-nlg](https://github.com/accelerated-text/awesome-nlg) — NLG全领域资源集(工具/论文/数据) `awesome` ⭐480 · 📅2023-09
- 🔴 [Named-Entity-Recognition-NER-Papers](https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers) — 涵盖7个会议的NER论文列表 `paper-list` ⭐392 · 📅2022-02
- 🔴 [Awesome-Sentence-Embedding](https://github.com/Doragd/Awesome-Sentence-Embedding) — 收录句子表示学习论文与STS排行榜(SimCSE等) `awesome` ⭐314 · 📅2023-10
- 🔴 [DeltaPapers](https://github.com/thunlp/DeltaPapers) — 预训练模型参数高效微调(Delta Tuning)的必读论文集 `paper-list` ⭐285 · 📅2023-06
- 🔴 [Awesome-KBQA](https://github.com/RUCAIBox/Awesome-KBQA) — 知识库问答(KBQA)的论文、工具与排行榜集 `paper-list` ⭐181 · 📅2022-04
- 🔴 [Accepted-Papers-Lists](https://github.com/audreycs/Accepted-Papers-Lists) — 汇总主要期刊与会议录用论文列表的仓库 `paper-list` ⭐147 · 📅2022-12
- 🔴 [MT-paper-lists](https://github.com/NiuTrans/MT-paper-lists) — 按会议整理的机器翻译论文列表 `paper-list` ⭐124 · 📅2020-12
- 🔴 [Data-to-Text-Generation](https://github.com/liang8qi/Data-to-Text-Generation) — data-to-text生成的论文与数据集集 `paper-list` ⭐108 · 📅2023-05
- 🔴 [awesome-NLP-Machine-Learning](https://github.com/tjunlp-lab/awesome-NLP-Machine-Learning) — 面向NLP研究的机器学习技法(RL/自监督等)论文与代码集 `paper-list` ⭐35 · 📅2020-03
- 🔴 [AWESOME-Dialogue](https://github.com/thuiar/AWESOME-Dialogue) — 对话与交互系统的论文列表 `paper-list` ⭐15 · 📅2020-06
- 🔴 [awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp) — 面向英语以外语言的多语言NLP研究精选 `awesome` ⭐8 · 📅2023-07
- 🔴 [AwesomeSemanticParsing](https://github.com/aarsri/AwesomeSemanticParsing) — 语义解析的论文与资源集 `awesome` ⭐0 · 📅2020-11

## 🖼️ 生成式 AI / Diffusion / 图像・视频生成

- 🟢 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) — 汇集视频生成与编辑diffusion model的经典列表 `awesome` ⭐5.7k · 📅2026-05
- 🟢 [really-awesome-gan](https://github.com/nightrome/really-awesome-gan) — 汇集GAN论文的全面列表 `paper-list` ⭐3.8k · 📅2025-08
- 🟢 [awesome-virtual-try-on](https://github.com/minar09/awesome-virtual-try-on) — 虚拟试穿的论文/代码/数据集经典列表 `awesome` ⭐3.1k · 📅2026-05
- 🟢 [Awesome-Text-to-Image](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image) — 文本生成图像的综述式论文列表 `survey` ⭐2.4k · 📅2026-02
- 🟢 [Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) — Video Diffusion Model综述(CSUR) `survey` ⭐2.3k · 📅2026-04
- 🟢 [awesome-diffusion-categorized](https://github.com/wangkai930418/awesome-diffusion-categorized) — 按子领域分类的diffusion论文实用合集 `awesome` ⭐2.2k · 📅2026-03
- 🟢 [awesome-talking-head-generation](https://github.com/harlanhong/awesome-talking-head-generation) — talking head生成论文列表 `paper-list` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) — Deepfake检测的工具/论文/代码 `awesome` ⭐1.8k · 📅2025-09
- 🟢 [awesome-image-translation](https://github.com/weihaox/awesome-image-translation) — image-to-image translation相关优质资源的合集 `awesome` ⭐1.2k · 📅2025-09
- 🟢 [Awesome-diffusion-model-for-image-processing](https://github.com/lixinustc/Awesome-diffusion-model-for-image-processing) — 整理修复/增强/编码/质量评估的diffusion model `survey` ⭐946 · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/showlab/Awesome-Unified-Multimodal-Models) — 统一理解与生成模型的论文集 `paper-list` ⭐825 · 📅2025-10
- 🟢 [Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) — 视觉自回归模型综述(TMLR 2025) `survey` ⭐797 · 📅2026-05
- 🟢 [awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) — 汇集视频生成研究的合集 `awesome` ⭐770 · 📅2026-03
- 🟢 [awesome-text-to-image-studies](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) — 汇集text-to-image研究的持续更新列表 `awesome` ⭐759 · 📅2026-04
- 🟢 [Awesome-Deepfake-Generation-and-Detection](https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection) — Deepfake生成与检测综述 `survey` ⭐637 · 📅2026-05
- 🟢 [Awesome-Video-World-Models-with-AR-Diffusion](https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion) — AR+diffusion视频世界模型(算法/应用/基础) `awesome` ⭐568 · 📅2026-05
- 🟢 [awesome-discrete-diffusion-models](https://github.com/kuleshov-group/awesome-discrete-diffusion-models) — 专注离散diffusion model的资源列表 `awesome` ⭐561 · 📅2025-09
- 🟢 [Awesome-Controllable-Diffusion](https://github.com/atfortes/Awesome-Controllable-Diffusion) — ControlNet、DreamBooth、IP-Adapter等可控生成资源 `awesome` ⭐505 · 📅2025-06
- 🟢 [Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model) — 整理从视频生成到世界模型的脉络 `paper-list` ⭐486 · 📅2026-03
- 🟢 [Awesome-Image-Editing](https://github.com/FudanCVL/Awesome-Image-Editing) — 基于T2I模型的图像编辑综述 `survey` ⭐472 · 📅2025-08
- 🟢 [Awesome-Evaluation-of-Visual-Generation](https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation) — 视觉生成的评估指标/模型/系统集 `paper-list` ⭐446 · 📅2026-05
- 🟢 [Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation) — 自回归视觉生成的最新论文追踪 `paper-list` ⭐431 · 📅2025-06
- 🟢 [Awesome-Try-On-Models](https://github.com/Zheng-Chong/Awesome-Try-On-Models) — 整理虚拟试穿模型(含2025) `paper-list` ⭐416 · 📅2026-05
- 🟢 [Awesome-AIGC-Image-Video-Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) — AI生成图像/视频检测的最新研究集 `paper-list` ⭐393 · 📅2026-05
- 🟢 [awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) — 图像inpainting研究合集 `awesome` ⭐386 · 📅2026-02
- 🟢 [Awesome-Comprehensive-Deepfake-Detection](https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection) — Deepfake检测的全面论文列表 `paper-list` ⭐313 · 📅2026-04
- 🟢 [awesome-diffusion-v2v](https://github.com/wenhao728/awesome-diffusion-v2v) — 基于diffusion的Video-to-Video编辑论文+基准 `paper-list` ⭐287 · 📅2026-04
- 🟢 [Awesome-Text-to-Video-Generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation) — 遵循Sora综述的T2V/I2V论文列表 `survey` ⭐259 · 📅2026-03
- 🟢 [Awesome-Consistency-Models](https://github.com/G-U-N/Awesome-Consistency-Models) — Consistency Model的资源列表 `awesome` ⭐131 · 📅2025-12
- 📑 [GAN-Inversion](https://github.com/weihaox/GAN-Inversion) — GAN Inversion综述(TPAMI 2022)配套仓库 `survey` ⭐1.1k · 📅2025-02
- 📑 [awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) — Text-to-Video生成综述 `survey` ⭐730 · 📅2024-07
- 🟡 [Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) — 涵盖diffusion model论文与资源的最大规模列表之一 `awesome` ⭐12.3k · 📅2024-08
- 🟡 [Awesome-High-Resolution-Diffusion](https://github.com/GuoLanqing/Awesome-High-Resolution-Diffusion) — 高分辨率图像/视频合成的diffusion论文 `paper-list` ⭐169 · 📅2024-12
- 🟡 [Awesome-Music-Generation](https://github.com/shaopengw/Awesome-Music-Generation) — 音乐生成模型MG²的资源 `model` ⭐165 · 📅2025-03
- 🟡 [awesome-diffusion-iclr-2025](https://github.com/moatifbutt/awesome-diffusion-iclr-2025) — ICLR 2025的diffusion相关投稿列表 `paper-list` ⭐61 · 📅2024-10
- 📚 [the-gan-zoo](https://github.com/hindupuravinash/the-gan-zoo) — 罗列所有命名GAN的经典列表 `paper-list` ⭐14.7k · 📅2023-10
- 🔴 [gans-awesome-applications](https://github.com/nashory/gans-awesome-applications) — 汇集GAN应用与演示的精选列表 `awesome` ⭐5.1k · 📅2023-08
- 🔴 [awesome-ai-art-image-synthesis](https://github.com/altryne/awesome-ai-art-image-synthesis) — DALL·E2/MidJourney/SD等工具与提示集 `awesome` ⭐1.8k · 📅2022-12
- 🔴 [awesome-diffusion-low-level-vision](https://github.com/yulunzhang/awesome-diffusion-low-level-vision) — 低层视觉diffusion model列表 `paper-list` ⭐186 · 📅2023-09
- 🔴 [awesome-controlnet](https://github.com/cobanov/awesome-controlnet) — ControlNet相关资源列表 `awesome` ⭐97 · 📅2023-03
- 🔴 [awesome-few-shot-generation](https://github.com/kobeshegu/awesome-few-shot-generation) — 少样本图像生成论文列表 `paper-list` ⭐87 · 📅2023-08
- 🔴 [Awsome-GAN-Training](https://github.com/subeeshvasu/Awsome-GAN-Training) — 汇集GAN训练(training)相关资源的列表 `awesome` ⭐30 · 📅2020-10

## 🍌 特定模型的提示词・范例集

- 🟢 [Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) — Gemini系Nano Banana的生成示例与提示集(公开数据集) `model` ⭐22.9k · 📅2025-12
- 🟢 [awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) — GPT-Image-2的API与提示、示例集 `model` ⭐15.8k · 📅2026-05
- 🟢 [awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) — 世界最大规模Nano Banana Pro提示集10,000+/16种语言(每日更新) `model` ⭐12.3k · 📅2026-06
- 🟢 [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) — Nano Banana Pro(Nano Banana 2)的提示与示例集 `model` ⭐10k · 📅2026-05
- 🟢 [awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) — Gemini-2.5-Flash-Image(Nano Banana)的示例/提示集 `model` ⭐8.8k · 📅2025-09
- 🟢 [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) — Seedance 2.0视频生成提示2000+(每日更新) `model` ⭐1.3k · 📅2026-05
- 🟢 [awesome-nano-banana-pro](https://github.com/muset-ai/awesome-nano-banana-pro) — Nano Banana Pro的图像与提示示例集 `model` ⭐1.1k · 📅2025-11
- 🟢 [awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) — 面向Veo3/Kling/Hailuo的视频提示集 `model` ⭐518 · 📅2025-10
- 🟢 [Awesome-Chinese-Stable-Diffusion](https://github.com/leeguandong/Awesome-Chinese-Stable-Diffusion) — 中国系文生图SD模型集(含Kolors/HunyuanDiT等) `model` ⭐425 · 📅2026-05
- 🟢 [awesome-qwen-prompt-insight](https://github.com/XiaomingX/awesome-qwen-prompt-insight) — 面向Qwen的优质提示大规模合集 `model` ⭐398 · 📅2026-02
- 🟢 [awesome-nano-banana-images](https://github.com/githubssg/awesome-nano-banana-images) — GPT-4o/gpt-image-1的图像与提示集 `model` ⭐306 · 📅2025-09
- 🟢 [Awesome-Open-AI-Sora](https://github.com/Curated-Awesome-Lists/Awesome-Open-AI-Sora) — Sora相关文章/视频/新闻的资源中心 `model` ⭐260 · 📅2026-05
- 🟢 [awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) — 跨多个视频模型的提示/技法集 `model` ⭐57 · 📅2026-01
- 🟢 [awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts) — Grok Imagine(xAI)视频生成提示集 `model` ⭐14 · 📅2026-05
- 🟢 [awesome-qwen-image-2512](https://github.com/shauray8/awesome-qwen-image-2512) — qwen-image-2512的示例/提示集 `model` ⭐0 · 📅2025-12
- 🟡 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) — GPT-4o、gpt-image-1的图像与提示示例集 `model` ⭐8.1k · 📅2025-05
- 🟡 [Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) — 汇集GPT Store上GPT的精选 `model` ⭐3.4k · 📅2024-11
- 🟡 [Awesome-GPT4o-Image-Prompts](https://github.com/ImgEdify/Awesome-GPT4o-Image-Prompts) — GPT-4o图像生成的提示词典 `model` ⭐564 · 📅2025-05
- 🟡 [awesome-grok-prompts](https://github.com/langgptai/awesome-grok-prompts) — 面向Grok(xAI)的高级提示与模板集 `model` ⭐506 · 📅2025-05
- 🟡 [awesome-llama-prompts](https://github.com/langgptai/awesome-llama-prompts) — 面向Llama2/Llama3的提示集 `model` ⭐269 · 📅2024-08
- 🟡 [awesome-flux](https://github.com/Eris2025/awesome-flux) — FLUX生态(LoRA/ControlNet/量化)的资源集 `model` ⭐105 · 📅2024-08

## 🧰 模型生态 / 运维工具 (MCP・LLMOps・LLM 应用)

- 🟢 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — 可运行的LLM应用/RAG/智能体合集 `awesome` ⭐112.4k · 📅2026-06
- 🟢 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 最大规模的MCP(Model Context Protocol)服务器合集 `awesome` ⭐88.3k · 📅2026-05
- 🟢 [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Claude Skill/工具的精选 `awesome` ⭐62.7k · 📅2026-05
- 🟢 [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — 面向Claude Code的skill/hook/slash-command/插件集 `awesome` ⭐45.3k · 📅2026-04
- 🟢 [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) — 将DeepSeek API集成到各类软件的官方精选 `model` ⭐37.7k · 📅2026-02
- 🟢 [Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) — 涵盖PyTorch相关模型、实现与库的大规模列表 `awesome` ⭐16.5k · 📅2026-02
- 🟢 [awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) — 精选现代生成AI项目与服务的列表 `awesome` ⭐12.1k · 📅2026-05
- 🟢 [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) — LangChain框架的工具与项目列表 `awesome` ⭐9.4k · 📅2026-04
- 🟢 [ai-collection](https://github.com/ai-collection/ai-collection) — 汇集生成AI应用的全景图 `awesome` ⭐9k · 📅2026-06
- 🟢 [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) — 面向ChatGPT的awesome列表(sindresorhus系列) `awesome` ⭐6.3k · 📅2026-02
- 🟢 [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) — 收集AI相关实用工具的合集(中英对照) `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) — 面向LLM开发与运维的工具(训练/服务/监控)精选列表 `awesome` ⭐5.8k · 📅2026-05
- 🟢 [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) — MCP服务器的精选 `awesome` ⭐5.6k · 📅2026-05
- 🟢 [awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools) — 精选AI顶级工具的列表 `awesome` ⭐5.4k · 📅2025-12
- 🟢 [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) — 精选真正开源的AI项目、模型、工具与基础设施的列表 `awesome` ⭐3.7k · 📅2026-05
- 🟢 [awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) — ChatGPT的库/SDK/API精选 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-claude](https://github.com/webfuse-com/awesome-claude) — Anthropic Claude全领域的精选列表 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) — 生成AI中RAG应用的awesome列表 `awesome` ⭐1.2k · 📅2026-05
- 🟢 [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) — 汇集DeepSeek Coder相关开源项目的官方列表 `model` ⭐789 · 📅2025-11
- 🟢 [awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) — ComfyUI自定义节点的大规模合集 `awesome` ⭐698 · 📅2025-07
- 🟢 [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) — 面向Gemini CLI的工具/扩展/资源集 `awesome` ⭐458 · 📅2026-05
- 🟢 [awesome-stable-diffusion](https://github.com/doanbactam/awesome-stable-diffusion) — Stable Diffusion资源的精选 `awesome` ⭐75 · 📅2026-03
- 🟢 [awesome-mistral](https://github.com/samouraiworld/awesome-mistral) — Mistral AI生态的资源/工具/项目集 `awesome` ⭐42 · 📅2026-05
- 🟡 [awesome-gpt](https://github.com/formulahendry/awesome-gpt) — GPT/ChatGPT/OpenAI相关项目与资源集 `awesome` ⭐1k · 📅2024-05
- 🟡 [awesome-flux-ai](https://github.com/AINativeLab/awesome-flux-ai) — 涵盖Flux AI的工具/库/应用 `awesome` ⭐111 · 📅2025-05

## 🎮 强化学习(RL)

- 🟢 [MARL-Papers](https://github.com/LantaoYu/MARL-Papers) — 多智能体RL的研究与综述论文列表(经典) `paper-list` ⭐4.8k · 📅2026-02
- 🟢 [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) — LLM与多模态在机器人/RL中应用的论文集 `paper-list` ⭐4.4k · 📅2026-04
- 🟢 [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — 持续更新RLHF的论文与资源 `paper-list` ⭐4.4k · 📅2026-05
- 🟢 [Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) — 面向大规模推理模型的RL综述论文仓库 `survey` ⭐2.5k · 📅2025-11
- 🟢 [Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) — 涵盖世界模型(视频生成、Embodied AI、自动驾驶)的论文 `paper-list` ⭐1.7k · 📅2026-06
- 🟢 [awesome-diffusion-model-in-rl](https://github.com/opendilab/awesome-diffusion-model-in-rl) — 持续更新强化学习中diffusion model资源的列表 `awesome` ⭐1.6k · 📅2026-05
- 🟢 [awesome-model-based-RL](https://github.com/opendilab/awesome-model-based-RL) — 持续更新收集基于模型的RL论文 `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-decision-transformer](https://github.com/opendilab/awesome-decision-transformer) — Decision Transformer资源持续更新列表 `awesome` ⭐899 · 📅2026-05
- 🟢 [awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) — 整理Deep RL库、环境与基准的列表 `awesome` ⭐892 · 📅2025-07
- 🟢 [Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) — 汇集Safe RL基线与论文的仓库 `paper-list` ⭐794 · 📅2026-03
- 🟢 [World-Model](https://github.com/tsinghua-fib-lab/World-Model) — 世界模型的全面综述(ACM CSUR 2025录用) `survey` ⭐727 · 📅2025-11
- 🟢 [awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl) — 专注探索(exploration)的RL论文列表 `paper-list` ⭐691 · 📅2026-05
- 🟢 [awesome-multi-modal-reinforcement-learning](https://github.com/opendilab/awesome-multi-modal-reinforcement-learning) — 持续更新多模态RL资源 `paper-list` ⭐607 · 📅2026-05
- 🟢 [Reinforcement-Learning-Papers](https://github.com/yingchengyang/Reinforcement-Learning-Papers) — 按年份整理ICLR/ICML/NeurIPS经典与最新论文 `paper-list` ⭐571 · 📅2026-02
- 🟢 [Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) — 整理视觉RL与面向多模态基础模型的RL论文 `paper-list` ⭐445 · 📅2026-04
- 🟢 [Reinforcement-Learning-Papers](https://github.com/Allenpandas/Reinforcement-Learning-Papers) — 涵盖NeurIPS/ICML/ICLR/AAAI/IJCAI/AAMAS/ICRA的论文 `paper-list` ⭐366 · 📅2025-11
- 🟢 [awesome-in-context-rl](https://github.com/dunnolab/awesome-in-context-rl) — In-Context RL论文精选 `paper-list` ⭐301 · 📅2025-09
- 🟢 [Awesome-Causal-Reinforcement-Learning](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) — 因果RL综述(TNNLS 2024)官方仓库 `survey` ⭐220 · 📅2026-04
- 🟢 [awesome-deep-reinforcement-learning](https://github.com/jgvictores/awesome-deep-reinforcement-learning) — 收录框架、模型、数据集、gym与baseline `awesome` ⭐206 · 📅2026-03
- 🟢 [awesome-RLVR](https://github.com/opendilab/awesome-RLVR) — 持续更新可验证奖励RL(RLVR)论文 `paper-list` ⭐166 · 📅2026-05
- 🟢 [AwesomeSim2Real](https://github.com/LongchaoDa/AwesomeSim2Real) — 综述《A Survey of Sim-to-Real Methods in RL》的配套 `survey` ⭐166 · 📅2025-09
- 🟢 [awesome-world-models-for-robots](https://github.com/operator22th/awesome-world-models-for-robots) — 面向机器人的世界模型论文集 `paper-list` ⭐136 · 📅2026-03
- 🟢 [Awesome-Embodied-World-Model](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) — 专注具身智能体世界模型的论文集 `survey` ⭐112 · 📅2026-05
- 🟡 [awesome-deep-rl](https://github.com/tigerneil/awesome-deep-rl) — 面向Deep RL与AI未来广泛收集资源的列表 `awesome` ⭐1.5k · 📅2024-03
- 🟡 [awesome-rl-envs](https://github.com/clvrai/awesome-rl-envs) — 涵盖RL用环境与模拟器的列表 `awesome` ⭐1.3k · 📅2024-05
- 🟡 [awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl) — offline RL算法索引(持续更新) `paper-list` ⭐1.1k · 📅2024-05
- 🟡 [awesome-game-ai](https://github.com/datamllab/awesome-game-ai) — 以多智能体学习为中心的游戏AI资源集 `awesome` ⭐964 · 📅2024-06
- 🟡 [Awesome-Imitation-Learning](https://github.com/kristery/Awesome-Imitation-Learning) — 汇集模仿学习论文与资源的列表 `paper-list` ⭐608 · 📅2024-02
- 📚 [deep-reinforcement-learning-papers](https://github.com/junhyukoh/deep-reinforcement-learning-papers) — 按主题整理Deep RL主要论文的经典列表 `paper-list` ⭐2.2k · 📅2016-06
- 🔴 [awesome-rl](https://github.com/aikorea/awesome-rl) — 汇集RL全领域代码、讲义、论文与环境的经典精选 `awesome` ⭐9.8k · 📅2023-05
- 🔴 [awesome-real-world-rl](https://github.com/ugurkanates/awesome-real-world-rl) — 在现实世界运行强化学习的论文与项目集(含sim2real) `awesome` ⭐453 · 📅2022-10
- 🔴 [MARL-papers-with-code](https://github.com/TimeBreaker/MARL-papers-with-code) — 按方法整理带代码的MARL论文 `paper-list` ⭐428 · 📅2022-09
- 🔴 [Imitation-Learning-Paper-Lists](https://github.com/apexrl/Imitation-Learning-Paper-Lists) — 带简要介绍收集模仿学习论文 `paper-list` ⭐157 · 📅2022-03
- 🔴 [awesome-irl](https://github.com/dit7ya/awesome-irl) — 逆强化学习的论文、代码、视频与教程集 `awesome` ⭐44 · 📅2022-02
- 🔴 [awesome-metarl](https://github.com/metarl/awesome-metarl) — 元强化学习精选列表 `paper-list` ⭐33 · 📅2020-05

## 🔀 多模态 / VLM / MLLM

- 🟢 [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) — MLLM领域最著名综述,涵盖架构、训练与评估的追踪 `survey` ⭐17.8k · 📅2026-05
- 🟢 [Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) — 面向视频理解的Vid-LLM最新论文、代码与数据集 `paper-list` ⭐3.2k · 📅2026-03
- 🟢 [VLM_survey](https://github.com/jingyi0000/VLM_survey) — 面向视觉任务的Vision-Language模型系统综述 `survey` ⭐3.1k · 📅2025-10
- 🟢 [Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) — 3D世界中多模态LLM资源的全面列表 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) — 统一理解与生成的多模态模型全面集(活跃) `survey` ⭐1.3k · 📅2026-03
- 🟢 [awesome-vlm-architectures](https://github.com/gokayfem/awesome-vlm-architectures) — 讲解著名VLM及其架构的合集 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) — 多模态LLM幻觉(hallucination)相关资源的精选列表 `awesome` ⭐1k · 📅2025-09
- 🟢 [Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) — 面向CLIP等VLM的提示/适配器学习方法精选列表 `paper-list` ⭐778 · 📅2026-05
- 🟢 [Awesome-Spatial-Intelligence-in-VLM](https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM) — VLM空间推理相关论文与基准约200篇(非常活跃) `paper-list` ⭐748 · 📅2026-01
- 🟢 [Awesome_Matching_Pretraining_Transfering](https://github.com/Paranioar/Awesome_Matching_Pretraining_Transfering) — 图像文本匹配、VL预训练与多模态模型的大规模论文列表 `paper-list` ⭐445 · 📅2025-09
- 🟢 [Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) — 多模态研究的精选论文集 `awesome` ⭐335 · 📅2026-05
- 🟢 [Awesome-Chart-Understanding](https://github.com/khuangaf/Awesome-Chart-Understanding) — 遵循IEEE TKDE综述的图表理解(QA/captioning/fact-checking)论文集 `survey` ⭐240 · 📅2025-12
- 🟢 [Awesome-Document-Understanding](https://github.com/harrytea/Awesome-Document-Understanding) — MLLM/OCR-free等多模态文档AI论文、代码与数据集集 `paper-list` ⭐201 · 📅2025-09
- 🟢 [Evaluation-Multimodal-LLMs-Survey](https://github.com/swordlidev/Evaluation-Multimodal-LLMs-Survey) — 评估综述,综述了200余个MLLM基准 `survey` ⭐149 · 📅2026-05
- 🟢 [Awesome-Multimodal-LLM-for-Math-STEM](https://github.com/InfiMM/Awesome-Multimodal-LLM-for-Math-STEM) — 面向Math/STEM/Code的多模态LLM论文集 `awesome` ⭐143 · 📅2026-05
- 🟢 [Awesome-MLLM-Tuning](https://github.com/WenkeHuang/Awesome-MLLM-Tuning) — MLLM面向下游任务的微调方法综述 `paper-list` ⭐98 · 📅2025-08
- 🟢 [Awesome-Composed-Multi-modal-Retrieval](https://github.com/kkzhang95/Awesome-Composed-Multi-modal-Retrieval) — 含组合图像检索(CIR)、组合视频检索(CVR)的CMR综述 `survey` ⭐89 · 📅2026-01
- 🟢 [Awesome-Multimodal-RAG](https://github.com/JarvisUSTC/Awesome-Multimodal-RAG) — 跨文本/图像/视频/音频的多模态RAG论文与工具集 `paper-list` ⭐53 · 📅2025-11
- 🟢 [Awesome-Large-Vision-Language-Model](https://github.com/SuperBruceJia/Awesome-Large-Vision-Language-Model) — 大规模VLM与医疗基础模型的论文与资源集 `awesome` ⭐47 · 📅2025-07
- 📑 [Efficient-Multimodal-LLMs-Survey](https://github.com/swordlidev/Efficient-Multimodal-LLMs-Survey) — 高效MLLM(轻量结构与策略)的系统综述 `survey` ⭐385 · 📅2025-04
- 🟡 [awesome-audio-visual](https://github.com/krantiparida/awesome-audio-visual) — 音频与视觉处理各领域的论文与数据集集 `awesome` ⭐772 · 📅2024-01
- 🟡 [Awesome-Table-Recognition](https://github.com/cv-small-snails/Awesome-Table-Recognition) — 整理表格识别的论文、数据集与竞赛解法 `awesome` ⭐404 · 📅2024-12
- 🟡 [awesome-emotion-recognition-in-conversations](https://github.com/declare-lab/awesome-emotion-recognition-in-conversations) — 会话中情感识别(ERC)的全面阅读列表 `paper-list` ⭐278 · 📅2024-02
- 🟡 [awesome-table-structure-recognition](https://github.com/Tan-Junwen/awesome-table-structure-recognition) — 表格结构识别(TSR)的模型、论文、数据集与代码集 `awesome` ⭐228 · 📅2024-09
- 🟡 [Prompt_Learning_Paper_List](https://github.com/Event-AHU/Prompt_Learning_Paper_List) — (视觉语言)提示学习的论文列表 `paper-list` ⭐19 · 📅2024-11
- 🔴 [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) — 涵盖KIE、布局解析、DocQA、OCR等的经典列表 `awesome` ⭐1.5k · 📅2023-06
- 🔴 [awesome-video-text-retrieval](https://github.com/danieljf24/awesome-video-text-retrieval) — 视频文本检索的深度学习资源集 `awesome` ⭐645 · 📅2023-10
- 🔴 [awesome-affective-computing](https://github.com/AmrMKayid/awesome-affective-computing) — 情感计算的论文、软件、开源与资源集 `awesome` ⭐192 · 📅2019-11
- 🔴 [AWESOME-MER](https://github.com/EvelynFan/AWESOME-MER) — 多模态情感识别(MER)的阅读列表 `paper-list` ⭐126 · 📅2020-10
- 🔴 [awesome-VLM](https://github.com/Lab-LVM/awesome-VLM) — 按对比学习、PrefixLM、融合等方法整理的VLM论文集 `paper-list` ⭐7 · 📅2023-06

## 🔊 语音 / 音频

- 🟢 [awesome-diarization](https://github.com/wq2012/awesome-diarization) — 涵盖说话人日志论文、库、数据集与评估工具的经典列表 `awesome` ⭐1.9k · 📅2025-07
- 🟢 [speech-trident](https://github.com/ga642381/speech-trident) — 语音/音频LLM、表示学习与codec模型的论文集 `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [audio-ai-hub](https://github.com/BinWang28/audio-ai-hub) — 音频大语言模型的论文与资源集 `awesome` ⭐925 · 📅2026-05
- 🟢 [awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) — LLM在Audio AI应用方面的资源集 `awesome` ⭐730 · 📅2026-05
- 🟢 [Awesome-Speaker-Diarization](https://github.com/DongKeon/Awesome-Speaker-Diarization) — 系统化End-to-End/聚类/多模态等的论文集(活跃) `paper-list` ⭐358 · 📅2026-03
- 🟢 [awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) — 开源TTS、语音克隆与音乐生成模型集 `model` ⭐338 · 📅2026-04
- 🟢 [awesome-voice-conversion](https://github.com/JeffC0628/awesome-voice-conversion) — voice conversion(音色转换)的项目与社区集 `awesome` ⭐267 · 📅2025-11
- 🟢 [Awesome-Sign-Language-Processing](https://github.com/VIPL-SLP/Awesome-Sign-Language-Processing) — 手语处理(识别/翻译/生成)的全面资源集 `awesome` ⭐248 · 📅2026-05
- 🟢 [Awesome-Sign-Language](https://github.com/ZechengLi19/Awesome-Sign-Language) — 手语识别(SLR)、翻译(SLT)等论文列表(活跃) `paper-list` ⭐220 · 📅2025-11
- 🟢 [Speech-and-audio-papers-Top-Conference](https://github.com/01Zhangbw/Speech-and-audio-papers-Top-Conference) — 汇集顶会(INTERSPEECH/ICASSP等)语音与音频论文 `paper-list` ⭐139 · 📅2026-01
- 🟢 [awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech) — 基于LLM的speech-to-speech模型/框架集 `awesome` ⭐56 · 📅2025-11
- 🟢 [Awesome-Large-Speech-Model](https://github.com/huangcanan/Awesome-Large-Speech-Model) — 大规模语音/音频模型的论文、数据、应用与工具集 `awesome` ⭐28 · 📅2025-11
- 🟡 [awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) — 应用于音乐的深度学习论文与学位论文集 `paper-list` ⭐3k · 📅2023-12
- 🟡 [INTERSPEECH-2023-24-Papers](https://github.com/DmitryRyumin/INTERSPEECH-2023-24-Papers) — 涵盖INTERSPEECH 2023-2024论文的合集 `paper-list` ⭐689 · 📅2024-12
- 🟡 [ICASSP-2023-24-Papers](https://github.com/DmitryRyumin/ICASSP-2023-24-Papers) — 涵盖ICASSP 2023-2024论文的合集 `paper-list` ⭐527 · 📅2025-05
- 🟡 [awesome-sound_event_detection](https://github.com/soham97/awesome-sound_event_detection) — Sound AI(声音事件检测、音频描述等)研究阅读列表 `paper-list` ⭐196 · 📅2024-08
- 🟡 [awesome-speech-emotion-recognition](https://github.com/abikaki/awesome-speech-emotion-recognition) — 语音情感识别(SER)的论文、数据集与工具精选列表 `awesome` ⭐101 · 📅2024-12
- 🟡 [awesome-vad](https://github.com/bigcash/awesome-vad) — 汇集VAD实现、工具与研究的列表 `awesome` ⭐74 · 📅2024-11
- 🟡 [Awesome-Speech-Enhancement](https://github.com/DmitryRyumin/Awesome-Speech-Enhancement) — 整理语音增强论文与效果指标的交互式列表 `paper-list` ⭐27 · 📅2024-04
- 📦 [awesome-tts-samples](https://github.com/seungwonpark/awesome-tts-samples) — 带语音样本的TTS论文列表 `paper-list` ⭐61 · 📅2020-08
- 🔴 [awesome-speech-recognition-speech-synthesis-papers](https://github.com/zzw922cn/awesome-speech-recognition-speech-synthesis-papers) — 涵盖ASR、说话人验证、TTS、语音合成与VC的论文列表 `paper-list` ⭐3.1k · 📅2023-10
- 🔴 [awesome-speech-enhancement](https://github.com/WenzheLiu-Speech/awesome-speech-enhancement) — speech enhancement、声源分离与定位的论文/代码/工具集 `paper-list` ⭐1.2k · 📅2023-11
- 🔴 [speech-synthesis-paper](https://github.com/wenet-e2e/speech-synthesis-paper) — 语音合成(TTS)论文的系统列表 `paper-list` ⭐1.1k · 📅2023-07
- 🔴 [Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion](https://github.com/guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion) — 歌声合成(SVS)、歌声转换(SVC)与自动记谱的论文/项目集 `paper-list` ⭐482 · 📅2022-09
- 🔴 [awesome-keyword-spotting](https://github.com/zycv/awesome-keyword-spotting) — 语音关键词检测/唤醒词检测的论文、实现与数据集集 `awesome` ⭐287 · 📅2022-05
- 🔴 [awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) — 音乐信息学的论文、教程、库与工具精选列表 `awesome` ⭐192 · 📅2023-07
- 🔴 [awesome-speech-translation](https://github.com/dqqcasia/awesome-speech-translation) — 语音翻译(管道/E2E/流式/多语言)的论文列表 `paper-list` ⭐179 · 📅2021-11
- 🔴 [awesome-speech-to-speech-translation](https://github.com/Rongjiehuang/awesome-speech-to-speech-translation) — 直接语音间翻译(S2ST)的论文列表 `paper-list` ⭐39 · 📅2023-01

## 🤖 机器人学 / Embodied AI

- 🟢 [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — embodied AI的VLA、VLN与多模态学习前沿研究集 `paper-list` ⭐3.2k · 📅2026-05
- 🟢 [awesome-robotics-libraries](https://github.com/jslee02/awesome-robotics-libraries) — 精选机器人库与软件的列表 `awesome` ⭐2.9k · 📅2026-05
- 🟢 [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — 人形机器人学习论文列表 `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — 涵盖具身AI感知、交互、智能体与sim-to-real(IEEE/ASME ToM 2025) `survey` ⭐2.1k · 📅2026-05
- 🟢 [Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) — 使用LLM的embodied AI/机器人研究精选 `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome_Quadrupedal_Robots](https://github.com/curieuxjy/Awesome_Quadrupedal_Robots) — 四足机器人的论文与资源集 `paper-list` ⭐1.1k · 📅2026-05
- 🟢 [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) — 机器人操作的论文与代码集 `paper-list` ⭐991 · 📅2026-05
- 🟢 [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam) — VLA与World Action Model(WAM)研究精选 `awesome` ⭐658 · 📅2026-05
- 🟢 [Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) — 持续收集顶会录用的Embodied AI论文(反映至2026会议,活跃) `paper-list` ⭐658 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) — 面向embodied AI的VLA模型带综述论文列表 `survey` ⭐580 · 📅2026-02
- 🟢 [Awesome-VLA-Robotics](https://github.com/Jiaaqiliu/Awesome-VLA-Robotics) — 机器人VLA模型论文、模型与数据集集 `paper-list` ⭐477 · 📅2026-03
- 🟢 [Awesome-Robotics-Diffusion](https://github.com/showlab/Awesome-Robotics-Diffusion) — 将diffusion model引入机器人学习的最新论文精选列表 `paper-list` ⭐335 · 📅2026-05
- 🟢 [Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI) — 涵盖embodied AI综述、VLA、数据集与模拟器等 `awesome` ⭐211 · 📅2026-04
- 🟢 [Awesome-VLN](https://github.com/KwanWaiPang/Awesome-VLN) — 视觉语言导航(VLN)的综述用论文集 `survey` ⭐140 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) — Vision-Language-Action(VLA)的综述用论文集 `survey` ⭐79 · 📅2026-02
- 🟢 [Awesome-Legged-Robot-Localization-and-Mapping](https://github.com/KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping) — 足式机器人SLAM的综述用论文集 `survey` ⭐63 · 📅2026-04
- 🟡 [Awesome-Robot-Learning](https://github.com/RayYoh/Awesome-Robot-Learning) — 机器人学习(主要为操作)资源集 `awesome` ⭐202 · 📅2024-08
- 🔴 [awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling) — 汇集基于C++/Python/ROS的专业机器人开发工具 `awesome` ⭐3.8k · 📅2023-11
- 🔴 [awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning) — 足式运动学习资源集 `awesome` ⭐478 · 📅2023-07

## 🕸️ 图学习(GNN) / 知识图谱

- 🟢 [graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) — 基于图/Transformer的欺诈、异常与离群检测论文集 `paper-list` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Knowledge-Graph-Reasoning](https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning) — 知识图谱推理的论文、代码与数据集集 `paper-list` ⭐1.5k · 📅2025-11
- 🟢 [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) — 面向时间序列与时空数据的diffusion model综述与论文集(活跃) `survey` ⭐988 · 📅2026-02
- 🟢 [Awesome-DynamicGraphLearning](https://github.com/SpaceLearner/Awesome-DynamicGraphLearning) — 动态(时序)图与知识图谱上机器学习论文集 `paper-list` ⭐710 · 📅2025-06
- 🟢 [awesome-gnn-systems](https://github.com/ch-wan/awesome-gnn-systems) — GNN系统与加速相关资源集 `awesome` ⭐343 · 📅2026-06
- 🟢 [awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation) — 生成式分子建模与设计的论文集 `paper-list` ⭐343 · 📅2025-07
- 🟢 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection) — 2025年TKDE综述官方仓库,基于GNN的图异常检测论文与数据集 `survey` ⭐212 · 📅2026-05
- 🟢 [Awesome-TKGC](https://github.com/jiapuwang/Awesome-TKGC) — 用5阶段分类涵盖时序知识图谱补全(TKGC)的论文与资源 `paper-list` ⭐115 · 📅2025-10
- 🟢 [awesome-molecular-diffusion-models](https://github.com/AzureLeon1/awesome-molecular-diffusion-models) — 分子diffusion model相关论文的精选列表(活跃) `paper-list` ⭐100 · 📅2026-04
- 📑 [awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) — TKDE论文(对比/生成/预测型)的配套列表 `survey` ⭐1.4k · 📅2024-08
- 📑 [Awesome-GNN4TS](https://github.com/KimMeen/Awesome-GNN4TS) — 面向时间序列分析的GNN(TPAMI 2024)资源集 `survey` ⭐858 · 📅2024-08
- 📑 [awesome-pretrain-on-molecules](https://github.com/junxia97/awesome-pretrain-on-molecules) — 化学预训练模型(IJCAI 2023 survey)的论文列表 `survey` ⭐539 · 📅2023-06
- 📑 [Generative_KG_Construction_Papers](https://github.com/zjunlp/Generative_KG_Construction_Papers) — 生成式知识图谱构建综述(EMNLP 2022)的论文集 `survey` ⭐113 · 📅2023-07
- 📑 [Awesome-Trustworthy-GNNs](https://github.com/Radical3-HeZhang/Awesome-Trustworthy-GNNs) — 可信GNN(隐私/鲁棒性/公平性/可解释性)综述(Proc. IEEE 2024) `survey` ⭐98 · 📅2024-07
- 🟡 [GNNPapers](https://github.com/thunlp/GNNPapers) — 图神经网络(GNN)的必读论文集(经典) `paper-list` ⭐16.8k · 📅2023-12
- 🟡 [Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) — GNN论文列表 `paper-list` ⭐2.3k · 📅2023-12
- 🟡 [awesome-self-supervised-gnn](https://github.com/ChandlerBang/awesome-self-supervised-gnn) — GNN预训练与自监督学习的论文集 `paper-list` ⭐1.7k · 📅2024-02
- 🟡 [GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) — 面向交通预测的GNN论文与代码大规模合集 `paper-list` ⭐1.2k · 📅2024-08
- 🟡 [awesome-graph-transformer](https://github.com/wehos/awesome-graph-transformer) — graph transformer论文集 `paper-list` ⭐929 · 📅2025-03
- 🟡 [PromptKG](https://github.com/zjunlp/PromptKG) — 提示学习与知识图谱相关研究、工具与论文画廊 `paper-list` ⭐733 · 📅2024-03
- 🟡 [awesome-graph-generation](https://github.com/yuanqidu/awesome-graph-generation) — 涵盖图与分子生成的最新论文列表 `paper-list` ⭐360 · 📅2025-01
- 🟡 [Awesome-Hypergraph-Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network) — 超图学习、理论、数据与工具的精选集 `awesome` ⭐332 · 📅2025-02
- 🟡 [Awesome-Fair-Graph-Learning](https://github.com/EdisonLeeeee/Awesome-Fair-Graph-Learning) — 公平图学习(FairGL)的论文列表 `paper-list` ⭐144 · 📅2024-09
- 🟡 [Awesome-Temporal-Graph-Learning](https://github.com/MGitHubL/Awesome-Temporal-Graph-Learning) — temporal graph learning方法(论文、代码、数据集)集 `paper-list` ⭐92 · 📅2025-05
- 🟡 [Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) — 图OOD(泛化、训练时/测试时适应)的论文列表 `paper-list` ⭐85 · 📅2024-10
- 🟡 [Awesome-GNN-based-drug-discovery](https://github.com/gozsari/Awesome-GNN-based-drug-discovery) — 基于GNN的药物发现(论文、数据集、工具)精选列表 `awesome` ⭐63 · 📅2024-04
- 🟡 [HGNN_Collection](https://github.com/PolarisRisingWar/HGNN_Collection) — 异构图神经网络的数据集与算法集 `paper-list` ⭐61 · 📅2024-05
- 🟡 [awesome-GNN-social-recsys](https://github.com/claws-lab/awesome-GNN-social-recsys) — 基于GNN的社交推荐论文集 `paper-list` ⭐53 · 📅2024-05
- 🔴 [awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification) — 图嵌入、分类与表示学习的重要论文集(含实现) `paper-list` ⭐4.8k · 📅2023-03
- 🔴 [awesome-network-embedding](https://github.com/chihming/awesome-network-embedding) — 网络嵌入方法的经典精选列表 `awesome` ⭐2.6k · 📅2020-12
- 🔴 [knowledge-graphs](https://github.com/shaoxiongji/knowledge-graphs) — 知识图谱研究(嵌入、补全、时序KG、应用)论文集 `paper-list` ⭐1.8k · 📅2022-10
- 🔴 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection) — 基于深度学习的图异常检测论文、数据集与实现集 `awesome` ⭐384 · 📅2023-07
- 🔴 [awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) — 面向小分子药物发现的机器学习资源精选集 `awesome` ⭐241 · 📅2023-11
- 🔴 [awesome-graph-ood](https://github.com/THUMNLab/awesome-graph-ood) — 图OOD泛化相关论文集 `paper-list` ⭐169 · 📅2023-06
- 🔴 [awesome-expressive-gnn](https://github.com/mengliu1998/awesome-expressive-gnn) — GNN表达能力相关研究与改进论文集 `paper-list` ⭐124 · 📅2023-11

## 🛒 推荐系统(RecSys)

- 🟢 [RSPapers](https://github.com/hongleizhang/RSPapers) — 用17个类别整理推荐系统必读论文,每周更新(新增LLM/Agentic RS等) `awesome` ⭐6.5k · 📅2026-03
- 🟢 [Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) — 面向搜索、推荐与广告的深度学习论文集 `paper-list` ⭐2.5k · 📅2026-04
- 🟢 [Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys) — LLM相关推荐系统论文集(含TOIS录用综述) `survey` ⭐1.5k · 📅2026-01
- 🟢 [Awesome-LLM4RS-Papers](https://github.com/nancheng58/Awesome-LLM4RS-Papers) — LLM增强推荐系统的论文集 `paper-list` ⭐762 · 📅2026-03
- 🟢 [Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) — 冷启动推荐资源集(含LLM时代综述) `survey` ⭐283 · 📅2026-03
- 📑 [LLM4Rec-Awesome-Papers](https://github.com/WLiK/LLM4Rec-Awesome-Papers) — 使用LLM的推荐系统论文与资源集(含综述) `survey` ⭐2.3k · 📅2025-03
- 📑 [RecDebiasing](https://github.com/jiawei-chen/RecDebiasing) — TOIS 2023《Bias and Debias in Recommender System: A Survey》的去偏方法集 `survey` ⭐462 · 📅2024-02
- 📑 [Awesome-SSLRec-Papers](https://github.com/HKUDS/Awesome-SSLRec-Papers) — ACM CSUR《Self-Supervised Learning for Recommendation》综述的配套 `survey` ⭐122 · 📅2024-08
- 🔴 [Awesome-RSPapers](https://github.com/RUCAIBox/Awesome-RSPapers) — 推荐系统论文的全面列表 `paper-list` ⭐989 · 📅2022-10
- 🔴 [CRSPapers](https://github.com/RUCAIBox/CRSPapers) — 对话式推荐系统(CRS)的论文列表 `paper-list` ⭐80 · 📅2022-11
- 🔴 [Awesome-Sequence-Modeling-for-Recommendation](https://github.com/AiHubCN/Awesome-Sequence-Modeling-for-Recommendation) — 序列推荐与序列建模论文集 `paper-list` ⭐39 · 📅2023-11
- 🔴 [Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems](https://github.com/YuyingZhao/Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems) — 全面整理推荐系统的公平性与多样性研究 `paper-list` ⭐25 · 📅2023-06

## 📈 时间序列(Time Series)

- 🟢 [awesome-time-series-papers](https://github.com/TSCenter/awesome-time-series-papers) — 顶级AI会议最新时间序列论文与代码集 `paper-list` ⭐994 · 📅2026-04
- 🟢 [Awesome_Imputation](https://github.com/WenjieDu/Awesome_Imputation) — 汇集时间序列缺失值填补(imputation)论文与方法的综述仓库 `survey` ⭐420 · 📅2026-03
- 🟢 [awesome-time-series-forecasting](https://github.com/TongjiFinLab/awesome-time-series-forecasting) — 时间序列预测的论文与代码集 `paper-list` ⭐264 · 📅2026-04
- 🟢 [Awesome-Anomaly-Detection-Foundation-Models](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) — 基于基础模型的异常检测论文集 `paper-list` ⭐195 · 📅2026-05
- 🟢 [awesome-multivariate-time-series-anomaly-detection-algorithms](https://github.com/lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms) — 多变量时间序列异常检测论文列表 `paper-list` ⭐76 · 📅2025-09
- 🟢 [awesome-time-series-analysis](https://github.com/qhliu26/awesome-time-series-analysis) — 时间序列的论文、基准、数据集与教程集 `awesome` ⭐66 · 📅2025-09
- 📑 [time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) — 专门整理面向时间序列Transformer资源(论文、代码、数据)的综述 `survey` ⭐3k · 📅2024-08
- 🟡 [awesome-TS-anomaly-detection](https://github.com/rob-med/awesome-TS-anomaly-detection) — 时间序列数据异常检测的工具与数据集列表 `awesome` ⭐3.2k · 📅2024-10
- 🟡 [awesome-AI-for-time-series-papers](https://github.com/qingsongedu/awesome-AI-for-time-series-papers) — 顶会与期刊的时间序列AI论文、教程与综述集 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) — 面向时间序列、时空与事件数据的LLM/基础模型论文集 `paper-list` ⭐1.2k · 📅2024-12
- 🟡 [Awesome-TimeSeries-LLM-FM](https://github.com/start2020/Awesome-TimeSeries-LLM-FM) — 面向时间序列任务的LLM与基础模型资源集 `paper-list` ⭐154 · 📅2024-06
- 🟡 [Awesome-Large-Models-for-Time-Series](https://github.com/SJTU-DMTai/Awesome-Large-Models-for-Time-Series) — 面向时间序列分析的LLM与基础模型论文集 `paper-list` ⭐47 · 📅2024-10

## 🦾 AI 智能体 / LLM Agents

- 🟢 [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) — 86页综述《The Rise and Potential of LLM Based Agents》的论文列表 `survey` ⭐8.1k · 📅2025-09
- 🟢 [LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) — LLM智能体的必读论文集 `paper-list` ⭐3k · 📅2026-04
- 🟢 [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) — LLM智能体方法、应用与挑战综述的论文集 `survey` ⭐2.7k · 📅2025-11
- 🟢 [LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) — 基于LLM的智能体相关论文列表 `paper-list` ⭐2.3k · 📅2025-07
- 🟢 [awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) — 多智能体论文的精选集(Swarms team) `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — LLM智能体框架的精选列表 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) — 多模态GUI智能体的论文与资源集 `paper-list` ⭐1.2k · 📅2025-08
- 🟢 [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) — LLM驱动的自主智能体合集 `awesome` ⭐1.1k · 📅2026-05
- 🟢 [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — AI智能体研究论文集(工程、记忆、评估、工作流) `paper-list` ⭐986 · 📅2026-05
- 🟢 [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) — GUI智能体论文的精选列表 `paper-list` ⭐804 · 📅2026-05
- 🟢 [awesome-computer-use](https://github.com/ranpox/awesome-computer-use) — Computer-use GUI智能体的视频、博客、论文与项目集 `awesome` ⭐558 · 📅2026-04
- 🟢 [Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) — 语言智能体记忆(用户画像、对话历史)相关论文集 `paper-list` ⭐527 · 📅2026-05
- 🟢 [awesome-ui-agents](https://github.com/opendilab/awesome-ui-agents) — 跨Web/App/OS的UI智能体资源持续更新列表 `awesome` ⭐300 · 📅2026-05
- 🟢 [Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) — 基于图的智能体记忆综述、论文与基准集 `survey` ⭐279 · 📅2026-04
- 🟡 [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI自主智能体(项目/框架)的大规模列表 `awesome` ⭐28.1k · 📅2025-02
- 🟡 [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) — LLM驱动智能体的论文、仓库与博客集 `awesome` ⭐2.2k · 📅2025-04
- 🟡 [LLM-Planning-Papers](https://github.com/AGI-Edgerunners/LLM-Planning-Papers) — LLM规划(planning)相关必读论文集 `paper-list` ⭐440 · 📅2024-07
- 🟡 [awesome-llm-agents](https://github.com/junhua/awesome-llm-agents) — LLM智能体的高质量论文与开源项目集 `paper-list` ⭐84 · 📅2024-11
- 🟡 [Awesome-LLM-based-MultiAgents](https://github.com/Andrewzh112/Awesome-LLM-based-MultiAgents) — 基于LLM的多智能体论文集 `paper-list` ⭐27 · 📅2024-10
- 🔴 [Multi-Agent-Papers](https://github.com/shizhl/Multi-Agent-Papers) — 面向复杂任务的多智能体协作必读论文集 `paper-list` ⭐71 · 📅2023-11

## 🔬 医疗 AI / AI for Science

- 🟢 [MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) — 医疗LLM实践指南(发表于Nature Reviews Bioengineering) `survey` ⭐2k · 📅2025-09
- 🟢 [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) — 加速物理、化学、生物、材料等科学发现的AI工具与论文集 `awesome` ⭐1.6k · 📅2026-06
- 🟢 [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration) — 图像配准全领域的书籍、论文与工具箱集 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — 多模态学习在医学影像中应用的资源集 `awesome` ⭐960 · 📅2026-02
- 🟢 [Awesome-Healthcare-Foundation-Models](https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models) — 医疗基础模型的论文合集 `paper-list` ⭐515 · 📅2026-04
- 🟢 [awesome-foundation-model-single-cell-papers](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) — 专注单细胞基础模型的论文列表 `paper-list` ⭐452 · 📅2026-01
- 🟢 [Awesome-Radiology-Report-Generation](https://github.com/mk-runner/Awesome-Radiology-Report-Generation) — 放射学报告生成的论文、数据集与工具集(非常活跃) `paper-list` ⭐437 · 📅2026-06
- 🟢 [Awesome-LWMs](https://github.com/jaychempan/Awesome-LWMs) — 大型气象模型(LWMs)合集(AI4Earth) `awesome` ⭐360 · 📅2025-06
- 🟢 [awesome-AI4MolConformation-MD](https://github.com/AspirinCode/awesome-AI4MolConformation-MD) — 生成式AI/深度学习用于分子构象与分子动力学的论文集 `paper-list` ⭐294 · 📅2026-06
- 🟢 [Awesome-Earth-Artificial-Intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) — 地球科学AI的教程、软件、数据集与论文集 `awesome` ⭐244 · 📅2026-05
- 🟢 [awesome-mmps](https://github.com/willxxy/awesome-mmps) — EEG/ECG/EMG等生理信号×机器学习的资源与数据集集(活跃) `awesome` ⭐160 · 📅2026-02
- 🟢 [Awesome-Active-Learning-for-Medical-Image-Analysis](https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis) — 医学影像分析主动学习综述论文与代码 `survey` ⭐134 · 📅2025-06
- 🟢 [awesome-pathology](https://github.com/open-pathology/awesome-pathology) — 涵盖数字/计算病理资源(自监督、特征提取、数据集等) `awesome` ⭐119 · 📅2026-02
- 🟢 [awesome-drug-discovery](https://github.com/yboulaamane/awesome-drug-discovery) — 专注计算药物发现方法的精选资源列表 `awesome` ⭐112 · 📅2026-05
- 🟢 [SurvivalAnalysisPapers](https://github.com/shi-ang/SurvivalAnalysisPapers) — 按类别整理生存分析的论文与资源(活跃) `paper-list` ⭐90 · 📅2026-05
- 🟢 [Awesome-DL-for-Medical-Imaging-Segmentation](https://github.com/faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation) — 医学影像分割的深度学习论文集 `paper-list` ⭐66 · 📅2026-02
- 🟢 [awesome-bci-reviews](https://github.com/okbalefthanded/awesome-bci-reviews) — 按年代整理BCI的同行评审综述(活跃) `survey` ⭐47 · 📅2025-08
- 🟢 [AwesomeWSI](https://github.com/BearCleverProud/AwesomeWSI) — WSI分析与病理基础模型的全面合集(遵循IJCAI 2025综述,活跃) `survey` ⭐35 · 📅2026-06
- 🟢 [Awesome-Generative-Models-in-Pathology](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology) — 病理中生成模型(图像合成、报告生成、跨模态)的150余篇综述 `survey` ⭐27 · 📅2025-10
- 🟢 [Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) — 面向医疗的智能体AI最新综述集 `paper-list` ⭐23 · 📅2026-03
- 🟢 [Awesome-MICCAI-2026](https://github.com/ambicuity/Awesome-MICCAI-2026) — 从arXiv自动收集MICCAI 2026论文,bot每日更新并按领域分类 `paper-list` ⭐23 · 📅2026-05
- 🟢 [Awesome-AI4BCI](https://github.com/Deepak-Mewada/Awesome-AI4BCI) — 脑信号编码/解码深度学习模型资源集 `paper-list` ⭐17 · 📅2025-09
- 📑 [Awesome-Foundation-Models-in-Medical-Imaging](https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging) — 医学影像视觉与语言基础模型精选列表 `survey` ⭐301 · 📅2024-06
- 📑 [Awesome-Foundation-Models-for-Weather-and-Climate](https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate) — 面向气象与气候数据理解的基础模型综合综述 `survey` ⭐293 · 📅2025-02
- 📑 [Awesome-Foundation-Models-for-Advancing-Healthcare](https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare) — 医疗基础模型(HFM)挑战、机遇与未来展望的综合综述 `survey` ⭐251 · 📅2024-12
- 📑 [DL-ECG-Review](https://github.com/hsd1503/DL-ECG-Review) — ECG深度学习方法综述与论文摘要表 `survey` ⭐250 · 📅2020-10
- 📑 [MedImgReg_Survey](https://github.com/JHU-MedImage-Reg/MedImgReg_Survey) — 基于学习的医学图像配准论文集+损失函数/评估指标实现 `survey` ⭐121 · 📅2025-05
- 🟡 [awesome-deep-learning-single-cell-papers](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) — 按30余项任务整理单细胞分析×深度学习的最新论文 `paper-list` ⭐857 · 📅2025-04
- 🟡 [awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning) — 蛋白质表示学习(含AlphaFold)的论文集 `paper-list` ⭐685 · 📅2024-11
- 🟡 [Awesome-Medical-Large-Language-Models](https://github.com/burglarhobbit/Awesome-Medical-Large-Language-Models) — 精选医疗与健康领域LLM论文的合集 `paper-list` ⭐392 · 📅2025-05
- 🟡 [awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design) — 基于AI的蛋白质设计研究论文集 `paper-list` ⭐306 · 📅2024-05
- 🟡 [Awesome-LLM-Healthcare](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) — 对应医疗领域LLM综述论文的论文列表 `paper-list` ⭐269 · 📅2023-12
- 🟡 [Awesome-Neuron-Segmentation-in-EM-Images](https://github.com/subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images) — 电子显微镜(EM)图像中神经突起3D分割资源集 `awesome` ⭐57 · 📅2024-03
- 🟡 [awesome-molecule-protein-pretrain-papers](https://github.com/OmicsML/awesome-molecule-protein-pretrain-papers) — 分子与蛋白质预训练论文集(药物发现、对接) `paper-list` ⭐47 · 📅2024-03
- 🟡 [Awesome_AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) — 地球系统(尤其气象与气候)机器学习论文集 `paper-list` ⭐14 · 📅2023-12
- 🔴 [MICCAI-OpenSourcePapers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) — 以带代码链接的表格整理MICCAI 2019-2023开源论文 `paper-list` ⭐1.3k · 📅2023-11
- 🔴 [awesome-ehr-deeplearning](https://github.com/hurcy/awesome-ehr-deeplearning) — EHR挖掘、机器学习与深度学习论文集 `awesome` ⭐429 · 📅2022-10
- 🔴 [Physiological-Signal-Classification-Papers](https://github.com/ziyujia/Physiological-Signal-Classification-Papers) — 按任务整理EEG/ECG/EMG/EOG的分类论文 `paper-list` ⭐249 · 📅2022-07
- 🔴 [awesome-radiology-report-generation](https://github.com/zhjohnchan/awesome-radiology-report-generation) — 放射学/医疗报告生成及相关领域的精选列表 `awesome` ⭐180 · 📅2022-05
- 🔴 [awesome-structural-bioinformatics](https://github.com/twoXes/awesome-structural-bioinformatics) — 结构生物信息学的资源集 `awesome` ⭐79 · 📅2023-05
- 🔴 [awesome-bio-chatgpt](https://github.com/OmicsML/awesome-bio-chatgpt) — ChatGPT/LLM应用于生物学与医疗领域的论文与资源集 `paper-list` ⭐22 · 📅2023-04

## 🌍 应用领域 (Code/Math/Finance/Law/科学)

- 🟢 [techniques](https://github.com/satellite-image-deep-learning/techniques) — 卫星与航空图像深度学习方法的超大规模参考 `awesome` ⭐10.2k · 📅2026-05
- 🟢 [awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) — 金融市场LLM、深度学习策略与工具的经典列表 `awesome` ⭐6k · 📅2026-05
- 🟢 [Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) — 面向代码的语言模型研究与数据集的全面精选 `paper-list` ⭐3.4k · 📅2026-05
- 🟢 [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) — 遥感变化检测的数据集、方法与综述集 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Remote-Sensing-Foundation-Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) — 涵盖RSFM论文、数据集、基准与预训练权重(活跃) `paper-list` ⭐1.8k · 📅2026-05
- 🟢 [awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) — 面向农业、农场与园艺的开源技术(含ML、GIS、遥感、机器人)经典列表 `awesome` ⭐1.8k · 📅2026-01
- 🟢 [awesome-search](https://github.com/frutik/awesome-search) — 以电商搜索为中心,涵盖语义检索、LTR、查询理解与搜索质量 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) — 对约510个原子论机器学习项目带评分排名(活跃) `awesome` ⭐691 · 📅2026-05
- 🟢 [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) — 涵盖数学、物理、化学、材料、生物、地球科学等科学领域预训练模型的综合综述 `survey` ⭐660 · 📅2025-06
- 🟢 [awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) — 现代材料科学中材料信息学的工作集 `awesome` ⭐515 · 📅2026-03
- 🟢 [awesome-digital-humanities](https://github.com/dh-tech/awesome-digital-humanities) — 面向人文学者的定量与计算方法软件集(NLP、主题模型、文本分析) `awesome` ⭐383 · 📅2026-05
- 🟢 [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) — 整理从需求、开发、测试到维护的SE全领域LLM论文 `survey` ⭐329 · 📅2026-04
- 🟢 [awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) — 判决预测、合同分类、判例检索、法律QA等LegalNLP资源集 `awesome` ⭐326 · 📅2025-10
- 🟢 [awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) — 收集顶会与期刊的面向教育AI/LLM论文 `paper-list` ⭐187 · 📅2026-04
- 🟢 [awesome-pinns](https://github.com/AI-in-Transportation-Lab/awesome-pinns) — PINN/物理信息机器学习的库、论文与教程精选集 `awesome` ⭐110 · 📅2026-06
- 🟢 [PINN_Paper_List](https://github.com/Event-AHU/PINN_Paper_List) — 物理信息神经网络(PINN)的论文列表 `paper-list` ⭐78 · 📅2026-04
- 📑 [FinLLMs](https://github.com/adlnlp/FinLLMs) — 论文《Large Language Models in Finance》的相关研究、基准与数据集集 `survey` ⭐370 · 📅2025-04
- 📑 [DL4TP](https://github.com/zhaoyu-li/DL4TP) — 深度学习用于定理证明的调查,按autoformalization、proof search等分类 `survey` ⭐224 · 📅2025-05
- 📑 [awesome-RSFMs](https://github.com/xiaoaoran/awesome-RSFMs) — 综述《Foundation Models for Remote Sensing and Earth Observation》官方仓库 `survey` ⭐51 · 📅2024-11
- 🟡 [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — 侧重机器学习的量化/算法交易资源集 `awesome` ⭐3.7k · 📅2025-05
- 🟡 [PINNpapers](https://github.com/idrl-lab/PINNpapers) — PINN必读论文集,按并行化、加速、迁移学习、不确定性量化与应用整理 `paper-list` ⭐1.5k · 📅2023-12
- 🟡 [LLM4SoftwareTesting](https://github.com/LLM-Testing/LLM4SoftwareTesting) — 使用LLM进行测试生成、测试补全等的论文集 `paper-list` ⭐529 · 📅2024-01
- 🟡 [awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) — AI应用于电子设计自动化(EDA、芯片设计)的论文集 `paper-list` ⭐209 · 📅2023-12
- 🟡 [awesome-ai4lam](https://github.com/AI4LAM/awesome-ai4lam) — 面向图书馆、档案馆与博物馆(GLAM/LAM)的AI项目、案例与资源集(AI4LAM社区运营) `awesome` ⭐178 · 📅2024-06
- 🟡 [Awesome-LLM4Math](https://github.com/tongyx361/Awesome-LLM4Math) — LLM数学推理的高质量精选列表,整理训练数据、SFT、RL与基准 `paper-list` ⭐157 · 📅2024-07
- 🟡 [Awesome-Education-LLM](https://github.com/Geralt-Targaryen/Awesome-Education-LLM) — 整理面向教育的LLM研究与应用(教学辅助、出题、自动批改等) `paper-list` ⭐77 · 📅2024-09
- 🟡 [LLM_X_papers](https://github.com/czyssrs/LLM_X_papers) — 持续更新金融、医疗、法律LLM论文的阅读列表 `paper-list` ⭐54 · 📅2025-02
- 🔴 [awesome-machine-learning-on-source-code](https://github.com/src-d/awesome-machine-learning-on-source-code) — 将机器学习应用于源代码(MLonCode)的论文与链接集 `awesome` ⭐6.6k · 📅2020-12
- 🔴 [Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) — 汇集司法AI的语料、基准、QA与摘要数据集 `awesome` ⭐303 · 📅2023-07
- 🔴 [awesome-program](https://github.com/shaohua0116/awesome-program) — 程序合成、归纳、执行、修复与programmatic RL的论文集 `paper-list` ⭐168 · 📅2021-10
- 🔴 [Awesome-Precision-Agriculture](https://github.com/px39n/Awesome-Precision-Agriculture) — 基于UAV与深度学习的产量预测、作物检测、杂草检测等论文集 `paper-list` ⭐137 · 📅2020-09
- 🔴 [awesome-ai4chem](https://github.com/sherrylixuecheng/awesome-ai4chem) — 面向化学的AI论文精选 `paper-list` ⭐49 · 📅2023-05
- 🔴 [Awesome-Sports-Analytics](https://github.com/wywyWang/Awesome-Sports-Analytics) — 足球、篮球、羽毛球等体育分析论文/代码集 `paper-list` ⭐20 · 📅2023-03

## 🚗 自动驾驶(Autonomous Driving)

- 🟢 [Birds-eye-view-Perception](https://github.com/OpenDriveLab/Birds-eye-view-Perception) — BEV感知研究与食谱(IEEE T-PAMI 2023) `survey` ⭐1.4k · 📅2025-07
- 🟢 [Awesome-Trajectory-Motion-Prediction-Papers](https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers) — 轨迹与运动预测的全面论文集 `paper-list` ⭐1.1k · 📅2026-01
- 📑 [Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) — 数据中心自动驾驶综述的官方仓库 `survey` ⭐180 · 📅2024-03
- 🟡 [awesome-lane-detection](https://github.com/amusi/awesome-lane-detection) — 车道检测(lane detection)的论文列表 `paper-list` ⭐3k · 📅2024-08
- 🟡 [Awesome-Interaction-Aware-Trajectory-Prediction](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction) — 考虑交互的轨迹预测前沿研究资料集 `paper-list` ⭐1.7k · 📅2024-09
- 🟡 [Awesome-Autonomous-Driving](https://github.com/autodriving-heart/Awesome-Autonomous-Driving) — 自动驾驶全领域的awesome列表 `awesome` ⭐1.1k · 📅2024-08
- 🟡 [awesome-knowledge-driven-AD](https://github.com/PJLab-ADG/awesome-knowledge-driven-AD) — 知识驱动型自动驾驶的精选论文集 `paper-list` ⭐501 · 📅2024-06
- 🟡 [Awesome-Autonomous-Driving](https://github.com/PeterJaq/Awesome-Autonomous-Driving) — 自动驾驶全领域的广泛列表 `awesome` ⭐353 · 📅2024-08
- 🟡 [Awesome-occupancy-perception](https://github.com/autodriving-heart/Awesome-occupancy-perception) — 占用感知(Occupancy)论文合集 `paper-list` ⭐308 · 📅2024-08
- 🟡 [CVPR-2024-Papers-Autonomous-Driving](https://github.com/autodriving-heart/CVPR-2024-Papers-Autonomous-Driving) — CVPR 2024自动驾驶相关论文列表 `paper-list` ⭐257 · 📅2024-08
- 🟡 [CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI](https://github.com/autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI) — CVPR 2025自动驾驶与具身AI相关论文列表 `paper-list` ⭐30 · 📅2025-04
- 🟡 [Awesome-4D-Radar](https://github.com/autodriving-heart/Awesome-4D-Radar) — 4D雷达感知相关论文与资源集 `paper-list` ⭐12 · 📅2024-02
- 🔴 [awesome-end-to-end-autonomous-driving](https://github.com/opendilab/awesome-end-to-end-autonomous-driving) — 持续更新End-to-End自动驾驶资源的列表 `awesome` ⭐493 · 📅2023-08
- 🔴 [Awesome-Occupancy-Prediction-Autonomous-Driving](https://github.com/chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving) — 多相机语义占用预测论文(Occ3D等) `paper-list` ⭐263 · 📅2023-07
- 🔴 [awesome-driving-behavior-prediction](https://github.com/opendilab/awesome-driving-behavior-prediction) — 驾驶行为预测的研究论文集 `paper-list` ⭐83 · 📅2022-12
- 🔴 [Awesome-BEV-Perception](https://github.com/autodriving-heart/Awesome-BEV-Perception) — BEV感知的精选论文合集 `paper-list` ⭐32 · 📅2023-06
- 🔴 [Awesome-Trajectory-Prediction](https://github.com/autodriving-heart/Awesome-Trajectory-Prediction) — 轨迹预测的论文合集 `paper-list` ⭐27 · 📅2023-06
- 🔴 [Awesome-BEV-Perception](https://github.com/ylhua/Awesome-BEV-Perception) — BEV感知相关论文(BEVFormer、PETRv2、FIERY等) `paper-list` ⭐5 · 📅2022-08

## 🛡️ AI 安全 / Alignment / 可解释性

- 🟢 [awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) — 负责任ML与可解释性的综合资源列表 `awesome` ⭐4k · 📅2026-05
- 🟢 [Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) — LLM安全的论文、文章、数据集与基准集 `awesome` ⭐1.9k · 📅2026-05
- 🟢 [awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) — ICDM/KDD/SDM等欺诈检测数据挖掘论文的经典列表 `paper-list` ⭐1.8k · 📅2026-01
- 🟢 [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) — 可解释AI/ML的研究资料集 `paper-list` ⭐1.6k · 📅2026-03
- 🟢 [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) — LLM安全的工具、文献与项目集 `awesome` ⭐1.6k · 📅2025-08
- 🟢 [TAADpapers](https://github.com/thunlp/TAADpapers) — 文本对抗攻击与防御(TAAD)的必读论文集 `paper-list` ⭐1.6k · 📅2025-06
- 🟢 [Awesome-Jailbreak-on-LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) — LLM越狱方法的论文、代码、数据集与评估集(非常活跃) `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) — 机器遗忘综述的官方列表,涵盖方法、数据集与评估指标 `awesome` ⭐950 · 📅2026-05
- 🟢 [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) — LLM机器遗忘的论文、综述与基准集 `paper-list` ⭐594 · 📅2026-05
- 🟢 [awesome-trustworthy-deep-learning](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning) — OOD泛化、对抗样本、后门等可信论文(每日更新) `paper-list` ⭐386 · 📅2026-05
- 🟢 [membership-inference-machine-learning-literature](https://github.com/HongshengHu/membership-inference-machine-learning-literature) — 专注成员推断攻击的文献集 `paper-list` ⭐371 · 📅2026-04
- 🟢 [Awesome-AI-for-cybersecurity](https://github.com/Billy1900/Awesome-AI-for-cybersecurity) — 涵盖网络入侵检测、反恶意软件、WAF与反欺诈的AI列表 `awesome` ⭐254 · 📅2026-05
- 🟢 [Awesome-model-inversion-attack](https://github.com/AndrewZhou924/Awesome-model-inversion-attack) — 模型反演攻击综述的官方列表,按CV/图/NLP整理 `paper-list` ⭐221 · 📅2026-04
- 🟢 [Awesome-LMMs-Mechanistic-Interpretability](https://github.com/itsqyh/Awesome-LMMs-Mechanistic-Interpretability) — 处理大规模多模态模型内部表示的机制可解释性资源集(活跃) `survey` ⭐203 · 📅2026-03
- 🟢 [Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) — 按模态与用途整理生成AI遗忘论文 `paper-list` ⭐188 · 📅2026-04
- 🟢 [Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) — 按图像、音频、文本整理生成AI模型水印方法(活跃) `awesome` ⭐141 · 📅2026-05
- 🟢 [awesome-mechanistic-interpretability](https://github.com/AI-in-Transportation-Lab/awesome-mechanistic-interpretability) — 将神经网络逆向解析为可理解计算要素的机制可解释性资源集 `awesome` ⭐98 · 📅2026-06
- 🟢 [awesome-fraud-detection](https://github.com/AI4Risk/awesome-fraud-detection) — 基于GNN的金融欺诈检测带综述论文与代码集(活跃) `paper-list` ⭐43 · 📅2026-05
- 📑 [Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers) — LLM安全综述论文列表 `survey` ⭐55 · 📅2024-12
- 🟡 [awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) — 用ML处理恶意软件、入侵检测等的工具、论文与教材经典列表 `awesome` ⭐8.8k · 📅2024-08
- 🟡 [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) — 涵盖针对提示注入的实用与已提出防御措施 `awesome` ⭐696 · 📅2025-02
- 🟡 [awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) — 涵盖成员推断、模型反演、属性推断与模型提取的论文列表 `awesome` ⭐639 · 📅2024-03
- 🟡 [Awesome-Backdoor-in-Deep-Learning](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning) — 按攻击类型与防御阶段整理深度学习后门攻防的论文集(活跃) `paper-list` ⭐238 · 📅2024-03
- 🟡 [awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) — AI质量与安全相关论文与技术文章精选列表 `paper-list` ⭐215 · 📅2025-04
- 🟡 [OpenRedTeaming](https://github.com/Libr-AI/OpenRedTeaming) — LLM/多模态的red teaming论文集(实现30+方法) `paper-list` ⭐165 · 📅2025-05
- 🟡 [trojai-literature](https://github.com/usnistgov/trojai-literature) — NIST运营的AI木马攻击研究文献综览 `paper-list` ⭐149 · 📅2024-10
- 🟡 [Learning-Deep-Hiding](https://github.com/TracyCuiq/Learning-Deep-Hiding) — 系统整理含图像隐写与水印的「deep hiding」论文 `paper-list` ⭐67 · 📅2024-06
- 🟡 [Constitutional-AI-awesome-papers](https://github.com/minbeomkim/Constitutional-AI-awesome-papers) — Constitutional AI/伦理准则下AI相关论文列表 `paper-list` ⭐13 · 📅2024-03
- 🔴 [awesome-adversarial-machine-learning](https://github.com/yenchenlin/awesome-adversarial-machine-learning) — 汇集对抗机器学习论文、博客与演讲的经典精选 `awesome` ⭐1.9k · 📅2020-11
- 🔴 [awesome-interpretable-machine-learning](https://github.com/lopusz/awesome-interpretable-machine-learning) — 可解释机器学习的资源列表 `awesome` ⭐916 · 📅2023-03
- 🔴 [awesome-fairness-in-ai](https://github.com/datamllab/awesome-fairness-in-ai) — AI公平性资源的精选集 `awesome` ⭐334 · 📅2023-09
- 🔴 [awesome-xai](https://github.com/altamiracorp/awesome-xai) — 可解释AI(XAI)与可解释ML的论文与资源 `awesome` ⭐188 · 📅2021-05
- 🔴 [awesome-ai-alignment](https://github.com/dit7ya/awesome-ai-alignment) — AI对齐研究优秀资源的精选列表 `awesome` ⭐81 · 📅2023-07
- 🔴 [awesome-ml-fairness](https://github.com/brandeis-machine-learning/awesome-ml-fairness) — 机器学习公平性相关论文与资源集 `paper-list` ⭐74 · 📅2023-05
- 🔴 [awesome-ai-safety](https://github.com/hari-sikchi/awesome-ai-safety) — AI安全的论文、项目与社区列表 `awesome` ⭐64 · 📅2020-02
- 🔴 [awesome-data-poisoning](https://github.com/ch-shin/awesome-data-poisoning) — 顶会数据投毒攻防论文集 `awesome` ⭐25 · 📅2022-09
- 🔴 [Awesome-Adversarial-Training](https://github.com/KululuMi/Awesome-Adversarial-Training) — FGSM/PGD/TRADES/AutoAttack等对抗训练论文列表 `paper-list` ⭐6 · 📅2022-04

## ⚖️ AI 伦理 / 治理 / 监管 / Human-AI Interaction

- 🟢 [awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) — 按地区涵盖各国AI监管、指南、伦理规范与标准 `awesome` ⭐1.4k · 📅2026-05
- 🟢 [awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) — 计算社会科学的书籍、课程与开源资源全面列表(GESIS运营) `awesome` ⭐890 · 📅2026-05
- 🟢 [Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science) — 将LLM应用于社会科学的论文集 `paper-list` ⭐623 · 📅2026-02
- 🟢 [AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI) — 在17个领域汇集负责任AI的研究、书籍、监管、成熟度模型与工具 `awesome` ⭐129 · 📅2026-05
- 🟢 [Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) — 从心理测量视角探讨LLM人格、价值观、心智理论与认知能力的论文集 `survey` ⭐109 · 📅2025-11
- 🔴 [NLP4SocialGood_Papers](https://github.com/zhijing-jin/NLP4SocialGood_Papers) — 面向社会公益的NLP论文阅读列表(救命、生活质量、公平性等) `paper-list` ⭐310 · 📅2023-09
- 🔴 [awesome-HAI](https://github.com/bwang514/awesome-HAI) — 从HCI视角探讨人与AI交互设计的学术资料集 `awesome` ⭐297 · 📅2021-05

## ⚡ 高效化 (压缩/量化/NAS/AutoML)

- 🟢 [Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) — 面向iOS的Core ML模型的最大规模列表 `model` ⭐7k · 📅2025-06
- 🟢 [Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) — 模型量化的论文、代码与文档列表 `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) — 高效LLM(剪枝、量化、蒸馏等)的精选列表 `awesome` ⭐2k · 📅2025-06
- 🟢 [Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) — 量化、剪枝、蒸馏等LLM压缩的论文与工具集 `awesome` ⭐1.8k · 📅2026-02
- 🟢 [tinyml-papers-and-projects](https://github.com/gigwegbe/tinyml-papers-and-projects) — TinyML的论文与项目集(活跃更新) `paper-list` ⭐1k · 📅2025-12
- 🟢 [awesome-AutoML](https://github.com/windmaple/awesome-AutoML) — AutoML精选列表 `awesome` ⭐936 · 📅2026-03
- 🟢 [awesome-ai-efficiency](https://github.com/PrunaAI/awesome-ai-efficiency) — AI模型加速、小型化与节能方法列表 `awesome` ⭐222 · 📅2026-02
- 🟢 [Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) — 端侧AI系统(推理引擎/基准/论文),活跃 `awesome` ⭐157 · 📅2026-05
- 🟢 [awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) — 评估与降低AI环境影响的Green AI工具/论文经典列表 `awesome` ⭐114 · 📅2026-05
- 📑 [Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) — 与LLM知识蒸馏综述联动的论文集 `survey` ⭐1.3k · 📅2025-03
- 🟡 [awesome-ml-model-compression](https://github.com/cedrickchee/awesome-ml-model-compression) — 模型压缩与量化的研究论文、工具与学习资料 `awesome` ⭐543 · 📅2024-09
- 🟡 [awesome-nas-papers](https://github.com/jackguagua/awesome-nas-papers) — Neural Architecture Search论文汇集列表 `paper-list` ⭐405 · 📅2024-01
- 🔴 [deep-learning-model-convertor](https://github.com/ysh329/deep-learning-model-convertor) — 不同深度学习框架间模型转换工具的一览 `awesome` ⭐3.2k · 📅2023-06
- 🔴 [Awesome-Knowledge-Distillation](https://github.com/FLHonker/Awesome-Knowledge-Distillation) — 对知识蒸馏论文分类整理(2014-2021) `paper-list` ⭐2.7k · 📅2023-05
- 🔴 [Awesome-AutoDL](https://github.com/D-X-Y/Awesome-AutoDL) — 自动深度学习(AutoDL)资源与详细分析 `awesome` ⭐2.3k · 📅2022-09
- 🔴 [awesome-emdl](https://github.com/csarron/awesome-emdl) — 嵌入式与移动深度学习的论文/库/工具集 `awesome` ⭐768 · 📅2023-03
- 🔴 [awesome-edge-machine-learning](https://github.com/Bisonai/awesome-edge-machine-learning) — 涵盖边缘机器学习的论文、推理引擎、挑战与书籍 `awesome` ⭐280 · 📅2023-02
- 🔴 [awesome-transformer-search](https://github.com/automl/awesome-transformer-search) — 结合Transformer与NAS的资源列表 `awesome` ⭐270 · 📅2023-06
- 🔴 [awesome-model-compression](https://github.com/ChanChiChoi/awesome-model-compression) — 模型压缩(结构、蒸馏、二值化、量化、剪枝)论文集 `paper-list` ⭐166 · 📅2023-02
- 🔴 [NASPapers](https://github.com/NiuTrans/NASPapers) — 神经架构搜索(NAS)的论文列表 `paper-list` ⭐135 · 📅2021-09
- 🔴 [awesome-compression-papers](https://github.com/chenbong/awesome-compression-papers) — 压缩与加速(剪枝、量化、蒸馏、低秩分解)论文集 `paper-list` ⭐25 · 📅2020-10
- 🔴 [awesome-architecture-search](https://github.com/chenyaofo/awesome-architecture-search) — 最新追踪NAS进展的论文列表 `paper-list` ⭐9 · 📅2022-05
- 🔴 [Awesome-NAS](https://github.com/Openning07/Awesome-NAS) — 神经架构搜索(NAS)资源精选 `awesome` ⭐1 · 📅2020-04

## 🔐 联邦学习 / 隐私

- 🟢 [Awesome-Differential-Privacy-and-Meachine-Learning](https://github.com/JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning) — 使用差分隐私的联邦学习与ML论文及实现 `paper-list` ⭐388 · 📅2025-09
- 🟢 [Awesome-ML-SP-Papers](https://github.com/gnipping/Awesome-ML-SP-Papers) — 安全四大顶会的ML Security & Privacy论文集 `paper-list` ⭐348 · 📅2025-11
- 🟡 [awesome-federated-learning](https://github.com/poga/awesome-federated-learning) — 联邦学习与ML隐私的资源集 `awesome` ⭐547 · 📅2024-06
- 🟡 [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper) — 联邦学习系统与框架的论文列表 `paper-list` ⭐75 · 📅2024-02
- 🔴 [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning) — 与FedML联动的联邦学习研究与生产集成列表 `paper-list` ⭐2k · 📅2022-09
- 🔴 [awesome-secure-federated-learning-papers](https://github.com/csl-cqu/awesome-secure-federated-learning-papers) — 安全联邦学习(攻击、防御、梯度反演)论文集 `paper-list` ⭐26 · 📅2023-03
- 🔴 [awesome-federated-learning](https://github.com/Willjay5991/awesome-federated-learning) — 联邦学习的论文、文章、框架与讲义资料 `awesome` ⭐2 · 📅2020-08

## ♻️ 持续学习(Continual Learning)

- 🟢 [Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning) — 增量学习、持续学习与灾难性遗忘的主要会议论文集 `paper-list` ⭐4.5k · 📅2026-05
- 📑 [awesome-lifelong-learning-methods-for-llm](https://github.com/zzz47zzz/awesome-lifelong-learning-methods-for-llm) — LLM终身学习相关综述与论文集 `survey` ⭐162 · 📅2025-05
- 🟡 [Best-Incremental-Learning](https://github.com/Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning) — 增量、持续与终身学习的仓库 `paper-list` ⭐607 · 📅2024-05
- 🟡 [Awesome-Continual-Learning](https://github.com/feifeiobama/Awesome-Continual-Learning) — 持续学习论文与BibTeX条目的精选列表 `paper-list` ⭐203 · 📅2024-10
- 🟡 [Awesome-Continual-Learning](https://github.com/lywang3081/Awesome-Continual-Learning) — 与持续学习综述联动的论文列表与实用资源 `paper-list` ⭐108 · 📅2024-02
- 🔴 [awesome-lifelong-continual-learning](https://github.com/prprbr/awesome-lifelong-continual-learning) — 终身/持续学习的论文、博客、数据集与软件列表 `awesome` ⭐298 · 📅2021-03
- 🔴 [LLM-Continual-Learning-Papers](https://github.com/AGI-Edgerunners/LLM-Continual-Learning-Papers) — LLM持续学习(continual learning)的必读论文集 `paper-list` ⭐149 · 📅2023-11

## 🖥️ ML 系统 / 训练・推理基础设施 / 数据

- 🟢 [AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) — 汇集AI系统论文与产业实践(OSDI/NSDI/MLSys等,含LLM、GenAI)的经典 `awesome` ⭐4.1k · 📅2025-07
- 🟢 [Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) — LLM合成数据生成的阅读列表(活跃) `paper-list` ⭐1.5k · 📅2025-06
- 🟢 [rtdl](https://github.com/yandex-research/rtdl) — 表格数据深度学习的论文与包集(Yandex Research) `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [ML4DB-paper-list](https://github.com/LumingSun/ML4DB-paper-list) — 用AI增强DB系统的论文集(学习型索引、查询优化) `paper-list` ⭐774 · 📅2026-04
- 🟢 [ml-systems-papers](https://github.com/byungsoo-oh/ml-systems-papers) — 系统收集ML系统领域论文的合集 `paper-list` ⭐569 · 📅2026-02
- 🟢 [awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) — 汇集AI系统论文及其代码的列表 `paper-list` ⭐362 · 📅2026-05
- 🟢 [awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) — 高维向量检索与数据库相关的精选列表(活跃) `awesome` ⭐353 · 📅2026-05
- 🟢 [Awesome-LLM-Inference-Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) — 按延迟/吞吐/内存分类LLM推理优化方法的全面总结 `survey` ⭐210 · 📅2026-04
- 🟢 [Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) — 《Representation Learning for Tabular Data》综述配套列表 `survey` ⭐123 · 📅2026-05
- 🟢 [awesome-ai4db-paper](https://github.com/Wind-Gone/awesome-ai4db-paper) — AI4DB论文集(学习型索引、基数估计、学习型查询优化、LLM×DB) `paper-list` ⭐112 · 📅2026-04
- 🟡 [data-augmentation-review](https://github.com/AgaMiko/data-augmentation-review) — 广泛收集数据增强方法、库与论文的综述 `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-vector-search](https://github.com/currentslab/awesome-vector-search) — 向量检索的库、服务与论文集(Faiss、Annoy等) `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) — 大模型分布式训练与推理相关项目与论文的精选列表 `awesome` ⭐279 · 📅2024-10
- 🟡 [awesome-synthetic-data](https://github.com/statice/awesome-synthetic-data) — 开源/商用合成数据工具精选列表(SDV等) `awesome` ⭐257 · 📅2024-01
- 🟡 [Awesome-LLM-Inference](https://github.com/DefTruth/Awesome-LLM-Inference) — LLM/VLM推理优化(FlashAttention、PagedAttention、MLA等)的论文+代码集 `paper-list` ⭐16 · 📅2025-03
- 🔴 [awesome-data-augmentation](https://github.com/CrazyVertigo/awesome-data-augmentation) — 数据增强方法(AugMix、CutMix等)的精选列表 `awesome` ⭐797 · 📅2021-03
- 🔴 [awesome-dl-hw-resources](https://github.com/RaviVijay/awesome-dl-hw-resources) — 深度学习硬件/芯片设计资源的精选列表 `awesome` ⭐58 · 📅2018-05
- 🔴 [awesome-ml-testing](https://github.com/yqtian-se/awesome-ml-testing) — ML/深度学习系统测试相关论文与工具集 `paper-list` ⭐47 · 📅2021-10
- 🔴 [Awesome-MLSys](https://github.com/dujiangsu/Awesome-MLSys) — 以大模型推理为中心的MLSys领域学术论文集 `paper-list` ⭐6 · 📅2023-09

## 🛠️ MLOps / 数据中心 AI

- 🟢 [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) — 用于ML部署、监控与扩展的开源库列表 `awesome` ⭐20.6k · 📅2026-05
- 🟢 [awesome-mlops](https://github.com/kelvins/awesome-mlops) — MLOps工具精选列表 `awesome` ⭐5.2k · 📅2026-04
- 🟢 [Awesome-Dataset-Distillation](https://github.com/Guang000/Awesome-Dataset-Distillation) — 涵盖梯度/分布匹配、生成方法与应用的经典列表(非常活跃) `awesome` ⭐1.9k · 📅2026-05
- 🟢 [awesome-data-centric-ai](https://github.com/Data-Centric-AI-Community/awesome-data-centric-ai) — 数据中心AI的开源、教程与研究 `awesome` ⭐350 · 📅2026-04
- 🟢 [awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) — 涵盖数据评估、数据归因与数据选择/剪枝/coreset `paper-list` ⭐120 · 📅2026-05
- 🟡 [awesome-mlops](https://github.com/visenger/awesome-mlops) — MLOps的参考文献与资源集 `awesome` ⭐13.9k · 📅2024-11
- 🟡 [awesome-data-labeling](https://github.com/HumanSignal/awesome-data-labeling) — 精选数据标注工具的列表 `awesome` ⭐4.3k · 📅2024-06
- 🟡 [data-centric-AI](https://github.com/daochenzha/data-centric-AI) — 数据中心AI的资源精选列表 `awesome` ⭐1.1k · 📅2024-06
- 🟡 [data-centric-ai](https://github.com/HazyResearch/data-centric-ai) — 数据中心AI资源集(Stanford HazyResearch) `awesome` ⭐1.1k · 📅2023-12
- 🟡 [Awesome-Coreset-Selection](https://github.com/PatrickZH/Awesome-Coreset-Selection) — coreset/子集选择与data pruning的论文集 `awesome` ⭐183 · 📅2024-06
- 🔴 [releasing-research-code](https://github.com/paperswithcode/releasing-research-code) — ML研究代码发布的最佳实践(NeurIPS 2020官方推荐) `awesome` ⭐2.9k · 📅2023-05
- 🔴 [awesome-open-data-centric-ai](https://github.com/Renumics/awesome-open-data-centric-ai) — 面向非结构化数据的数据中心AI开源工具集 `awesome` ⭐732 · 📅2023-11

## 📊 数据集 / 基准测试

- 🟢 [Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) — LLM评估的工具、基准、排行榜与论文精选列表 `awesome` ⭐637 · 📅2025-11
- 🟢 [Awesome-Datasets-Hub](https://github.com/ahammadmejbah/Awesome-Datasets-Hub) — 医疗AI、NLP、多模态等面向LLM的数据集集 `awesome` ⭐135 · 📅2026-05
- 🟢 [Awesome-LLM-Benchmark](https://github.com/SihyeongPark/Awesome-LLM-Benchmark) — 面向大语言模型的基准一览 `awesome` ⭐11 · 📅2026-04
- 🟢 [awesome-llm-benchmarks](https://github.com/BenchGecko/awesome-llm-benchmarks) — LLM/AI模型的基准、数据集与排行榜集 `awesome` ⭐1 · 📅2026-03
- 🟡 [llm_benchmarks](https://github.com/leobeeson/llm_benchmarks) — LLM评估用基准与数据集的合集 `awesome` ⭐569 · 📅2024-07

## 官方论文集・论文入口(非 GitHub)

因非 GitHub 仓库而未纳入主列表,但作为一手来源十分有用的官方论文入口。

- [CVF Open Access](https://openaccess.thecvf.com/menu) — CVPR/ICCV/WACV 官方开放获取论文
- [ECVA / ECCV Papers](https://www.ecva.net/papers.php) — ECCV 官方论文(ECVA 开放获取)
- [Ke-Sen Huang's Home Page](https://kesen.realtimerendering.com/) — SIGGRAPH 等图形学论文链接的经典汇总
- [OpenReview](https://openreview.net/) — ICLR/NeurIPS 等审稿与录用论文
- [ACL Anthology](https://aclanthology.org/) — NLP(ACL/EMNLP/NAACL 等)官方论文存档
- [PMLR](https://proceedings.mlr.press/) — ICML/AISTATS/CoLT 等官方论文集
- [NeurIPS Proceedings](https://papers.nips.cc/) — NeurIPS 官方论文集
- [Papers with Code](https://paperswithcode.com/) — 论文 + 代码 + SOTA 排行榜
- [DBLP](https://dblp.org/) — 计算机科学论文书目数据库
- [arXiv](https://arxiv.org/) — 预印本服务器(cs.LG/cs.CV/cs.CL 等)

---

## 关于本仓库

- 由各领域分工的调查代理横跨 GitHub 收集,仅收录确认存在的仓库。
- star 数与最后更新为生成当下 GitHub API 的实际值;新鲜度标记可判别是否过时。
- 所有链接均解析重定向后统一为规范 URL。
- ⭐star・📅更新可通过 `./scripts/refresh.sh` 或 GitHub Actions(每周)重新生成与自动更新。

## 许可

本列表(汇整本身)以 [CC0 1.0](LICENSE)(公有领域)发布。各链接仓库遵循其各自许可。

Generated with Claude Code
