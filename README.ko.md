# Awesome AI Research Lists [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](LICENSE)

**언어:** [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-lightgrey)](README.md) [![English](https://img.shields.io/badge/English-lightgrey)](README.en.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-blue)](README.ko.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-lightgrey)](README.zh-Hant.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-lightgrey)](README.zh-Hans.md)

> AI 연구 전 분야의 **awesome 리스트·survey 리포지토리·학회 논문 리스트·특정 모델 컬렉션**을 가로질러 수집·분류한 “리스트의 리스트(awesome-of-awesome)”입니다.

CV / CG / NLP / RL을 비롯한 전 분야를 포괄하며, `awesome-`가 붙지 않은 survey 리포지토리(예: [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey))나 `awesome-nanobanana-pro` 같은 특정 모델 예시 모음도 대상으로 합니다.

**총 902건** / 33개 분야 — 🟢 활발 447건, 🟡 보통 202건 (2026-06-22 기준 GitHub 메타데이터로 자동 생성).

## 범례 / 수록 기준

각 항목에는 **⭐star 수**와 **📅마지막 업데이트(년-월)**, 그리고 신선도 마커를 함께 표기합니다. 역사적 자료 모음을 제외하고는 최신성·업데이트 빈도를 중시하여 수록·정렬합니다.

| 마커 | 의미 |
|:--:|:--|
| 🟢 | 활발 (최근 12개월 이내 업데이트) |
| 🟡 | 보통 (13~30개월) |
| 🔴 | 정체 (30개월 초과 미업데이트) |
| 📑 | 피어리뷰 survey 논문 기반 큐레이션 (업데이트 빈도보다 망라성·권위가 가치, 오래돼도 유용) |
| 📚 | 역사적·고전 컬렉션 (업데이트 중단 전제, 신선도 대상 외) |
| 📦 | 아카이브됨 (read-only) |

종류: `awesome`=큐레이션 리스트 / `survey`=survey 논문 부속 / `paper-list`=논문 리스트 / `model`=특정 모델 예시

> 상세 메타데이터·전체 결과·통계는 [docs/research-notes.md](docs/research-notes.md), 작성 방법론은 [docs/best-practices.md](docs/best-practices.md) 참고(일본어).

## 목차

- [🧠 머신러닝 일반 / 딥러닝](#-머신러닝-일반--딥러닝) (24)
- [📐 ML 이론 / 최적화](#-ml-이론--최적화) (12)
- [🎲 확률 모델 / 베이지안 / 인과 / 불확실성](#-확률-모델--베이지안--인과--불확실성) (17)
- [🏗️ 새로운 아키텍처 (SSM·Mamba·KAN·SNN·양자 ML)](#-새로운-아키텍처-ssmmambakansnn양자-ml) (24)
- [🌱 자기지도 / 표현 학습 / 파운데이션 모델](#-자기지도--표현-학습--파운데이션-모델) (6)
- [🎓 학습 패러다임 (메타/전이/퓨샷/OOD/준지도)](#-학습-패러다임-메타전이퓨샷ood준지도) (27)
- [👁️ 컴퓨터 비전 (Computer Vision)](#-컴퓨터-비전-computer-vision) (111)
- [🎨 컴퓨터 그래픽스 / 3D / 렌더링](#-컴퓨터-그래픽스--3d--렌더링) (65)
- [🖌️ 저수준 영상처리 / 복원 / 압축](#-저수준-영상처리--복원--압축) (22)
- [🎬 애니메이션 · 일러스트 · 폰트](#-애니메이션--일러스트--폰트) (8)
- [💬 NLP / 대규모 언어 모델(LLM)](#-nlp--대규모-언어-모델llm) (98)
- [🖼️ 생성 AI / Diffusion / 이미지·동영상 생성](#-생성-ai--diffusion--이미지동영상-생성) (42)
- [🍌 특정 모델 프롬프트·예시 컬렉션](#-특정-모델-프롬프트예시-컬렉션) (21)
- [🧰 모델 에코시스템 / 운영 도구 (MCP·LLMOps·LLM 앱)](#-모델-에코시스템--운영-도구-mcpllmopsllm-앱) (25)
- [🎮 강화학습(RL)](#-강화학습rl) (35)
- [🔀 멀티모달 / VLM / MLLM](#-멀티모달--vlm--mllm) (30)
- [🔊 음성 / 오디오](#-음성--오디오) (28)
- [🤖 로보틱스 / Embodied AI](#-로보틱스--embodied-ai) (19)
- [🕸️ 그래프 학습(GNN) / 지식 그래프](#-그래프-학습gnn--지식-그래프) (35)
- [🛒 추천 시스템(RecSys)](#-추천-시스템recsys) (12)
- [📈 시계열(Time Series)](#-시계열time-series) (12)
- [🦾 AI 에이전트 / LLM Agents](#-ai-에이전트--llm-agents) (20)
- [🔬 의료 AI / AI for Science](#-의료-ai--ai-for-science) (41)
- [🌍 응용 도메인 (Code/Math/Finance/Law/과학)](#-응용-도메인-codemathfinancelaw과학) (33)
- [🚗 자율주행(Autonomous Driving)](#-자율주행autonomous-driving) (18)
- [🛡️ AI 안전성 / Alignment / 해석가능성](#-ai-안전성--alignment--해석가능성) (37)
- [⚖️ AI 윤리 / 거버넌스 / 규제 / Human-AI Interaction](#-ai-윤리--거버넌스--규제--human-ai-interaction) (7)
- [⚡ 효율화 (압축/양자화/NAS/AutoML)](#-효율화-압축양자화nasautoml) (23)
- [🔐 연합학습 / 프라이버시](#-연합학습--프라이버시) (7)
- [♻️ 지속 학습(Continual Learning)](#-지속-학습continual-learning) (7)
- [🖥️ ML 시스템 / 학습·추론 인프라 / 데이터](#-ml-시스템--학습추론-인프라--데이터) (19)
- [🛠️ MLOps / 데이터 중심 AI](#-mlops--데이터-중심-ai) (12)
- [📊 데이터셋 / 벤치마크](#-데이터셋--벤치마크) (5)


## 🧠 머신러닝 일반 / 딥러닝

- 🟢 [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) — 언어별 ML 프레임워크 및 라이브러리의 대표 큐레이션 리스트 `awesome` ⭐73k · 📅2026-06
- 🟢 [awesome-datascience](https://github.com/academic/awesome-datascience) — 데이터 사이언스를 학습하고 실제 문제에 적용하기 위한 대표 리소스 모음 `awesome` ⭐29.4k · 📅2026-06
- 🟢 [awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) — AI 연구의 논문 작성 및 퇴고를 지원하는 도구 및 리소스 모음 `awesome` ⭐29.1k · 📅2026-05
- 🟢 [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources) — 이상 탐지의 도서, 논문, 동영상, 툴박스를 망라한 대표 리스트 `awesome` ⭐9.3k · 📅2026-03
- 🟢 [kaggle-solutions](https://github.com/faridrashidi/kaggle-solutions) — Kaggle 대회의 솔루션 및 아이디어를 모은 컬렉션 `awesome` ⭐6.4k · 📅2026-06
- 🟢 [awesome-python-data-science](https://github.com/krzjoa/awesome-python-data-science) — Python의 데이터 사이언스 소프트웨어를 엄선한 리스트 `awesome` ⭐3.5k · 📅2026-04
- 🟢 [awesome-deeplearning-resources](https://github.com/endymecy/awesome-deeplearning-resources) — DL 및 심층 강화학습 논문, 코드를 시계열로 정리 `paper-list` ⭐3k · 📅2026-01
- 🟢 [paperlists](https://github.com/papercopilot/paperlists) — Paper Copilot의 정형화 데이터. 주요 학회를 연도별 JSON으로 횡단 망라하고 지속 업데이트(대형) `paper-list` ⭐941 · 📅2026-02
- 🟢 [ai-deadlines](https://github.com/huggingface/ai-deadlines) — 주요 AI 학회의 마감 카운트다운(paperswithcode 버전의 후속, 현행 주류) `awesome` ⭐344 · 📅2026-06
- 🟢 [ai_papers_scrapper](https://github.com/george-gca/ai_papers_scrapper) — 주요 AI 학회(2017-)의 PDF, 저자, 초록 등을 학회×연도로 취득하는 스크레이퍼 `paper-list` ⭐53 · 📅2026-06
- 🟢 [ICML-2025-Papers](https://github.com/DmitryRyumin/ICML-2025-Papers) — ICML 2025 채택 논문을 코드 구현 링크 포함으로 체계화 `paper-list` ⭐40 · 📅2025-10
- 📑 [awesome-AI-tutorials-surveys](https://github.com/qingsongedu/awesome-AI-tutorials-surveys) — 주요 AI 학회의 DL/ML/DM/CV/NLP/음성 튜토리얼 및 서베이 모음 `survey` ⭐165 · 📅2023-02
- 🟡 [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning) — DL 튜토리얼, 프로젝트, 커뮤니티를 모은 대표 리스트 `awesome` ⭐28.5k · 📅2025-05
- 🟡 [Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials) — 머신러닝 및 딥러닝의 튜토리얼, 기사, 리소스의 대규모 모음 `awesome` ⭐17.9k · 📅2024-06
- 🟡 [Conference-Accepted-Paper-List](https://github.com/Lionelsy/Conference-Accepted-Paper-List) — 주요 AI/ML/로보틱스 학회의 채택 논문 링크와 마감 정보를 2015-2025로 집약(활발) `paper-list` ⭐1.3k · 📅2025-01
- 🟡 [AAAI-2024-Papers](https://github.com/DmitryRyumin/AAAI-2024-Papers) — AAAI 2024의 혁신적 연구 논문을 망라한 컬렉션 `paper-list` ⭐591 · 📅2025-01
- 🟡 [AI-Conference-Info](https://github.com/tranhungnghiep/AI-Conference-Info) — 주요 AI 학회 40+의 채택률, 투고 통계, 마감을 연도 횡단으로 집약 `awesome` ⭐165 · 📅2024-07
- 🟡 [Conference-Paper](https://github.com/hzxwonder/Conference-Paper) — CCF-A 학회의 채택 논문을 제목, 저자, URL, 초록 포함으로 정리 `paper-list` ⭐8 · 📅2024-04
- 📚 [Deep-Learning-Papers-Reading-Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap) — 딥러닝 주요 논문을 학습 순으로 정리한 고전적 로드맵 `paper-list` ⭐39.5k · 📅2022-11
- 📚 [awesome-deep-learning-papers](https://github.com/terryum/awesome-deep-learning-papers) — 2012~2016년 가장 많이 인용된 중요 DL 논문 Top100 `paper-list` ⭐26.2k · 📅2024-01
- 🔴 [awesome-project-ideas](https://github.com/NirantK/awesome-project-ideas) — ML/NLP/Vision/추천의 프로젝트 아이디어를 모은 리스트 `awesome` ⭐9.2k · 📅2023-03
- 🔴 [awesome-ai-awesomeness](https://github.com/amusi/awesome-ai-awesomeness) — AI에 관한 awesome 리스트를 모은 'awesome의 awesome' `awesome` ⭐979 · 📅2023-08
- 🔴 [Awesome-Paper-List](https://github.com/Doragd/Awesome-Paper-List) — NLP/CV/ML의 다수 논문 리스트 및 관련 리소스를 집약한 메타 리스트 `awesome` ⭐195 · 📅2022-04
- 🔴 [awesome-machine-learning-papers](https://github.com/solaris33/awesome-machine-learning-papers) — 중요 ML 논문 및 리포지토리의 큐레이션 리스트 `paper-list` ⭐79 · 📅2017-06

## 📐 ML 이론 / 최적화

- 🟢 [awesome-ml4co](https://github.com/Thinklab-SJTU/awesome-ml4co) — 조합 최적화에의 머신러닝 적용 논문을 36개 분야 이상으로 망라(활발) `paper-list` ⭐2.1k · 📅2026-06
- 🟢 [awesome-neuro-ai-papers](https://github.com/CYHSM/awesome-neuro-ai-papers) — 딥러닝과 신경과학의 교차 영역 논문 및 리뷰 모음(활발) `paper-list` ⭐443 · 📅2026-01
- 🟢 [awesome-deep-phenomena](https://github.com/MinghuiChen43/awesome-deep-phenomena) — grokking, double descent, lottery ticket 가설 등 DL의 경험적 현상과 이론 논문 리스트 `paper-list` ⭐403 · 📅2026-05
- 🟢 [awesome-language-model-analysis](https://github.com/Furyton/awesome-language-model-analysis) — 언어 모델의 이론 및 실증 분석(창발 능력, scaling law, ICL 이론, grokking) `paper-list` ⭐100 · 📅2026-06
- 🟡 [awesome-automl-papers](https://github.com/hibayesian/awesome-automl-papers) — AutoML 논문, 기사, 튜토리얼, 프로젝트의 대표 대규모 리스트 `paper-list` ⭐4.2k · 📅2024-06
- 🟡 [must-read-papers-for-ml](https://github.com/hurshd0/must-read-papers-for-ml) — 데이터 사이언스, ML/DL 엔지니어용 필독 논문 모음(고전 포함) `paper-list` ⭐1.4k · 📅2023-12
- 🟡 [NeuralTangentKernel-Papers](https://github.com/kwignb/NeuralTangentKernel-Papers) — Neural Tangent Kernel(NTK) 관련 논문 집약 리스트 `paper-list` ⭐123 · 📅2025-01
- 🟡 [awesome-bayesian-optimization](https://github.com/materials-data-facility/awesome-bayesian-optimization) — 재료과학 및 화학용 베이지안 최적화의 소프트웨어/논문/튜토리얼 모음 `awesome` ⭐54 · 📅2024-04
- 🔴 [Open-L2O](https://github.com/VITA-Group/Open-L2O) — L2O 기법 최초의 포괄적 벤치마크 겸 논문 정리 리포지토리 `paper-list` ⭐299 · 📅2023-06
- 🔴 [awesome-deep-neuroevolution](https://github.com/Alro10/awesome-deep-neuroevolution) — 딥러닝에 진화 계산을 적용하는 Deep Neuroevolution 리소스 모음 `awesome` ⭐227 · 📅2021-04
- 🔴 [Awesome-ScalingLaws](https://github.com/RZFan525/Awesome-ScalingLaws) — LLM의 scaling law에 특화된 리소스 모음 `awesome` ⭐84 · 📅2023-04
- 🔴 [MLT-Papers](https://github.com/guoji-fu/MLT-Papers) — 머신러닝 이론(일반화 한계, 최적화, 딥러닝의 수학) 논문 리스트 `paper-list` ⭐10 · 📅2022-02

## 🎲 확률 모델 / 베이지안 / 인과 / 불확실성

- 🟢 [Diffusion-Models-Papers-Survey-Taxonomy](https://github.com/YangLing0818/Diffusion-Models-Papers-Survey-Taxonomy) — ACM CSUR 게재 서베이 대응 diffusion, score 기반, SDE 생성 모델 논문 분류 `survey` ⭐3.3k · 📅2025-09
- 🟢 [awesome-normalizing-flows](https://github.com/janosh/awesome-normalizing-flows) — normalizing flow의 논문, 구현(PyTorch/JAX/Julia), 동영상을 모은 대표 리스트 `awesome` ⭐1.6k · 📅2026-06
- 🟢 [awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) — 분포 무관 불확실성 정량화(CP)의 동영상, 논문, 라이브러리를 모은 충실한 리스트 `awesome` ⭐1.2k · 📅2026-06
- 🟢 [awesome-uncertainty-deeplearning](https://github.com/ENSTA-U2IS-AI/awesome-uncertainty-deeplearning) — 딥러닝의 예측 불확실성 추정 서베이, 논문, 코드를 망라한 활발한 리스트 `awesome` ⭐815 · 📅2026-05
- 🟢 [awesome-flow-matching](https://github.com/dongzhuoyao/awesome-flow-matching) — flow matching 및 stochastic interpolant 관련 연구를 정리한 활발한 리스트 `awesome` ⭐683 · 📅2026-04
- 🟢 [awesome-ebm](https://github.com/yataobian/awesome-ebm) — EBM의 논문, 라이브러리, 튜토리얼을 연대순으로 정리한 활발한 리스트 `awesome` ⭐393 · 📅2026-04
- 🟡 [awesome-causality-algorithms](https://github.com/rguo12/awesome-causality-algorithms) — 재현 가능한 인과 추론 및 인과 ML 기법의 인덱스(서베이 논문 포함) `awesome` ⭐3.3k · 📅2025-01
- 🟡 [awesome-neural-ode](https://github.com/Zymrael/awesome-neural-ode) — Neural ODE/SDE/CDE, 동역학계, 제어, 수치해법의 교차 영역을 망라 `awesome` ⭐1.5k · 📅2024-09
- 🟡 [Awesome-GFlowNets](https://github.com/zdhNarsil/Awesome-GFlowNets) — GFlowNet의 기초 논문, 응용, 튜토리얼을 모은 중심적 리스트 `awesome` ⭐500 · 📅2024-10
- 🟡 [Awesome-Optimal-Transport-in-Deep-Learning](https://github.com/changwxx/Awesome-Optimal-Transport-in-Deep-Learning) — 딥러닝에서의 optimal transport 논문, 코드, 자료를 집약 `awesome` ⭐350 · 📅2024-05
- 🟡 [Awesome-VQVAE](https://github.com/wenhaochai/Awesome-VQVAE) — Vector Quantized VAE(VQ-VAE)와 그 응용에 관한 논문 및 리소스 모음 `awesome` ⭐332 · 📅2025-01
- 🔴 [Awesome-VAEs](https://github.com/matthewvowels1/Awesome-VAEs) — VAE, disentanglement, 표현 학습, 생성 모델 논문 약 900건을 집약 `paper-list` ⭐843 · 📅2021-07
- 🔴 [awesome-bayesian-deep-learning](https://github.com/robi56/awesome-bayesian-deep-learning) — 베이지안 딥러닝 논문 및 학위 논문을 연대별로 정리한 대표 리스트 `awesome` ⭐416 · 📅2017-05
- 🔴 [awesome-optimal-transport](https://github.com/kilianFatras/awesome-optimal-transport) — 머신러닝용 optimal transport(OT)의 논문, 튜토리얼, 라이브러리, 도서 모음 `awesome` ⭐246 · 📅2021-05
- 🔴 [Awesome-Causal-Inference](https://github.com/matthewvowels1/Awesome-Causal-Inference) — 머신러닝 지향 인과 추론 및 인과 발견 논문을 연대순으로 정리한 문헌 리스트 `paper-list` ⭐115 · 📅2021-05
- 🔴 [awesome-gaussian-processes](https://github.com/RaulPL/awesome-gaussian-processes) — Gaussian process를 학습하기 위한 도서, 동영상, 소프트웨어, 논문을 집약 `awesome` ⭐42 · 📅2021-07
- 🔴 [Awesome-Causal-Discovery](https://github.com/CharonWangg/Awesome-Causal-Discovery) — 인과 발견 및 인과 표현 학습에 초점을 맞춘 논문 및 도서 리스트 `awesome` ⭐12 · 📅2023-11

## 🏗️ 새로운 아키텍처 (SSM·Mamba·KAN·SNN·양자 ML)

- 🟢 [awesome-kan](https://github.com/mintisan/awesome-kan) — KAN의 라이브러리, 구현, 논문, 튜토리얼을 망라하는 사실상 표준 리스트 `awesome` ⭐3.2k · 📅2026-06
- 🟢 [Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) — 주요 학회 및 저널의 SNN 논문과 코드를 지속 업데이트 `paper-list` ⭐789 · 📅2026-03
- 🟢 [Mamba_State_Space_Model_Paper_List](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) — Mamba 서베이 부속 응용처별 페이퍼 리스트 `paper-list` ⭐752 · 📅2025-06
- 🟢 [Awesome-Mamba-Collection](https://github.com/XiudingCai/Awesome-Mamba-Collection) — Mamba의 논문, 튜토리얼, 구현을 분야 횡단으로 망라한 대표적 큐레이션 `paper-list` ⭐741 · 📅2026-06
- 🟢 [Awesome-state-space-models](https://github.com/radarFudan/Awesome-state-space-models) — S4부터 Mamba까지 state space model의 이론 지향 논문을 모은 리스트 `paper-list` ⭐621 · 📅2025-11
- 🟢 [Awesome-Hyperbolic-Representation-and-Deep-Learning](https://github.com/marlin-codes/Awesome-Hyperbolic-Representation-and-Deep-Learning) — 쌍곡 임베딩, 쌍곡 모델, 응용의 최신 논문을 활발히 업데이트 `paper-list` ⭐600 · 📅2026-06
- 🟢 [awesome-snn-conference-paper](https://github.com/AXYZdong/awesome-snn-conference-paper) — SNN 분야의 난이도 높은 학회 및 저널 논문과 코드 구현을 정리한 리스트 `paper-list` ⭐455 · 📅2026-05
- 🟢 [Awesome-Efficient-Arch](https://github.com/weigao266/Awesome-Efficient-Arch) — LLM용 효율 아키텍처(선형 attention, SSM, RWKV 등) 대규모 서베이 `survey` ⭐408 · 📅2025-11
- 🟢 [Awesome-LLM-Reasoning-with-NeSy](https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy) — LLM 시대의 뉴로 심볼릭 학습 최신 동향을 추적하는 리스트 `paper-list` ⭐310 · 📅2025-06
- 🟢 [Efficient_Attention_Survey](https://github.com/attention-survey/Efficient_Attention_Survey) — 효율적 attention 기구를 하드웨어 효율, 희소, 선형 등으로 분류한 서베이 `survey` ⭐299 · 📅2025-12
- 🟢 [Awesome_Mamba](https://github.com/xmindflow/Awesome_Mamba) — 의료 영상 분석에서의 SSM 포괄 서베이 대응 리스트 `survey` ⭐266 · 📅2025-07
- 🟢 [Awesome-RWKV-in-Vision](https://github.com/Yaziwel/Awesome-RWKV-in-Vision) — RWKV의 컴퓨터 비전 응용 논문을 모은 리스트 `paper-list` ⭐243 · 📅2025-06
- 🟢 [Awesome-Mamba-in-Vision](https://github.com/vgthengane/Awesome-Mamba-in-Vision) — 컴퓨터 비전 분야의 Mamba 논문을 집약 `paper-list` ⭐36 · 📅2026-03
- 🟢 [Awesome_Modern_Hopfield_Networks](https://github.com/Event-AHU/Awesome_Modern_Hopfield_Networks) — 현대적 Hopfield network 논문 리스트 `paper-list` ⭐27 · 📅2026-03
- 🟢 [Awesome-Linear-Attention-Survey](https://github.com/btzyd/Awesome-Linear-Attention-Survey) — 선형 attention의 알고리즘, 이론, 응용, 인프라를 다루는 서베이 부속 리스트 `survey` ⭐12 · 📅2026-02
- 🟢 [KAN-Papers](https://github.com/RamtinMoslemi/KAN-Papers) — arXiv에서 추출한 KAN 논문의 완전 리스트 `paper-list` ⭐7 · 📅2026-05
- 🟡 [awesome-quantum-machine-learning](https://github.com/krishnakumarsekar/awesome-quantum-machine-learning) — QML의 기초, 알고리즘, 교재, 프로젝트를 대규모로 수집 `awesome` ⭐3.6k · 📅2024-05
- 🟡 [awesome-quantum-ml](https://github.com/artix41/awesome-quantum-ml) — 양자 디바이스에서 동작하는 ML 알고리즘 논문 및 자료 큐레이션 `paper-list` ⭐529 · 📅2024-06
- 🟡 [awesome-deeplogic](https://github.com/ccclyu/awesome-deeplogic) — NLP 응용 중심의 뉴럴 심볼릭 AI 논문 모음 `paper-list` ⭐303 · 📅2024-08
- 🟡 [awesome-snn](https://github.com/coderonion/awesome-snn) — Spike-Driven-Transformer 등 공개 SNN 구현 모음 `model` ⭐235 · 📅2024-10
- 📦 [awesome-fast-attention](https://github.com/Separius/awesome-fast-attention) — 효율적 attention 모듈의 고전적 망라 리스트 `awesome` ⭐1k · 📅2021-08
- 🔴 [awesome-capsule-networks](https://github.com/sekwiatkowski/awesome-capsule-networks) — Dynamic Routing/EM Routing 등 capsule network의 주요 논문 및 구현 모음 `awesome` ⭐975 · 📅2020-02
- 🔴 [awesome-neuromorphic-hw](https://github.com/open-neuromorphic/awesome-neuromorphic-hw) — SNN의 ASIC/FPGA 등 뉴로모픽 하드웨어 논문 모음 `paper-list` ⭐212 · 📅2023-11
- 🔴 [Neural-Symbolic-and-Probabilistic-Logic-Papers](https://github.com/thuwzy/Neural-Symbolic-and-Probabilistic-Logic-Papers) — 뉴럴 심볼릭 및 확률 논리 논문 큐레이션 `paper-list` ⭐138 · 📅2023-09

## 🌱 자기지도 / 표현 학습 / 파운데이션 모델

- 🟢 [awesome-self-supervised-learning](https://github.com/jason718/awesome-self-supervised-learning) — self-supervised learning 기법의 대표 큐레이션 리스트 `awesome` ⭐6.4k · 📅2026-02
- 🟢 [Awesome-Foundation-Models](https://github.com/uncbiag/Awesome-Foundation-Models) — 시각 및 언어 태스크용 기반 모델의 큐레이션 리스트 `paper-list` ⭐1.2k · 📅2026-04
- 🟢 [Awesome-LLM-VLM-Foundation-Models](https://github.com/srebroa/Awesome-LLM-VLM-Foundation-Models) — LLM, VLM, 기반 모델의 큐레이션 리스트 `awesome` ⭐6 · 📅2026-02
- 🟡 [awesome-contrastive-self-supervised-learning](https://github.com/asheeshcric/awesome-contrastive-self-supervised-learning) — 대조형 self-supervised learning(SimCLR/VICReg 등) 논문 모음 `paper-list` ⭐1.3k · 📅2024-09
- 🟡 [Awesome-SSL4TS](https://github.com/qingsongedu/Awesome-SSL4TS) — 시계열용 self-supervised learning(SSL4TS) 논문, 코드, 데이터 모음 `paper-list` ⭐381 · 📅2024-04
- 🟡 [awesome-self-supervised-multimodal-learning](https://github.com/ys-zong/awesome-self-supervised-multimodal-learning) — self-supervised 멀티모달 학습 리소스(T-PAMI 연동) `paper-list` ⭐278 · 📅2024-08

## 🎓 학습 패러다임 (메타/전이/퓨샷/OOD/준지도)

- 🟢 [awesome-domain-adaptation](https://github.com/zhaoxin94/awesome-domain-adaptation) — 도메인 적응에 관한 논문 및 코드를 모은 대표 리스트 `awesome` ⭐5.4k · 📅2025-12
- 🟢 [awesome-imbalanced-learning](https://github.com/ZhiningLiu1998/awesome-imbalanced-learning) — 클래스 불균형/롱테일 학습의 논문, 코드, 프레임워크, 라이브러리를 총람 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [awesome-test-time-adaptation](https://github.com/tim-learn/awesome-test-time-adaptation) — SFDA/TTBA/TTIA/OTTA 등을 망라한 테스트 시 적응의 대표 리스트 `awesome` ⭐1.3k · 📅2025-11
- 🟢 [Awesome-LongTailed-Learning](https://github.com/Vanint/Awesome-LongTailed-Learning) — TPAMI2023 서베이 대응. 클래스 재균형/정보 증강/모듈 개선으로 분류 `survey` ⭐1k · 📅2025-11
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/huytransformer/Awesome-Out-Of-Distribution-Detection) — OOD 검출 및 일반화의 벤치마크, 논문, 라이브러리를 망라 `awesome` ⭐1k · 📅2026-04
- 🟢 [awesome-multi-task-learning](https://github.com/thuml/awesome-multi-task-learning) — MTL의 데이터셋, 코드베이스, 논문을 집약(칭화대 THUML) `awesome` ⭐840 · 📅2026-03
- 🟢 [awesome-active-learning](https://github.com/baifanxxx/awesome-active-learning) — 능동 학습의 논문, 도구, 벤치마크를 모은 리스트 `awesome` ⭐802 · 📅2026-03
- 🟢 [Awesome-Multi-Task-Learning](https://github.com/WeihongLi-ac/Awesome-Multi-Task-Learning) — 멀티태스크 학습 최신 논문을 시계열로 정리 `paper-list` ⭐378 · 📅2026-03
- 🟢 [Awesome-Out-Of-Distribution-Detection](https://github.com/shuolucs/Awesome-Out-Of-Distribution-Detection) — ACM CSUR 2025 채택 태스크 지향 OOD 검출 서베이에 대응하는 논문 리스트 `survey` ⭐166 · 📅2026-01
- 🟢 [Awesome-OOD-VLM](https://github.com/AtsuMiyai/Awesome-OOD-VLM) — vision-language 모델 시대의 일반화 OOD 검출 서베이(TMLR2025) 대응 리스트 `survey` ⭐102 · 📅2025-06
- 📑 [Awesome-Noisy-Labels](https://github.com/songhwanjun/Awesome-Noisy-Labels) — 노이즈 레이블 학습 서베이에 대응하는 논문 리스트 `survey` ⭐573 · 📅2023-02
- 🟡 [transferlearning](https://github.com/jindongwang/transferlearning) — 전이 학습 분야의 최대급 리포지토리. 논문, 코드, 데이터셋을 망라 `paper-list` ⭐14.3k · 📅2025-02
- 🟡 [Awesome-Learning-with-Label-Noise](https://github.com/subeeshvasu/Awesome-Learning-with-Label-Noise) — 노이즈 레이블 학습의 논문, 코드, 서베이를 망라한 최대급 리스트 `awesome` ⭐2.7k · 📅2025-05
- 🟡 [awesome-semi-supervised-learning](https://github.com/yassouali/awesome-semi-supervised-learning) — semi-supervised learning 논문 및 기법을 CV/NLP/생성/그래프별로 정리 `awesome` ⭐1.9k · 📅2024-05
- 🟡 [awesome_OpenSetRecognition_list](https://github.com/gary23ai/awesome_OpenSetRecognition_list) — 오픈셋 인식, OOD, 오픈월드 인식 논문을 모은 대표 리스트 `paper-list` ⭐1.2k · 📅2024-03
- 🟡 [awesome-source-free-test-time-adaptation](https://github.com/YuejiangLIU/awesome-source-free-test-time-adaptation) — 테스트 시 적응, 테스트 시 훈련, 소스프리 도메인 적응 논문 리스트 `paper-list` ⭐549 · 📅2024-06
- 🟡 [Awesome-Domain-Generalization](https://github.com/junkunyuan/Awesome-Domain-Generalization) — 도메인 일반화의 논문, 코드, 데이터셋을 모은 리스트 `awesome` ⭐540 · 📅2025-04
- 🔴 [Awesome-Meta-Learning](https://github.com/sudharsan13296/Awesome-Meta-Learning) — 메타 학습의 논문, 코드, 도서, 동영상, 데이터셋을 망라한 대표 리스트 `awesome` ⭐1.6k · 📅2020-11
- 🔴 [awesome-zero-shot-learning](https://github.com/sbharadwajj/awesome-zero-shot-learning) — 제로샷 학습 논문, 코드, 리소스를 모은 큐레이션 `awesome` ⭐933 · 📅2021-07
- 🔴 [awesome-curriculum-learning](https://github.com/Openning07/awesome-curriculum-learning) — 커리큘럼 학습 논문을 검출/분할/분류/전이/RL별로 태깅 `awesome` ⭐248 · 📅2022-08
- 🔴 [Awesome-Weak-Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) — 프로그램적/규칙 기반 약지도 학습 논문 및 리소스 모음 `awesome` ⭐195 · 📅2023-03
- 🔴 [awesome-distribution-shift](https://github.com/weitianxin/awesome-distribution-shift) — 분포 시프트와 벤치마크 논문 모음 `awesome` ⭐128 · 📅2023-08
- 🔴 [awesome-few-shot-learning](https://github.com/indussky8/awesome-few-shot-learning) — 표준 데이터셋 상의 비교 결과를 포함한 few-shot 학습 논문 큐레이션 `paper-list` ⭐126 · 📅2021-10
- 🔴 [Awesome-Zero-Shot-Learning](https://github.com/WilliamYi96/Awesome-Zero-Shot-Learning) — 제로샷 학습의 최신 논문 및 데이터셋 동향을 정리한 리스트 `paper-list` ⭐85 · 📅2022-08
- 🔴 [Awesome-Failure-Detection](https://github.com/Impression2805/Awesome-Failure-Detection) — OOD 검출과 오분류 검출(failure detection)을 통합적으로 다루는 논문 리스트 `paper-list` ⭐53 · 📅2023-10
- 🔴 [Awesome-compositional-zero-shot-learning](https://github.com/uqzhichen/Awesome-compositional-zero-shot-learning) — 구성적 제로샷 학습(속성과 객체의 조합 일반화)에 특화된 논문 리스트 `paper-list` ⭐11 · 📅2022-07
- 🔴 [awsome-domain-adaptation](https://github.com/cmhungsteve/awsome-domain-adaptation) — 도메인 적응 관련 논문을 분류 정리한 널리 참조되는 일람 `awesome` ⭐1 · 📅2019-09

## 👁️ 컴퓨터 비전 (Computer Vision)

- 🟢 [CVPR2026-Papers-with-Code](https://github.com/amusi/CVPR2026-Papers-with-Code) — CVPR 2026의 논문과 오픈소스 프로젝트의 대규모 집약(대표) `paper-list` ⭐22.7k · 📅2026-03
- 🟢 [awesome-industrial-anomaly-detection](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) — 산업 영상의 이상/결함 검출 논문 및 데이터셋 모음(매우 활발) `awesome` ⭐3.6k · 📅2026-06
- 🟢 [awesome-hand-pose-estimation](https://github.com/xinghaochen/awesome-hand-pose-estimation) — 손 자세 추정/트래킹(3D 포함)의 대표 리스트 `awesome` ⭐3.4k · 📅2025-12
- 🟢 [Awesome-Super-Resolution](https://github.com/ChaofWang/Awesome-Super-Resolution) — 초해상도 관련 논문, 데이터, 리포지토리를 집약 `awesome` ⭐3.1k · 📅2026-06
- 🟢 [Awesome-Deblurring](https://github.com/subeeshvasu/Awesome-Deblurring) — 이미지 및 동영상 디블러링 리소스를 모은 리스트 `awesome` ⭐2.9k · 📅2025-06
- 🟢 [ICCV2025-Papers-with-Code](https://github.com/amusi/ICCV2025-Papers-with-Code) — ICCV 2025의 논문과 오픈소스 프로젝트 모음 `paper-list` ⭐2.9k · 📅2025-07
- 🟢 [Awesome-Crowd-Counting](https://github.com/gjy3035/Awesome-Crowd-Counting) — 군중 계수의 대표 리스트. 데이터셋, 코드 포함으로 활발 `awesome` ⭐2.6k · 📅2026-01
- 🟢 [awesome-multiple-object-tracking](https://github.com/luanshiyinyang/awesome-multiple-object-tracking) — MOT의 리뷰 논문, 연도별 알고리즘, 데이터셋을 정리 `awesome` ⭐1.5k · 📅2025-10
- 🟢 [awesome-grounding](https://github.com/TheShadow29/awesome-grounding) — 이미지/동영상/3D의 참조 표현 및 grounding 논문 모음 `paper-list` ⭐1.1k · 📅2025-09
- 🟢 [SAM4MIS](https://github.com/YichiZhang98/SAM4MIS) — 의료 영상 세그멘테이션에의 SAM 응용 논문 및 OSS 요약 `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary](https://github.com/jianzongwu/Awesome-Open-Vocabulary) — TPAMI 2024 "Towards Open Vocabulary Learning: A Survey"의 companion `survey` ⭐997 · 📅2026-05
- 🟢 [ICCV-2023-25-Papers](https://github.com/DmitryRyumin/ICCV-2023-25-Papers) — ICCV 2023-2025 채택 논문의 큐레이션 `paper-list` ⭐968 · 📅2025-11
- 🟢 [top-cvpr-2025-papers](https://github.com/SkalskiP/top-cvpr-2025-papers) — CVPR 2025의 주목 논문을 엄선한 컬렉션 `paper-list` ⭐887 · 📅2026-04
- 🟢 [Awesome-Open-Vocabulary-Semantic-Segmentation](https://github.com/Qinying-Liu/Awesome-Open-Vocabulary-Semantic-Segmentation) — 오픈 보캐뷸러리/제로샷 시맨틱 세그멘테이션 논문 리스트 `paper-list` ⭐881 · 📅2026-05
- 🟢 [Awesome-Referring-Image-Segmentation](https://github.com/MarkMoHR/Awesome-Referring-Image-Segmentation) — 참조 이미지 세그멘테이션의 논문 및 데이터셋 모음 `awesome` ⭐826 · 📅2026-01
- 🟢 [Awesome-Skeleton-based-Action-Recognition](https://github.com/firework8/Awesome-Skeleton-based-Action-Recognition) — 스켈레톤 기반 행동 인식 논문을 매월 업데이트하는 리스트 `paper-list` ⭐715 · 📅2026-06
- 🟢 [HOI-Learning-List](https://github.com/DirtyHarryLYL/HOI-Learning-List) — 데이터셋, 벤치마크, 논문을 망라하는 HOI 학습 리스트(활발) `awesome` ⭐711 · 📅2025-10
- 🟢 [Awesome-Scene-Graph-Generation](https://github.com/ChocoWu/Awesome-Scene-Graph-Generation) — LLM/비LLM 기법, 2D/3D/동영상을 망라하는 활발한 scene graph 생성 리스트 `awesome` ⭐680 · 📅2026-06
- 🟢 [Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC](https://github.com/Kobaayyy/Awesome-CVPR2026-CVPR2025-ICCV2025-CVPR2024-ECCV2024-AIGC) — 주요 학회의 AIGC 관련 논문 및 코드를 집약 `paper-list` ⭐669 · 📅2026-06
- 🟢 [Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation](https://github.com/zhenyingfang/Awesome-Temporal-Action-Detection-Temporal-Action-Proposal-Generation) — 시계열 행동 검출, 제안 생성, 약지도를 횡단적으로 수집 `paper-list` ⭐590 · 📅2026-05
- 🟢 [Awesome-Gaze-Estimation](https://github.com/cvlab-uob/Awesome-Gaze-Estimation) — 시선 추정 논문의 엄선 큐레이션 리스트 `awesome` ⭐536 · 📅2025-06
- 🟢 [Awesome-Image-Harmonization](https://github.com/bcmi/Awesome-Image-Harmonization) — 이미지 하모나이제이션의 논문, 코드, 리소스 모음(활발) `awesome` ⭐533 · 📅2026-02
- 🟢 [Awesome-Video-Object-Segmentation](https://github.com/gaomingqi/Awesome-Video-Object-Segmentation) — VOS의 최신 논문, 데이터셋, 프로젝트 모음 `awesome` ⭐503 · 📅2026-06
- 🟢 [Awesome-Face-Restoration](https://github.com/TaoWangzj/Awesome-Face-Restoration) — 얼굴 복원 기법 논문 및 리포지토리를 모은 리스트 `paper-list` ⭐492 · 📅2026-03
- 🟢 [awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) — 위장/은폐 객체 검출의 엄선 리소스 모음 `awesome` ⭐478 · 📅2025-12
- 🟢 [Awesome-Object-Pose-Estimation](https://github.com/CNJianLiu/Awesome-Object-Pose-Estimation) — IJCV2026 서베이 "Deep Learning-Based Object Pose Estimation"의 프로젝트 페이지 `survey` ⭐426 · 📅2026-01
- 🟢 [Awesome_Long_Form_Video_Understanding](https://github.com/ttengwang/Awesome_Long_Form_Video_Understanding) — 장편 동영상에 특화된 논문 및 데이터셋 모음 `paper-list` ⭐380 · 📅2025-10
- 🟢 [awesome-described-object-detection](https://github.com/Charles-Xie/awesome-described-object-detection) — Described/Open-Vocabulary 객체 검출 및 참조 표현 이해 논문 모음 `paper-list` ⭐354 · 📅2025-11
- 🟢 [awesome-concealed-object-segmentation](https://github.com/ChunmingHe/awesome-concealed-object-segmentation) — 은폐 객체 세그멘테이션 리소스 모음 `awesome` ⭐343 · 📅2026-01
- 🟢 [Awesome-Visual-Grounding](https://github.com/linhuixiao/Awesome-Visual-Grounding) — TPAMI 2025 서베이. REC/phrase grounding/grounding MLLM을 망라(활발) `survey` ⭐318 · 📅2025-11
- 🟢 [Awesome-3D-Visual-Grounding](https://github.com/liudaizong/Awesome-3D-Visual-Grounding) — 3D 시각 grounding 논문에 특화(활발) `paper-list` ⭐281 · 📅2026-01
- 🟢 [Awesome-Multimodal-Referring-Segmentation](https://github.com/henghuiding/Awesome-Multimodal-Referring-Segmentation) — 멀티모달 참조 세그멘테이션 리스트 `awesome` ⭐252 · 📅2026-05
- 🟢 [awesome-micro-expression-recognition](https://github.com/Vision-Intelligence-and-Robots-Group/awesome-micro-expression-recognition) — 미세 표정(micro-expression) 인식, 검출, 스포팅 논문 모음 `paper-list` ⭐180 · 📅2025-08
- 🟢 [awesome-video-self-supervised-learning](https://github.com/Malitha123/awesome-video-self-supervised-learning) — 동영상에서의 self-supervised learning 기법 논문 모음 `paper-list` ⭐172 · 📅2026-03
- 🟢 [Awesome-SAM2](https://github.com/GuoleiSun/Awesome-SAM2) — 이미지 및 동영상용 SAM2 논문 및 코드 모음 `paper-list` ⭐151 · 📅2025-10
- 🟢 [awesome-3d-anomaly-detection](https://github.com/M-3LAB/awesome-3d-anomaly-detection) — 포인트 클라우드 및 멀티모달 3D 이상 탐지 서베이 리포지토리 `awesome` ⭐120 · 📅2026-06
- 🟢 [Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference) — 주요 국제 학회 게재 이벤트/스파이크 카메라 논문 모음 `paper-list` ⭐120 · 📅2026-04
- 🟢 [awesome-3D-scene-graphs](https://github.com/DennisRotondi/awesome-3D-scene-graphs) — 로보틱스 응용을 포함한 3D scene graph 전문 리스트 `awesome` ⭐111 · 📅2026-06
- 🟢 [TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding](https://github.com/iLearn-Lab/TPAMI26-Awesome-MLLMs-for-Video-Temporal-Grounding) — MLLM을 활용한 동영상 시간적 grounding(VTG-LLM)의 최신 논문, 코드, 데이터 모음 `paper-list` ⭐94 · 📅2026-06
- 🟢 [Awesome-MultiModal-Visual-Object-Tracking](https://github.com/Zhangyong-Tang/Awesome-MultiModal-Visual-Object-Tracking) — RGBT/RGBD/RGBE 등 멀티모달 시각 객체 추적 서베이 `survey` ⭐84 · 📅2026-04
- 🟢 [Awesome-Temporal-Video-Grounding](https://github.com/Tangkfan/Awesome-Temporal-Video-Grounding) — VMR/TVG/TSGV 논문 리스트 `paper-list` ⭐42 · 📅2025-12
- 🟢 [awesome-captioning-evaluation](https://github.com/aimagelab/awesome-captioning-evaluation) — MLLM 시대의 이미지 캡셔닝 평가에 관한 논문 모음 `paper-list` ⭐35 · 📅2025-11
- 📑 [Awesome-3D-Object-Detection-for-Autonomous-Driving](https://github.com/PointsCoder/Awesome-3D-Object-Detection-for-Autonomous-Driving) — IJCV 2023 서베이. LiDAR/카메라/멀티모달 3D 검출을 체계화 `survey` ⭐609 · 📅2023-05
- 📑 [Awesome-Image-Prior](https://github.com/yunfanLu/Awesome-Image-Prior) — 딥 이미지 복원/향상에서의 사전 분포 서베이 `survey` ⭐87 · 📅2025-05
- 📑 [360_Survey](https://github.com/vlislab22/360_Survey) — 전방위 비전(깊이 추정, 3D 복원, 세그멘테이션)의 포괄 서베이 `survey` ⭐23 · 📅2024-12
- 🟡 [Awesome-Transformer-Attention](https://github.com/cmhungsteve/Awesome-Transformer-Attention) — ViT/Attention을 망라한 매우 포괄적인 논문 리스트 `paper-list` ⭐5k · 📅2024-07
- 🟡 [Awesome-Visual-Transformer](https://github.com/dk-liang/Awesome-Visual-Transformer) — CV용 Transformer 논문을 모은 컬렉션 `awesome` ⭐3.6k · 📅2025-01
- 🟡 [awesome-ocr](https://github.com/kba/awesome-ocr) — OCR, 손글씨 문자 인식(HTR) 소프트웨어, 라이브러리, 문헌 모음(역사 문서 디지털화의 핵심) `awesome` ⭐3.1k · 📅2024-07
- 🟡 [ECCV2024-Papers-with-Code](https://github.com/amusi/ECCV2024-Papers-with-Code) — ECCV 2024의 논문과 오픈소스 프로젝트 모음 `paper-list` ⭐2.3k · 📅2024-08
- 🟡 [SOTA-MedSeg](https://github.com/JunMa11/SOTA-MedSeg) — 각종 챌린지 기반 SOTA 의료 영상 세그멘테이션 기법 모음 `paper-list` ⭐1.7k · 📅2023-12
- 🟡 [Awesome-Edge-Detection-Papers](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers) — 엣지/윤곽/경계 검출 논문과 툴박스 모음 `paper-list` ⭐1.6k · 📅2024-12
- 🟡 [Awesome-person-re-identification](https://github.com/bismex/Awesome-person-re-identification) — 지도/비지도/크로스모달 ReID를 망라한 대규모 논문 리스트 `awesome` ⭐1.4k · 📅2024-06
- 🟡 [awesome-point-cloud-registration](https://github.com/XuyangBai/awesome-point-cloud-registration) — 매칭 전략별로 정리한 포인트 클라우드 정합 논문 모음 `paper-list` ⭐947 · 📅2024-07
- 🟡 [Awesome-Computer-Vision-Paper-List](https://github.com/yarkable/Awesome-Computer-Vision-Paper-List) — 주요 학회 채택 논문을 횡단 검색할 수 있도록 정리한 논문 리스트 `paper-list` ⭐760 · 📅2024-04
- 🟡 [Awesome-Optical-Flow](https://github.com/hzwer/Awesome-Optical-Flow) — 옵티컬 플로우와 관련 연구 논문 리스트 `awesome` ⭐650 · 📅2024-11
- 🟡 [awesome-diffusion-models-in-low-level-vision](https://github.com/ChunmingHe/awesome-diffusion-models-in-low-level-vision) — 초해상도/인페인팅 등 저수준 비전용 diffusion model 논문 모음 `paper-list` ⭐555 · 📅2025-02
- 🟡 [CVPR-2023-24-Papers](https://github.com/DmitryRyumin/CVPR-2023-24-Papers) — CVPR 2023/2024 채택 논문을 주제별로 정리 `paper-list` ⭐451 · 📅2024-07
- 🟡 [awesome-ocr-resources](https://github.com/ZumingHuang/awesome-ocr-resources) — OCR 논문 및 데이터셋을 모은 리소스 모음 `awesome` ⭐431 · 📅2025-01
- 🟡 [Awesome-Segment-Anything](https://github.com/Vision-Intelligence-and-Robots-Group/Awesome-Segment-Anything) — Segment Anything Model(SAM) 관련 논문 및 프로젝트 모음 `paper-list` ⭐371 · 📅2024-12
- 🟡 [awesome-temporal-action-segmentation](https://github.com/nus-cvml/awesome-temporal-action-segmentation) — 시계열 행동 세그멘테이션의 논문 및 데이터셋 모음(활발) `paper-list` ⭐249 · 📅2024-04
- 🟡 [Awesome-Monocular-Depth](https://github.com/choyingw/Awesome-Monocular-Depth) — 2020년 이후 단안 깊이 추정 논문에 초점을 맞춘 리스트 `paper-list` ⭐209 · 📅2024-10
- 🟡 [Awesome-Gait-Recognition](https://github.com/BNU-IVC/Awesome-Gait-Recognition) — 보행 인식의 논문 및 데이터셋 모음(CVPR'25 등 수록, 활발) `paper-list` ⭐186 · 📅2025-05
- 🟡 [awesome-salient-object-detection](https://github.com/visionxiang/awesome-salient-object-detection) — RGB-D 등을 포함한 현저성 객체 검출 리소스 모음 `awesome` ⭐147 · 📅2024-09
- 🟡 [WACV-2024-Papers](https://github.com/DmitryRyumin/WACV-2024-Papers) — WACV 2024의 논문을 체계적으로 정리한 컬렉션 `paper-list` ⭐97 · 📅2024-09
- 🟡 [awesome-human-visual-attention](https://github.com/aimagelab/awesome-human-visual-attention) — saliency, scanpath, 시선 예측, 시각적 주의 논문/리소스 모음 `paper-list` ⭐66 · 📅2025-05
- 📚 [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) — CV 전반의 도서, 강의, 논문, 도구, 데이터셋을 망라한 대표 리스트 `awesome` ⭐23.4k · 📅2024-05
- 📚 [really-awesome-semantic-segmentation](https://github.com/nightrome/really-awesome-semantic-segmentation) — 시맨틱 세그멘테이션 논문 리스트(2018년 업데이트 중단) `paper-list` ⭐404 · 📅2018-03
- 🔴 [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) — 시맨틱 세그멘테이션의 대표 리소스 모음 `awesome` ⭐10.8k · 📅2021-05
- 🔴 [awesome-object-detection](https://github.com/amusi/awesome-object-detection) — R-CNN 계열, YOLO, SSD 등 객체 검출 논문/구현을 모은 대표 리스트 `awesome` ⭐7.5k · 📅2022-12
- 🔴 [awesome-Face_Recognition](https://github.com/ChanChiChoi/awesome-Face_Recognition) — 얼굴 검출/인식/복원/생성 등을 망라한 대규모 논문 모음 `paper-list` ⭐4.7k · 📅2023-02
- 🔴 [awesome-action-recognition](https://github.com/jinwchoi/awesome-action-recognition) — 행동 인식과 관련 분야 리소스를 망라한 대표 리스트 `awesome` ⭐4k · 📅2023-05
- 🔴 [awesome-image-classification](https://github.com/weiaicunzai/awesome-image-classification) — 2014년 이후 딥러닝 이미지 분류 논문/구현 리스트 `paper-list` ⭐3.1k · 📅2022-04
- 🔴 [awesome-deep-text-detection-recognition](https://github.com/hwalsuklee/awesome-deep-text-detection-recognition) — 딥러닝 기반 텍스트 검출/인식 논문을 정리 `paper-list` ⭐2.5k · 📅2021-08
- 🔴 [awesome-human-pose-estimation](https://github.com/cbsudux/awesome-human-pose-estimation) — 인체 자세 추정 논문 및 리소스 모음 `awesome` ⭐2.5k · 📅2022-10
- 🔴 [awesome-cbir-papers](https://github.com/willard-yuan/awesome-cbir-papers) — 고전적, 대표적인 내용 기반 이미지 검색(CBIR) 논문 모음 `paper-list` ⭐1.8k · 📅2023-10
- 🔴 [multi-object-tracking-paper-list](https://github.com/SpyderXu/multi-object-tracking-paper-list) — 다중 객체 추적 논문 리스트와 소스 코드 모음 `paper-list` ⭐1.7k · 📅2020-04
- 🔴 [Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition) — 장면 텍스트의 위치 검출 및 인식에 특화된 리소스 모음 `awesome` ⭐1.7k · 📅2018-07
- 🔴 [awesome-tiny-object-detection](https://github.com/kuanhungchen/awesome-tiny-object-detection) — Tiny Object Detection(미소 객체 검출) 논문 및 리소스 모음 `paper-list` ⭐1.6k · 📅2023-10
- 🔴 [awesome-human-pose-estimation](https://github.com/wangzheallen/awesome-human-pose-estimation) — 2D/3D 인체 자세 추정 관련 논문 모음 `paper-list` ⭐1.4k · 📅2020-08
- 🔴 [awesome-image-captioning](https://github.com/zhjohnchan/awesome-image-captioning) — 이미지 캡셔닝과 관련 분야 리소스를 연도별로 정리 `awesome` ⭐1.1k · 📅2023-03
- 🔴 [activityrecognition](https://github.com/jindongwang/activityrecognition) — 행동 인식(activity recognition) 자료, 코드, 데이터셋 모음 `paper-list` ⭐929 · 📅2019-08
- 🔴 [awesome-face](https://github.com/polarisZhao/awesome-face) — 얼굴 관련 알고리즘, 데이터셋, 논문의 큐레이션 `awesome` ⭐916 · 📅2019-08
- 🔴 [Awesome-Face-Forgery-Generation-and-Detection](https://github.com/clpeng/Awesome-Face-Forgery-Generation-and-Detection) — 얼굴 위조 생성과 검출에 관한 논문 및 코드 모음 `paper-list` ⭐780 · 📅2022-11
- 🔴 [Awesome-Temporal-Action-Localization](https://github.com/Alvin-Zeng/Awesome-Temporal-Action-Localization) — temporal action localization/detection/proposal 논문 및 벤치마크 정리 `paper-list` ⭐588 · 📅2022-09
- 🔴 [awesome-metric-learning](https://github.com/qdrant/awesome-metric-learning) — 실용적인 metric learning과 그 응용의 큐레이션 `awesome` ⭐520 · 📅2023-04
- 🔴 [Awesome-Image-Matting](https://github.com/wchstrife/Awesome-Image-Matting) — 딥러닝 기반 매팅 논문 및 코드 엄선 리스트 `awesome` ⭐439 · 📅2023-11
- 🔴 [Awesome-Visual-Captioning](https://github.com/forence/Awesome-Visual-Captioning) — 이미지/동영상 캡셔닝과 Seq2Seq 학습에 초점을 맞춘 논문 모음 `paper-list` ⭐410 · 📅2022-11
- 🔴 [Awesome-3D-Detectors](https://github.com/Hub-Tian/Awesome-3D-Detectors) — LiDAR 중심의 3D 검출 기법 논문 및 코드 모음 `paper-list` ⭐398 · 📅2022-02
- 🔴 [Awesome-Super-Resolution](https://github.com/ptkin/Awesome-Super-Resolution) — 초해상도 리소스의 큐레이션 `awesome` ⭐386 · 📅2019-09
- 🔴 [Awesome-FAS](https://github.com/RizhaoCai/Awesome-FAS) — 얼굴 안티 스푸핑/PAD/liveness 논문의 포괄적 컬렉션 `paper-list` ⭐383 · 📅2022-08
- 🔴 [awesome-depth](https://github.com/scott89/awesome-depth) — 깊이 추정 출판물을 모은 큐레이션 리스트 `paper-list` ⭐337 · 📅2020-09
- 🔴 [Awesome-generalizable-6D-object-pose](https://github.com/liuyuan-pal/Awesome-generalizable-6D-object-pose) — 일반화 가능한 6DoF 객체 자세 추정 최신 논문 모음 `paper-list` ⭐328 · 📅2023-04
- 🔴 [Awesome-Vision-Transformer-Collection](https://github.com/GuanRunwei/Awesome-Vision-Transformer-Collection) — ViT의 파생과 다운스트림 태스크를 정리한 컬렉션 `awesome` ⭐256 · 📅2022-07
- 🔴 [Awesome-Fine-grained-Visual-Classification](https://github.com/haoweiz23/Awesome-Fine-grained-Visual-Classification) — 세밀한 시각 분류(FGVC) 논문 컬렉션 `paper-list` ⭐241 · 📅2023-09
- 🔴 [Awesome-Person-Re-Identification](https://github.com/FDU-VTS/Awesome-Person-Re-Identification) — 데이터셋과 서베이를 포함한 인물 재식별 리스트 `awesome` ⭐205 · 📅2021-12
- 🔴 [6d-object-pose-estimation](https://github.com/GeorgeDu/6d-object-pose-estimation) — 6D 객체 자세 추정 논문 및 코드 정리 `paper-list` ⭐205 · 📅2023-06
- 🔴 [awesome-optical-flow-algorithm](https://github.com/antran89/awesome-optical-flow-algorithm) — 고전 기법부터 RAFT 등 딥러닝까지의 플로우 알고리즘 모음 `awesome` ⭐160 · 📅2022-10
- 🔴 [awesome-video-understanding](https://github.com/sujiongming/awesome-video-understanding) — 동영상 분류, 행동 인식, 동영상 데이터셋 리소스 모음 `awesome` ⭐143 · 📅2017-12
- 🔴 [Awesome-Video-Captioning](https://github.com/tgc1997/Awesome-Video-Captioning) — 동영상 캡셔닝 논문 모음 `paper-list` ⭐121 · 📅2021-01
- 🔴 [awesome-360-vision](https://github.com/hsientzucheng/awesome-360-vision) — 360도 비전 전반의 논문 모음 `paper-list` ⭐121 · 📅2019-01
- 🔴 [Awesome-3D-Semantic-Segmentation](https://github.com/vvincenttttt/Awesome-3D-Semantic-Segmentation) — 3D 시맨틱 세그멘테이션 논문 및 코드 모음 `paper-list` ⭐75 · 📅2022-09
- 🔴 [Awesome-Events-Deep-Learning](https://github.com/vlislab2022/Awesome-Events-Deep-Learning) — 이벤트 카메라용 딥러닝 리소스 모음 `awesome` ⭐62 · 📅2023-09
- 🔴 [awesome-vqa-latest](https://github.com/Taaccoo/awesome-vqa-latest) — VQA 논문을 지속 업데이트하는 독서 리스트 `paper-list` ⭐52 · 📅2022-08
- 🔴 [awesome-rec](https://github.com/daqingliu/awesome-rec) — Referring Expression Comprehension(REC) 전용 논문 리스트 `paper-list` ⭐47 · 📅2021-05
- 🔴 [awesome-image-retrieval-papers](https://github.com/lgbwust/awesome-image-retrieval-papers) — 이미지 검색 논문 및 구현의 포괄적 컬렉션 `paper-list` ⭐36 · 📅2018-12
- 🔴 [TSGV-Learning-List](https://github.com/Huntersxsx/TSGV-Learning-List) — TSGV/NLVL/VMR 관련 연구 정리 `paper-list` ⭐31 · 📅2022-03
- 🔴 [awesome-computer-vision-papers](https://github.com/tzxiang/awesome-computer-vision-papers) — CV와 딥러닝 관련 논문 및 리소스 리스트 `awesome` ⭐26 · 📅2020-09
- 🔴 [awesome-hyperspectral-image-classification](https://github.com/immortal13/awesome-hyperspectral-image-classification) — 하이퍼스펙트럴 이미지 분류 논문 및 코드 모음 `paper-list` ⭐20 · 📅2023-07
- 🔴 [Awesome-image-captioning](https://github.com/luo3300612/Awesome-image-captioning) — ICCV/ECCV/CVPR 등 이미지 캡셔닝 논문 리스트 `paper-list` ⭐8 · 📅2019-09
- 🔴 [Awesome-3D-Human-Pose-Estimation](https://github.com/bsridatta/Awesome-3D-Human-Pose-Estimation) — 3D 인체 자세 추정에 특화된 논문 컬렉션 `paper-list` ⭐5 · 📅2021-04
- 🔴 [Awesome-Human-Object-Interaction-Detection](https://github.com/KainingYing/Awesome-Human-Object-Interaction-Detection) — 학회 및 연도별 HOI 검출 논문 모음 `paper-list` ⭐3 · 📅2021-08

## 🎨 컴퓨터 그래픽스 / 3D / 렌더링

- 🟢 [awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) — 3DGS의 논문, 구현, 뷰어, 도구를 모은 포괄 리스트 `awesome` ⭐8.7k · 📅2026-06
- 🟢 [awesome-neural-rendering](https://github.com/weihaox/awesome-neural-rendering) — 뉴럴 렌더링과 미분 가능 렌더링 자료 모음 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-NeRF-and-3DGS-SLAM](https://github.com/3D-Vision-World/awesome-NeRF-and-3DGS-SLAM) — 암묵 표현, NeRF, 3DGS를 활용한 SLAM 논문 모음 `paper-list` ⭐2k · 📅2026-06
- 🟢 [awesome-digital-human](https://github.com/weihaox/awesome-digital-human) — 2D/3D/4D 인체 모델링 및 아바타 생성 종합 모음 `awesome` ⭐2k · 📅2026-04
- 🟢 [Awesome-Talking-Head-Synthesis](https://github.com/Kedreamix/Awesome-Talking-Head-Synthesis) — 토킹 페이스 합성의 광범위한 리소스 모음 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-3d-diffusion](https://github.com/cwchenwang/awesome-3d-diffusion) — 3D 생성용 diffusion model 논문 모음 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [awesome-point-cloud-processing](https://github.com/mmolero/awesome-point-cloud-processing) — 포인트 클라우드 처리 라이브러리, 소프트웨어, 자료 모음 `awesome` ⭐799 · 📅2025-11
- 🟢 [awesome-dust3r](https://github.com/ruili3/awesome-dust3r) — DUSt3R 계열 기하 기반 모델 논문 및 리소스 추적 `model` ⭐796 · 📅2025-11
- 🟢 [Awesome-AIGC-3D](https://github.com/hitcslj/Awesome-AIGC-3D) — AIGC 3D(생성, 텍스처, 소재) 논문 모음 `awesome` ⭐779 · 📅2026-05
- 🟢 [awesome-ray-tracing](https://github.com/dannyfritz/awesome-ray-tracing) — 레이 트레이싱 논문, 코스, 구현 리스트 `awesome` ⭐658 · 📅2025-10
- 🟢 [Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — Text-to-3D/Diffusion-to-3D 연구의 큐레이션 `paper-list` ⭐591 · 📅2026-06
- 🟢 [awesome-graphics-libraries](https://github.com/jslee02/awesome-graphics-libraries) — 3D 그래픽스 라이브러리의 큐레이션 `awesome` ⭐526 · 📅2026-05
- 🟢 [Awesome-4D-Spatial-Intelligence](https://github.com/yukangcao/Awesome-4D-Spatial-Intelligence) — 동영상 기반 4D 공간 지능 복원 서베이 `survey` ⭐509 · 📅2026-06
- 🟢 [awesome-simulation](https://github.com/Housz/awesome-simulation) — CG의 물리 시뮬레이션 리소스 정리 `awesome` ⭐390 · 📅2026-06
- 🟢 [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) — arXiv에서 매일 자동 업데이트되는 3DGS 논문 추적 `paper-list` ⭐298 · 📅2026-06
- 🟢 [Awesome-Transformer-based-SLAM](https://github.com/KwanWaiPang/Awesome-Transformer-based-SLAM) — Transformer 기반 SLAM의 서베이용 논문 모음 `survey` ⭐273 · 📅2026-06
- 🟢 [Awesome-3DGS-SLAM](https://github.com/KwanWaiPang/Awesome-3DGS-SLAM) — 3DGS SLAM 서베이용 논문 모음 `survey` ⭐268 · 📅2026-02
- 🟢 [Awesome-Learning-based-VO-VIO](https://github.com/KwanWaiPang/Awesome-Learning-based-VO-VIO) — 학습 기반 시각 오도메트리(VO/VIO)의 서베이용 논문 모음 `survey` ⭐199 · 📅2026-04
- 🟢 [awesome-geometry-processing](https://github.com/zishun/awesome-geometry-processing) — 기하 처리 라이브러리, 도구, 자료 모음 `awesome` ⭐174 · 📅2026-03
- 🟢 [Awesome-SIGGRAPH-Computational-Optics](https://github.com/zhaoguangyuan123/Awesome-SIGGRAPH-Computational-Optics) — SIGGRAPH 게재 계산 광학 논문의 독서 리스트 `paper-list` ⭐105 · 📅2026-06
- 🟢 [Awesome-3D-Reconstruction-and-Generation](https://github.com/PolySummit/Awesome-3D-Reconstruction-and-Generation) — 3D 복원 및 생성 논문, 데이터셋 모음 `paper-list` ⭐81 · 📅2026-03
- 🟢 [awesome-dynamic-NeRF](https://github.com/pdaicode/awesome-dynamic-NeRF) — 동적 장면용 NeRF 논문 모음 `paper-list` ⭐67 · 📅2026-04
- 🟢 [quad-meshing-survey](https://github.com/Bigger-and-Stronger/quad-meshing-survey) — 쿼드 메싱 관련 논문, 코드, 프로젝트 모음 `survey` ⭐44 · 📅2026-06
- 🟢 [Awesome-Diffusion-based-SLAM](https://github.com/KwanWaiPang/Awesome-Diffusion-based-SLAM) — diffusion model 기반 SLAM의 서베이용 논문 모음 `survey` ⭐34 · 📅2026-05
- 🟢 [awesome-brep-reconstruction](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) — B-rep(경계 표현) 재구성 논문과 OSS 프로젝트 모음. 정기 업데이트 `survey` ⭐30 · 📅2026-01
- 🟢 [Awesome-Event-based-SLAM](https://github.com/KwanWaiPang/Awesome-Event-based-SLAM) — 이벤트 기반 SLAM의 서베이용 논문 모음 `survey` ⭐23 · 📅2026-01
- 🟢 [offset-mesh-survey](https://github.com/Bigger-and-Stronger/offset-mesh-survey) — 오프셋 메시 생성에 관한 논문, 프로젝트, 코드의 지속 업데이트 서베이 `survey` ⭐13 · 📅2026-06
- 🟢 [awesome-3d-medial-axis](https://github.com/Bigger-and-Stronger/awesome-3d-medial-axis) — medial axis/스켈레톤과 그 응용 논문 및 OSS 모음. 정기 업데이트 `survey` ⭐5 · 📅2025-10
- 🟢 [direction-field-survey](https://github.com/Bigger-and-Stronger/direction-field-survey) — direction field에 관한 논문, 프로젝트, 코드의 지속 업데이트 서베이 `survey` ⭐4 · 📅2026-06
- 🟢 [parameterization-survey](https://github.com/Bigger-and-Stronger/parameterization-survey) — 메시 파라미터화에 관한 논문, 프로젝트, 코드의 지속 업데이트 서베이 `survey` ⭐2 · 📅2026-06
- 📑 [Gen3D](https://github.com/weihaox/Gen3D) — 심층 생성적 3D-aware 이미지 합성 서베이(CSUR 2023) `survey` ⭐164 · 📅2025-02
- 📑 [boundary-layer-generation-survey](https://github.com/Bigger-and-Stronger/boundary-layer-generation-survey) — 경계층 메시 생성에 관한 논문, 프로젝트, 코드의 지속 업데이트 서베이 `survey` ⭐3 · 📅2025-02
- 🟡 [3D-Machine-Learning](https://github.com/timzhang642/3D-Machine-Learning) — 3D 머신러닝(포인트 클라우드/메시/복셀/SDF 등) 리소스 리포지토리 `awesome` ⭐10.2k · 📅2024-07
- 🟡 [awesome-NeRF](https://github.com/awesome-NeRF/awesome-NeRF) — Neural Radiance Fields 논문의 대표 큐레이션 리스트 `awesome` ⭐6.8k · 📅2025-01
- 🟡 [awesome-implicit-representations](https://github.com/vsitzmann/awesome-implicit-representations) — DeepSDF 등 암묵적 뉴럴 표현 자료 모음 `awesome` ⭐2.6k · 📅2024-02
- 🟡 [awesome-point-cloud-analysis-2023](https://github.com/NUAAXQ/awesome-point-cloud-analysis-2023) — 2017년 이후 포인트 클라우드 분석 논문을 매일 업데이트하는 리스트 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-Talking-Face](https://github.com/JosephPai/Awesome-Talking-Face) — 토킹 페이스 전문 큐레이션 `awesome` ⭐1.5k · 📅2024-12
- 🟡 [awesome-3d-reconstruction-papers](https://github.com/bluestyle97/awesome-3d-reconstruction-papers) — 딥러닝 시대의 3D 복원 논문 모음 `paper-list` ⭐910 · 📅2023-12
- 🟡 [awesome-taichi](https://github.com/taichi-dev/awesome-taichi) — Taichi로 만든 시뮬레이션(유체, 천 등) 앱 모음 `awesome` ⭐684 · 📅2024-06
- 🟡 [awesome-3dbody-papers](https://github.com/3DFaceBody/awesome-3dbody-papers) — 3D 인체(SMPL 등) 논문 모음 `paper-list` ⭐661 · 📅2024-01
- 🟡 [awesome-4d-generation](https://github.com/cwchenwang/awesome-4d-generation) — 4D 생성(text-to-4D 등) 논문 리스트 `paper-list` ⭐331 · 📅2024-10
- 🟡 [Awesome-Avatars](https://github.com/pansanity666/Awesome-Avatars) — 인간 아바타의 생성, 복원, 편집 최신 동향 `paper-list` ⭐276 · 📅2024-04
- 🟡 [Awesome-Inverse-Rendering](https://github.com/ingra14m/Awesome-Inverse-Rendering) — neural field 기반 역렌더링 논문 모음 `paper-list` ⭐260 · 📅2024-12
- 🟡 [Awesome-InverseRendering](https://github.com/tkuri/Awesome-InverseRendering) — 내재 분해 및 역렌더링 논문 리스트 `paper-list` ⭐234 · 📅2025-04
- 🟡 [awesome-3dgs](https://github.com/pdaicode/awesome-3dgs) — 3DGS 관련 논문의 큐레이션 `paper-list` ⭐123 · 📅2024-08
- 🟡 [awesome-avatar](https://github.com/Jason-cs18/awesome-avatar) — talking-face/talking-body 관련 리소스 모음 `awesome` ⭐61 · 📅2024-11
- 🟡 [Awesome-3D-Human-Motion-Generation](https://github.com/Run542968/Awesome-3D-Human-Motion-Generation) — Text-to-Motion 중심의 인체 동작 생성 논문 모음 `paper-list` ⭐25 · 📅2024-07
- 🟡 [awesome-dynamic-scene-representations](https://github.com/yklcs/awesome-dynamic-scene-representations) — 동적 장면 표현 자료 모음 `paper-list` ⭐8 · 📅2024-04
- 🟡 [awesome-visualization](https://github.com/Bigger-and-Stronger/awesome-visualization) — CG 관련 데이터 시각화 기법 및 렌더링 사례를 기록하는 리포지토리 `awesome` ⭐1 · 📅2025-03
- 🔴 [awesome_3DReconstruction_list](https://github.com/openMVG/awesome_3DReconstruction_list) — 이미지 기반 3D 복원의 고전적 논문 및 자료 모음 `awesome` ⭐4.4k · 📅2021-10
- 🔴 [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis) — 포인트 클라우드 분석 및 처리에 관한 논문과 데이터셋 리스트 `awesome` ⭐4.2k · 📅2023-05
- 🔴 [awesome-visual-slam](https://github.com/tzutalin/awesome-visual-slam) — 시각 SLAM/시각 오도메트리 OSS 및 논문 모음 `awesome` ⭐2.4k · 📅2022-05
- 🔴 [awesome-slam](https://github.com/kanster/awesome-slam) — SLAM 튜토리얼, 프로젝트, 커뮤니티 모음 `awesome` ⭐1.7k · 📅2020-07
- 🔴 [awesome-3D-generation](https://github.com/justimyhxu/awesome-3D-generation) — 3D 생성 논문의 큐레이션 리스트 `awesome` ⭐1.2k · 📅2023-03
- 🔴 [awesome-graphics](https://github.com/ericjang/awesome-graphics) — CG 튜토리얼 및 논문 종합 리스트 `awesome` ⭐1.1k · 📅2020-02
- 🔴 [Awesome-SLAM](https://github.com/SilenceOverflow/Awesome-SLAM) — SLAM 논문의 지속 업데이트 리스트 `paper-list` ⭐1.1k · 📅2023-10
- 🔴 [3D-Reconstruction-with-Deep-Learning-Methods](https://github.com/natowi/3D-Reconstruction-with-Deep-Learning-Methods) — 딥러닝을 통한 3D 복원 프로젝트 일람 `paper-list` ⭐1k · 📅2023-05
- 🔴 [awesome-computer-graphics](https://github.com/luisdnsantos/awesome-computer-graphics) — CG 학습용 도서, 강좌, 자료 모음 `awesome` ⭐1k · 📅2021-07
- 🔴 [Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) — 학습 기반 MVS 논문 리스트 `paper-list` ⭐634 · 📅2023-11
- 🔴 [Awsome_Deep_Geometry_Learning](https://github.com/subeeshvasu/Awsome_Deep_Geometry_Learning) — 3D 형상의 딥러닝 솔루션 자료 모음 `paper-list` ⭐361 · 📅2021-08
- 🔴 [awesome-mvs](https://github.com/krahets/awesome-mvs) — MVS의 튜토리얼, 논문, 소프트웨어 모음 `awesome` ⭐278 · 📅2022-08
- 🔴 [awesome-pbr](https://github.com/neil3d/awesome-pbr) — PBR 자료, 슬라이드, 논문의 종합 컬렉션 `awesome` ⭐118 · 📅2021-01
- 🔴 [Awesome-BRDF](https://github.com/tkuri/Awesome-BRDF) — BRDF 표현에 관한 논문을 표현 방식별로 정리 `paper-list` ⭐32 · 📅2021-06
- 🔴 [awesome-Implicit-NeRF-SLAM](https://github.com/Taeyoung96/awesome-Implicit-NeRF-SLAM) — 암묵 표현 및 NeRF의 SLAM/로보틱스 응용 논문 모음 `paper-list` ⭐13 · 📅2023-11
- 🔴 [texture-synthesis-papers](https://github.com/lzhbrian/texture-synthesis-papers) — 텍스처 합성 논문(코드 포함)의 집적 `paper-list` ⭐4 · 📅2019-03

## 🖌️ 저수준 영상처리 / 복원 / 압축

- 🟢 [awesome-low-light-image-enhancement](https://github.com/zhihongz/awesome-low-light-image-enhancement) — 저조도 이미지 향상의 데이터셋/기법/논문/평가 지표를 망라(활발) `awesome` ⭐1.8k · 📅2026-05
- 🟢 [Awesome-Image-Quality-Assessment](https://github.com/chaofengc/Awesome-Image-Quality-Assessment) — IQA 논문/데이터셋/코드의 포괄 모음(매우 활발) `awesome` ⭐1.5k · 📅2026-04
- 🟢 [Image-Fusion](https://github.com/Linfeng-Tang/Image-Fusion) — "Deep Learning-based Image Fusion" 서베이, 적외선-가시광/의료/멀티 노출 등 횡단 `survey` ⭐1.2k · 📅2026-06
- 🟢 [Awesome-Image-Colorization](https://github.com/MarkMoHR/Awesome-Image-Colorization) — 딥러닝 기반 이미지/동영상 컬러화 논문(2025-2026까지 활발) `awesome` ⭐1.2k · 📅2026-06
- 🟢 [Awesome-Deep-Learning-Based-Video-Compression](https://github.com/ppingzhang/Awesome-Deep-Learning-Based-Video-Compression) — 딥러닝 기반 동영상 압축 논문 리스트 `paper-list` ⭐294 · 📅2025-09
- 🟢 [Awesome-High-Dynamic-Range-Imaging](https://github.com/rebeccaeexu/Awesome-High-Dynamic-Range-Imaging) — HDR 논문 모음(멀티/싱글 프레임, HDRTV, HDR 동영상, 톤 매핑) `awesome` ⭐238 · 📅2026-02
- 🟢 [awesome-computational-photography](https://github.com/visionxiang/awesome-computational-photography) — 딥러닝을 통한 계산 사진(이미지 매칭, 정렬, 스티칭, 안정화) `paper-list` ⭐180 · 📅2025-07
- 🟢 [Awesome-Video-Frame-Interpolation](https://github.com/CMLab-Korea/Awesome-Video-Frame-Interpolation) — IEEE TCSVT'26 채택 VFI 서베이. 250+ 논문을 체계화(활발) `survey` ⭐151 · 📅2026-06
- 🟢 [Awesome-Image-Restoration](https://github.com/TaoWangzj/Awesome-Image-Restoration) — 서베이 "Deep Image Restoration" 부속, denoise/deblur/SR/dehaze/derain 등 횡단 `survey` ⭐14 · 📅2025-11
- 🟡 [Awesome-Denoise](https://github.com/oneTaken/Awesome-Denoise) — 이미지/버스트/동영상 디노이즈 논문을 색 공간, 노이즈 모델별로 정리 `awesome` ⭐503 · 📅2024-04
- 🟡 [Awesome-Shadow-Removal](https://github.com/GuoLanqing/Awesome-Shadow-Removal) — 그림자 제거의 논문/코드/데이터셋/지표 모음(활발) `awesome` ⭐395 · 📅2025-04
- 🟡 [awesome-reflection-removal](https://github.com/ChenyangLEI/awesome-reflection-removal) — 반사 제거 기법 모음(단일 이미지/플래시/편광/인터랙티브) `awesome` ⭐157 · 📅2024-12
- 🟡 [awesome-video-enhancement](https://github.com/liuzhen03/awesome-video-enhancement) — 동영상 초해상도, 보간, 디노이즈, 디블러, 인페인팅을 횡단하는 논문 모음 `paper-list` ⭐157 · 📅2024-08
- 🟡 [UIE](https://github.com/YuZhao1999/UIE) — 수중 이미지 향상 리소스 리스트 `paper-list` ⭐118 · 📅2024-05
- 🟡 [Awesome-Neural-Compression](https://github.com/Xinjie-Q/Awesome-Neural-Compression) — 이미지, 동영상, 포인트 클라우드, NeRF, 3DGS까지 망라한 뉴럴 압축 논문/리소스 모음 `awesome` ⭐83 · 📅2024-08
- 🟡 [Awesome-Deblurring-Resources](https://github.com/kawchar85/Awesome-Deblurring-Resources) — 연도별로 정리된 이미지/동영상 디블러 논문/데이터셋(활발) `paper-list` ⭐13 · 📅2024-08
- 🔴 [Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers) — 서베이 "Neural Style Transfer: A Review" 부속 대표 논문 및 코드 모음 `paper-list` ⭐1.6k · 📅2022-02
- 🔴 [DerainZoo](https://github.com/nnUyi/DerainZoo) — 비 제거 기법, 데이터셋, 코드 모음(단일 이미지/동영상) `paper-list` ⭐516 · 📅2022-05
- 🔴 [awesome-image-alignment-and-stitching](https://github.com/tzxiang/awesome-image-alignment-and-stitching) — 이미지 정렬 및 스티칭의 큐레이션 `paper-list` ⭐463 · 📅2022-08
- 🔴 [Awesome-Image-Distortion-Correction](https://github.com/subeeshvasu/Awesome-Image-Distortion-Correction) — 롤링 셔터 효과 및 방사 왜곡 보정에 관한 리소스 모음 `awesome` ⭐282 · 📅2023-07
- 🔴 [awesome-dehazing](https://github.com/youngguncho/awesome-dehazing) — 단일/다중 이미지 디헤이즈, 수중 향상, 데이터셋을 분류한 논문 모음 `awesome` ⭐202 · 📅2020-08
- 🔴 [Video-Frame-Interpolation-Collections](https://github.com/lyh-18/Video-Frame-Interpolation-Collections) — SOTA VFI 기법 컬렉션 `paper-list` ⭐65 · 📅2021-11

## 🎬 애니메이션 · 일러스트 · 폰트

- 🟢 [AwesomeAnimeResearch](https://github.com/SerialLain3170/AwesomeAnimeResearch) — 애니메이션/만화 연구 논문 및 데이터셋 모음(생성, 컬러화, 캐릭터 애니메이션 등) `awesome` ⭐1.2k · 📅2025-12
- 🟢 [Awesome-Sketch-Based-Applications](https://github.com/MarkMoHR/Awesome-Sketch-Based-Applications) — 스케치 기반 응용 논문 모음 `paper-list` ⭐708 · 📅2026-06
- 🟢 [Awesome-Sketch-Synthesis](https://github.com/MarkMoHR/Awesome-Sketch-Synthesis) — 스케치 합성(생성) 논문 모음 `paper-list` ⭐568 · 📅2026-06
- 🟢 [Awesome-Animation-Research](https://github.com/zhenglinpan/Awesome-Animation-Research) — 애니메이션(2D/카툰 등) 연구 논문과 데이터셋을 모은 리스트 `paper-list` ⭐207 · 📅2026-04
- 🟢 [Awesome-AI4Animation](https://github.com/yunlong10/Awesome-AI4Animation) — AI 기반 애니메이션 생성·보간·채색·제작 지원 논문 모음 `paper-list` ⭐205 · 📅2026-01
- 🟢 [TypographyResearchCollection](https://github.com/IShengFang/TypographyResearchCollection) — 타이포그래피 관련 CG/CV/ML 연구 수집(폰트 생성, 애니메이션 포함) `paper-list` ⭐163 · 📅2025-08
- 🟢 [Awesome-2D-Animation](https://github.com/MarkMoHR/Awesome-2D-Animation) — 인비트위닝·2D 애니메이션 도구·데이터셋·논문 모음 `paper-list` ⭐39 · 📅2026-06
- 🔴 [Sketch-Based-Deep-Learning](https://github.com/qyzdao/Sketch-Based-Deep-Learning) — 스케치 기반 딥러닝 논문 모음(선화 컬러화, 벡터화 등) `paper-list` ⭐179 · 📅2021-05

## 💬 NLP / 대규모 언어 모델(LLM)

- 🟢 [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — LLM 논문, 모델, 도구, 코스를 망라한 최대급 리스트 `awesome` ⭐27k · 📅2025-07
- 🟢 [Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM) — 오픈소스 중국어 대규모 언어 모델(베이스/도메인 미세조정/데이터/튜토리얼)을 정리 `awesome` ⭐22.6k · 📅2026-05
- 🟢 [awesome-nlp](https://github.com/keon/awesome-nlp) — NLP 전반의 라이브러리, 데이터, 튜토리얼을 모은 대표 리스트 `awesome` ⭐18.7k · 📅2026-06
- 🟢 [LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) — LLM 진화 계통수와 실무 활용 가이드를 정리한 서베이 모음 `survey` ⭐10.2k · 📅2026-04
- 🟢 [awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources) — 멀티모달 생성, Agent, 보조 코딩, 데이터 처리, 훈련, 추론 등 LLM 자료 총정리 `awesome` ⭐8.6k · 📅2026-06
- 🟢 [awesome-prompts](https://github.com/ai-boost/awesome-prompts) — 고평가 GPTs의 프롬프트와 선도적 프롬프트 엔지니어링 논문 컬렉션 `awesome` ⭐8.3k · 📅2026-06
- 🟢 [Awesome-LLM-Strawberry](https://github.com/hijkzzz/Awesome-LLM-Strawberry) — OpenAI o1과 추론 기법에 초점을 맞춘 논문 및 블로그 모음 `paper-list` ⭐6.9k · 📅2025-12
- 🟢 [Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) — GPT/ChatGPT용 프롬프트 기법 논문 및 도구를 모은 리스트 `awesome` ⭐6.1k · 📅2026-06
- 🟢 [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) — FlashAttention, PagedAttention 등 추론 고속화 논문 모음 `paper-list` ⭐5.3k · 📅2026-04
- 🟢 [Awesome-Text2SQL](https://github.com/eosphoros-ai/Awesome-Text2SQL) — Text2SQL/Text2DSL 등 튜토리얼과 리소스 모음 `awesome` ⭐3.7k · 📅2026-01
- 🟢 [Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — CoT부터 o1/DeepSeek-R1까지의 LLM 추론 논문 모음(매우 활발) `awesome` ⭐3.6k · 📅2026-04
- 🟢 [Awesome-Context-Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) — 프롬프트 엔지니어링부터 프로덕션 AI 시스템까지의 컨텍스트 엔지니어링 서베이 `survey` ⭐3.2k · 📅2026-05
- 🟢 [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) — 그래프 기반 RAG의 서베이, 논문, 벤치마크 모음 `awesome` ⭐2.5k · 📅2026-06
- 🟢 [Awesome-Graph-LLM](https://github.com/XiaoxinHe/Awesome-Graph-LLM) — 그래프 관련 LLM 리소스를 모은 큐레이션 `awesome` ⭐2.4k · 📅2025-11
- 🟢 [prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning) — ICL과 프롬프트 엔지니어링 최신 리소스를 지속 업데이트하는 논문 리스트 `paper-list` ⭐2.2k · 📅2026-05
- 🟢 [KG-LLM-Papers](https://github.com/zjukg/KG-LLM-Papers) — 지식 그래프와 LLM을 통합하는 논문 리스트 `paper-list` ⭐2.2k · 📅2026-03
- 🟢 [Awesome-LLM-Long-Context-Modeling](https://github.com/Xnhyacinth/Awesome-LLM-Long-Context-Modeling) — 장문맥 모델링(효율적 attention, KV 캐시, 위치 부호화 등) 논문 모음 `paper-list` ⭐2.1k · 📅2026-06
- 🟢 [Awesome-LLMs-Datasets](https://github.com/lmmlzn/Awesome-LLMs-Datasets) — 사전 학습 코퍼스, 지시/선호/평가 데이터셋을 5가지 관점으로 정리 `awesome` ⭐1.5k · 📅2026-03
- 🟢 [Awesome-LLM-based-Text2SQL](https://github.com/DEEP-PolyU/Awesome-LLM-based-Text2SQL) — TKDE2025 서베이 기반 LLM Text-to-SQL 논문 및 벤치마크 모음 `survey` ⭐1.3k · 📅2026-05
- 🟢 [SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers) — speculative decoding의 필독 논문 및 블로그 모음(서베이 연동) `survey` ⭐1.3k · 📅2026-06
- 🟢 [KnowledgeEditingPapers](https://github.com/zjunlp/KnowledgeEditingPapers) — LLM의 지식 편집에 관한 논문 리스트 `paper-list` ⭐1.2k · 📅2025-07
- 🟢 [awesome-hallucination-detection](https://github.com/EdinburghNLP/awesome-hallucination-detection) — LLM의 환각 검출 논문을 모델별로 정리한 리스트 `paper-list` ⭐1.1k · 📅2026-06
- 🟢 [llm-hallucination-survey](https://github.com/HillZhang1999/llm-hallucination-survey) — "Siren's Song in the AI Ocean" 환각 서베이 읽을거리 리스트 `survey` ⭐1.1k · 📅2025-09
- 🟢 [Paper-Reading-ConvAI](https://github.com/iwangjian/Paper-Reading-ConvAI) — 대화 시스템과 NLG 중심의 대화형 AI 논문 리스트 `paper-list` ⭐1k · 📅2026-05
- 🟢 [awesome-data-llm](https://github.com/OpenDataBox/awesome-data-llm) — "LLM × DATA" 서베이 공식 리포지토리 `survey` ⭐791 · 📅2026-06
- 🟢 [Awesome-Efficient-Reasoning-LLMs](https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs) — "Stop Overthinking" 효율적 추론 서베이(TMLR2025) 논문 모음 `survey` ⭐775 · 📅2026-02
- 🟢 [Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) — "LLMs-as-Judges" 평가 기법 서베이의 공식 논문 모음 `survey` ⭐591 · 📅2025-07
- 🟢 [A-Survey-on-Mixture-of-Experts-in-LLMs](https://github.com/withinmiaov/A-Survey-on-Mixture-of-Experts-in-LLMs) — TKDE 채택 "MoE in LLMs" 서베이의 공식 논문 모음 `survey` ⭐506 · 📅2026-06
- 🟢 [LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey) — 도구 학습 서베이의 공식 리포지토리. task planning/tool selection 등으로 분류 `survey` ⭐485 · 📅2025-08
- 🟢 [Awesome-LLM-Quantization](https://github.com/pprp/Awesome-LLM-Quantization) — LLM 양자화에 특화된 논문 리스트 `awesome` ⭐428 · 📅2026-04
- 🟢 [awesome-moe-inference](https://github.com/MoE-Inf/awesome-moe-inference) — MoE 모델의 추론 최적화 논문을 모은 리스트 `paper-list` ⭐400 · 📅2026-03
- 🟢 [Awesome-Inference-Time-Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling) — 추론 시/테스트 시 스케일링 논문 리스트(활발) `awesome` ⭐391 · 📅2026-06
- 🟢 [Awesome_papers_on_LLMs_detection](https://github.com/Xianjun-Yang/Awesome_papers_on_LLMs_detection) — LLM 생성 텍스트 및 코드 검출 논문 리스트 `paper-list` ⭐289 · 📅2025-06
- 🟢 [Awesome-Fake-News-Detection](https://github.com/wangbing1416/Awesome-Fake-News-Detection) — 페이크 뉴스 및 루머 검출 논문 리스트 `awesome` ⭐164 · 📅2026-04
- 🟢 [GEC-Info](https://github.com/gotutiyan/GEC-Info) — GEC 논문을 수집 및 분류한 리포지토리 `paper-list` ⭐128 · 📅2026-01
- 🟢 [llm-self-correction-papers](https://github.com/ryokamoi/llm-self-correction-papers) — LLM 자기 수정 논문 리스트(서베이 준거) `paper-list` ⭐81 · 📅2026-05
- 🟢 [Awesome-Function-Callings](https://github.com/Applied-Machine-Learning-Lab/Awesome-Function-Callings) — LLM의 function calling에 특화된 논문 리스트 `paper-list` ⭐72 · 📅2026-04
- 🟢 [Awesome-Personalized-LLMs](https://github.com/VanillaCreamer/Awesome-Personalized-LLMs) — 퍼스널라이즈드 LLM(선호 모델링, persona 제어, 메모리 기반)의 최신 논문 모음 `paper-list` ⭐48 · 📅2026-06
- 🟢 [awesome-lora-adapter](https://github.com/marlin-codes/awesome-lora-adapter) — LoRA, 어댑터 계열 기법을 모은 논문 리스트 `paper-list` ⭐22 · 📅2026-05
- 🟢 [Awesome-PEFT](https://github.com/XiaoshuangJi/Awesome-PEFT) — LoRA 각종 파생을 중심으로 한 PEFT 논문, 라이브러리, 구현 모음 `awesome` ⭐7 · 📅2026-06
- 🟢 [Awesome-Text-Generation-Evaluation](https://github.com/SuperBruceJia/Awesome-Text-Generation-Evaluation) — NLG 평가 지표(참조 있음/없음)의 큐레이션 리스트 `awesome` ⭐4 · 📅2026-05
- 📑 [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) — "A Survey of Large Language Models" 공식 리포지토리 `survey` ⭐12.2k · 📅2025-03
- 📑 [ABigSurvey](https://github.com/NiuTrans/ABigSurvey) — NLP·ML의 수백 편 서베이 논문을 일람화한 서베이의 서베이 `survey` ⭐2k · 📅2024-03
- 📑 [RAG-Survey](https://github.com/hymie122/RAG-Survey) — "RAG for AI-Generated Content" 서베이의 분류 체계와 논문 모음 `survey` ⭐1.8k · 📅2024-08
- 📑 [Awesome-Language-Model-on-Graphs](https://github.com/PeterGriffinJin/Awesome-Language-Model-on-Graphs) — "LLMs on Graphs" TKDE 서베이의 논문 및 리소스 모음 `survey` ⭐995 · 📅2025-03
- 📑 [Awesome-LLMs-Evaluation-Papers](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) — "Evaluating LLMs: A Comprehensive Survey"의 논문 모음 `survey` ⭐802 · 📅2024-05
- 📑 [CNSurvey](https://github.com/NiuTrans/CNSurvey) — NLP·머신러닝의 중국어 서베이 문헌 리스트 `survey` ⭐580 · 📅2023-05
- 📑 [ABigSurveyOfLLMs](https://github.com/NiuTrans/ABigSurveyOfLLMs) — LLM에 관한 150편 이상의 서베이를 모은 컬렉션 `survey` ⭐352 · 📅2025-02
- 📑 [Semantic-Retrieval-Models](https://github.com/caiyinqiong/Semantic-Retrieval-Models) — 의미 검색 모델(DPR, RAG, RepBERT 등)을 망라한 TOIS 채택 서베이 논문 리스트 `survey` ⭐340 · 📅2023-06
- 📑 [CTGSurvey](https://github.com/IAAR-Shanghai/CTGSurvey) — LLM용 제어 텍스트 생성 서베이 논문 리스트(학습 시/추론 시 기법으로 분류) `survey` ⭐204 · 📅2024-08
- 📑 [Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models](https://github.com/THUDM/Awesome-Parameter-Efficient-Fine-Tuning-for-Foundation-Models) — 기반 모델용 PEFT 기법을 체계적으로 정리한 서베이 겸 논문 리스트 `survey` ⭐112 · 📅2025-03
- 📑 [llm-alignment-survey](https://github.com/Magnetic2014/llm-alignment-survey) — "LLM Alignment: A Survey"의 alignment 읽을거리 리스트 `survey` ⭐82 · 📅2023-09
- 📑 [Awesome_Information_Extraction](https://github.com/wutong8023/Awesome_Information_Extraction) — RE, EE, slot filling을 포함한 IE 문헌 서베이 `survey` ⭐72 · 📅2023-01
- 📑 [Awesome-Data-Efficient-LLM](https://github.com/luo-junyu/Awesome-Data-Efficient-LLM) — 데이터 효율, 데이터 중심 LLM 논문 모음(서베이 포함) `survey` ⭐60 · 📅2025-02
- 🟡 [Awesome-Code-LLM](https://github.com/huybery/Awesome-Code-LLM) — 코드 생성 LLM 연구의 엄선 큐레이션 리스트 `awesome` ⭐1.3k · 📅2024-12
- 🟡 [Awesome-LLM4IE-Papers](https://github.com/quqxui/Awesome-LLM4IE-Papers) — LLM을 통한 생성적 정보 추출(NER/RE/EE) 논문 모음 `paper-list` ⭐1.1k · 📅2024-11
- 🟡 [Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers) — ACL2023 서베이 "Reasoning with LM Prompting" 논문 리스트 `paper-list` ⭐1k · 📅2025-05
- 🟡 [ToolLearningPapers](https://github.com/thunlp/ToolLearningPapers) — 기반 모델의 도구 학습(tool learning) 필독 논문 모음 `paper-list` ⭐922 · 📅2024-07
- 🟡 [ICL_PaperList](https://github.com/dqxiu/ICL_PaperList) — In-Context Learning 서베이 기반 논문 리스트 `paper-list` ⭐877 · 📅2024-10
- 🟡 [awesome-pretrained-models-for-information-retrieval](https://github.com/ict-bigdatalab/awesome-pretrained-models-for-information-retrieval) — IR용 사전 학습 모델(pretraining for IR) 논문 모음 `awesome` ⭐676 · 📅2024-01
- 🟡 [Awesome-Mixture-of-Experts-Papers](https://github.com/codecaution/Awesome-Mixture-of-Experts-Papers) — MoE 연구 읽을거리 리스트 `paper-list` ⭐668 · 📅2024-10
- 🟡 [EventExtractionPapers](https://github.com/BaptisteBlouin/EventExtractionPapers) — 이벤트 추출 태스크 중심의 NLP 리소스 리스트 `paper-list` ⭐580 · 📅2024-03
- 🟡 [awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning) — Instruction Tuning/Following 논문과 데이터셋 모음 `paper-list` ⭐511 · 📅2024-04
- 🟡 [awesome-llm-pretraining](https://github.com/RUCAIBox/awesome-llm-pretraining) — LLM 사전 학습의 데이터, 프레임워크, 기법 리소스 모음 `awesome` ⭐384 · 📅2025-04
- 🟡 [Awesome-LLM-Watermark](https://github.com/hzy312/Awesome-LLM-Watermark) — 최신 LLM 워터마크 논문을 지속 업데이트하는 리스트 `paper-list` ⭐374 · 📅2024-12
- 🟡 [ABSAPapers](https://github.com/ZhengZixiang/ABSAPapers) — 측면 기반 감성 분석(ABSA) 논문 및 리소스 모음 `paper-list` ⭐363 · 📅2024-03
- 🟡 [Awesome-LLM-hallucination](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) — LLM 환각에 관한 논문 리스트 `paper-list` ⭐336 · 📅2024-03
- 🟡 [LLM-Optimizers-Papers](https://github.com/AGI-Edgerunners/LLM-Optimizers-Papers) — LLM을 최적화기로 사용/프롬프트 자동 최적화 필독 논문 모음 `paper-list` ⭐252 · 📅2024-03
- 🟡 [awesome-tool-llm](https://github.com/zorazrw/awesome-tool-llm) — 도구 확장 LLM(ToRA, MINT 등)을 모은 큐레이션 리스트 `awesome` ⭐245 · 📅2024-08
- 🟡 [Awesome-RAG-Evaluation](https://github.com/YHPeter/Awesome-RAG-Evaluation) — "Evaluation of RAG: A Survey" 공식 평가 논문 리스트 `paper-list` ⭐199 · 📅2025-04
- 🟡 [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) — 테스트 시 LLM(self-correction/refine 포함) 논문 모음 `awesome` ⭐153 · 📅2025-03
- 🟡 [Low-resource-KEPapers](https://github.com/zjunlp/Low-resource-KEPapers) — 저자원 정보 추출(NER/RE/EE) 논문, 도구, 데이터셋 모음 `paper-list` ⭐137 · 📅2024-11
- 🟡 [EMNLP-2023-Papers](https://github.com/DmitryRyumin/EMNLP-2023-Papers) — EMNLP 2023의 논문을 체계적으로 정리한 컬렉션 `paper-list` ⭐111 · 📅2024-05
- 🟡 [Paper-Neural-Topic-Models](https://github.com/bobxwu/Paper-Neural-Topic-Models) — neural topic model(NTM) 논문 모음 `paper-list` ⭐96 · 📅2024-07
- 🟡 [Awesome-Papers-Retrieval-Augmented-Generation](https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation) — 지식 지향 RAG 서베이 기반 논문 분류 리스트 `paper-list` ⭐89 · 📅2025-03
- 🟡 [Awesome-Multilingual-LLMs-Papers](https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers) — 다국어 LLM 논문 리스트 `paper-list` ⭐34 · 📅2025-01
- 🟡 [awesome-llm-tool-learning](https://github.com/AngxiaoYue/awesome-llm-tool-learning) — LLM의 도구 학습 논문(Gorilla, HuggingGPT, ART 등) 리스트 `paper-list` ⭐28 · 📅2024-07
- 🟡 [Awesome-LLM-Reasoning-Techniques](https://github.com/Junting-Lu/Awesome-LLM-Reasoning-Techniques) — CoT와 o1을 포함한 LLM 추론 기법 논문 및 리소스 모음 `paper-list` ⭐18 · 📅2024-10
- 📦 [Fact-Checking-Survey](https://github.com/neemakot/Fact-Checking-Survey) — COLING2020 "Explainable Automated Fact-Checking" 서베이 논문 모음 `survey` ⭐51 · 📅2021-01
- 🔴 [PromptPapers](https://github.com/thunlp/PromptPapers) — 사전 학습 모델의 프롬프트 기반 튜닝 필독 논문 모음 `paper-list` ⭐4.3k · 📅2023-07
- 🔴 [Top-AI-Conferences-Paper-with-Code](https://github.com/MLNLP-World/Top-AI-Conferences-Paper-with-Code) — ACL/EMNLP/NAACL/COLING 등 주요 학회의 코드 포함 논문 모음 `paper-list` ⭐2.7k · 📅2022-10
- 🔴 [Style-Transfer-in-Text](https://github.com/fuzhenxin/Style-Transfer-in-Text) — 텍스트 스타일 변환의 대표 논문 리스트(지도/비지도/평가로 분류) `paper-list` ⭐1.6k · 📅2023-03
- 🔴 [awesome-text-summarization](https://github.com/mathsyouth/awesome-text-summarization) — 텍스트 요약 논문, 도구, 데이터셋 모음 `awesome` ⭐1.5k · 📅2023-01
- 🔴 [awesome-relation-extraction](https://github.com/roomylee/awesome-relation-extraction) — 관계 추출에 특화된 리소스 리스트 `awesome` ⭐1.2k · 📅2022-01
- 🔴 [awesome-qa](https://github.com/seriousran/awesome-qa) — 질의응답 데이터셋, 논문, 리소스 모음 `awesome` ⭐769 · 📅2022-01
- 🔴 [awesome-sentiment-analysis](https://github.com/declare-lab/awesome-sentiment-analysis) — 감성 분석 논문 읽을거리 리스트 `paper-list` ⭐538 · 📅2023-03
- 🔴 [awesome-nlg](https://github.com/accelerated-text/awesome-nlg) — NLG 전반의 리소스 모음(도구/논문/데이터) `awesome` ⭐483 · 📅2023-09
- 🔴 [Named-Entity-Recognition-NER-Papers](https://github.com/pfliu-nlp/Named-Entity-Recognition-NER-Papers) — 7개 학회의 NER 논문을 망라한 리스트 `paper-list` ⭐390 · 📅2022-02
- 🔴 [Awesome-Sentence-Embedding](https://github.com/Doragd/Awesome-Sentence-Embedding) — 문장 표현 학습 논문과 STS 리더보드(SimCSE 등)를 수록 `awesome` ⭐314 · 📅2023-10
- 🔴 [DeltaPapers](https://github.com/thunlp/DeltaPapers) — 사전 학습 모델의 파라미터 효율 튜닝(Delta Tuning) 필독 논문 모음 `paper-list` ⭐283 · 📅2023-06
- 🔴 [Awesome-KBQA](https://github.com/RUCAIBox/Awesome-KBQA) — 지식 베이스 QA(KBQA) 논문, 도구, 리더보드 모음 `paper-list` ⭐182 · 📅2022-04
- 🔴 [Accepted-Papers-Lists](https://github.com/audreycs/Accepted-Papers-Lists) — 주요 저널 및 학회의 채택 논문 리스트를 정리한 리포지토리 `paper-list` ⭐147 · 📅2022-12
- 🔴 [MT-paper-lists](https://github.com/NiuTrans/MT-paper-lists) — 학회별로 기계 번역 논문을 정리한 리스트 `paper-list` ⭐124 · 📅2020-12
- 🔴 [Data-to-Text-Generation](https://github.com/liang8qi/Data-to-Text-Generation) — data-to-text 생성 논문 및 데이터셋 모음 `paper-list` ⭐108 · 📅2023-05
- 🔴 [awesome-NLP-Machine-Learning](https://github.com/tjunlp-lab/awesome-NLP-Machine-Learning) — NLP 연구용 머신러닝 기법(RL/self-supervised 등) 논문 및 코드 모음 `paper-list` ⭐35 · 📅2020-03
- 🔴 [AWESOME-Dialogue](https://github.com/thuiar/AWESOME-Dialogue) — 대화 및 인터랙티브 시스템 논문 리스트 `paper-list` ⭐15 · 📅2020-06
- 🔴 [awesome-multilingual-nlp](https://github.com/simran-khanuja/awesome-multilingual-nlp) — 영어 이외를 대상으로 하는 다국어 NLP 연구의 큐레이션 `awesome` ⭐8 · 📅2023-07
- 🔴 [AwesomeSemanticParsing](https://github.com/aarsri/AwesomeSemanticParsing) — 의미 파싱 논문 및 리소스 모음 `awesome` ⭐0 · 📅2020-11

## 🖼️ 생성 AI / Diffusion / 이미지·동영상 생성

- 🟢 [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) — 동영상 생성 및 편집의 diffusion model을 모은 대표 리스트 `awesome` ⭐5.7k · 📅2026-06
- 🟢 [gans-awesome-applications](https://github.com/nashory/gans-awesome-applications) — GAN의 응용 및 데모를 모은 큐레이션 리스트 `awesome` ⭐5.1k · 📅2026-06
- 🟢 [really-awesome-gan](https://github.com/nightrome/really-awesome-gan) — GAN 논문을 모은 망라적 리스트 `paper-list` ⭐3.8k · 📅2025-08
- 🟢 [awesome-virtual-try-on](https://github.com/minar09/awesome-virtual-try-on) — 가상 피팅 논문/코드/데이터셋의 대표 리스트 `awesome` ⭐3.1k · 📅2026-06
- 🟢 [Awesome-Text-to-Image](https://github.com/Yutong-Zhou-cv/Awesome-Text-to-Image) — 텍스트 기반 이미지 생성의 서베이형 논문 리스트 `survey` ⭐2.4k · 📅2026-02
- 🟢 [Awesome-Video-Diffusion-Models](https://github.com/ChenHsing/Awesome-Video-Diffusion-Models) — Video Diffusion Model 서베이(CSUR) `survey` ⭐2.3k · 📅2026-04
- 🟢 [awesome-diffusion-categorized](https://github.com/wangkai930418/awesome-diffusion-categorized) — Diffusion 논문을 세부 분야별로 분류한 실용적 컬렉션 `awesome` ⭐2.2k · 📅2026-03
- 🟢 [awesome-talking-head-generation](https://github.com/harlanhong/awesome-talking-head-generation) — 토킹 헤드 생성 논문 리스트 `paper-list` ⭐1.9k · 📅2026-04
- 🟢 [Awesome-Deepfakes-Detection](https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection) — Deepfake 검출 도구/논문/코드 `awesome` ⭐1.8k · 📅2025-09
- 🟢 [awesome-image-translation](https://github.com/weihaox/awesome-image-translation) — image-to-image translation에 관한 우수 리소스 컬렉션 `awesome` ⭐1.2k · 📅2025-09
- 🟢 [Awesome-diffusion-model-for-image-processing](https://github.com/lixinustc/Awesome-diffusion-model-for-image-processing) — 복원/향상/부호화/품질 평가의 diffusion model 정리 `survey` ⭐947 · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/showlab/Awesome-Unified-Multimodal-Models) — 이해와 생성을 통일하는 모델 논문 모음 `paper-list` ⭐827 · 📅2025-10
- 🟢 [Autoregressive-Models-in-Vision-Survey](https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey) — 비전의 autoregressive 모델 서베이(TMLR 2025) `survey` ⭐799 · 📅2026-05
- 🟢 [awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) — 동영상 생성 연구를 모은 컬렉션 `awesome` ⭐771 · 📅2026-03
- 🟢 [awesome-text-to-image-studies](https://github.com/AlonzoLeeeooo/awesome-text-to-image-studies) — text-to-image 연구를 모은 지속 업데이트 리스트 `awesome` ⭐759 · 📅2026-04
- 🟢 [awesome-text-to-video](https://github.com/jianzhnie/awesome-text-to-video) — Text-to-Video 생성 서베이 `survey` ⭐736 · 📅2026-06
- 🟢 [Awesome-Deepfake-Generation-and-Detection](https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection) — Deepfake 생성과 검출 서베이 `survey` ⭐640 · 📅2026-05
- 🟢 [Awesome-Video-World-Models-with-AR-Diffusion](https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion) — AR+diffusion의 동영상 세계 모델(알고리즘/응용/기반) `awesome` ⭐605 · 📅2026-06
- 🟢 [awesome-discrete-diffusion-models](https://github.com/kuleshov-group/awesome-discrete-diffusion-models) — 이산 diffusion model에 특화된 리소스 리스트 `awesome` ⭐563 · 📅2025-09
- 🟢 [Awesome-Controllable-Diffusion](https://github.com/atfortes/Awesome-Controllable-Diffusion) — ControlNet, DreamBooth, IP-Adapter 등 제어 생성 리소스 `awesome` ⭐507 · 📅2025-06
- 🟢 [Awesome-From-Video-Generation-to-World-Model](https://github.com/ziqihuangg/Awesome-From-Video-Generation-to-World-Model) — 동영상 생성에서 세계 모델로의 흐름을 정리 `paper-list` ⭐496 · 📅2026-03
- 🟢 [Awesome-Image-Editing](https://github.com/FudanCVL/Awesome-Image-Editing) — T2I 모델을 통한 이미지 편집 서베이 `survey` ⭐472 · 📅2025-08
- 🟢 [Awesome-Evaluation-of-Visual-Generation](https://github.com/ziqihuangg/Awesome-Evaluation-of-Visual-Generation) — 시각 생성의 평가 지표/모델/시스템 모음 `paper-list` ⭐452 · 📅2026-05
- 🟢 [Awesome-Autoregressive-Visual-Generation](https://github.com/lxa9867/Awesome-Autoregressive-Visual-Generation) — autoregressive 비주얼 생성 최신 논문 추적 `paper-list` ⭐430 · 📅2025-06
- 🟢 [Awesome-Try-On-Models](https://github.com/Zheng-Chong/Awesome-Try-On-Models) — 가상 피팅 모델(2025 포함)을 정리 `paper-list` ⭐428 · 📅2026-05
- 🟢 [Awesome-AIGC-Image-Video-Detection](https://github.com/ant-research/Awesome-AIGC-Image-Video-Detection) — AI 생성 이미지/동영상 검출 최신 연구 모음 `paper-list` ⭐420 · 📅2026-06
- 🟢 [awesome-image-inpainting-studies](https://github.com/AlonzoLeeeooo/awesome-image-inpainting-studies) — 이미지 인페인팅 연구 컬렉션 `awesome` ⭐390 · 📅2026-02
- 🟢 [Awesome-Comprehensive-Deepfake-Detection](https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection) — Deepfake 검출의 포괄적 논문 리스트 `paper-list` ⭐315 · 📅2026-04
- 🟢 [awesome-diffusion-v2v](https://github.com/wenhao728/awesome-diffusion-v2v) — diffusion 기반 Video-to-Video 편집 논문+벤치마크 `paper-list` ⭐288 · 📅2026-04
- 🟢 [Awesome-Text-to-Video-Generation](https://github.com/soraw-ai/Awesome-Text-to-Video-Generation) — Sora 서베이 기반 T2V/I2V 논문 리스트 `survey` ⭐258 · 📅2026-03
- 🟢 [Awesome-Consistency-Models](https://github.com/G-U-N/Awesome-Consistency-Models) — Consistency Model 리소스 리스트 `awesome` ⭐131 · 📅2025-12
- 📑 [GAN-Inversion](https://github.com/weihaox/GAN-Inversion) — GAN Inversion 서베이(TPAMI 2022) 부속 리포지토리 `survey` ⭐1.1k · 📅2025-02
- 🟡 [Awesome-Diffusion-Models](https://github.com/diff-usion/Awesome-Diffusion-Models) — Diffusion Model 논문 및 리소스를 망라한 최대급 리스트 `awesome` ⭐12.3k · 📅2024-08
- 🟡 [Awesome-High-Resolution-Diffusion](https://github.com/GuoLanqing/Awesome-High-Resolution-Diffusion) — 고해상도 이미지/동영상 합성 diffusion 논문 `paper-list` ⭐169 · 📅2024-12
- 🟡 [Awesome-Music-Generation](https://github.com/shaopengw/Awesome-Music-Generation) — 음악 생성 모델 MG²의 리소스 `model` ⭐165 · 📅2025-03
- 🟡 [awesome-diffusion-iclr-2025](https://github.com/moatifbutt/awesome-diffusion-iclr-2025) — ICLR 2025의 diffusion 관련 투고 리스트 `paper-list` ⭐61 · 📅2024-10
- 📚 [the-gan-zoo](https://github.com/hindupuravinash/the-gan-zoo) — 명명된 모든 GAN을 일람화한 고전적 리스트 `paper-list` ⭐14.7k · 📅2023-10
- 🔴 [awesome-ai-art-image-synthesis](https://github.com/altryne/awesome-ai-art-image-synthesis) — DALL·E2/MidJourney/SD 등 도구 및 프롬프트 모음 `awesome` ⭐1.8k · 📅2022-12
- 🔴 [awesome-diffusion-low-level-vision](https://github.com/yulunzhang/awesome-diffusion-low-level-vision) — 저수준 비전 diffusion model 리스트 `paper-list` ⭐186 · 📅2023-09
- 🔴 [awesome-controlnet](https://github.com/cobanov/awesome-controlnet) — ControlNet 관련 리소스 리스트 `awesome` ⭐97 · 📅2023-03
- 🔴 [awesome-few-shot-generation](https://github.com/kobeshegu/awesome-few-shot-generation) — 소수 이미지 생성 논문 리스트 `paper-list` ⭐87 · 📅2023-08
- 🔴 [Awsome-GAN-Training](https://github.com/subeeshvasu/Awsome-GAN-Training) — GAN의 학습(training)에 관한 리소스를 모은 리스트 `awesome` ⭐30 · 📅2020-10

## 🍌 특정 모델 프롬프트·예시 컬렉션

- 🟢 [Awesome-Nano-Banana-images](https://github.com/PicoTrex/Awesome-Nano-Banana-images) — Gemini 계열 Nano Banana의 생성 예시 및 프롬프트 모음(데이터셋 공개) `model` ⭐23k · 📅2025-12
- 🟢 [awesome-gpt-image-2-API-and-Prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-API-and-Prompts) — GPT-Image-2의 API와 프롬프트 및 작례 모음 `model` ⭐16.9k · 📅2026-06
- 🟢 [awesome-nano-banana-pro-prompts](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) — 세계 최대급 Nano Banana Pro 프롬프트 모음 10,000+/16개 언어(매일 업데이트) `model` ⭐12.6k · 📅2026-06
- 🟢 [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) — Nano Banana Pro(Nano Banana 2)의 프롬프트 및 작례 모음 `model` ⭐10.1k · 📅2026-05
- 🟢 [awesome-nano-banana](https://github.com/JimmyLv/awesome-nano-banana) — Gemini-2.5-Flash-Image(Nano Banana)의 작례/프롬프트 모음 `model` ⭐8.8k · 📅2025-09
- 🟢 [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) — Seedance 2.0 동영상 생성 프롬프트 2000+(매일 업데이트) `model` ⭐1.4k · 📅2026-06
- 🟢 [awesome-nano-banana-pro](https://github.com/muset-ai/awesome-nano-banana-pro) — Nano Banana Pro의 이미지 및 프롬프트 작례 모음 `model` ⭐1.1k · 📅2025-11
- 🟢 [awesome-video-prompts](https://github.com/songguoxs/awesome-video-prompts) — Veo3/Kling/Hailuo용 동영상 프롬프트 모음 `model` ⭐552 · 📅2025-10
- 🟢 [Awesome-Chinese-Stable-Diffusion](https://github.com/leeguandong/Awesome-Chinese-Stable-Diffusion) — 중국계 text-to-image SD 모델 모음(Kolors/HunyuanDiT 등 포함) `model` ⭐431 · 📅2026-06
- 🟢 [awesome-qwen-prompt-insight](https://github.com/XiaomingX/awesome-qwen-prompt-insight) — Qwen용 우수 프롬프트의 대규모 컬렉션 `model` ⭐403 · 📅2026-02
- 🟢 [awesome-nano-banana-images](https://github.com/githubssg/awesome-nano-banana-images) — GPT-4o/gpt-image-1 이미지 및 프롬프트 모음 `model` ⭐307 · 📅2025-09
- 🟢 [Awesome-Open-AI-Sora](https://github.com/Curated-Awesome-Lists/Awesome-Open-AI-Sora) — Sora 관련 기사/동영상/뉴스 리소스 허브 `model` ⭐262 · 📅2026-05
- 🟢 [awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts) — 여러 동영상 모델 횡단의 프롬프트/기법 모음 `model` ⭐61 · 📅2026-01
- 🟢 [awesome-grok-imagine-prompts](https://github.com/YouMind-OpenLab/awesome-grok-imagine-prompts) — Grok Imagine(xAI) 동영상 생성 프롬프트 모음 `model` ⭐22 · 📅2026-06
- 🟢 [awesome-qwen-image-2512](https://github.com/shauray8/awesome-qwen-image-2512) — qwen-image-2512 작례/프롬프트 모음 `model` ⭐0 · 📅2025-12
- 🟡 [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images) — GPT-4o, gpt-image-1의 이미지 및 프롬프트 작례 모음 `model` ⭐8.1k · 📅2025-05
- 🟡 [Awesome-GPTs](https://github.com/ai-boost/Awesome-GPTs) — GPT Store 게재 GPT를 모은 큐레이션 `model` ⭐3.4k · 📅2024-11
- 🟡 [Awesome-GPT4o-Image-Prompts](https://github.com/ImgEdify/Awesome-GPT4o-Image-Prompts) — GPT-4o 이미지 생성 프롬프트 사전 `model` ⭐570 · 📅2025-05
- 🟡 [awesome-grok-prompts](https://github.com/langgptai/awesome-grok-prompts) — Grok(xAI)용 고급 프롬프트 및 템플릿 모음 `model` ⭐505 · 📅2025-05
- 🟡 [awesome-llama-prompts](https://github.com/langgptai/awesome-llama-prompts) — Llama2/Llama3용 프롬프트 모음 `model` ⭐270 · 📅2024-08
- 🟡 [awesome-flux](https://github.com/Eris2025/awesome-flux) — FLUX 에코시스템(LoRA/ControlNet/양자화) 리소스 모음 `model` ⭐106 · 📅2024-08

## 🧰 모델 에코시스템 / 운영 도구 (MCP·LLMOps·LLM 앱)

- 🟢 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — 실행 가능한 LLM 앱/RAG/에이전트 컬렉션 `awesome` ⭐115.3k · 📅2026-06
- 🟢 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 최대 규모의 MCP(Model Context Protocol) 서버 컬렉션 `awesome` ⭐89.6k · 📅2026-06
- 🟢 [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — Claude Skill/도구의 큐레이션 `awesome` ⭐65.5k · 📅2026-05
- 🟢 [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Claude Code용 skill/hook/slash-command/플러그인 모음 `awesome` ⭐47k · 📅2026-04
- 🟢 [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) — DeepSeek API를 각종 소프트웨어에 통합하는 공식 큐레이션 `model` ⭐38k · 📅2026-02
- 🟢 [Awesome-pytorch-list](https://github.com/bharathgs/Awesome-pytorch-list) — PyTorch 관련 모델, 구현, 라이브러리를 망라한 대규모 리스트 `awesome` ⭐16.5k · 📅2026-02
- 🟢 [awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai) — 현대 생성 AI 프로젝트 및 서비스를 엄선한 리스트 `awesome` ⭐12.2k · 📅2026-06
- 🟢 [awesome-langchain](https://github.com/kyrolabs/awesome-langchain) — LangChain 프레임워크의 도구 및 프로젝트 리스트 `awesome` ⭐9.4k · 📅2026-04
- 🟢 [ai-collection](https://github.com/ai-collection/ai-collection) — 생성 AI 애플리케이션을 모은 랜드스케이프 `awesome` ⭐9k · 📅2026-06
- 🟢 [awesome-chatgpt](https://github.com/sindresorhus/awesome-chatgpt) — ChatGPT용 awesome 리스트(sindresorhus 계열) `awesome` ⭐6.3k · 📅2026-02
- 🟢 [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) — AI 관련 실용 도구를 수집한 컬렉션(중영 병기) `awesome` ⭐6k · 📅2026-06
- 🟢 [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) — LLM 개발 및 운영용 도구(학습/서빙/모니터링)의 엄선 리스트 `awesome` ⭐5.8k · 📅2026-05
- 🟢 [awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) — MCP 서버의 큐레이션 `awesome` ⭐5.6k · 📅2026-05
- 🟢 [awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools) — AI의 톱 도구를 엄선한 리스트 `awesome` ⭐5.5k · 📅2025-12
- 🟢 [awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai) — 진정한 오픈소스 AI 프로젝트, 모델, 도구, 기반의 엄선 리스트 `awesome` ⭐3.9k · 📅2026-06
- 🟢 [awesome-chatgpt](https://github.com/eon01/awesome-chatgpt) — ChatGPT의 라이브러리/SDK/API 큐레이션 `awesome` ⭐2.4k · 📅2026-03
- 🟢 [awesome-claude](https://github.com/webfuse-com/awesome-claude) — Anthropic Claude 전반의 큐레이션 리스트 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [Awesome-RAG](https://github.com/Danielskry/Awesome-RAG) — 생성 AI에서의 RAG 앱 awesome 리스트 `awesome` ⭐1.3k · 📅2026-06
- 🟢 [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) — DeepSeek Coder 관련 OSS 프로젝트를 정리한 공식 리스트 `model` ⭐791 · 📅2025-11
- 🟢 [awesome-comfyui](https://github.com/ComfyUI-Workflow/awesome-comfyui) — ComfyUI 커스텀 노드의 대규모 컬렉션 `awesome` ⭐711 · 📅2025-07
- 🟢 [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli) — Gemini CLI용 도구/확장/리소스 모음 `awesome` ⭐473 · 📅2026-06
- 🟢 [awesome-stable-diffusion](https://github.com/doanbactam/awesome-stable-diffusion) — Stable Diffusion 리소스의 큐레이션 `awesome` ⭐77 · 📅2026-03
- 🟢 [awesome-mistral](https://github.com/samouraiworld/awesome-mistral) — Mistral AI 에코시스템의 리소스/도구/프로젝트 모음 `awesome` ⭐42 · 📅2026-06
- 🟡 [awesome-gpt](https://github.com/formulahendry/awesome-gpt) — GPT/ChatGPT/OpenAI 관련 프로젝트 및 리소스 모음 `awesome` ⭐1k · 📅2024-05
- 🟡 [awesome-flux-ai](https://github.com/AINativeLab/awesome-flux-ai) — Flux AI의 도구/라이브러리/앱 망라 `awesome` ⭐111 · 📅2025-05

## 🎮 강화학습(RL)

- 🟢 [MARL-Papers](https://github.com/LantaoYu/MARL-Papers) — 멀티 에이전트 RL의 연구 및 서베이 논문 리스트(대표) `paper-list` ⭐4.8k · 📅2026-02
- 🟢 [Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) — 로보틱스/RL에의 LLM 및 멀티모달 활용 논문 모음 `paper-list` ⭐4.4k · 📅2026-06
- 🟢 [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — RLHF의 논문 및 리소스를 지속 업데이트 `paper-list` ⭐4.4k · 📅2026-05
- 🟢 [Awesome-RL-for-LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) — 대규모 추론 모델용 RL 서베이 논문 리포지토리 `survey` ⭐2.5k · 📅2025-11
- 🟢 [Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) — world model(동영상 생성, Embodied AI, 자율주행) 논문 망라 `paper-list` ⭐1.8k · 📅2026-06
- 🟢 [awesome-diffusion-model-in-rl](https://github.com/opendilab/awesome-diffusion-model-in-rl) — 강화학습에서의 diffusion model 리소스를 지속 업데이트하는 리스트 `awesome` ⭐1.6k · 📅2026-05
- 🟢 [awesome-model-based-RL](https://github.com/opendilab/awesome-model-based-RL) — 모델 기반 RL 논문을 지속 업데이트로 수집 `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [awesome-decision-transformer](https://github.com/opendilab/awesome-decision-transformer) — Decision Transformer 리소스의 지속 업데이트 리스트 `awesome` ⭐905 · 📅2026-05
- 🟢 [awesome-deep-rl](https://github.com/kengz/awesome-deep-rl) — Deep RL의 라이브러리, 환경, 벤치마크를 정리한 리스트 `awesome` ⭐893 · 📅2025-07
- 🟢 [Safe-Reinforcement-Learning-Baselines](https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines) — Safe RL의 베이스라인 및 논문을 모은 리포지토리 `paper-list` ⭐802 · 📅2026-03
- 🟢 [World-Model](https://github.com/tsinghua-fib-lab/World-Model) — world model의 포괄적 서베이(ACM CSUR 2025 채택) `survey` ⭐764 · 📅2025-11
- 🟢 [awesome-exploration-rl](https://github.com/opendilab/awesome-exploration-rl) — 탐색(exploration)에 특화된 RL 논문 리스트 `paper-list` ⭐697 · 📅2026-05
- 🟢 [awesome-multi-modal-reinforcement-learning](https://github.com/opendilab/awesome-multi-modal-reinforcement-learning) — 멀티모달 RL 리소스를 지속 업데이트 `paper-list` ⭐609 · 📅2026-05
- 🟢 [Reinforcement-Learning-Papers](https://github.com/yingchengyang/Reinforcement-Learning-Papers) — ICLR/ICML/NeurIPS의 고전 및 최신 논문을 연도별로 정리 `paper-list` ⭐578 · 📅2026-02
- 🟢 [Awesome-RL-for-Multimodal-Foundation-Models](https://github.com/weijiawu/Awesome-RL-for-Multimodal-Foundation-Models) — 시각 RL 및 멀티모달 기반 모델용 RL 논문 정리 `paper-list` ⭐450 · 📅2026-04
- 🟢 [Reinforcement-Learning-Papers](https://github.com/Allenpandas/Reinforcement-Learning-Papers) — NeurIPS/ICML/ICLR/AAAI/IJCAI/AAMAS/ICRA 논문을 망라 `paper-list` ⭐367 · 📅2025-11
- 🟢 [awesome-in-context-rl](https://github.com/dunnolab/awesome-in-context-rl) — In-Context RL 논문 큐레이션 `paper-list` ⭐303 · 📅2025-09
- 🟢 [Awesome-Causal-Reinforcement-Learning](https://github.com/libo-huang/Awesome-Causal-Reinforcement-Learning) — 인과 RL 서베이(TNNLS 2024) 공식 리포지토리 `survey` ⭐221 · 📅2026-06
- 🟢 [awesome-deep-reinforcement-learning](https://github.com/jgvictores/awesome-deep-reinforcement-learning) — 프레임워크, 모델, 데이터셋, gym, 베이스라인을 수록 `awesome` ⭐206 · 📅2026-03
- 🟢 [awesome-RLVR](https://github.com/opendilab/awesome-RLVR) — 검증 가능 보상 기반 RL(RLVR) 논문을 지속 업데이트 `paper-list` ⭐205 · 📅2026-06
- 🟢 [AwesomeSim2Real](https://github.com/LongchaoDa/AwesomeSim2Real) — 서베이 "A Survey of Sim-to-Real Methods in RL"의 companion `survey` ⭐177 · 📅2025-09
- 🟢 [awesome-world-models-for-robots](https://github.com/operator22th/awesome-world-models-for-robots) — 로보틱스용 world model 논문 모음 `paper-list` ⭐139 · 📅2026-03
- 🟢 [Awesome-Embodied-World-Model](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) — 체화 에이전트용 world model에 특화된 논문 모음 `survey` ⭐120 · 📅2026-05
- 🟡 [awesome-deep-rl](https://github.com/tigerneil/awesome-deep-rl) — Deep RL과 AI의 미래를 위한 리소스를 폭넓게 수집한 리스트 `awesome` ⭐1.5k · 📅2024-03
- 🟡 [awesome-rl-envs](https://github.com/clvrai/awesome-rl-envs) — RL용 환경 및 시뮬레이터를 망라한 리스트 `awesome` ⭐1.3k · 📅2024-05
- 🟡 [awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl) — 오프라인 RL 알고리즘 색인(지속 업데이트) `paper-list` ⭐1.1k · 📅2024-05
- 🟡 [awesome-game-ai](https://github.com/datamllab/awesome-game-ai) — 멀티 에이전트 학습 중심의 게임 AI 리소스 모음 `awesome` ⭐970 · 📅2024-06
- 🟡 [Awesome-Imitation-Learning](https://github.com/kristery/Awesome-Imitation-Learning) — 모방 학습 논문 및 리소스를 모은 리스트 `paper-list` ⭐607 · 📅2024-02
- 📚 [deep-reinforcement-learning-papers](https://github.com/junhyukoh/deep-reinforcement-learning-papers) — Deep RL의 주요 논문을 주제별로 정리한 고전적 리스트 `paper-list` ⭐2.2k · 📅2016-06
- 🔴 [awesome-rl](https://github.com/aikorea/awesome-rl) — RL 전반의 코드, 강의, 논문, 환경을 모은 대표 큐레이션 `awesome` ⭐9.8k · 📅2023-05
- 🔴 [awesome-real-world-rl](https://github.com/ugurkanates/awesome-real-world-rl) — 실세계에서 강화학습을 구동하기 위한 논문 및 프로젝트 모음(sim2real 포함) `awesome` ⭐457 · 📅2022-10
- 🔴 [MARL-papers-with-code](https://github.com/TimeBreaker/MARL-papers-with-code) — 코드 포함 MARL 논문을 기법별로 정리 `paper-list` ⭐428 · 📅2022-09
- 🔴 [Imitation-Learning-Paper-Lists](https://github.com/apexrl/Imitation-Learning-Paper-Lists) — 모방 학습 논문을 간결한 소개와 함께 수집 `paper-list` ⭐157 · 📅2022-03
- 🔴 [awesome-irl](https://github.com/dit7ya/awesome-irl) — 역강화학습 논문, 코드, 동영상, 튜토리얼 모음 `awesome` ⭐44 · 📅2022-02
- 🔴 [awesome-metarl](https://github.com/metarl/awesome-metarl) — 메타 강화학습 큐레이션 리스트 `paper-list` ⭐33 · 📅2020-05

## 🔀 멀티모달 / VLM / MLLM

- 🟢 [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models) — MLLM 분야의 가장 유명한 서베이. 아키텍처, 학습, 평가를 망라 추적 `survey` ⭐17.9k · 📅2026-06
- 🟢 [Awesome-LLMs-for-Video-Understanding](https://github.com/yunlong10/Awesome-LLMs-for-Video-Understanding) — 동영상 이해용 Vid-LLM의 최신 논문, 코드, 데이터셋 `paper-list` ⭐3.2k · 📅2026-06
- 🟢 [VLM_survey](https://github.com/jingyi0000/VLM_survey) — 시각 태스크용 Vision-Language 모델의 체계적 리뷰 `survey` ⭐3.1k · 📅2025-10
- 🟢 [Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) — 3D 세계에서의 멀티모달 LLM 리소스 망라 리스트 `awesome` ⭐2.2k · 📅2026-04
- 🟢 [Awesome-Unified-Multimodal-Models](https://github.com/AIDC-AI/Awesome-Unified-Multimodal-Models) — 이해와 생성을 통합하는 멀티모달 모델의 망라 모음(활발) `survey` ⭐1.3k · 📅2026-03
- 🟢 [awesome-vlm-architectures](https://github.com/gokayfem/awesome-vlm-architectures) — 유명 VLM과 그 아키텍처를 해설한 컬렉션 `paper-list` ⭐1.3k · 📅2026-01
- 🟢 [Awesome-MLLM-Hallucination](https://github.com/showlab/Awesome-MLLM-Hallucination) — 멀티모달 LLM의 환각(hallucination)에 관한 리소스 엄선 리스트 `awesome` ⭐1k · 📅2025-09
- 🟢 [Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP](https://github.com/zhengli97/Awesome-Prompt-Adapter-Learning-for-VLMs-CLIP) — CLIP 등 VLM용 프롬프트/어댑터 학습 기법의 엄선 리스트 `paper-list` ⭐781 · 📅2026-06
- 🟢 [Awesome-Spatial-Intelligence-in-VLM](https://github.com/mll-lab-nu/Awesome-Spatial-Intelligence-in-VLM) — VLM의 공간 추론에 관한 논문 및 벤치마크 약 200편(매우 활발) `paper-list` ⭐758 · 📅2026-01
- 🟢 [Awesome_Matching_Pretraining_Transfering](https://github.com/Paranioar/Awesome_Matching_Pretraining_Transfering) — 이미지 텍스트 매칭, VL 사전 학습, 멀티모달 모델의 대규모 논문 리스트 `paper-list` ⭐445 · 📅2025-09
- 🟢 [Awesome-Multimodal-Papers](https://github.com/friedrichor/Awesome-Multimodal-Papers) — 멀티모달 연구 전반의 엄선 논문 모음 `awesome` ⭐340 · 📅2026-06
- 🟢 [Awesome-Chart-Understanding](https://github.com/khuangaf/Awesome-Chart-Understanding) — IEEE TKDE 서베이 준거의 차트 이해(QA/captioning/fact-checking) 논문 모음 `survey` ⭐240 · 📅2025-12
- 🟢 [Awesome-Document-Understanding](https://github.com/harrytea/Awesome-Document-Understanding) — MLLM/OCR-free 등 멀티모달 문서 AI 논문, 코드, 데이터셋 모음 `paper-list` ⭐202 · 📅2025-09
- 🟢 [Evaluation-Multimodal-LLMs-Survey](https://github.com/swordlidev/Evaluation-Multimodal-LLMs-Survey) — MLLM 벤치마크 200건 이상을 리뷰한 평가 서베이 `survey` ⭐154 · 📅2026-06
- 🟢 [Awesome-Multimodal-LLM-for-Math-STEM](https://github.com/InfiMM/Awesome-Multimodal-LLM-for-Math-STEM) — Math/STEM/Code용 멀티모달 LLM 논문 모음 `awesome` ⭐144 · 📅2026-05
- 🟢 [Awesome-MLLM-Tuning](https://github.com/WenkeHuang/Awesome-MLLM-Tuning) — MLLM의 다운스트림 태스크용 튜닝 기법 서베이 `paper-list` ⭐100 · 📅2025-08
- 🟢 [Awesome-Composed-Multi-modal-Retrieval](https://github.com/kkzhang95/Awesome-Composed-Multi-modal-Retrieval) — 합성 이미지 검색(CIR), 합성 동영상 검색(CVR)을 포함한 CMR 서베이 `survey` ⭐89 · 📅2026-01
- 🟢 [Awesome-Multimodal-RAG](https://github.com/JarvisUSTC/Awesome-Multimodal-RAG) — 텍스트/이미지/동영상/음성을 넘나드는 멀티모달 RAG의 논문 및 도구 모음 `paper-list` ⭐53 · 📅2025-11
- 🟢 [Awesome-Large-Vision-Language-Model](https://github.com/SuperBruceJia/Awesome-Large-Vision-Language-Model) — 대규모 VLM과 의료 기반 모델 논문 및 리소스 모음 `awesome` ⭐49 · 📅2025-07
- 📑 [Efficient-Multimodal-LLMs-Survey](https://github.com/swordlidev/Efficient-Multimodal-LLMs-Survey) — 효율적 MLLM(경량 구조, 전략)의 체계적 리뷰 `survey` ⭐385 · 📅2025-04
- 🟡 [awesome-audio-visual](https://github.com/krantiparida/awesome-audio-visual) — 음성 및 시각 처리 각 분야의 논문 및 데이터셋 모음 `awesome` ⭐772 · 📅2024-01
- 🟡 [Awesome-Table-Recognition](https://github.com/cv-small-snails/Awesome-Table-Recognition) — 표 인식 논문, 데이터셋, 대회 솔루션을 정리 `awesome` ⭐404 · 📅2024-12
- 🟡 [awesome-emotion-recognition-in-conversations](https://github.com/declare-lab/awesome-emotion-recognition-in-conversations) — 대화에서의 감정 인식(ERC) 망라적 리딩 리스트 `paper-list` ⭐279 · 📅2024-02
- 🟡 [awesome-table-structure-recognition](https://github.com/Tan-Junwen/awesome-table-structure-recognition) — 표 구조 인식(TSR)의 모델, 논문, 데이터셋, 코드 모음 `awesome` ⭐231 · 📅2024-09
- 🟡 [Prompt_Learning_Paper_List](https://github.com/Event-AHU/Prompt_Learning_Paper_List) — (vision-language) 프롬프트 학습 논문 리스트 `paper-list` ⭐19 · 📅2024-11
- 🔴 [awesome-document-understanding](https://github.com/tstanislawek/awesome-document-understanding) — KIE, 레이아웃 분석, DocQA, OCR 등을 망라한 대표 리스트 `awesome` ⭐1.5k · 📅2023-06
- 🔴 [awesome-video-text-retrieval](https://github.com/danieljf24/awesome-video-text-retrieval) — 동영상 텍스트 검색 딥러닝 리소스 모음 `awesome` ⭐645 · 📅2023-10
- 🔴 [awesome-affective-computing](https://github.com/AmrMKayid/awesome-affective-computing) — 감성 컴퓨팅의 논문, 소프트웨어, OSS, 리소스 모음 `awesome` ⭐192 · 📅2019-11
- 🔴 [AWESOME-MER](https://github.com/EvelynFan/AWESOME-MER) — 멀티모달 감정 인식(MER)의 리딩 리스트 `paper-list` ⭐126 · 📅2020-10
- 🔴 [awesome-VLM](https://github.com/Lab-LVM/awesome-VLM) — 대조 학습, PrefixLM, 융합 등 기법별로 정리한 VLM 논문 모음 `paper-list` ⭐7 · 📅2023-06

## 🔊 음성 / 오디오

- 🟢 [awesome-diarization](https://github.com/wq2012/awesome-diarization) — 화자 다이어라이제이션의 논문, 라이브러리, 데이터셋, 평가 도구를 망라한 대표 리스트 `awesome` ⭐1.9k · 📅2026-06
- 🟢 [speech-trident](https://github.com/ga642381/speech-trident) — 음성/오디오 LLM, 표현 학습, codec 모델 논문 모음 `paper-list` ⭐1.2k · 📅2026-06
- 🟢 [audio-ai-hub](https://github.com/BinWang28/audio-ai-hub) — 오디오 대규모 언어 모델 논문 및 리소스 모음 `awesome` ⭐933 · 📅2026-06
- 🟢 [awesome-large-audio-models](https://github.com/EmulationAI/awesome-large-audio-models) — LLM의 Audio AI 응용에 관한 리소스 모음 `awesome` ⭐732 · 📅2026-06
- 🟢 [Awesome-Speaker-Diarization](https://github.com/DongKeon/Awesome-Speaker-Diarization) — End-to-End/클러스터링/멀티모달 등을 체계화한 논문 모음(활발) `paper-list` ⭐364 · 📅2026-03
- 🟢 [awesome-ai-voice](https://github.com/wildminder/awesome-ai-voice) — OSS TTS, 음성 클로닝, 음악 생성 모델 모음 `model` ⭐351 · 📅2026-04
- 🟢 [awesome-voice-conversion](https://github.com/JeffC0628/awesome-voice-conversion) — voice conversion(음색 변환) 프로젝트 및 커뮤니티 모음 `awesome` ⭐267 · 📅2025-11
- 🟢 [Awesome-Sign-Language-Processing](https://github.com/VIPL-SLP/Awesome-Sign-Language-Processing) — 수어 처리(인식/번역/생성)의 포괄 리소스 모음 `awesome` ⭐250 · 📅2026-05
- 🟢 [Awesome-Sign-Language](https://github.com/ZechengLi19/Awesome-Sign-Language) — 수어 인식(SLR), 번역(SLT) 등 논문 리스트(활발) `paper-list` ⭐220 · 📅2025-11
- 🟢 [Speech-and-audio-papers-Top-Conference](https://github.com/01Zhangbw/Speech-and-audio-papers-Top-Conference) — 주요 학회(INTERSPEECH/ICASSP 등)의 음성 및 음향 논문을 집약 `paper-list` ⭐140 · 📅2026-01
- 🟢 [awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech) — LLM 기반 speech-to-speech 모델/프레임워크 모음 `awesome` ⭐59 · 📅2025-11
- 🟢 [Awesome-Large-Speech-Model](https://github.com/huangcanan/Awesome-Large-Speech-Model) — 대규모 음성/오디오 모델의 논문, 데이터, 응용, 도구 모음 `awesome` ⭐28 · 📅2025-11
- 🟡 [awesome-deep-learning-music](https://github.com/ybayle/awesome-deep-learning-music) — 음악에 응용된 딥러닝 논문 및 학위 논문 모음 `paper-list` ⭐3k · 📅2023-12
- 🟡 [INTERSPEECH-2023-24-Papers](https://github.com/DmitryRyumin/INTERSPEECH-2023-24-Papers) — INTERSPEECH 2023-2024의 논문을 망라한 컬렉션 `paper-list` ⭐686 · 📅2024-12
- 🟡 [ICASSP-2023-24-Papers](https://github.com/DmitryRyumin/ICASSP-2023-24-Papers) — ICASSP 2023-2024의 논문을 망라한 컬렉션 `paper-list` ⭐525 · 📅2025-05
- 🟡 [awesome-sound_event_detection](https://github.com/soham97/awesome-sound_event_detection) — Sound AI(음향 이벤트 검출, 오디오 캡셔닝 등) 연구 리딩 리스트 `paper-list` ⭐198 · 📅2024-08
- 🟡 [awesome-speech-emotion-recognition](https://github.com/abikaki/awesome-speech-emotion-recognition) — 음성 감정 인식(SER)의 논문, 데이터셋, 도구 엄선 리스트 `awesome` ⭐101 · 📅2024-12
- 🟡 [awesome-vad](https://github.com/bigcash/awesome-vad) — VAD의 구현, 도구, 연구를 모은 리스트 `awesome` ⭐75 · 📅2024-11
- 🟡 [Awesome-Speech-Enhancement](https://github.com/DmitryRyumin/Awesome-Speech-Enhancement) — 음성 향상의 논문 및 효과 지표를 정리한 인터랙티브 리스트 `paper-list` ⭐27 · 📅2024-04
- 📦 [awesome-tts-samples](https://github.com/seungwonpark/awesome-tts-samples) — 음성 샘플 포함 TTS 논문 리스트 `paper-list` ⭐61 · 📅2020-08
- 🔴 [awesome-speech-recognition-speech-synthesis-papers](https://github.com/zzw922cn/awesome-speech-recognition-speech-synthesis-papers) — ASR, 화자 인증, TTS, 음성 합성, VC를 망라한 논문 리스트 `paper-list` ⭐3.1k · 📅2023-10
- 🔴 [awesome-speech-enhancement](https://github.com/WenzheLiu-Speech/awesome-speech-enhancement) — speech enhancement, 음원 분리, 정위 논문/코드/도구 모음 `paper-list` ⭐1.2k · 📅2023-11
- 🔴 [speech-synthesis-paper](https://github.com/wenet-e2e/speech-synthesis-paper) — 음성 합성(TTS) 논문의 체계적 리스트 `paper-list` ⭐1.1k · 📅2023-07
- 🔴 [Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion](https://github.com/guan-yuan/Awesome-Singing-Voice-Synthesis-and-Singing-Voice-Conversion) — 가창 합성(SVS), 가창 변환(SVC), 자동 채보 논문/프로젝트 모음 `paper-list` ⭐483 · 📅2022-09
- 🔴 [awesome-keyword-spotting](https://github.com/zycv/awesome-keyword-spotting) — 음성 키워드 검출/웨이크 워드 검출의 논문, 구현, 데이터셋 모음 `awesome` ⭐287 · 📅2022-05
- 🔴 [awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) — 음악 정보학의 논문, 튜토리얼, 라이브러리, 도구의 엄선 리스트 `awesome` ⭐193 · 📅2023-07
- 🔴 [awesome-speech-translation](https://github.com/dqqcasia/awesome-speech-translation) — 음성 번역(파이프라인/E2E/스트리밍/다국어) 논문 리스트 `paper-list` ⭐179 · 📅2021-11
- 🔴 [awesome-speech-to-speech-translation](https://github.com/Rongjiehuang/awesome-speech-to-speech-translation) — 직접 음성 간 번역(S2ST) 논문 리스트 `paper-list` ⭐39 · 📅2023-01

## 🤖 로보틱스 / Embodied AI

- 🟢 [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — embodied AI의 VLA, VLN, 멀티모달 학습 최신 연구 모음 `paper-list` ⭐3.3k · 📅2026-06
- 🟢 [awesome-robotics-libraries](https://github.com/jslee02/awesome-robotics-libraries) — 로보틱스의 라이브러리 및 소프트웨어를 엄선한 리스트 `awesome` ⭐3k · 📅2026-06
- 🟢 [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — 휴머노이드 로봇 학습 논문 리스트 `paper-list` ⭐2.5k · 📅2026-06
- 🟢 [Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — 체화 AI의 지각, 상호작용, 에이전트, sim-to-real을 망라(IEEE/ASME ToM 2025) `survey` ⭐2.1k · 📅2026-06
- 🟢 [Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) — LLM을 활용한 embodied AI/로봇 연구의 큐레이션 `awesome` ⭐1.8k · 📅2026-06
- 🟢 [Awesome_Quadrupedal_Robots](https://github.com/curieuxjy/Awesome_Quadrupedal_Robots) — 사족 보행 로봇 논문 및 리소스 모음 `paper-list` ⭐1.1k · 📅2026-06
- 🟢 [Awesome-Robotics-Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation) — 로봇 매니퓰레이션 논문 및 코드 모음 `paper-list` ⭐1k · 📅2026-06
- 🟢 [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam) — VLA와 World Action Model(WAM) 연구의 큐레이션 `awesome` ⭐772 · 📅2026-06
- 🟢 [Embodied-AI-Paper-TopConf](https://github.com/Songwxuan/Embodied-AI-Paper-TopConf) — 주요 학회 채택 Embodied AI 논문을 지속 수집(2026 학회까지 반영, 활발) `paper-list` ⭐685 · 📅2026-05
- 🟢 [Awesome-VLA](https://github.com/yueen-ma/Awesome-VLA) — embodied AI용 VLA 모델의 서베이 논문 포함 리스트 `survey` ⭐594 · 📅2026-06
- 🟢 [Awesome-VLA-Robotics](https://github.com/Jiaaqiliu/Awesome-VLA-Robotics) — 로보틱스의 VLA 모델 논문, 모델, 데이터셋 모음 `paper-list` ⭐478 · 📅2026-03
- 🟢 [Awesome-Robotics-Diffusion](https://github.com/showlab/Awesome-Robotics-Diffusion) — 로봇 학습에 diffusion model을 도입한 최신 논문 엄선 리스트 `paper-list` ⭐342 · 📅2026-06
- 🟢 [Awesome-Embodied-AI](https://github.com/wadeKeith/Awesome-Embodied-AI) — embodied AI의 서베이, VLA, 데이터셋, 시뮬레이터 등을 망라 `awesome` ⭐216 · 📅2026-06
- 🟢 [Awesome-VLN](https://github.com/KwanWaiPang/Awesome-VLN) — vision-language navigation(VLN) 서베이용 논문 모음 `survey` ⭐148 · 📅2026-06
- 🟢 [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA) — Vision-Language-Action(VLA) 서베이용 논문 모음 `survey` ⭐83 · 📅2026-02
- 🟢 [Awesome-Legged-Robot-Localization-and-Mapping](https://github.com/KwanWaiPang/Awesome-Legged-Robot-Localization-and-Mapping) — 다리 로봇의 SLAM에 관한 서베이용 논문 모음 `survey` ⭐65 · 📅2026-06
- 🟡 [Awesome-Robot-Learning](https://github.com/RayYoh/Awesome-Robot-Learning) — 로봇 학습(주로 매니퓰레이션) 리소스 모음 `awesome` ⭐203 · 📅2024-08
- 🔴 [awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling) — C++/Python/ROS를 통한 프로용 로봇 개발 도구 집약 `awesome` ⭐3.8k · 📅2023-11
- 🔴 [awesome-legged-locomotion-learning](https://github.com/gaiyi7788/awesome-legged-locomotion-learning) — 다리 보행 로코모션 학습 리소스 모음 `awesome` ⭐481 · 📅2023-07

## 🕸️ 그래프 학습(GNN) / 지식 그래프

- 🟢 [graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) — 그래프/Transformer 기반 부정, 이상, 이상치 탐지 논문 모음 `paper-list` ⭐1.9k · 📅2026-06
- 🟢 [Awesome-TimeSeries-SpatioTemporal-Diffusion-Model](https://github.com/yyysjz1997/Awesome-TimeSeries-SpatioTemporal-Diffusion-Model) — 시계열 및 시공간 데이터용 diffusion model 서베이 및 논문 모음(활발) `survey` ⭐996 · 📅2026-02
- 🟢 [Awesome-DynamicGraphLearning](https://github.com/SpaceLearner/Awesome-DynamicGraphLearning) — 동적(시계열) 그래프 및 지식 그래프 상의 머신러닝 논문 모음 `paper-list` ⭐710 · 📅2025-06
- 🟢 [awesome-gnn-systems](https://github.com/ch-wan/awesome-gnn-systems) — GNN 시스템 및 고속화에 관한 리소스 모음 `awesome` ⭐344 · 📅2026-06
- 🟢 [awesome-molecular-generation](https://github.com/amorehead/awesome-molecular-generation) — 생성적 분자 모델링 및 설계 논문 모음 `paper-list` ⭐343 · 📅2026-06
- 🟢 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/mala-lab/Awesome-Deep-Graph-Anomaly-Detection) — 2025년 TKDE 서베이 공식 리포지토리. GNN 기반 그래프 이상 탐지 논문 및 데이터셋 `survey` ⭐218 · 📅2026-06
- 🟢 [Awesome-TKGC](https://github.com/jiapuwang/Awesome-TKGC) — 시계열 지식 그래프 보완(TKGC)의 논문 및 리소스를 5단계 분류로 망라 `paper-list` ⭐116 · 📅2025-10
- 🟢 [awesome-molecular-diffusion-models](https://github.com/AzureLeon1/awesome-molecular-diffusion-models) — 분자 diffusion model 관련 논문의 엄선 리스트(활발) `paper-list` ⭐102 · 📅2026-04
- 🟢 [Awesome-Knowledge-Graph-Reasoning](https://github.com/LIANGKE23/Awesome-Knowledge-Graph-Reasoning) — 지식 그래프 추론 논문, 코드, 데이터셋 모음 `paper-list` ⭐7 · 📅2025-11
- 📑 [awesome-graph-self-supervised-learning](https://github.com/LirongWu/awesome-graph-self-supervised-learning) — TKDE 논문(대조/생성/예측형) 부속 리스트 `survey` ⭐1.4k · 📅2024-08
- 📑 [Awesome-GNN4TS](https://github.com/KimMeen/Awesome-GNN4TS) — 시계열 분석용 GNN(TPAMI 2024) 리소스 모음 `survey` ⭐859 · 📅2024-08
- 📑 [awesome-pretrain-on-molecules](https://github.com/junxia97/awesome-pretrain-on-molecules) — 화학 사전 학습 모델(IJCAI 2023 survey) 논문 리스트 `survey` ⭐539 · 📅2023-06
- 📑 [Generative_KG_Construction_Papers](https://github.com/zjunlp/Generative_KG_Construction_Papers) — 생성적 지식 그래프 구축 리뷰(EMNLP 2022) 논문 모음 `survey` ⭐113 · 📅2023-07
- 📑 [Awesome-Trustworthy-GNNs](https://github.com/Radical3-HeZhang/Awesome-Trustworthy-GNNs) — 신뢰할 수 있는 GNN(프라이버시/강건성/공정성/설명성) 서베이(Proc. IEEE 2024) `survey` ⭐98 · 📅2024-07
- 🟡 [GNNPapers](https://github.com/thunlp/GNNPapers) — GNN의 필독 논문 모음(대표) `paper-list` ⭐16.8k · 📅2023-12
- 🟡 [Awesome-Graph-Neural-Networks](https://github.com/TrustAGI-Lab/Awesome-Graph-Neural-Networks) — GNN 논문 리스트 `paper-list` ⭐2.3k · 📅2023-12
- 🟡 [awesome-self-supervised-gnn](https://github.com/ChandlerBang/awesome-self-supervised-gnn) — GNN의 사전 학습 및 self-supervised learning 논문 모음 `paper-list` ⭐1.7k · 📅2024-02
- 🟡 [GNN4Traffic](https://github.com/jwwthu/GNN4Traffic) — 교통 예측용 GNN 논문 및 코드의 대규모 컬렉션 `paper-list` ⭐1.2k · 📅2024-08
- 🟡 [awesome-graph-transformer](https://github.com/wehos/awesome-graph-transformer) — graph transformer 논문 모음 `paper-list` ⭐931 · 📅2025-03
- 🟡 [PromptKG](https://github.com/zjunlp/PromptKG) — 프롬프트 학습 및 지식 그래프 관련 연구, 도구, 논문 갤러리 `paper-list` ⭐734 · 📅2024-03
- 🟡 [awesome-graph-generation](https://github.com/yuanqidu/awesome-graph-generation) — 그래프 및 분자 생성 논문을 망라한 최신 리스트 `paper-list` ⭐360 · 📅2025-01
- 🟡 [Awesome-Hypergraph-Network](https://github.com/gzcsudo/Awesome-Hypergraph-Network) — 하이퍼그래프 학습, 이론, 데이터, 도구의 엄선 모음 `awesome` ⭐334 · 📅2025-02
- 🟡 [Awesome-Fair-Graph-Learning](https://github.com/EdisonLeeeee/Awesome-Fair-Graph-Learning) — 공정한 그래프 학습(FairGL) 논문 리스트 `paper-list` ⭐144 · 📅2024-09
- 🟡 [Awesome-Temporal-Graph-Learning](https://github.com/MGitHubL/Awesome-Temporal-Graph-Learning) — temporal graph learning 기법(논문, 코드, 데이터셋) 모음 `paper-list` ⭐94 · 📅2025-05
- 🟡 [Awesome-Graph-OOD](https://github.com/kaize0409/Awesome-Graph-OOD) — 그래프 OOD(일반화, 훈련 시/테스트 시 적응) 논문 리스트 `paper-list` ⭐85 · 📅2024-10
- 🟡 [Awesome-GNN-based-drug-discovery](https://github.com/gozsari/Awesome-GNN-based-drug-discovery) — GNN을 통한 신약 개발(논문, 데이터셋, 도구)의 엄선 리스트 `awesome` ⭐65 · 📅2024-04
- 🟡 [HGNN_Collection](https://github.com/PolarisRisingWar/HGNN_Collection) — 이종 그래프 NN의 데이터셋 및 알고리즘 모음 `paper-list` ⭐62 · 📅2024-05
- 🟡 [awesome-GNN-social-recsys](https://github.com/claws-lab/awesome-GNN-social-recsys) — GNN 기반 소셜 추천 논문 모음 `paper-list` ⭐53 · 📅2024-05
- 🔴 [awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification) — 그래프 임베딩, 분류, 표현 학습의 중요 논문 모음(구현 포함) `paper-list` ⭐4.8k · 📅2023-03
- 🔴 [awesome-network-embedding](https://github.com/chihming/awesome-network-embedding) — 네트워크 임베딩 기법의 대표 엄선 리스트 `awesome` ⭐2.6k · 📅2020-12
- 🔴 [knowledge-graphs](https://github.com/shaoxiongji/knowledge-graphs) — 지식 그래프 연구(임베딩, 보완, 시계열 KG, 응용) 논문 모음 `paper-list` ⭐1.8k · 📅2022-10
- 🔴 [Awesome-Deep-Graph-Anomaly-Detection](https://github.com/XiaoxiaoMa-MQ/Awesome-Deep-Graph-Anomaly-Detection) — 딥러닝을 통한 그래프 이상 탐지 논문, 데이터셋, 구현 모음 `awesome` ⭐384 · 📅2023-07
- 🔴 [awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) — 저분자 신약 개발용 머신러닝 리소스의 엄선 모음 `awesome` ⭐241 · 📅2023-11
- 🔴 [awesome-graph-ood](https://github.com/THUMNLab/awesome-graph-ood) — 그래프의 OOD 일반화에 관한 논문 모음 `paper-list` ⭐169 · 📅2023-06
- 🔴 [awesome-expressive-gnn](https://github.com/mengliu1998/awesome-expressive-gnn) — GNN의 표현력에 관한 연구 및 개선 논문 모음 `paper-list` ⭐124 · 📅2023-11

## 🛒 추천 시스템(RecSys)

- 🟢 [RSPapers](https://github.com/hongleizhang/RSPapers) — 추천 시스템 필독 논문을 17개 카테고리로 정리, 매주 업데이트(LLM/Agentic RS 등도 추가) `awesome` ⭐6.5k · 📅2026-03
- 🟢 [Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising](https://github.com/guyulongcs/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising) — 검색, 추천, 광고용 딥러닝 논문 모음 `paper-list` ⭐2.5k · 📅2026-04
- 🟢 [Awesome-LLM-for-RecSys](https://github.com/CHIANGEL/Awesome-LLM-for-RecSys) — LLM 관련 추천 시스템 논문 모음(TOIS 채택 서베이 포함) `survey` ⭐1.5k · 📅2026-01
- 🟢 [Awesome-LLM4RS-Papers](https://github.com/nancheng58/Awesome-LLM4RS-Papers) — LLM 강화 추천 시스템 논문 모음 `paper-list` ⭐766 · 📅2026-03
- 🟢 [Awesome-Cold-Start-Recommendation](https://github.com/YuanchenBei/Awesome-Cold-Start-Recommendation) — 콜드 스타트 추천 리소스 모음(LLM 시대 서베이 포함) `survey` ⭐284 · 📅2026-03
- 📑 [LLM4Rec-Awesome-Papers](https://github.com/WLiK/LLM4Rec-Awesome-Papers) — LLM을 활용한 추천 시스템 논문 및 리소스 모음(서베이 포함) `survey` ⭐2.3k · 📅2025-03
- 📑 [RecDebiasing](https://github.com/jiawei-chen/RecDebiasing) — TOIS 2023 "Bias and Debias in Recommender System: A Survey"의 편향 제거 기법 모음 `survey` ⭐462 · 📅2024-02
- 📑 [Awesome-SSLRec-Papers](https://github.com/HKUDS/Awesome-SSLRec-Papers) — ACM CSUR "Self-Supervised Learning for Recommendation" 서베이의 companion `survey` ⭐124 · 📅2024-08
- 🔴 [Awesome-RSPapers](https://github.com/RUCAIBox/Awesome-RSPapers) — 추천 시스템 논문의 망라적 리스트 `paper-list` ⭐988 · 📅2022-10
- 🔴 [CRSPapers](https://github.com/RUCAIBox/CRSPapers) — 대화형 추천 시스템(CRS) 논문 리스트 `paper-list` ⭐80 · 📅2022-11
- 🔴 [Awesome-Sequence-Modeling-for-Recommendation](https://github.com/AiHubCN/Awesome-Sequence-Modeling-for-Recommendation) — 순차 추천 및 순차 모델링 논문 모음 `paper-list` ⭐39 · 📅2023-11
- 🔴 [Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems](https://github.com/YuyingZhao/Awesome-Fairness-and-Diversity-Papers-in-Recommender-Systems) — 추천 시스템의 공정성 및 다양성 연구를 포괄적으로 정리 `paper-list` ⭐25 · 📅2023-06

## 📈 시계열(Time Series)

- 🟢 [awesome-time-series-papers](https://github.com/TSCenter/awesome-time-series-papers) — 주요 AI 학회의 최신 시계열 논문 및 코드 모음 `paper-list` ⭐1k · 📅2026-06
- 🟢 [Awesome_Imputation](https://github.com/WenjieDu/Awesome_Imputation) — 시계열의 결측값 보완(imputation) 논문 및 기법을 모은 서베이 리포지토리 `survey` ⭐421 · 📅2026-03
- 🟢 [awesome-time-series-forecasting](https://github.com/TongjiFinLab/awesome-time-series-forecasting) — 시계열 예측 논문 및 코드 모음 `paper-list` ⭐279 · 📅2026-06
- 🟢 [Awesome-Anomaly-Detection-Foundation-Models](https://github.com/mala-lab/Awesome-Anomaly-Detection-Foundation-Models) — 기반 모델을 통한 이상 탐지 논문 모음 `paper-list` ⭐202 · 📅2026-06
- 🟢 [awesome-multivariate-time-series-anomaly-detection-algorithms](https://github.com/lzz19980125/awesome-multivariate-time-series-anomaly-detection-algorithms) — 다변량 시계열 이상 탐지 논문 리스트 `paper-list` ⭐77 · 📅2025-09
- 🟢 [awesome-time-series-analysis](https://github.com/qhliu26/awesome-time-series-analysis) — 시계열의 논문, 벤치마크, 데이터셋, 튜토리얼 모음 `awesome` ⭐66 · 📅2025-09
- 📑 [time-series-transformers-review](https://github.com/qingsongedu/time-series-transformers-review) — 시계열용 Transformer 리소스(논문, 코드, 데이터)를 전문적으로 정리한 리뷰 `survey` ⭐3k · 📅2024-08
- 🟡 [awesome-TS-anomaly-detection](https://github.com/rob-med/awesome-TS-anomaly-detection) — 시계열 데이터의 이상 탐지 도구 및 데이터셋 리스트 `awesome` ⭐3.2k · 📅2024-10
- 🟡 [awesome-AI-for-time-series-papers](https://github.com/qingsongedu/awesome-AI-for-time-series-papers) — 주요 학회 및 저널의 시계열 AI 논문, 튜토리얼, 서베이 모음 `paper-list` ⭐1.6k · 📅2024-04
- 🟡 [Awesome-TimeSeries-SpatioTemporal-LM-LLM](https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM) — 시계열, 시공간, 이벤트 데이터용 LLM/기반 모델 논문 모음 `paper-list` ⭐1.2k · 📅2024-12
- 🟡 [Awesome-TimeSeries-LLM-FM](https://github.com/start2020/Awesome-TimeSeries-LLM-FM) — 시계열 태스크용 LLM 및 기반 모델 리소스 모음 `paper-list` ⭐154 · 📅2024-06
- 🟡 [Awesome-Large-Models-for-Time-Series](https://github.com/SJTU-DMTai/Awesome-Large-Models-for-Time-Series) — 시계열 분석용 LLM 및 기반 모델 논문 모음 `paper-list` ⭐47 · 📅2024-10

## 🦾 AI 에이전트 / LLM Agents

- 🟢 [LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) — 86페이지 서베이 "The Rise and Potential of LLM Based Agents" 논문 리스트 `survey` ⭐8.2k · 📅2025-09
- 🟢 [LLMAgentPapers](https://github.com/zjunlp/LLMAgentPapers) — LLM 에이전트의 필독 논문 모음 `paper-list` ⭐3.1k · 📅2026-06
- 🟢 [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) — LLM 에이전트의 기법, 응용, 과제 서베이 논문 모음 `survey` ⭐2.8k · 📅2025-11
- 🟢 [LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) — LLM 기반 에이전트 관련 논문 리스트 `paper-list` ⭐2.3k · 📅2025-07
- 🟢 [awesome-multi-agent-papers](https://github.com/kyegomez/awesome-multi-agent-papers) — 멀티 에이전트 논문의 큐레이션 모음(Swarms team) `awesome` ⭐1.6k · 📅2026-06
- 🟢 [awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — LLM 에이전트 프레임워크의 엄선 리스트 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers) — AI 에이전트 연구 논문 모음(엔지니어링, 메모리, 평가, 워크플로) `paper-list` ⭐1.4k · 📅2026-05
- 🟢 [Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) — 멀티모달 GUI 에이전트의 논문 및 리소스 모음 `paper-list` ⭐1.2k · 📅2025-08
- 🟢 [Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) — LLM 주도 자율 에이전트 컬렉션 `awesome` ⭐1.2k · 📅2026-06
- 🟢 [GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) — GUI 에이전트 논문의 엄선 리스트 `paper-list` ⭐823 · 📅2026-06
- 🟢 [Awesome-Memory-for-Agents](https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents) — 언어 에이전트의 메모리(사용자 프로필, 대화 이력)에 관한 논문 모음 `paper-list` ⭐576 · 📅2026-06
- 🟢 [awesome-computer-use](https://github.com/ranpox/awesome-computer-use) — Computer-use GUI 에이전트의 동영상, 블로그, 논문, 프로젝트 모음 `awesome` ⭐567 · 📅2026-04
- 🟢 [awesome-ui-agents](https://github.com/opendilab/awesome-ui-agents) — Web/App/OS를 횡단하는 UI 에이전트 리소스의 지속 업데이트 리스트 `awesome` ⭐304 · 📅2026-06
- 🟢 [Awesome-GraphMemory](https://github.com/DEEP-PolyU/Awesome-GraphMemory) — 그래프 기반 에이전트 메모리의 서베이, 논문, 벤치마크 모음 `survey` ⭐298 · 📅2026-06
- 🟡 [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — AI 자율 에이전트(프로젝트/프레임워크)의 대규모 리스트 `awesome` ⭐28.4k · 📅2025-02
- 🟡 [awesome-llm-powered-agent](https://github.com/hyp1231/awesome-llm-powered-agent) — LLM 주도 에이전트의 논문, 리포지토리, 블로그 모음 `awesome` ⭐2.2k · 📅2025-04
- 🟡 [LLM-Planning-Papers](https://github.com/AGI-Edgerunners/LLM-Planning-Papers) — LLM의 플래닝(planning)에 관한 필독 논문 모음 `paper-list` ⭐441 · 📅2024-07
- 🟡 [awesome-llm-agents](https://github.com/junhua/awesome-llm-agents) — LLM 에이전트의 고품질 논문 및 OSS 프로젝트 모음 `paper-list` ⭐85 · 📅2024-11
- 🟡 [Awesome-LLM-based-MultiAgents](https://github.com/Andrewzh112/Awesome-LLM-based-MultiAgents) — LLM 기반 멀티 에이전트 논문 모음 `paper-list` ⭐28 · 📅2024-10
- 🔴 [Multi-Agent-Papers](https://github.com/shizhl/Multi-Agent-Papers) — 복잡 태스크용 멀티 에이전트 협조의 필독 논문 모음 `paper-list` ⭐71 · 📅2023-11

## 🔬 의료 AI / AI for Science

- 🟢 [MedLLMsPracticalGuide](https://github.com/AI-in-Health/MedLLMsPracticalGuide) — 의료 LLM 실전 가이드(Nature Reviews Bioengineering 게재) `survey` ⭐2k · 📅2025-09
- 🟢 [awesome-ai-for-science](https://github.com/ai-boost/awesome-ai-for-science) — 물리, 화학, 생물, 재료 등 과학적 발견을 가속하는 AI 도구 및 논문 모음 `awesome` ⭐1.7k · 📅2026-06
- 🟢 [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration) — 이미지 정합 전반의 도서, 논문, 툴박스 모음 `awesome` ⭐1.5k · 📅2026-05
- 🟢 [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — 의료 영상에의 멀티모달 학습 응용 리소스 모음 `awesome` ⭐966 · 📅2026-06
- 🟢 [Awesome-Healthcare-Foundation-Models](https://github.com/Jianing-Qiu/Awesome-Healthcare-Foundation-Models) — 헬스케어 기반 모델 논문 컬렉션 `paper-list` ⭐518 · 📅2026-04
- 🟢 [awesome-foundation-model-single-cell-papers](https://github.com/OmicsML/awesome-foundation-model-single-cell-papers) — 단일 세포 기반 모델에 특화된 논문 리스트 `paper-list` ⭐477 · 📅2026-06
- 🟢 [Awesome-Radiology-Report-Generation](https://github.com/mk-runner/Awesome-Radiology-Report-Generation) — 방사선 리포트 생성의 논문, 데이터셋, 도구 모음(매우 활발) `paper-list` ⭐447 · 📅2026-06
- 🟢 [Awesome-LWMs](https://github.com/jaychempan/Awesome-LWMs) — 대규모 기상 모델(LWMs) 컬렉션(AI4Earth) `awesome` ⭐361 · 📅2025-06
- 🟢 [awesome-AI4MolConformation-MD](https://github.com/AspirinCode/awesome-AI4MolConformation-MD) — 생성 AI/딥러닝을 통한 분자 컨포메이션 및 분자 동역학 논문 모음 `paper-list` ⭐298 · 📅2026-06
- 🟢 [Awesome-Earth-Artificial-Intelligence](https://github.com/ESIPFed/Awesome-Earth-Artificial-Intelligence) — 지구과학 AI의 튜토리얼, 소프트웨어, 데이터셋, 논문 모음 `awesome` ⭐245 · 📅2026-05
- 🟢 [awesome-mmps](https://github.com/willxxy/awesome-mmps) — EEG/ECG/EMG 등 생리 신호 × 머신러닝의 리소스 및 데이터셋 모음(활발) `awesome` ⭐162 · 📅2026-02
- 🟢 [Awesome-Active-Learning-for-Medical-Image-Analysis](https://github.com/LightersWang/Awesome-Active-Learning-for-Medical-Image-Analysis) — 의료 영상 분석의 능동 학습 서베이 논문 및 코드 `survey` ⭐135 · 📅2025-06
- 🟢 [awesome-drug-discovery](https://github.com/yboulaamane/awesome-drug-discovery) — 계산 신약 개발 기법에 특화된 엄선 리소스 리스트 `awesome` ⭐120 · 📅2026-05
- 🟢 [awesome-pathology](https://github.com/open-pathology/awesome-pathology) — 디지털/계산 병리 리소스(self-supervised, 특징 추출, 데이터셋 등)를 망라 `awesome` ⭐120 · 📅2026-02
- 🟢 [SurvivalAnalysisPapers](https://github.com/shi-ang/SurvivalAnalysisPapers) — 생존 시간 분석 논문 및 리소스를 카테고리별로 정리(활발) `paper-list` ⭐92 · 📅2026-06
- 🟢 [Awesome-DL-for-Medical-Imaging-Segmentation](https://github.com/faresbougourzi/Awesome-DL-for-Medical-Imaging-Segmentation) — 의료 영상 세그멘테이션 딥러닝 논문 모음 `paper-list` ⭐66 · 📅2026-02
- 🟢 [awesome-bci-reviews](https://github.com/okbalefthanded/awesome-bci-reviews) — BCI의 동료 심사 리뷰 및 서베이를 연대순으로 정리(활발) `survey` ⭐47 · 📅2025-08
- 🟢 [AwesomeWSI](https://github.com/BearCleverProud/AwesomeWSI) — WSI 분석과 병리 기반 모델의 포괄적 컬렉션(IJCAI 2025 서베이 준거, 활발) `survey` ⭐34 · 📅2026-06
- 🟢 [Awesome-Generative-Models-in-Pathology](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology) — 병리에서의 생성 모델(이미지 합성, 리포트 생성, 크로스모달) 150편 이상 서베이 `survey` ⭐27 · 📅2026-06
- 🟢 [Awesome-MICCAI-2026](https://github.com/ambicuity/Awesome-MICCAI-2026) — MICCAI 2026 논문을 arXiv에서 자동 수집하고 봇이 매일 업데이트, 분야별 분류 `paper-list` ⭐26 · 📅2026-06
- 🟢 [Awesome-AI-Agents-Medicine](https://github.com/AIM-Research-Lab/Awesome-AI-Agents-Medicine) — 의료용 에이전트 AI 최신 서베이 모음 `paper-list` ⭐25 · 📅2026-03
- 🟢 [Awesome-AI4BCI](https://github.com/Deepak-Mewada/Awesome-AI4BCI) — 뇌 신호 인코딩/디코딩의 딥러닝 모델 리소스 모음 `paper-list` ⭐17 · 📅2025-09
- 📑 [Awesome-Foundation-Models-in-Medical-Imaging](https://github.com/xmindflow/Awesome-Foundation-Models-in-Medical-Imaging) — 의료 영상의 시각 및 언어 기반 모델 엄선 리스트 `survey` ⭐300 · 📅2024-06
- 📑 [Awesome-Foundation-Models-for-Weather-and-Climate](https://github.com/shengchaochen82/Awesome-Foundation-Models-for-Weather-and-Climate) — 기상 및 기후 데이터 이해용 기반 모델의 포괄 서베이 `survey` ⭐294 · 📅2025-02
- 📑 [Awesome-Foundation-Models-for-Advancing-Healthcare](https://github.com/YutingHe-list/Awesome-Foundation-Models-for-Advancing-Healthcare) — 헬스케어 기반 모델(HFM)의 과제, 기회, 미래 전망 포괄 리뷰 `survey` ⭐252 · 📅2024-12
- 📑 [DL-ECG-Review](https://github.com/hsd1503/DL-ECG-Review) — ECG 딥러닝 기법 리뷰와 논문 요약 표 `survey` ⭐251 · 📅2020-10
- 📑 [MedImgReg_Survey](https://github.com/JHU-MedImage-Reg/MedImgReg_Survey) — 학습 기반 의료 영상 정합 논문+손실 함수/평가 지표 구현 `survey` ⭐121 · 📅2025-05
- 🟡 [awesome-deep-learning-single-cell-papers](https://github.com/OmicsML/awesome-deep-learning-single-cell-papers) — 단일 세포 분석 × 딥러닝의 최신 논문을 30개 이상 태스크별로 정리 `paper-list` ⭐858 · 📅2025-04
- 🟡 [awesome-protein-representation-learning](https://github.com/LirongWu/awesome-protein-representation-learning) — 단백질 표현 학습(AlphaFold 포함) 논문 모음 `paper-list` ⭐684 · 📅2024-11
- 🟡 [Awesome-Medical-Large-Language-Models](https://github.com/burglarhobbit/Awesome-Medical-Large-Language-Models) — 의료 및 헬스케어 분야 LLM 논문을 엄선한 컬렉션 `paper-list` ⭐394 · 📅2025-05
- 🟡 [awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design) — AI 기반 단백질 설계 연구 논문 모음 `paper-list` ⭐307 · 📅2024-05
- 🟡 [Awesome-LLM-Healthcare](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) — 의료 분야 LLM 리뷰 논문에 대응하는 논문 리스트 `paper-list` ⭐269 · 📅2023-12
- 🟡 [Awesome-Neuron-Segmentation-in-EM-Images](https://github.com/subeeshvasu/Awesome-Neuron-Segmentation-in-EM-Images) — 전자현미경(EM) 영상에서의 신경 돌기 3D 세그멘테이션 리소스 모음 `awesome` ⭐57 · 📅2024-03
- 🟡 [awesome-molecule-protein-pretrain-papers](https://github.com/OmicsML/awesome-molecule-protein-pretrain-papers) — 분자 및 단백질 사전 학습 논문 모음(신약 개발, 도킹) `paper-list` ⭐47 · 📅2024-03
- 🟡 [Awesome_AI4Earth](https://github.com/taohan10200/Awesome_AI4Earth) — 지구 시스템(특히 기상, 기후)의 머신러닝 논문 모음 `paper-list` ⭐14 · 📅2023-12
- 🔴 [MICCAI-OpenSourcePapers](https://github.com/JunMa11/MICCAI-OpenSourcePapers) — MICCAI 2019-2023의 오픈소스 논문을 코드 링크 포함 표로 정리 `paper-list` ⭐1.3k · 📅2023-11
- 🔴 [awesome-ehr-deeplearning](https://github.com/hurcy/awesome-ehr-deeplearning) — EHR 마이닝, 머신러닝, 딥러닝 논문 모음 `awesome` ⭐430 · 📅2022-10
- 🔴 [Physiological-Signal-Classification-Papers](https://github.com/ziyujia/Physiological-Signal-Classification-Papers) — EEG/ECG/EMG/EOG 분류 논문을 태스크별로 정리 `paper-list` ⭐250 · 📅2022-07
- 🔴 [awesome-radiology-report-generation](https://github.com/zhjohnchan/awesome-radiology-report-generation) — 방사선/의료 리포트 생성과 관련 분야의 큐레이션 리스트 `awesome` ⭐180 · 📅2022-05
- 🔴 [awesome-structural-bioinformatics](https://github.com/twoXes/awesome-structural-bioinformatics) — 구조 생물정보학 리소스 모음 `awesome` ⭐80 · 📅2023-05
- 🔴 [awesome-bio-chatgpt](https://github.com/OmicsML/awesome-bio-chatgpt) — 생물학 및 의료 분야에의 ChatGPT/LLM 응용 논문 및 리소스 모음 `paper-list` ⭐22 · 📅2023-04

## 🌍 응용 도메인 (Code/Math/Finance/Law/과학)

- 🟢 [techniques](https://github.com/satellite-image-deep-learning/techniques) — 위성 및 항공 영상의 딥러닝 기법 초대규모 레퍼런스 `awesome` ⭐10.2k · 📅2026-06
- 🟢 [awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) — 금융 시장의 LLM, 딥러닝 전략, 도구의 대표 리스트 `awesome` ⭐6.1k · 📅2026-06
- 🟢 [Awesome-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM) — 코드용 언어 모델 연구와 데이터셋의 망라적 큐레이션 `paper-list` ⭐3.4k · 📅2026-05
- 🟢 [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) — RS 변화 검출의 데이터셋, 기법, 서베이 모음 `awesome` ⭐2.3k · 📅2026-04
- 🟢 [Awesome-Remote-Sensing-Foundation-Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models) — RSFM의 논문, 데이터셋, 벤치마크, 사전 학습 가중치를 망라(활발) `paper-list` ⭐1.9k · 📅2026-05
- 🟢 [awesome-agriculture](https://github.com/brycejohnston/awesome-agriculture) — 농업, 농장, 원예용 OSS 기술(ML, GIS, 원격 탐사, 로보틱스 포함)의 대표 리스트 `awesome` ⭐1.8k · 📅2026-01
- 🟢 [awesome-search](https://github.com/frutik/awesome-search) — EC 검색을 중심으로 시맨틱 검색, LTR, 쿼리 이해, 검색 품질을 망라 `awesome` ⭐1.5k · 📅2026-06
- 🟢 [best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning) — 원자론적 머신러닝 프로젝트 약 510건을 점수화 랭킹(활발) `awesome` ⭐695 · 📅2026-06
- 🟢 [Awesome-Scientific-Language-Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models) — 수학, 물리, 화학, 재료, 생물, 지구과학 등 과학 도메인 사전 학습 모델 포괄 서베이 `survey` ⭐660 · 📅2025-06
- 🟢 [awesome-materials-informatics](https://github.com/tilde-lab/awesome-materials-informatics) — 현대 재료과학에서의 materials informatics 노력 모음 `awesome` ⭐518 · 📅2026-03
- 🟢 [awesome-digital-humanities](https://github.com/dh-tech/awesome-digital-humanities) — 인문학자를 위한 정량적, 계산적 기법 소프트웨어 모음(NLP, 토픽 모델, 텍스트 분석) `awesome` ⭐388 · 📅2026-05
- 🟢 [AwesomeLLM4SE](https://github.com/iSEngLab/AwesomeLLM4SE) — 요구, 개발, 테스트, 유지보수까지 SE 전 영역의 LLM 논문을 정리 `survey` ⭐331 · 📅2026-04
- 🟢 [awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) — 판결 예측, 계약 분류, 판례 검색, 법무 QA 등의 LegalNLP 리소스 모음 `awesome` ⭐330 · 📅2025-10
- 🟢 [awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) — 주요 학회 및 저널의 교육용 AI/LLM 논문을 수집 `paper-list` ⭐193 · 📅2026-06
- 🟢 [awesome-pinns](https://github.com/AI-in-Transportation-Lab/awesome-pinns) — PINN/물리 정보 머신러닝의 라이브러리, 논문, 튜토리얼 엄선 모음 `awesome` ⭐124 · 📅2026-06
- 🟢 [PINN_Paper_List](https://github.com/Event-AHU/PINN_Paper_List) — 물리 정보 뉴럴 네트워크(PINN) 논문 리스트 `paper-list` ⭐81 · 📅2026-04
- 📑 [FinLLMs](https://github.com/adlnlp/FinLLMs) — 논문 "Large Language Models in Finance"의 관련 연구, 벤치마크, 데이터셋 모음 `survey` ⭐374 · 📅2025-04
- 📑 [DL4TP](https://github.com/zhaoyu-li/DL4TP) — 정리 증명에의 딥러닝 조사. autoformalization, proof search 등으로 분류 `survey` ⭐225 · 📅2025-05
- 📑 [awesome-RSFMs](https://github.com/xiaoaoran/awesome-RSFMs) — 서베이 "Foundation Models for Remote Sensing and Earth Observation" 공식 리포지토리 `survey` ⭐51 · 📅2024-11
- 🟡 [Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) — 머신러닝에 중점을 둔 퀀트/알고리즘 트레이딩 리소스 모음 `awesome` ⭐3.7k · 📅2025-05
- 🟡 [PINNpapers](https://github.com/idrl-lab/PINNpapers) — PINN의 필독 논문 모음. 병렬화, 가속, 전이 학습, 불확실성 정량화, 응용으로 정리 `paper-list` ⭐1.5k · 📅2023-12
- 🟡 [LLM4SoftwareTesting](https://github.com/LLM-Testing/LLM4SoftwareTesting) — LLM을 활용한 테스트 생성 및 테스트 보완 등 논문 모음 `paper-list` ⭐531 · 📅2024-01
- 🟡 [awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) — 전자 설계 자동화(EDA, 칩 설계)에의 AI 응용 논문 모음 `paper-list` ⭐212 · 📅2023-12
- 🟡 [awesome-ai4lam](https://github.com/AI4LAM/awesome-ai4lam) — 도서관, 기록관, 박물관(GLAM/LAM)용 AI 프로젝트, 사례, 리소스 모음(AI4LAM 커뮤니티 운영) `awesome` ⭐179 · 📅2024-06
- 🟡 [Awesome-LLM4Math](https://github.com/tongyx361/Awesome-LLM4Math) — LLM 수학 추론의 고품질 엄선 리스트. 학습 데이터, SFT, RL, 벤치마크를 정리 `paper-list` ⭐157 · 📅2024-07
- 🟡 [Awesome-Education-LLM](https://github.com/Geralt-Targaryen/Awesome-Education-LLM) — 교육용 LLM 연구 및 응용(교수 지원, 문제 생성, 자동 채점 등)을 정리 `paper-list` ⭐77 · 📅2024-09
- 🟡 [LLM_X_papers](https://github.com/czyssrs/LLM_X_papers) — 금융, 의료, 법무의 LLM 논문을 지속 업데이트하는 독서 리스트 `paper-list` ⭐54 · 📅2025-02
- 🔴 [awesome-machine-learning-on-source-code](https://github.com/src-d/awesome-machine-learning-on-source-code) — 소스 코드에 적용한 머신러닝(MLonCode) 논문 및 링크 모음 `awesome` ⭐6.6k · 📅2020-12
- 🔴 [Awesome-LegalAI-Resources](https://github.com/CSHaitao/Awesome-LegalAI-Resources) — 사법 AI용 코퍼스, 벤치마크, QA, 요약 데이터셋을 집약 `awesome` ⭐305 · 📅2023-07
- 🔴 [awesome-program](https://github.com/shaohua0116/awesome-program) — 프로그램 합성, 귀납, 실행, 수리, programmatic RL 논문 모음 `paper-list` ⭐168 · 📅2021-10
- 🔴 [Awesome-Precision-Agriculture](https://github.com/px39n/Awesome-Precision-Agriculture) — UAV 및 딥러닝을 통한 수확량 예측, 작물 검출, 잡초 검출 등 논문 모음 `paper-list` ⭐140 · 📅2020-09
- 🔴 [awesome-ai4chem](https://github.com/sherrylixuecheng/awesome-ai4chem) — 화학용 AI 논문의 큐레이션 `paper-list` ⭐48 · 📅2023-05
- 🔴 [Awesome-Sports-Analytics](https://github.com/wywyWang/Awesome-Sports-Analytics) — 축구, 농구, 배드민턴 등 스포츠 분석 논문/코드 모음 `paper-list` ⭐21 · 📅2023-03

## 🚗 자율주행(Autonomous Driving)

- 🟢 [Birds-eye-view-Perception](https://github.com/OpenDriveLab/Birds-eye-view-Perception) — BEV 인지 연구와 쿡북(IEEE T-PAMI 2023) `survey` ⭐1.4k · 📅2025-07
- 🟢 [Awesome-Trajectory-Motion-Prediction-Papers](https://github.com/colorfulfuture/Awesome-Trajectory-Motion-Prediction-Papers) — 궤적 및 모션 예측의 포괄적 논문 모음 `paper-list` ⭐1.1k · 📅2026-01
- 🟢 [awesome-end-to-end-autonomous-driving](https://github.com/opendilab/awesome-end-to-end-autonomous-driving) — End-to-End 자율주행 리소스를 지속 업데이트하는 리스트 `awesome` ⭐492 · 📅2026-06
- 📑 [Awesome-Data-Centric-Autonomous-Driving](https://github.com/LincanLi-X/Awesome-Data-Centric-Autonomous-Driving) — 데이터 중심 자율주행 서베이의 공식 리포지토리 `survey` ⭐179 · 📅2024-03
- 🟡 [awesome-lane-detection](https://github.com/amusi/awesome-lane-detection) — 차선 검출(lane detection) 논문 리스트 `paper-list` ⭐3.1k · 📅2024-08
- 🟡 [Awesome-Interaction-Aware-Trajectory-Prediction](https://github.com/jiachenli94/Awesome-Interaction-Aware-Trajectory-Prediction) — 상호작용을 고려한 궤적 예측 최신 연구 자료 모음 `paper-list` ⭐1.7k · 📅2024-09
- 🟡 [Awesome-Autonomous-Driving](https://github.com/autodriving-heart/Awesome-Autonomous-Driving) — 자율주행 전반의 awesome 리스트 `awesome` ⭐1.1k · 📅2024-08
- 🟡 [awesome-knowledge-driven-AD](https://github.com/PJLab-ADG/awesome-knowledge-driven-AD) — 지식 주도형 자율주행의 엄선 논문 모음 `paper-list` ⭐501 · 📅2024-06
- 🟡 [Awesome-Autonomous-Driving](https://github.com/PeterJaq/Awesome-Autonomous-Driving) — 자율주행 전반의 광범위한 리스트 `awesome` ⭐353 · 📅2024-08
- 🟡 [Awesome-occupancy-perception](https://github.com/autodriving-heart/Awesome-occupancy-perception) — 점유 인지(Occupancy) 논문 컬렉션 `paper-list` ⭐307 · 📅2024-08
- 🟡 [CVPR-2024-Papers-Autonomous-Driving](https://github.com/autodriving-heart/CVPR-2024-Papers-Autonomous-Driving) — CVPR 2024의 자율주행 관련 논문 리스트 `paper-list` ⭐257 · 📅2024-08
- 🟡 [CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI](https://github.com/autodriving-heart/CVPR2025-Papers-about-Autonomous-Driving-and-Embodied-AI) — CVPR 2025의 자율주행 및 체화 AI 관련 논문 리스트 `paper-list` ⭐30 · 📅2025-04
- 🟡 [Awesome-4D-Radar](https://github.com/autodriving-heart/Awesome-4D-Radar) — 4D 레이더 인지에 관한 논문 및 리소스 모음 `paper-list` ⭐12 · 📅2024-02
- 🔴 [Awesome-Occupancy-Prediction-Autonomous-Driving](https://github.com/chaytonmin/Awesome-Occupancy-Prediction-Autonomous-Driving) — 멀티 카메라 시맨틱 점유 예측 논문(Occ3D 등) `paper-list` ⭐264 · 📅2023-07
- 🔴 [awesome-driving-behavior-prediction](https://github.com/opendilab/awesome-driving-behavior-prediction) — 운전 행동 예측 연구 논문 모음 `paper-list` ⭐83 · 📅2022-12
- 🔴 [Awesome-BEV-Perception](https://github.com/autodriving-heart/Awesome-BEV-Perception) — BEV 인지의 엄선 논문 컬렉션 `paper-list` ⭐33 · 📅2023-06
- 🔴 [Awesome-Trajectory-Prediction](https://github.com/autodriving-heart/Awesome-Trajectory-Prediction) — 궤적 예측 논문 컬렉션 `paper-list` ⭐27 · 📅2023-06
- 🔴 [Awesome-BEV-Perception](https://github.com/ylhua/Awesome-BEV-Perception) — BEV 인지 관련 논문(BEVFormer, PETRv2, FIERY 등) `paper-list` ⭐5 · 📅2022-08

## 🛡️ AI 안전성 / Alignment / 해석가능성

- 🟢 [awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) — 책임 있는 ML 및 해석성의 종합 리소스 리스트 `awesome` ⭐4k · 📅2026-06
- 🟢 [Awesome-LLM-Safety](https://github.com/ydyjya/Awesome-LLM-Safety) — LLM 안전성 논문, 기사, 데이터셋, 벤치마크 모음 `awesome` ⭐1.9k · 📅2026-06
- 🟢 [awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) — ICDM/KDD/SDM 등 부정 탐지 데이터 마이닝 논문의 대표 리스트 `paper-list` ⭐1.8k · 📅2026-01
- 🟢 [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) — 설명 가능 AI/ML 연구 자료 모음 `paper-list` ⭐1.6k · 📅2026-03
- 🟢 [awesome-llm-security](https://github.com/corca-ai/awesome-llm-security) — LLM 보안 도구, 문헌, 프로젝트 모음 `awesome` ⭐1.6k · 📅2025-08
- 🟢 [TAADpapers](https://github.com/thunlp/TAADpapers) — 텍스트의 적대적 공격 및 방어(TAAD) 필독 논문 모음 `paper-list` ⭐1.6k · 📅2025-06
- 🟢 [Awesome-Jailbreak-on-LLMs](https://github.com/yueliu1999/Awesome-Jailbreak-on-LLMs) — LLM 탈옥 기법의 논문, 코드, 데이터셋, 평가 모음(매우 활발) `paper-list` ⭐1.5k · 📅2026-06
- 🟢 [awesome-machine-unlearning](https://github.com/tamlhp/awesome-machine-unlearning) — machine unlearning 서베이 공식 리스트. 기법, 데이터셋, 평가 지표를 망라 `awesome` ⭐960 · 📅2026-05
- 🟢 [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) — LLM의 machine unlearning 논문, 서베이, 벤치마크 모음 `paper-list` ⭐598 · 📅2026-06
- 🟢 [awesome-trustworthy-deep-learning](https://github.com/MinghuiChen43/awesome-trustworthy-deep-learning) — OOD 일반화, 적대적 샘플, 백도어 등 신뢰성 논문(매일 업데이트) `paper-list` ⭐387 · 📅2026-05
- 🟢 [membership-inference-machine-learning-literature](https://github.com/HongshengHu/membership-inference-machine-learning-literature) — 멤버십 추론 공격에 특화된 문헌 모음 `paper-list` ⭐372 · 📅2026-04
- 🟢 [Awesome-AI-for-cybersecurity](https://github.com/Billy1900/Awesome-AI-for-cybersecurity) — 네트워크 침입 탐지, 안티멀웨어, WAF, 부정 대책을 망라한 AI 리스트 `awesome` ⭐256 · 📅2026-06
- 🟢 [Awesome-model-inversion-attack](https://github.com/AndrewZhou924/Awesome-model-inversion-attack) — 모델 역전 공격 서베이의 공식 리스트. CV/그래프/NLP별로 정리 `paper-list` ⭐222 · 📅2026-04
- 🟢 [Awesome-LMMs-Mechanistic-Interpretability](https://github.com/itsqyh/Awesome-LMMs-Mechanistic-Interpretability) — 대규모 멀티모달 모델의 내부 표현을 다루는 mechanistic interpretability 리소스 모음(활발) `survey` ⭐211 · 📅2026-03
- 🟢 [Awesome-GenAI-Unlearning](https://github.com/franciscoliu/Awesome-GenAI-Unlearning) — 생성 AI의 unlearning 논문을 모달리티, 용도별로 정리 `paper-list` ⭐189 · 📅2026-04
- 🟢 [Awesome-GenAI-Watermarking](https://github.com/and-mill/Awesome-GenAI-Watermarking) — 생성 AI 모델용 워터마크 기법을 이미지, 음성, 텍스트별로 정리(활발) `awesome` ⭐142 · 📅2026-05
- 🟢 [awesome-mechanistic-interpretability](https://github.com/AI-in-Transportation-Lab/awesome-mechanistic-interpretability) — 뉴럴넷을 이해 가능한 계산 요소로 역해석하는 mechanistic interpretability 리소스 모음 `awesome` ⭐113 · 📅2026-06
- 🟢 [awesome-fraud-detection](https://github.com/AI4Risk/awesome-fraud-detection) — GNN을 통한 금융 부정 탐지의 서베이 포함 논문 및 코드 모음(활발) `paper-list` ⭐46 · 📅2026-05
- 📑 [Awesome-LLM-Safety-Papers](https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers) — LLM 안전성 서베이 논문 리스트 `survey` ⭐55 · 📅2024-12
- 🟡 [awesome-ml-for-cybersecurity](https://github.com/jivoi/awesome-ml-for-cybersecurity) — 악성코드, 침입 탐지 등에 ML을 사용하는 도구, 논문, 교재의 대표 리스트 `awesome` ⭐9k · 📅2024-08
- 🟡 [prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) — 프롬프트 인젝션에 대한 실용 및 제안된 방어책을 망라 `awesome` ⭐706 · 📅2025-02
- 🟡 [awesome-ml-privacy-attacks](https://github.com/stratosphereips/awesome-ml-privacy-attacks) — 멤버십 추론, 모델 역전, 속성 추론, 모델 추출을 망라한 논문 리스트 `awesome` ⭐639 · 📅2024-03
- 🟡 [Awesome-Backdoor-in-Deep-Learning](https://github.com/zihao-ai/Awesome-Backdoor-in-Deep-Learning) — 딥러닝의 백도어 공격과 방어를 공격 종류, 방어 단계로 정리한 논문 모음(활발) `paper-list` ⭐239 · 📅2024-03
- 🟡 [awesome-ai-safety](https://github.com/Giskard-AI/awesome-ai-safety) — AI 품질 및 안전성에 관한 논문과 기술 기사의 큐레이션 리스트 `paper-list` ⭐216 · 📅2025-04
- 🟡 [OpenRedTeaming](https://github.com/Libr-AI/OpenRedTeaming) — LLM/멀티모달의 레드 티밍 논문 모음(30+ 기법 구현) `paper-list` ⭐168 · 📅2025-05
- 🟡 [trojai-literature](https://github.com/usnistgov/trojai-literature) — NIST가 운영하는 AI 트로이목마 공격 연구 문헌 총람 `paper-list` ⭐151 · 📅2024-10
- 🟡 [Learning-Deep-Hiding](https://github.com/TracyCuiq/Learning-Deep-Hiding) — 이미지 스테가노그래피와 워터마크를 포함한 "deep hiding" 논문을 체계 정리 `paper-list` ⭐67 · 📅2024-06
- 🟡 [Constitutional-AI-awesome-papers](https://github.com/minbeomkim/Constitutional-AI-awesome-papers) — Constitutional AI/윤리 지침 하의 AI에 관한 논문 리스트 `paper-list` ⭐13 · 📅2024-03
- 🔴 [awesome-adversarial-machine-learning](https://github.com/yenchenlin/awesome-adversarial-machine-learning) — 적대적 머신러닝 논문, 블로그, 강연을 모은 고전적 큐레이션 `awesome` ⭐1.9k · 📅2020-11
- 🔴 [awesome-interpretable-machine-learning](https://github.com/lopusz/awesome-interpretable-machine-learning) — 해석 가능 머신러닝 리소스 리스트 `awesome` ⭐917 · 📅2023-03
- 🔴 [awesome-fairness-in-ai](https://github.com/datamllab/awesome-fairness-in-ai) — AI에서의 공정성 리소스의 엄선 모음 `awesome` ⭐334 · 📅2023-09
- 🔴 [awesome-xai](https://github.com/altamiracorp/awesome-xai) — 설명 가능 AI(XAI) 및 해석 가능 ML 논문과 리소스 `awesome` ⭐191 · 📅2021-05
- 🔴 [awesome-ai-alignment](https://github.com/dit7ya/awesome-ai-alignment) — AI alignment 연구의 우수 리소스 큐레이션 리스트 `awesome` ⭐81 · 📅2023-07
- 🔴 [awesome-ml-fairness](https://github.com/brandeis-machine-learning/awesome-ml-fairness) — 머신러닝의 공정성에 관한 논문 및 리소스 모음 `paper-list` ⭐74 · 📅2023-05
- 🔴 [awesome-ai-safety](https://github.com/hari-sikchi/awesome-ai-safety) — AI 안전성 논문, 프로젝트, 커뮤니티 리스트 `awesome` ⭐65 · 📅2020-02
- 🔴 [awesome-data-poisoning](https://github.com/ch-shin/awesome-data-poisoning) — 주요 학회의 데이터 포이즈닝 공격 및 방어 논문 모음 `awesome` ⭐25 · 📅2022-09
- 🔴 [Awesome-Adversarial-Training](https://github.com/KululuMi/Awesome-Adversarial-Training) — FGSM/PGD/TRADES/AutoAttack 등 적대적 훈련 논문 리스트 `paper-list` ⭐6 · 📅2022-04

## ⚖️ AI 윤리 / 거버넌스 / 규제 / Human-AI Interaction

- 🟢 [awesome-artificial-intelligence-regulation](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) — 각국의 AI 규제, 가이드라인, 윤리 규범, 표준을 지역별로 망라 `awesome` ⭐1.4k · 📅2026-06
- 🟢 [awesome-computational-social-science](https://github.com/gesiscss/awesome-computational-social-science) — 계산 사회과학의 도서, 강좌, OSS 리소스 망라 리스트(GESIS 운영) `awesome` ⭐903 · 📅2026-05
- 🟢 [Awesome-LLM-in-Social-Science](https://github.com/ValueByte-AI/Awesome-LLM-in-Social-Science) — 사회과학에 LLM을 응용하는 논문 모음 `paper-list` ⭐631 · 📅2026-06
- 🟢 [AwesomeResponsibleAI](https://github.com/AthenaCore/AwesomeResponsibleAI) — 책임 있는 AI의 연구, 도서, 규제, 성숙도 모델, 도구를 17개 분야로 집약 `awesome` ⭐130 · 📅2026-05
- 🟢 [Awesome-LLM-Psychometrics](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics) — LLM의 인격, 가치관, 마음 이론, 인지 능력을 심리 측정 관점에서 다루는 논문 모음 `survey` ⭐120 · 📅2025-11
- 🔴 [NLP4SocialGood_Papers](https://github.com/zhijing-jin/NLP4SocialGood_Papers) — 사회적 선을 위한 NLP 논문 독해 리스트(인명 구조, QoL, 공정성 등) `paper-list` ⭐309 · 📅2023-09
- 🔴 [awesome-HAI](https://github.com/bwang514/awesome-HAI) — HCI 관점에서의 인간과 AI 상호작용 설계에 관한 학술 자료 모음 `awesome` ⭐297 · 📅2021-05

## ⚡ 효율화 (압축/양자화/NAS/AutoML)

- 🟢 [Awesome-CoreML-Models](https://github.com/likedan/Awesome-CoreML-Models) — iOS용 Core ML 모델의 최대급 리스트 `model` ⭐7k · 📅2025-06
- 🟢 [Awesome-Model-Quantization](https://github.com/Efficient-ML/Awesome-Model-Quantization) — 모델 양자화 논문, 코드, 문서 리스트 `paper-list` ⭐2.4k · 📅2026-05
- 🟢 [Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM) — 효율적 LLM(가지치기, 양자화, 증류 등)의 큐레이션 리스트 `awesome` ⭐2k · 📅2025-06
- 🟢 [Awesome-LLM-Compression](https://github.com/HuangOwen/Awesome-LLM-Compression) — 양자화, 가지치기, 증류 등 LLM 압축 논문과 도구 모음 `awesome` ⭐1.8k · 📅2026-02
- 🟢 [tinyml-papers-and-projects](https://github.com/gigwegbe/tinyml-papers-and-projects) — TinyML 논문 및 프로젝트 모음(활발히 업데이트) `paper-list` ⭐1k · 📅2025-12
- 🟢 [awesome-AutoML](https://github.com/windmaple/awesome-AutoML) — AutoML 큐레이션 리스트 `awesome` ⭐938 · 📅2026-03
- 🟢 [awesome-ai-efficiency](https://github.com/PrunaAI/awesome-ai-efficiency) — AI 모델의 고속화, 소형화, 에너지 절감 기법 리스트 `awesome` ⭐222 · 📅2026-06
- 🟢 [Awesome-On-Device-AI-Systems](https://github.com/jeho-lee/Awesome-On-Device-AI-Systems) — 온디바이스 AI 시스템(추론 엔진/벤치마크/논문), 활발 `awesome` ⭐162 · 📅2026-06
- 🟢 [awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) — AI의 환경 영향을 평가 및 감축하는 Green AI 도구/논문의 대표 리스트 `awesome` ⭐114 · 📅2026-05
- 📑 [Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) — LLM 지식 증류 서베이 연동 논문 모음 `survey` ⭐1.3k · 📅2025-03
- 🟡 [awesome-ml-model-compression](https://github.com/cedrickchee/awesome-ml-model-compression) — 모델 압축 및 양자화 연구 논문, 도구, 학습 자료 `awesome` ⭐545 · 📅2024-09
- 🟡 [awesome-nas-papers](https://github.com/jackguagua/awesome-nas-papers) — Neural Architecture Search 논문 집약 리스트 `paper-list` ⭐405 · 📅2024-01
- 🔴 [deep-learning-model-convertor](https://github.com/ysh329/deep-learning-model-convertor) — 서로 다른 딥러닝 프레임워크 간의 모델 변환 도구 일람 `awesome` ⭐3.2k · 📅2023-06
- 🔴 [Awesome-Knowledge-Distillation](https://github.com/FLHonker/Awesome-Knowledge-Distillation) — 지식 증류 논문을 분류 정리(2014-2021) `paper-list` ⭐2.7k · 📅2023-05
- 🔴 [Awesome-AutoDL](https://github.com/D-X-Y/Awesome-AutoDL) — 자동 딥러닝(AutoDL) 리소스와 상세 분석 `awesome` ⭐2.3k · 📅2022-09
- 🔴 [awesome-emdl](https://github.com/csarron/awesome-emdl) — 임베디드 및 모바일 딥러닝 논문/라이브러리/도구 모음 `awesome` ⭐769 · 📅2023-03
- 🔴 [awesome-edge-machine-learning](https://github.com/Bisonai/awesome-edge-machine-learning) — 엣지 머신러닝 논문, 추론 엔진, 과제, 도서를 망라 `awesome` ⭐280 · 📅2023-02
- 🔴 [awesome-transformer-search](https://github.com/automl/awesome-transformer-search) — Transformer와 NAS를 결합한 리소스 리스트 `awesome` ⭐270 · 📅2023-06
- 🔴 [awesome-model-compression](https://github.com/ChanChiChoi/awesome-model-compression) — 모델 압축(구조, 증류, 이진화, 양자화, 가지치기) 논문 모음 `paper-list` ⭐166 · 📅2023-02
- 🔴 [NASPapers](https://github.com/NiuTrans/NASPapers) — Neural Architecture Search(NAS) 논문 리스트 `paper-list` ⭐135 · 📅2021-09
- 🔴 [awesome-compression-papers](https://github.com/chenbong/awesome-compression-papers) — 압축 및 고속화(가지치기, 양자화, 증류, 저랭크 분해) 논문 모음 `paper-list` ⭐25 · 📅2020-10
- 🔴 [awesome-architecture-search](https://github.com/chenyaofo/awesome-architecture-search) — NAS 동향을 최신 추적하는 논문 리스트 `paper-list` ⭐9 · 📅2022-05
- 🔴 [Awesome-NAS](https://github.com/Openning07/Awesome-NAS) — Neural Architecture Search(NAS) 리소스의 큐레이션 `awesome` ⭐1 · 📅2020-04

## 🔐 연합학습 / 프라이버시

- 🟢 [Awesome-Differential-Privacy-and-Meachine-Learning](https://github.com/JeffffffFu/Awesome-Differential-Privacy-and-Meachine-Learning) — 차분 프라이버시를 활용한 연합 학습 및 ML 논문과 구현 `paper-list` ⭐386 · 📅2025-09
- 🟢 [Awesome-ML-SP-Papers](https://github.com/gnipping/Awesome-ML-SP-Papers) — 보안 톱4 학회의 ML Security & Privacy 논문 모음 `paper-list` ⭐355 · 📅2025-11
- 🟡 [awesome-federated-learning](https://github.com/poga/awesome-federated-learning) — 연합 학습과 ML에서의 프라이버시 리소스 모음 `awesome` ⭐546 · 📅2024-06
- 🟡 [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper) — 연합 학습 시스템 및 프레임워크 논문 리스트 `paper-list` ⭐75 · 📅2024-02
- 🔴 [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning) — FedML 연계 연합 학습 연구 및 프로덕션 통합 리스트 `paper-list` ⭐2k · 📅2022-09
- 🔴 [awesome-secure-federated-learning-papers](https://github.com/csl-cqu/awesome-secure-federated-learning-papers) — 안전한 연합 학습(공격, 방어, 기울기 역전) 논문 모음 `paper-list` ⭐26 · 📅2023-03
- 🔴 [awesome-federated-learning](https://github.com/Willjay5991/awesome-federated-learning) — 연합 학습 논문, 기사, 프레임워크, 강의 자료 `awesome` ⭐2 · 📅2020-08

## ♻️ 지속 학습(Continual Learning)

- 🟢 [Awesome-Incremental-Learning](https://github.com/xialeiliu/Awesome-Incremental-Learning) — 증분 학습, 지속 학습, 파국적 망각 주요 학회 논문 모음 `paper-list` ⭐4.5k · 📅2026-06
- 📑 [awesome-lifelong-learning-methods-for-llm](https://github.com/zzz47zzz/awesome-lifelong-learning-methods-for-llm) — LLM의 평생 학습에 관한 서베이 및 논문 모음 `survey` ⭐164 · 📅2025-05
- 🟡 [Best-Incremental-Learning](https://github.com/Vision-Intelligence-and-Robots-Group/Best-Incremental-Learning) — 증분, 지속, 평생 학습 리포지토리 `paper-list` ⭐608 · 📅2024-05
- 🟡 [Awesome-Continual-Learning](https://github.com/feifeiobama/Awesome-Continual-Learning) — 지속 학습 논문과 BibTeX 항목의 큐레이션 리스트 `paper-list` ⭐203 · 📅2024-10
- 🟡 [Awesome-Continual-Learning](https://github.com/lywang3081/Awesome-Continual-Learning) — 지속 학습 서베이 연동 논문 리스트와 유용한 리소스 `paper-list` ⭐108 · 📅2024-02
- 🔴 [awesome-lifelong-continual-learning](https://github.com/prprbr/awesome-lifelong-continual-learning) — 평생/지속 학습 논문, 블로그, 데이터셋, 소프트웨어 리스트 `awesome` ⭐298 · 📅2021-03
- 🔴 [LLM-Continual-Learning-Papers](https://github.com/AGI-Edgerunners/LLM-Continual-Learning-Papers) — LLM의 지속 학습(continual learning) 필독 논문 모음 `paper-list` ⭐150 · 📅2023-11

## 🖥️ ML 시스템 / 학습·추론 인프라 / 데이터

- 🟢 [AI-Infra-from-Zero-to-Hero](https://github.com/HuaizhengZhang/AI-Infra-from-Zero-to-Hero) — AI 시스템 논문과 산업 실무(OSDI/NSDI/MLSys 등, LLM·GenAI 포함)를 모은 대표작 `awesome` ⭐4.1k · 📅2025-07
- 🟢 [Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data) — LLM을 통한 합성 데이터 생성의 리딩 리스트(활발) `paper-list` ⭐1.5k · 📅2025-06
- 🟢 [rtdl](https://github.com/yandex-research/rtdl) — 테이블 데이터 딥러닝 논문과 패키지 모음(Yandex Research) `paper-list` ⭐1.1k · 📅2026-04
- 🟢 [ML4DB-paper-list](https://github.com/LumingSun/ML4DB-paper-list) — DB 시스템을 AI로 강화하는 논문 모음(학습형 인덱스, 쿼리 최적화) `paper-list` ⭐775 · 📅2026-04
- 🟢 [ml-systems-papers](https://github.com/byungsoo-oh/ml-systems-papers) — ML 시스템 분야의 논문을 체계적으로 모은 컬렉션 `paper-list` ⭐623 · 📅2026-02
- 🟢 [awesome-AI-system](https://github.com/lambda7xx/awesome-AI-system) — AI 시스템 논문과 그 코드를 정리한 리스트 `paper-list` ⭐367 · 📅2026-05
- 🟢 [awesome-vector-database](https://github.com/dangkhoasdc/awesome-vector-database) — 고차원 벡터 검색 및 데이터베이스 관련 엄선 리스트(활발) `awesome` ⭐354 · 📅2026-06
- 🟢 [Awesome-LLM-Inference-Engine](https://github.com/sihyeong/Awesome-LLM-Inference-Engine) — LLM 추론 최적화 기법을 레이턴시/스루풋/메모리별로 분류한 망라적 정리 `survey` ⭐218 · 📅2026-04
- 🟢 [Tabular-Survey](https://github.com/LAMDA-Tabular/Tabular-Survey) — "Representation Learning for Tabular Data" 서베이 부속 리스트 `survey` ⭐127 · 📅2026-06
- 🟢 [awesome-ai4db-paper](https://github.com/Wind-Gone/awesome-ai4db-paper) — AI4DB 논문 모음(학습형 인덱스, 카디널리티 추정, 학습형 쿼리 최적화, LLM×DB) `paper-list` ⭐113 · 📅2026-04
- 🟡 [data-augmentation-review](https://github.com/AgaMiko/data-augmentation-review) — 데이터 증강의 기법, 라이브러리, 논문을 폭넓게 모은 리뷰 `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-vector-search](https://github.com/currentslab/awesome-vector-search) — 벡터 검색의 라이브러리, 서비스, 논문 모음(Faiss, Annoy 등) `awesome` ⭐1.6k · 📅2024-08
- 🟡 [awesome-distributed-ml](https://github.com/Shenggan/awesome-distributed-ml) — 대규모 모델의 분산 학습 및 추론에 관한 프로젝트와 논문의 엄선 리스트 `awesome` ⭐279 · 📅2024-10
- 🟡 [awesome-synthetic-data](https://github.com/statice/awesome-synthetic-data) — OSS/상용 합성 데이터 도구 엄선 리스트(SDV 등) `awesome` ⭐260 · 📅2024-01
- 🟡 [Awesome-LLM-Inference](https://github.com/DefTruth/Awesome-LLM-Inference) — LLM/VLM 추론 최적화(FlashAttention, PagedAttention, MLA 등) 논문+코드 모음 `paper-list` ⭐16 · 📅2025-03
- 🔴 [awesome-data-augmentation](https://github.com/CrazyVertigo/awesome-data-augmentation) — 데이터 증강 기법(AugMix, CutMix 등)의 엄선 리스트 `awesome` ⭐797 · 📅2021-03
- 🔴 [awesome-dl-hw-resources](https://github.com/RaviVijay/awesome-dl-hw-resources) — 딥러닝용 하드웨어/칩 설계 리소스의 엄선 리스트 `awesome` ⭐59 · 📅2018-05
- 🔴 [awesome-ml-testing](https://github.com/yqtian-se/awesome-ml-testing) — ML/딥러닝 시스템의 테스트에 관한 논문 및 도구 모음 `paper-list` ⭐47 · 📅2021-10
- 🔴 [Awesome-MLSys](https://github.com/dujiangsu/Awesome-MLSys) — 대규모 모델 추론을 중심으로 한 MLSys 분야의 학술 논문 모음 `paper-list` ⭐6 · 📅2023-09

## 🛠️ MLOps / 데이터 중심 AI

- 🟢 [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) — ML의 배포, 모니터링, 스케일링용 OSS 라이브러리 리스트 `awesome` ⭐20.6k · 📅2026-06
- 🟢 [awesome-mlops](https://github.com/kelvins/awesome-mlops) — MLOps 도구의 큐레이션 리스트 `awesome` ⭐5.2k · 📅2026-04
- 🟢 [Awesome-Dataset-Distillation](https://github.com/Guang000/Awesome-Dataset-Distillation) — 기울기/분포 매칭, 생성 기법, 응용을 망라한 대표 리스트(매우 활발) `awesome` ⭐1.9k · 📅2026-06
- 🟢 [awesome-data-centric-ai](https://github.com/Data-Centric-AI-Community/awesome-data-centric-ai) — 데이터 중심 AI의 OSS, 튜토리얼, 연구 `awesome` ⭐351 · 📅2026-04
- 🟢 [awesome-ml-data-quality-papers](https://github.com/SJTU-DMTai/awesome-ml-data-quality-papers) — 데이터 평가, 데이터 귀속, 데이터 선정/프루닝/coreset을 망라 `paper-list` ⭐123 · 📅2026-06
- 🟡 [awesome-mlops](https://github.com/visenger/awesome-mlops) — MLOps 참고 문헌 및 리소스 모음 `awesome` ⭐13.9k · 📅2024-11
- 🟡 [awesome-data-labeling](https://github.com/HumanSignal/awesome-data-labeling) — 데이터 라벨링 도구를 엄선한 리스트 `awesome` ⭐4.3k · 📅2024-06
- 🟡 [data-centric-AI](https://github.com/daochenzha/data-centric-AI) — 데이터 중심 AI의 리소스 큐레이션 리스트 `awesome` ⭐1.1k · 📅2024-06
- 🟡 [data-centric-ai](https://github.com/HazyResearch/data-centric-ai) — 데이터 중심 AI 리소스 모음(Stanford HazyResearch) `awesome` ⭐1.1k · 📅2023-12
- 🟡 [Awesome-Coreset-Selection](https://github.com/PatrickZH/Awesome-Coreset-Selection) — coreset/subset 선택 및 data pruning 논문 모음 `awesome` ⭐184 · 📅2024-06
- 🔴 [releasing-research-code](https://github.com/paperswithcode/releasing-research-code) — ML 연구 코드 공개의 베스트 프랙티스(NeurIPS 2020 공식 권장) `awesome` ⭐2.9k · 📅2023-05
- 🔴 [awesome-open-data-centric-ai](https://github.com/Renumics/awesome-open-data-centric-ai) — 비구조화 데이터용 데이터 중심 AI의 OSS 도구 모음 `awesome` ⭐732 · 📅2023-11

## 📊 데이터셋 / 벤치마크

- 🟢 [Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) — LLM 평가의 도구, 벤치마크, 리더보드, 논문의 엄선 리스트 `awesome` ⭐644 · 📅2025-11
- 🟢 [Awesome-Datasets-Hub](https://github.com/ahammadmejbah/Awesome-Datasets-Hub) — 의료 AI, NLP, 멀티모달 등 LLM용 데이터셋 모음 `awesome` ⭐140 · 📅2026-06
- 🟢 [Awesome-LLM-Benchmark](https://github.com/SihyeongPark/Awesome-LLM-Benchmark) — 대규모 언어 모델용 벤치마크 일람 `awesome` ⭐12 · 📅2026-06
- 🟢 [awesome-llm-benchmarks](https://github.com/BenchGecko/awesome-llm-benchmarks) — LLM/AI 모델의 벤치마크, 데이터셋, 리더보드 모음 `awesome` ⭐1 · 📅2026-03
- 🟡 [llm_benchmarks](https://github.com/leobeeson/llm_benchmarks) — LLM 평가용 벤치마크 및 데이터셋 컬렉션 `awesome` ⭐570 · 📅2024-07

## 공식 프로시딩·논문 포털 (비-GitHub)

GitHub 리포지토리가 아니라 본 리스트에는 포함하지 않았지만, 일차 자료로 유용한 공식 논문 포털입니다.

- [CVF Open Access](https://openaccess.thecvf.com/menu) — CVPR/ICCV/WACV 공식 오픈액세스 논문
- [ECVA / ECCV Papers](https://www.ecva.net/papers.php) — ECCV 공식 논문(ECVA 오픈액세스)
- [Ke-Sen Huang's Home Page](https://kesen.realtimerendering.com/) — SIGGRAPH 등 그래픽스 논문 링크의 정평난 모음
- [OpenReview](https://openreview.net/) — ICLR/NeurIPS 등 리뷰·채택 논문
- [ACL Anthology](https://aclanthology.org/) — NLP(ACL/EMNLP/NAACL 등) 공식 논문 아카이브
- [PMLR](https://proceedings.mlr.press/) — ICML/AISTATS/CoLT 등 공식 프로시딩
- [NeurIPS Proceedings](https://papers.nips.cc/) — NeurIPS 공식 프로시딩
- [Papers with Code](https://paperswithcode.com/) — 논문 + 코드 + SOTA 리더보드
- [DBLP](https://dblp.org/) — 컴퓨터과학 논문 서지 데이터베이스
- [arXiv](https://arxiv.org/) — 프리프린트 서버(cs.LG/cs.CV/cs.CL 등)

---

## 이 리포지토리에 대하여

- 분야별 조사 에이전트가 GitHub을 가로질러 조사하고, 실재가 확인된 리포지토리만 수록했습니다.
- star 수·마지막 업데이트는 생성 시점의 GitHub API 실값이며, 신선도 마커로 노후화를 판별할 수 있습니다.
- 모든 링크는 리다이렉트 해소 후의 정규 URL로 통일했습니다.
- ⭐star·📅업데이트는 `./scripts/refresh.sh` 또는 GitHub Actions(주간)로 재생성·자동 갱신할 수 있습니다.

## 라이선스

본 리스트(큐레이션)는 [CC0 1.0](LICENSE)(퍼블릭 도메인)으로 제공합니다. 링크된 리포지토리는 각자의 라이선스를 따릅니다.

Generated with Claude Code
