# A-Review-for-remote-sensing-vision-language-models
This is a repository for ...
## Overleaf
https://www.overleaf.com/5469324254jsdvcqwcsmzz#0edfd1

## Table of Contents
- [A-Review-for-remote-sensing-vision-language-models](#a-review-for-remote-sensing-vision-language-models)
  - [Overleaf](#overleaf)
  - [Table of Contents](#table-of-contents)
- [README](#readme)
- [dataset](#dataset)
  - [图像](#图像)
  - [图像、文本](#图像文本)
  - [视频](#视频)
  - [视频、文本](#视频文本)
- [paper](#paper)
  - [Pretrain](#pretrain)
  - [Other](#other)
  - [VLM](#vlm)
  - [nan](#nan)
  - [MLLM](#mllm)
  - [Agent](#agent)

# README

# dataset

## 图像

| Paper Name | Categories | Detailed Info |
|------------|------------|---------------|
| TAS | 检测 | [Link](https://irip-buaa.github.io/posts/TAS) |
| OIRDS | 检测 | [Link](https://irip-buaa.github.io/posts/OIRDS) |
| SZTAKI-INRIA AirChange | 变化检测 | [Link](https://irip-buaa.github.io/posts/SZTAKI-INRIA-AirChange) |
| UCMerced_LandUse | 分类 | [Link](https://irip-buaa.github.io/posts/UCMerced_LandUse) |
| ISPRS Potsdam | 分割 | [Link](https://irip-buaa.github.io/posts/ISPRS-Potsdam) |
| ISPRS Vaihingen | 分割 | [Link](https://irip-buaa.github.io/posts/ISPRS-Vaihingen) |
| WHU RS19 | 分类 | [Link](https://irip-buaa.github.io/posts/WHU-RS19) |
| Massachusetts Builds | 分割 | [Link](https://irip-buaa.github.io/posts/Massachusetts-Builds) |
| Massachusetts Roads | 分割 | [Link](https://irip-buaa.github.io/posts/Massachusetts-Roads) |
| SPARCS | 分割 | [Link](https://irip-buaa.github.io/posts/SPARCS) |
| RSSCN7 | 分类 | [Link](https://irip-buaa.github.io/posts/RSSCN7) |
| SAT | 分类 | [Link](https://irip-buaa.github.io/posts/SAT) |
| VEDAI | 检测 | [Link](https://irip-buaa.github.io/posts/VEDAI) |
| DLR3k | 检测 | [Link](https://irip-buaa.github.io/posts/DLR3k) |
| HRSC2016 | 检测 | [Link](https://irip-buaa.github.io/posts/HRSC2016) |
| NWPU-RESISC45 | 分类 | [Link](https://irip-buaa.github.io/posts/NWPU-RESISC45) |
| RS_C11 | 分类 | [Link](https://irip-buaa.github.io/posts/RS_C11) |
| SIRI-WHU | 分类 | [Link](https://irip-buaa.github.io/posts/SIRI-WHU) |
| Aerial to Map | 图像生成 | [Link](https://irip-buaa.github.io/posts/Aerial-to-Map) |
| AID | 分类 | [Link](https://irip-buaa.github.io/posts/AID) |
| AIST Building Change Detection(ABCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/AIST-Building-Change-Detection(ABCD)) |
| CITY-OSM | 分割 | [Link](https://irip-buaa.github.io/posts/CITY-OSM) |
| Dstl Satellite Imagery Feature Detection | 分割 | [Link](https://irip-buaa.github.io/posts/Dstl-Satellite-Imagery-Feature-Detection) |
| OpenSARShip | 检测 | [Link](https://irip-buaa.github.io/posts/OpenSARShip) |
| RSD46-WHU | 分类 | [Link](https://irip-buaa.github.io/posts/RSD46-WHU) |
| RSI-CB | 分类 | [Link](https://irip-buaa.github.io/posts/RSI-CB) |
| SateHaze1k | 图像生成 | [Link](https://irip-buaa.github.io/posts/SateHaze1k) |
| TGRS-HRRSD | 检测 | [Link](https://irip-buaa.github.io/posts/TGRS-HRRSD) |
| 2018 Open AI Tanzania Building Footprint | 分割 | [Link](https://irip-buaa.github.io/posts/2018-Open-AI-Tanzania-Building-Footprint) |
| Aeroscapes | 分割 | [Link](https://irip-buaa.github.io/posts/Aeroscapes) |
| AIRS | 分割 | [Link](https://irip-buaa.github.io/posts/AIRS) |
| CDD Dataset (season-varying) | 变化检测 | [Link](https://irip-buaa.github.io/posts/CDD-Dataset-(season-varying)) |
| DeepGlobe Land Cover Classificat | 分割 | [Link](https://irip-buaa.github.io/posts/DeepGlobe-Land-Cover-Classificat) |
| DeepGlobe Road Detection Challen | 分割 | [Link](https://irip-buaa.github.io/posts/DeepGlobe-Road-Detection-Challen) |
| DLRSD | 分割 | [Link](https://irip-buaa.github.io/posts/DLRSD) |
| DOTA1.0 | 检测 | [Link](https://irip-buaa.github.io/posts/DOTA1.0) |
| EuroSAT | 分类 | [Link](https://irip-buaa.github.io/posts/EuroSAT) |
| fMoW | 检测 | [Link](https://irip-buaa.github.io/posts/fMoW) |
| ITCVD | 检测 | [Link](https://irip-buaa.github.io/posts/ITCVD) |
| LEVIR | 检测 | [Link](https://irip-buaa.github.io/posts/LEVIR) |
| Mapping Challenge | 分割 | [Link](https://irip-buaa.github.io/posts/Mapping-Challenge) |
| MASATI | 检测 | [Link](https://irip-buaa.github.io/posts/MASATI) |
| Onera Satellite Change Detection (OSCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/Onera-Satellite-Change-Detection-(OSCD)) |
| PatternNet | 分类 | [Link](https://irip-buaa.github.io/posts/PatternNet) |
| RIT-18 | 分割 | [Link](https://irip-buaa.github.io/posts/RIT-18) |
| Urban Drone Dataset(UDD) | 分割 | [Link](https://irip-buaa.github.io/posts/Urban-Drone-Dataset(UDD)) |
| VisDrone2019-DET | 检测 | [Link](https://irip-buaa.github.io/posts/VisDrone2019-DET) |
| WHDLD | 分割 | [Link](https://irip-buaa.github.io/posts/WHDLD) |
| WHU Building Change Detection Dataset | 变化检测 | [Link](https://irip-buaa.github.io/posts/WHU-Building-Change-Detection-Dataset) |
| WHU_GID中的Fine部分 | 分割 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Fine部分) |
| WHU_GID中的Large-scale部分 | 分割 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Large-scale部分) |
| WHU_GID中的secenClass部分 | 分类 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的secenClass部分) |
| xView | 检测 | [Link](https://irip-buaa.github.io/posts/xView) |
| 38-Cloud | 分割 | [Link](https://irip-buaa.github.io/posts/38-Cloud) |
| Bijie Landslide Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/Bijie-Landslide-Dataset) |
| Bridge Dataset | 检测 | [Link](https://irip-buaa.github.io/posts/Bridge-Dataset) |
| Change Detection Dataset(CDD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/Change-Detection-Dataset(CDD)) |
| DOTA1.5 | 检测 | [Link](https://irip-buaa.github.io/posts/DOTA1.5) |
| DroneDeploy | 分割 | [Link](https://irip-buaa.github.io/posts/DroneDeploy) |
| DSIFN Dataset | 变化检测 | [Link](https://irip-buaa.github.io/posts/DSIFN-Dataset) |
| GF2 Dataset for 3DFGC | 分割 | [Link](https://irip-buaa.github.io/posts/GF2-Dataset-for-3DFGC) |
| High Resolution Semantic Change (HRSCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/High-Resolution-Semantic-Change-(HRSCD)) |
| iSAID | 检测 | [Link](https://irip-buaa.github.io/posts/iSAID) |
| Multi-temporal Scene WuHan (MtS-WH) | 变化检测 | [Link](https://irip-buaa.github.io/posts/Multi-temporal-Scene-WuHan-(MtS-WH)) |
| OPTIMAL-31 | 分类 | [Link](https://irip-buaa.github.io/posts/OPTIMAL-31) |
| ORSSD | 分割 | [Link](https://irip-buaa.github.io/posts/ORSSD) |
| RoadTracer | 分割 | [Link](https://irip-buaa.github.io/posts/RoadTracer) |
| Semantic Drone Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/Semantic-Drone-Dataset) |
| SEN12MS | 分割 | [Link](https://irip-buaa.github.io/posts/SEN12MS) |
| WHU Building Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHU-Building-Dataset) |
| 95-Cloud | 分割 | [Link](https://irip-buaa.github.io/posts/95-Cloud) |
| BDCI2020 | 分割 | [Link](https://irip-buaa.github.io/posts/BDCI2020) |
| BH-POOLS | 分割 | [Link](https://irip-buaa.github.io/posts/BH-POOLS) |
| BH-WATERTANKS | 分割 | [Link](https://irip-buaa.github.io/posts/BH-WATERTANKS) |
| Change-Detection-dataset-for-High-resolution-Satellite-Image | 变化检测 | [Link](https://irip-buaa.github.io/posts/Change-Detection-dataset-for-High-resolution-Satellite-Image) |
| Continual Learning Benchmark for Remote | 分类 | [Link](https://irip-buaa.github.io/posts/Continual-Learning-Benchmark-for-Remote) |
| DroneCrowd | 检测 | [Link](https://irip-buaa.github.io/posts/DroneCrowd) |
| EORSSD | 分割 | [Link](https://irip-buaa.github.io/posts/EORSSD) |
| HRSID | 检测 | [Link](https://irip-buaa.github.io/posts/HRSID) |
| landcover_ai | 分割 | [Link](https://irip-buaa.github.io/posts/landcover_ai) |
| LEVIR-CD | 变化检测 | [Link](https://irip-buaa.github.io/posts/LEVIR-CD) |
| MLRSNet | 分类 | [Link](https://irip-buaa.github.io/posts/MLRSNet) |
| Multi-View Datasets中的AiRound部分 | 分类 | [Link](https://irip-buaa.github.io/posts/Multi-View-Datasets中的AiRound部分) |
| Multi-View Datasets中的CV-BrCT部分 | 分类 | [Link](https://irip-buaa.github.io/posts/Multi-View-Datasets中的CV-BrCT部分) |
| RarePlanes | 检测 | [Link](https://irip-buaa.github.io/posts/RarePlanes) |
| SEmantic Change detectiON Data(SECOND) | 变化检测 | [Link](https://irip-buaa.github.io/posts/SEmantic-Change-detectiON-Data(SECOND)) |
| SenseEarth ChangeDetection | 变化检测 | [Link](https://irip-buaa.github.io/posts/SenseEarth-ChangeDetection) |
| Sentinel-2 Cloud Mask Catalogue | 分割 | [Link](https://irip-buaa.github.io/posts/Sentinel-2-Cloud-Mask-Catalogue) |
| Sentinel-2 Multitemporal Cities Pairs | 变化检测 | [Link](https://irip-buaa.github.io/posts/Sentinel-2-Multitemporal-Cities-Pairs) |
| UAVid | 分割 | [Link](https://irip-buaa.github.io/posts/UAVid) |
| WHU Cloud Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHU-Cloud-Dataset) |
| WHU Multi-view Dataset | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHU-Multi-view-Dataset) |
| WHU Stereo Dataset | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHU-Stereo-Dataset) |
| xBD | 变化检测 | [Link](https://irip-buaa.github.io/posts/xBD) |
| 全国人工智能大赛AI遥感影像 | 分割 | [Link](https://irip-buaa.github.io/posts/全国人工智能大赛AI遥感影像) |
| CASIA-aircraft | 检测 | [Link](https://irip-buaa.github.io/posts/CASIA-aircraft) |
| CASIA-Ship | 检测 | [Link](https://irip-buaa.github.io/posts/CASIA-Ship) |
| DOTA2.0 | 检测 | [Link](https://irip-buaa.github.io/posts/DOTA2.0) |
| FAIR1M | 检测 | [Link](https://irip-buaa.github.io/posts/FAIR1M) |
| LEVIR-CD2 | 变化检测 | [Link](https://irip-buaa.github.io/posts/LEVIR-CD2) |
| LoveDA | 分割 | [Link](https://irip-buaa.github.io/posts/LoveDA) |
| MillionAID | 分类 | [Link](https://irip-buaa.github.io/posts/MillionAID) |
| NaSC-TG2 | 分类 | [Link](https://irip-buaa.github.io/posts/NaSC-TG2) |
| S2Looking | 变化检测 | [Link](https://irip-buaa.github.io/posts/S2Looking) |
| SeCo | 单模态预训练 | [Link](https://irip-buaa.github.io/posts/SeCo) |
| Sun Yat-Sen University (SYSU)-CD | 变化检测 | [Link](https://irip-buaa.github.io/posts/Sun-Yat-Sen-University-(SYSU)-CD) |
| TG1HRSSC | 分类 | [Link](https://irip-buaa.github.io/posts/TG1HRSSC) |
| VISO-Detection | 检测 | [Link](https://irip-buaa.github.io/posts/VISO-Detection) |
| WHU TCL SatMVS dataset1.0 | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHU-TCL-SatMVS-dataset1.0) |
| WHU TCL SatMVS dataset2.0 | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHU-TCL-SatMVS-dataset2.0) |
| 船只智能检测-训练数据集 | 检测 | [Link](https://irip-buaa.github.io/posts/船只智能检测-训练数据集) |
| 飞机目标识别-训练数据集 | 检测 | [Link](https://irip-buaa.github.io/posts/飞机目标识别-训练数据集) |
| MiniFrance-DFC22 | 分割 | [Link](https://irip-buaa.github.io/posts/MiniFrance-DFC22) |
| SAMRS | 分割 | [Link](https://irip-buaa.github.io/posts/SAMRS) |
| TOV-RS-balanced | 分类 | [Link](https://irip-buaa.github.io/posts/TOV-RS-balanced) |
| CACo | 单模态预训练 | [Link](https://irip-buaa.github.io/posts/CACo) |
| GEO-Bench | 评估 | [Link](https://irip-buaa.github.io/posts/GEO-Bench) |
| SATIN | 分类 | [Link](https://irip-buaa.github.io/posts/SATIN) |
| SatlasPretrain | 分类 | [Link](https://irip-buaa.github.io/posts/SatlasPretrain) |
| WHU-Mix (vector) building dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHU-Mix-(vector)-building-dataset) |
| Constellation | 检测 | [Link](https://irip-buaa.github.io/posts/Constellation) |
| Earth Parser Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/Earth-Parser-Dataset) |
| EarthView | 单模态预训练 | [Link](https://irip-buaa.github.io/posts/EarthView) |
| GeoPile-2 | 多模态预训练 | [Link](https://irip-buaa.github.io/posts/GeoPile-2) |
| HSODBIT-V1 | 检测 | [Link](https://irip-buaa.github.io/posts/HSODBIT-V1) |
| SARDet-100K | 检测 | [Link](https://irip-buaa.github.io/posts/SARDet-100K) |

## 图像、文本

| Paper Name | Categories | Detailed Info |
|------------|------------|---------------|
| Sydney-Captions | 图文对 | [Link](https://irip-buaa.github.io/posts/Sydney-Captions) |
| UCM-Captions | 图文对 | [Link](https://irip-buaa.github.io/posts/UCM-Captions) |
| RSICD | 图文对 | [Link](https://irip-buaa.github.io/posts/RSICD) |
| RSVQA-HR | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA-HR) |
| RSVQA-LR | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA-LR) |
| TextRS | 图文对 | [Link](https://irip-buaa.github.io/posts/TextRS) |
| BigEarthNet-MM | 图文对 | [Link](https://irip-buaa.github.io/posts/BigEarthNet-MM) |
| FloodNet | VQA | [Link](https://irip-buaa.github.io/posts/FloodNet) |
| RSIVQA | VQA | [Link](https://irip-buaa.github.io/posts/RSIVQA) |
| RSVQA×BEN | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA×BEN) |
| CDVQA | VQA | [Link](https://irip-buaa.github.io/posts/CDVQA) |
| GeoVG | 视觉定位 | [Link](https://irip-buaa.github.io/posts/GeoVG) |
| LEVIR-CC | 图文对 | [Link](https://irip-buaa.github.io/posts/LEVIR-CC) |
| NWPU-Captions | 图文对 | [Link](https://irip-buaa.github.io/posts/NWPU-Captions) |
| RSITMD | 图文对 | [Link](https://irip-buaa.github.io/posts/RSITMD) |
| SSL4EO-S12 | 多模态预训练 | [Link](https://irip-buaa.github.io/posts/SSL4EO-S12) |
| VQA-TextRS | VQA | [Link](https://irip-buaa.github.io/posts/VQA-TextRS) |
| DIOR_RSVG | 视觉定位 | [Link](https://irip-buaa.github.io/posts/DIOR_RSVG) |
| LAION-5B | 图文对 | [Link](https://irip-buaa.github.io/posts/LAION-5B) |
| OPT-RSVG | 视觉定位 | [Link](https://irip-buaa.github.io/posts/OPT-RSVG) |
| RS5M | 图文对 | [Link](https://irip-buaa.github.io/posts/RS5M) |
| RSICap | 图文对 | [Link](https://irip-buaa.github.io/posts/RSICap) |
| RSIEval | 图文对 | [Link](https://irip-buaa.github.io/posts/RSIEval) |
| SkyScript | 图文对 | [Link](https://irip-buaa.github.io/posts/SkyScript) |
| ChatEarthNet | 图文对 | [Link](https://irip-buaa.github.io/posts/ChatEarthNet) |
| MMEarth | 多模态预训练 | [Link](https://irip-buaa.github.io/posts/MMEarth) |

## 视频

| Paper Name | Categories | Detailed Info |
|------------|------------|---------------|
| UAV123 | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/UAV123) |
| VisDrone2019-MOT | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/VisDrone2019-MOT) |
| VisDrone2019-SOT | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/VisDrone2019-SOT) |
| VisDrone2019-VID | 检测 | [Link](https://irip-buaa.github.io/posts/VisDrone2019-VID) |
| 地空背景下红外图像弱小飞机目标检测跟踪数据集 | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/地空背景下红外图像弱小飞机目标检测跟踪数据集) |
| VISO-MOT | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/VISO-MOT) |
| VISO-SOT | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/VISO-SOT) |
| 复杂背景下红外弱小运动目标检测数据集 | 目标跟踪 | [Link](https://irip-buaa.github.io/posts/复杂背景下红外弱小运动目标检测数据集) |

## 视频、文本

| Paper Name | Categories | Detailed Info |
|------------|------------|---------------|
| CapERA | 图文对 | [Link](https://irip-buaa.github.io/posts/CapERA) |

# paper

## Pretrain

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Functional Map of the World | CVPR 2018 | [Link](https://irip-buaa.github.io/posts/Functional-Map-of-the-World) |
| BIGEARTHNET A LARGE-SCALE BENCHMARK ARCHIVE FOR REMOTE SENSINGIMAGE UNDERSTANDING | IEEE International Geoscience and Remote Sensing Symposium 2019 | [Link](https://irip-buaa.github.io/posts/BIGEARTHNET-A-LARGE-SCALE-BENCHMARK-ARCHIVE-FOR-REMOTE-SENSINGIMAGE-UNDERSTANDING) |
| Tile2Vec Unsupervised representation learning for spatially distributed data | AAAI 2019 | [Link](https://irip-buaa.github.io/posts/Tile2Vec-Unsupervised-representation-learning-for-spatially-distributed-data) |
| Remote Sensing Image Scene Classification with Self-Supervised Paradigm under Limited Labeled Samples | IEEE Geoscience and Remote Sensing Letters 2020 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-Image-Scene-Classification-with-Self-Supervised-Paradigm-under-Limited-Labeled-Samples) |
| Geography-aware self-supervised learning | ICCV 2021 | [Link](https://irip-buaa.github.io/posts/Geography-aware-self-supervised-learning) |
| On Creating Benchmark Dataset for Aerial Image Interpretation Reviews, Guidances, and Million-AID | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2021 | [Link](https://irip-buaa.github.io/posts/On-Creating-Benchmark-Dataset-for-Aerial-Image-Interpretation-Reviews,-Guidances,-and-Million-AID) |
| Seasonal ContrastUnsupervised Pre-Training from Uncurated Remote Sensing Data | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/Seasonal-ContrastUnsupervised-Pre-Training-from-Uncurated-Remote-Sensing-Data) |
| Self-Supervised Learning of Remote Sensing Scene Representations Using Contrastive Multiview Coding | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Learning-of-Remote-Sensing-Scene-Representations-Using-Contrastive-Multiview-Coding) |
| Advancing plain vision transformer toward remote sensing foundation model | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Advancing-plain-vision-transformer-toward-remote-sensing-foundation-model) |
| Consecutive Pre-Training A Knowledge Transfer Learning Strategy with Relevant Unlabeled Data for Remote Sensing Domain | Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Consecutive-Pre-Training-A-Knowledge-Transfer-Learning-Strategy-with-Relevant-Unlabeled-Data-for-Remote-Sensing-Domain) |
| Geographical Knowledge-Driven RepresentationLearning for Remote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Geographical-Knowledge-Driven-RepresentationLearning-for-Remote-Sensing-Images) |
| Global and Local Contrastive Self-Supervised Learning for Semantic Segmentation of HR Remote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Global-and-Local-Contrastive-Self-Supervised-Learning-for-Semantic-Segmentation-of-HR-Remote-Sensing-Images) |
| SatMAE Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery | NeurIPS 2022 | [Link](https://irip-buaa.github.io/posts/SatMAE-Pre-training-Transformers-for-Temporal-and-Multi-Spectral-Satellite-Imagery) |
| Self-Supervised Learning for Invariant Representations from Multi-Spectral and SAR Images | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Learning-for-Invariant-Representations-from-Multi-Spectral-and-SAR-Images) |
| Self-Supervised Material and Texture Representation Learning for Remote Sensing Tasks | CVPR 2022 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Material-and-Texture-Representation-Learning-for-Remote-Sensing-Tasks) |
| Self-supervised vision transformers for joint sar-optical representation learning | Arxiv 2022 | [Link](https://irip-buaa.github.io/posts/Self-supervised-vision-transformers-for-joint-sar-optical-representation-learning) |
| Semantic segmentation of remote sensing images with self-supervised semantic-aware inpainting | IEEE Geoscience and Remote Sensing Letters 2022 | [Link](https://irip-buaa.github.io/posts/Semantic-segmentation-of-remote-sensing-images-with-self-supervised-semantic-aware-inpainting) |
| A billion-scale foundation model for remote sensing images | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/A-billion-scale-foundation-model-for-remote-sensing-images) |
| A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion | IGARSS 2023 | [Link](https://irip-buaa.github.io/posts/A-Self-Supervised-Cross-Modal-Remote-Sensing-Foundation-Model-with-Multi-Domain-Representation-and-Cross-Domain-Fusion) |
| An Empirical Study of Remote Sensing Pretraining | IEEE Transactions on Geoscience and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/An-Empirical-Study-of-Remote-Sensing-Pretraining) |
| Change-Aware Sampling and Contrastive Learning for Satellite Images | CVPR 2023 | [Link](https://irip-buaa.github.io/posts/Change-Aware-Sampling-and-Contrastive-Learning-for-Satellite-Images) |
| CMID A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/CMID-A-Unified-Self-Supervised-Learning-Framework-for-Remote-Sensing-Image-Understanding) |
| CROMA Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/CROMA-Remote-Sensing-Representations-with-Contrastive-Radar-Optical-Masked-Autoencoders) |
| Cross-Scale MAE A Tale of Multiscale Exploitation in Remote Sensing | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/Cross-Scale-MAE-A-Tale-of-Multiscale-Exploitation-in-Remote-Sensing) |
| CtxMIM Context-Enhanced Masked Image Modeling for Remote Sensing Image Understanding | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/CtxMIM-Context-Enhanced-Masked-Image-Modeling-for-Remote-Sensing-Image-Understanding) |
| DeCUR decoupling common & unique representations for multimodal self-supervision | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DeCUR-decoupling-common-&-unique-representations-for-multimodal-self-supervision) |
| DINO-MC Self-supervised Contrastive Learning for Remote Sensing Imagery with Multi-sized Local Crops | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DINO-MC-Self-supervised-Contrastive-Learning-for-Remote-Sensing-Imagery-with-Multi-sized-Local-Crops) |
| EarthPT a foundation model for Earth Observation | NeurIPS CCAI workshop 2023 | [Link](https://irip-buaa.github.io/posts/EarthPT-a-foundation-model-for-Earth-Observation) |
| Feature Guided Masked Autoencoder for Self-supervised Learning in Remote Sensing | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Feature-Guided-Masked-Autoencoder-for-Self-supervised-Learning-in-Remote-Sensing) |
| FoMo-Bench a multi-modal, multi-scale and multi-task Forest Monitoring Benchmark for remote sensing foundation models | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/FoMo-Bench-a-multi-modal,-multi-scale-and-multi-task-Forest-Monitoring-Benchmark-for-remote-sensing-foundation-models) |
| Foundation Models for Generalist Geospatial Artificial Intelligence | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Foundation-Models-for-Generalist-Geospatial-Artificial-Intelligence) |
| Lightweight, Pre-trained Transformers for Remote Sensing Timeseries | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Lightweight,-Pre-trained-Transformers-for-Remote-Sensing-Timeseries) |
| Multi Modal Multi Objective Contrastive Learning for Sentinel 1-2 Imagery | CVPRW 2023 | [Link](https://irip-buaa.github.io/posts/Multi-Modal-Multi-Objective-Contrastive-Learning-for-Sentinel-1-2-Imagery) |
| Predicting Gradient is Better Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Predicting-Gradient-is-Better-Exploring-Self-Supervised-Learning-for-SAR-ATR-with-a-Joint-Embedding-Predictive-Architecture) |
| RingMo-lite A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RingMo-lite-A-Remote-Sensing-Multi-task-Lightweight-Network-with-CNN-Transformer-Hybrid-Framework) |
| Rsprompter Learning to prompt for remote sensing instance segmentation based on visual foundation model | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Rsprompter-Learning-to-prompt-for-remote-sensing-instance-segmentation-based-on-visual-foundation-model) |
| SatlasPretrain A Large-Scale Dataset for Remote Sensing Image Understanding | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/SatlasPretrain-A-Large-Scale-Dataset-for-Remote-Sensing-Image-Understanding) |
| Scale-MAE A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Geospatial-Representation-Learning) |
| TOV The original vision model for optical remote sensing image understanding via self-supervised learning | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/TOV-The-original-vision-model-for-optical-remote-sensing-image-understanding-via-self-supervised-learning) |
| TOV The Original Vision Model for Optical Remote Sensing Image Understanding via Self-Supervised Learning | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/TOV The Original Vision-Model-for-Optical-Remote-Sensing-Image-Understanding-via-Self-Supervised-Learning) |
| Towards Geospatial Foundation Models via Continual Pretraining | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/Towards-Geospatial-Foundation-Models-via-Continual-Pretraining) |
| USat A Unified Self-Supervised Encoder for Multi-Sensor Satellite Imagery | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/USat-A-Unified-Self-Supervised-Encoder-for-Multi-Sensor-Satellite-Imagery) |
| Generative ConvNet Foundation Model With Sparse Modeling and Low-Frequency Reconstruction for Remote Sensing Image Interpretation | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/Generative-ConvNet-Foundation-Model-With-Sparse-Modeling-and-Low-Frequency-Reconstruction-for-Remote-Sensing-Image-Interpretation) |
| Generic Knowledge Boosted Pre-training ForRemote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2024 | [Link](https://irip-buaa.github.io/posts/Generic-Knowledge-Boosted-Pre-training-ForRemote-Sensing-Images) |
| MTP Advancing Remote Sensing FoundationModel via Multi-Task Pretraining | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MTP-Advancing-Remote-Sensing-FoundationModel-via-Multi-Task-Pretraining) |
| One for All Toward Unified Foundation Models for Earth Vision | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/One-for-All-Toward-Unified-Foundation-Models-for-Earth-Vision) |
| Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/Rethinking-Transformers-Pre-training-for-Multi-Spectral-Satellite-Imagery) |
| RingMo A Remote Sensing Foundation Model With Masked Image Modeling | IEEE Transactions on Geoscience and Remote Sensing 2024 | [Link](https://irip-buaa.github.io/posts/RingMo-A-Remote-Sensing-Foundation-Model-With-Masked-Image-Modeling) |
| S2MAE A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/S2MAE-A-Spatial-Spectral-Pretraining-Foundation-Model-for-Spectral-Remote-Sensing-Data) |
| Self-Supervised Spatio-Temporal Representation Learning of Satellite Image Time Series | JSTARS 2024 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Spatio-Temporal-Representation-Learning-of-Satellite-Image-Time-Series) |
| SkySense A Multi-Modal Remote Sensing Foundation Model Towards Universal Interpretation for Earth Observation Imagery | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/SkySense-A-Multi-Modal-Remote-Sensing-Foundation-Model-Towards-Universal-Interpretation-for-Earth-Observation-Imagery) |
| SpectralGPT Spectral Foundation Model | TPAMI 2024 | [Link](https://irip-buaa.github.io/posts/SpectralGPT-Spectral-Foundation-Model) |
| SwiMDiff Scene-wide Matching Contrastive Learning with Diffusion Constraint for Remote Sensing Image | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SwiMDiff-Scene-wide-Matching-Contrastive-Learning-with-Diffusion-Constraint-for-Remote-Sensing-Image) |
| Multi-source remote sensing pretraining based on contrastive self-supervised learning | Remote Sensing 22 | [Link](https://irip-buaa.github.io/posts/Multi-source-remote-sensing-pretraining-based-on-contrastive-self-supervised-learning) |

## Other

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Transforming remote sensing images to textual descriptions | INT J APPL EARTH OBS 2022 | [Link](https://irip-buaa.github.io/posts/Transforming-remote-sensing-images-to-textual-descriptions) |
| CSP Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations | ICML 2023 | [Link](https://irip-buaa.github.io/posts/CSP-Self-Supervised-Contrastive-Spatial-Pre-Training-for-Geospatial-Visual-Representations) |
| GeoCLIP Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/GeoCLIP-Clip-Inspired-Alignment-between-Locations-and-Images-for-Effective-Worldwide-Geo-localization) |
| Good at captioning, bad at counting Benchmarking GPT-4V on Earth observation data | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Good-at-captioning,-bad-at-counting-Benchmarking-GPT-4V-on-Earth-observation-data) |
| On the Promises and Challenges of Multimodal Foundation Models for Geographical, Environmental, Agricultural, and Urban Planning Applications | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/On-the-Promises-and-Challenges-of-Multimodal-Foundation-Models-for-Geographical,-Environmental,-Agricultural,-and-Urban-Planning-Applications) |
| SatCLIP Global, General-Purpose Location Embeddings with Satellite Imagery | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/SatCLIP-Global,-General-Purpose-Location-Embeddings-with-Satellite-Imagery) |
| The Potential of Visual ChatGPT for Remote Sensing | RS 2023 | [Link](https://irip-buaa.github.io/posts/The-Potential-of-Visual-ChatGPT-for-Remote-Sensing) |
| 遥感基础模型发展综述与未来设想 | 遥感学报 2023 | [Link](https://irip-buaa.github.io/posts/遥感基础模型发展综述与未来设想) |
| Bridging Remote Sensors with Multisensor Geospatial Foundation Models | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/Bridging-Remote-Sensors-with-Multisensor-Geospatial-Foundation-Models) |
| Charting New Territories Exploring the Geographic and Geospatial Capabilities of Multimodal LLMs | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Charting-New-Territories-Exploring-the-Geographic-and-Geospatial-Capabilities-of-Multimodal-LLMs) |
| GeoLLM Extracting Geospatial Knowledge from Large Language Models | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM-Extracting-Geospatial-Knowledge-from-Large-Language-Models) |
| LeMeViT Efficient Vision Transformer with Learnable Meta Tokens for Remote Sensing Image Interpretation | IJCAI 2024 | [Link](https://irip-buaa.github.io/posts/LeMeViT-Efficient-Vision-Transformer-with-Learnable-Meta-Tokens-for-Remote-Sensing-Image-Interpretation) |
| MMEarth Exploring Multi-Modal Pretext Tasks For Geospatial Representation Learning | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MMEarth-Exploring-Multi-Modal-Pretext-Tasks-For-Geospatial-Representation-Learning) |
| Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Neural-Plasticity-Inspired-Foundation-Model-for-Observing-the-Earth-Crossing-Modalities) |
| On the Foundations of Earth and Climate Foundation Models | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/On-the-Foundations-of-Earth-and-Climate-Foundation-Models) |
| SARATR-X A Foundation Model for Synthetic Aperture Radar Images Target Recognition | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SARATR-X-A-Foundation-Model-for-Synthetic-Aperture-Radar-Images-Target-Recognition) |

## VLM

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Bootstrapping Interactive Image-Text Alignment for Remote Sensing Image Captioning | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Bootstrapping-Interactive-Image-Text-Alignment-for-Remote-Sensing-Image-Captioning) |
| Language-aware domain generalization network for cross-scene hyperspectral image classification | IEEE Transactions on Geoscience and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/Language-aware-domain-generalization-network-for-cross-scene-hyperspectral-image-classification) |
| Parameter-Efficient Transfer Learning for Remote Sensing Image-Text Retrieval | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/Parameter-Efficient-Transfer-Learning-for-Remote-Sensing-Image-Text-Retrieval) |
| RS5M and GeoRSCLIP A Large Scale Vision-Language Dataset and A Large Vision-Language Model for Remote Sensing | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RS5M-and-GeoRSCLIP-A-Large-Scale-Vision-Language-Dataset-and-A-Large-Vision-Language-Model-for-Remote-Sensing) |
| S-CLIP Semi-supervised Vision-Language Learning using Few Specialist Captions | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/S-CLIP-Semi-supervised-Vision-Language-Learning-using-Few-Specialist-Captions) |
| Vlca vision-language aligning model with cross-modal attention for bilingual remote sensing image captioning | J SYST ENG ELECTRON 2023 | [Link](https://irip-buaa.github.io/posts/Vlca-vision-language-aligning-model-with-cross-modal-attention-for-bilingual-remote-sensing-image-captioning) |
| Large Language Models for Captioning and Retrieving Remote Sensing Images | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Large-Language-Models-for-Captioning-and-Retrieving-Remote-Sensing-Images) |
| Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-Vision-Language-Foundation-Models-without-Annotations-via-Ground-Remote-Alignment) |
| RemoteCLIP A Vision Language Foundation Model for Remote Sensing | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/RemoteCLIP-A-Vision-Language-Foundation-Model-for-Remote-Sensing) |
| SkyScript A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing | AAAI 2024 | [Link](https://irip-buaa.github.io/posts/SkyScript-A-Large-and-Semantically-Diverse-Vision-Language-Dataset-for-Remote-Sensing) |

## nan

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Changes to Captions An Attentive Network for Remote Sensing Change Captioning | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Changes-to-Captions-An-Attentive-Network-for-Remote-Sensing-Change-Captioning) |
| Multi-source interactive stair attention for remote sensing image captioning | RS 2023 | [Link](https://irip-buaa.github.io/posts/Multi-source-interactive-stair-attention-for-remote-sensing-image-captioning) |

## MLLM

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| RSGPT A Remote Sensing Vision Language Model and Benchmark | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RSGPT-A-Remote-Sensing-Vision-Language-Model-and-Benchmark) |
| EarthGPT A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/EarthGPT-A-Universal-Multi-modal-Large-Language-Model-for-Multi-sensor-Image-Comprehension-in-Remote-Sensing-Domain) |
| GeoChat Grounded Large Vision-Language Model for Remote Sensing | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoChat-Grounded-Large-Vision-Language-Model-for-Remote-Sensing) |
| H2RSVLM Towards Helpful and Honest Remote Sensing Large Vision Language Model | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/H2RSVLM-Towards-Helpful-and-Honest-Remote-Sensing-Large-Vision-Language-Model) |
| LHRS-Bot Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/LHRS-Bot-Empowering-Remote-Sensing-with-VGI-Enhanced-Large-Multimodal-Language-Model) |
| Popeye A Unified Visual-Language Model for Multi-Source Ship Detection from Remote Sensing Imagery | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Popeye-A-Unified-Visual-Language-Model-for-Multi-Source-Ship-Detection-from-Remote-Sensing-Imagery) |
| RS-LLaVA Large Vision Language Model for Joint Captioning and Question Answering in Remote Sensing Imagery | RS 2024 | [Link](https://irip-buaa.github.io/posts/RS-LLaVA-Large-Vision-Language-Model-for-Joint-Captioning-and-Question-Answering-in-Remote-Sensing-Imagery) |
| SkyEyeGPT Unifying Remote Sensing Vision-Language Tasks via Instruction Tuning with Large Language Model | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SkyEyeGPT-Unifying-Remote-Sensing-Vision-Language-Tasks-via-Instruction-Tuning-with-Large-Language-Model) |

## Agent

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Tree-GPT Modular Large Language Model Expert System for Forest Remote Sensing Image Understanding and Interactive Analysis | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Tree-GPT-Modular-Large-Language-Model-Expert-System-for-Forest-Remote-Sensing-Image-Understanding-and-Interactive-Analysis) |
| Change-Agent Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Change-Agent-Towards-Interactive-Comprehensive-Remote-Sensing-Change-Interpretation-and-Analysis) |
| Evaluating Tool-Augmented Agents in Remote Sensing Platforms | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/Evaluating-Tool-Augmented-Agents-in-Remote-Sensing-Platforms) |
| GeoLLM-Engine A Realistic Environment for Building Geospatial Copilots | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM-Engine-A-Realistic-Environment-for-Building-Geospatial-Copilots) |
| Remote Sensing ChatGPT Solving Remote Sensing Tasks with ChatGPT and Visual Models | IGARSS 2024 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-ChatGPT-Solving-Remote-Sensing-Tasks-with-ChatGPT-and-Visual-Models) |

