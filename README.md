# A-Review-for-remote-sensing-vision-language-models
This is a repository for ...
## Overleaf
https://www.overleaf.com/5469324254jsdvcqwcsmzz#0edfd1

## Table of Contents
- [A-Review-for-remote-sensing-vision-language-models](#a-review-for-remote-sensing-vision-language-models)
  - [Overleaf](#overleaf)
  - [Table of Contents](#table-of-contents)
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


# dataset

## 图像

| Paper Name | Categories | Detailed Info |
|------------|------------|---------------|
| TAS | 检测 | [Link](https://irip-buaa.github.io/posts/TAS) |
| OIRDS | 检测 | [Link](https://irip-buaa.github.io/posts/OIRDS) |
| SZTAKI-INRIA AirChange | 变化检测 | [Link](https://irip-buaa.github.io/posts/SZTAKI-INRIAAirChange) |
| UCMerced_LandUse | 分类 | [Link](https://irip-buaa.github.io/posts/UCMerced_LandUse) |
| ISPRS Potsdam | 分割 | [Link](https://irip-buaa.github.io/posts/ISPRSPotsdam) |
| ISPRS Vaihingen | 分割 | [Link](https://irip-buaa.github.io/posts/ISPRSVaihingen) |
| WHU RS19 | 分类 | [Link](https://irip-buaa.github.io/posts/WHURS19) |
| Massachusetts Builds | 分割 | [Link](https://irip-buaa.github.io/posts/MassachusettsBuilds) |
| Massachusetts Roads | 分割 | [Link](https://irip-buaa.github.io/posts/MassachusettsRoads) |
| SPARCS | 分割 | [Link](https://irip-buaa.github.io/posts/SPARCS) |
| RSSCN7 | 分类 | [Link](https://irip-buaa.github.io/posts/RSSCN7) |
| SAT | 分类 | [Link](https://irip-buaa.github.io/posts/SAT) |
| VEDAI | 检测 | [Link](https://irip-buaa.github.io/posts/VEDAI) |
| DLR3k | 检测 | [Link](https://irip-buaa.github.io/posts/DLR3k) |
| HRSC2016 | 检测 | [Link](https://irip-buaa.github.io/posts/HRSC2016) |
| NWPU-RESISC45 | 分类 | [Link](https://irip-buaa.github.io/posts/NWPU-RESISC45) |
| RS_C11 | 分类 | [Link](https://irip-buaa.github.io/posts/RS_C11) |
| SIRI-WHU | 分类 | [Link](https://irip-buaa.github.io/posts/SIRI-WHU) |
| Aerial to Map | 图像生成 | [Link](https://irip-buaa.github.io/posts/AerialtoMap) |
| AID | 分类 | [Link](https://irip-buaa.github.io/posts/AID) |
| AIST Building Change Detection(ABCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/AISTBuildingChangeDetection(ABCD)) |
| CITY-OSM | 分割 | [Link](https://irip-buaa.github.io/posts/CITY-OSM) |
| Dstl Satellite Imagery Feature Detection | 分割 | [Link](https://irip-buaa.github.io/posts/DstlSatelliteImageryFeatureDetection) |
| OpenSARShip | 检测 | [Link](https://irip-buaa.github.io/posts/OpenSARShip) |
| RSD46-WHU | 分类 | [Link](https://irip-buaa.github.io/posts/RSD46-WHU) |
| RSI-CB | 分类 | [Link](https://irip-buaa.github.io/posts/RSI-CB) |
| SateHaze1k | 图像生成 | [Link](https://irip-buaa.github.io/posts/SateHaze1k) |
| TGRS-HRRSD | 检测 | [Link](https://irip-buaa.github.io/posts/TGRS-HRRSD) |
| 2018 Open AI Tanzania Building Footprint | 分割 | [Link](https://irip-buaa.github.io/posts/2018OpenAITanzaniaBuildingFootprint) |
| Aeroscapes | 分割 | [Link](https://irip-buaa.github.io/posts/Aeroscapes) |
| AIRS | 分割 | [Link](https://irip-buaa.github.io/posts/AIRS) |
| CDD Dataset (season-varying) | 变化检测 | [Link](https://irip-buaa.github.io/posts/CDDDataset(season-varying)) |
| DeepGlobe Land Cover Classificat | 分割 | [Link](https://irip-buaa.github.io/posts/DeepGlobeLandCoverClassificat) |
| DeepGlobe Road Detection Challen | 分割 | [Link](https://irip-buaa.github.io/posts/DeepGlobeRoadDetectionChallen) |
| DLRSD | 分割 | [Link](https://irip-buaa.github.io/posts/DLRSD) |
| DOTA1.0 | 检测 | [Link](https://irip-buaa.github.io/posts/DOTA1.0) |
| EuroSAT | 分类 | [Link](https://irip-buaa.github.io/posts/EuroSAT) |
| fMoW | 检测 | [Link](https://irip-buaa.github.io/posts/fMoW) |
| ITCVD | 检测 | [Link](https://irip-buaa.github.io/posts/ITCVD) |
| LEVIR | 检测 | [Link](https://irip-buaa.github.io/posts/LEVIR) |
| Mapping Challenge | 分割 | [Link](https://irip-buaa.github.io/posts/MappingChallenge) |
| MASATI | 检测 | [Link](https://irip-buaa.github.io/posts/MASATI) |
| Onera Satellite Change Detection (OSCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/OneraSatelliteChangeDetection(OSCD)) |
| PatternNet | 分类 | [Link](https://irip-buaa.github.io/posts/PatternNet) |
| RIT-18 | 分割 | [Link](https://irip-buaa.github.io/posts/RIT-18) |
| Urban Drone Dataset(UDD) | 分割 | [Link](https://irip-buaa.github.io/posts/UrbanDroneDataset(UDD)) |
| VisDrone2019-DET | 检测 | [Link](https://irip-buaa.github.io/posts/VisDrone2019-DET) |
| WHDLD | 分割 | [Link](https://irip-buaa.github.io/posts/WHDLD) |
| WHU Building Change Detection Dataset | 变化检测 | [Link](https://irip-buaa.github.io/posts/WHUBuildingChangeDetectionDataset) |
| WHU_GID中的Fine部分 | 分割 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Fine部分) |
| WHU_GID中的Large-scale部分 | 分割 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Large-scale部分) |
| WHU_GID中的secenClass部分 | 分类 | [Link](https://irip-buaa.github.io/posts/WHU_GID中的secenClass部分) |
| xView | 检测 | [Link](https://irip-buaa.github.io/posts/xView) |
| 38-Cloud | 分割 | [Link](https://irip-buaa.github.io/posts/38-Cloud) |
| Bijie Landslide Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/BijieLandslideDataset) |
| Bridge Dataset | 检测 | [Link](https://irip-buaa.github.io/posts/BridgeDataset) |
| Change Detection Dataset(CDD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/ChangeDetectionDataset(CDD)) |
| DOTA1.5 | 检测 | [Link](https://irip-buaa.github.io/posts/DOTA1.5) |
| DroneDeploy | 分割 | [Link](https://irip-buaa.github.io/posts/DroneDeploy) |
| DSIFN Dataset | 变化检测 | [Link](https://irip-buaa.github.io/posts/DSIFNDataset) |
| GF2 Dataset for 3DFGC | 分割 | [Link](https://irip-buaa.github.io/posts/GF2Datasetfor3DFGC) |
| High Resolution Semantic Change (HRSCD) | 变化检测 | [Link](https://irip-buaa.github.io/posts/HighResolutionSemanticChange(HRSCD)) |
| iSAID | 检测 | [Link](https://irip-buaa.github.io/posts/iSAID) |
| Multi-temporal Scene WuHan (MtS-WH) | 变化检测 | [Link](https://irip-buaa.github.io/posts/Multi-temporalSceneWuHan(MtS-WH)) |
| OPTIMAL-31 | 分类 | [Link](https://irip-buaa.github.io/posts/OPTIMAL-31) |
| ORSSD | 分割 | [Link](https://irip-buaa.github.io/posts/ORSSD) |
| RoadTracer | 分割 | [Link](https://irip-buaa.github.io/posts/RoadTracer) |
| Semantic Drone Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/SemanticDroneDataset) |
| SEN12MS | 分割 | [Link](https://irip-buaa.github.io/posts/SEN12MS) |
| WHU Building Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHUBuildingDataset) |
| 95-Cloud | 分割 | [Link](https://irip-buaa.github.io/posts/95-Cloud) |
| BDCI2020 | 分割 | [Link](https://irip-buaa.github.io/posts/BDCI2020) |
| BH-POOLS | 分割 | [Link](https://irip-buaa.github.io/posts/BH-POOLS) |
| BH-WATERTANKS | 分割 | [Link](https://irip-buaa.github.io/posts/BH-WATERTANKS) |
| Change-Detection-dataset-for-High-resolution-Satellite-Image | 变化检测 | [Link](https://irip-buaa.github.io/posts/Change-Detection-dataset-for-High-resolution-Satellite-Image) |
| Continual Learning Benchmark for Remote | 分类 | [Link](https://irip-buaa.github.io/posts/ContinualLearningBenchmarkforRemote) |
| DroneCrowd | 检测 | [Link](https://irip-buaa.github.io/posts/DroneCrowd) |
| EORSSD | 分割 | [Link](https://irip-buaa.github.io/posts/EORSSD) |
| HRSID | 检测 | [Link](https://irip-buaa.github.io/posts/HRSID) |
| landcover_ai | 分割 | [Link](https://irip-buaa.github.io/posts/landcover_ai) |
| LEVIR-CD | 变化检测 | [Link](https://irip-buaa.github.io/posts/LEVIR-CD) |
| MLRSNet | 分类 | [Link](https://irip-buaa.github.io/posts/MLRSNet) |
| Multi-View Datasets中的AiRound部分 | 分类 | [Link](https://irip-buaa.github.io/posts/Multi-ViewDatasets中的AiRound部分) |
| Multi-View Datasets中的CV-BrCT部分 | 分类 | [Link](https://irip-buaa.github.io/posts/Multi-ViewDatasets中的CV-BrCT部分) |
| RarePlanes | 检测 | [Link](https://irip-buaa.github.io/posts/RarePlanes) |
| SEmantic Change detectiON Data(SECOND) | 变化检测 | [Link](https://irip-buaa.github.io/posts/SEmanticChangedetectiONData(SECOND)) |
| SenseEarth ChangeDetection | 变化检测 | [Link](https://irip-buaa.github.io/posts/SenseEarthChangeDetection) |
| Sentinel-2 Cloud Mask Catalogue | 分割 | [Link](https://irip-buaa.github.io/posts/Sentinel-2CloudMaskCatalogue) |
| Sentinel-2 Multitemporal Cities Pairs | 变化检测 | [Link](https://irip-buaa.github.io/posts/Sentinel-2MultitemporalCitiesPairs) |
| UAVid | 分割 | [Link](https://irip-buaa.github.io/posts/UAVid) |
| WHU Cloud Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHUCloudDataset) |
| WHU Multi-view Dataset | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHUMulti-viewDataset) |
| WHU Stereo Dataset | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHUStereoDataset) |
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
| Sun Yat-Sen University (SYSU)-CD | 变化检测 | [Link](https://irip-buaa.github.io/posts/SunYat-SenUniversity(SYSU)-CD) |
| TG1HRSSC | 分类 | [Link](https://irip-buaa.github.io/posts/TG1HRSSC) |
| VISO-Detection | 检测 | [Link](https://irip-buaa.github.io/posts/VISO-Detection) |
| WHU TCL SatMVS dataset1.0 | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHUTCLSatMVSdataset1.0) |
| WHU TCL SatMVS dataset2.0 | 图像生成 | [Link](https://irip-buaa.github.io/posts/WHUTCLSatMVSdataset2.0) |
| 船只智能检测-训练数据集 | 检测 | [Link](https://irip-buaa.github.io/posts/船只智能检测-训练数据集) |
| 飞机目标识别-训练数据集 | 检测 | [Link](https://irip-buaa.github.io/posts/飞机目标识别-训练数据集) |
| MiniFrance-DFC22 | 分割 | [Link](https://irip-buaa.github.io/posts/MiniFrance-DFC22) |
| SAMRS | 分割 | [Link](https://irip-buaa.github.io/posts/SAMRS) |
| TOV-RS-balanced | 分类 | [Link](https://irip-buaa.github.io/posts/TOV-RS-balanced) |
| CACo | 单模态预训练 | [Link](https://irip-buaa.github.io/posts/CACo) |
| GEO-Bench | 评估 | [Link](https://irip-buaa.github.io/posts/GEO-Bench) |
| SATIN | 分类 | [Link](https://irip-buaa.github.io/posts/SATIN) |
| SatlasPretrain | 分类 | [Link](https://irip-buaa.github.io/posts/SatlasPretrain) |
| WHU-Mix (vector) building dataset | 分割 | [Link](https://irip-buaa.github.io/posts/WHU-Mix(vector)buildingdataset) |
| Constellation | 检测 | [Link](https://irip-buaa.github.io/posts/Constellation) |
| Earth Parser Dataset | 分割 | [Link](https://irip-buaa.github.io/posts/EarthParserDataset) |
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
| Functional Map of the World | CVPR 2018 | [Link](https://irip-buaa.github.io/posts/FunctionalMapoftheWorld) |
| BIGEARTHNET | IEEE International Geoscience and Remote Sensing Symposium 2019 | [Link](https://irip-buaa.github.io/posts/BIGEARTHNET) |
| Tile2Vec | AAAI 2019 | [Link](https://irip-buaa.github.io/posts/Tile2Vec) |
| Remote Sensing Image Scene Classification with Self-Supervised Paradigm under Limited Labeled Samples | IEEE Geoscience and Remote Sensing Letters 2020 | [Link](https://irip-buaa.github.io/posts/RemoteSensingImageSceneClassificationwithSelf-SupervisedParadigmunderLimitedLabeledSamples) |
| Geography-aware self-supervised learning | ICCV 2021 | [Link](https://irip-buaa.github.io/posts/Geography-awareself-supervisedlearning) |
| On Creating Benchmark Dataset for Aerial Image Interpretation | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2021 | [Link](https://irip-buaa.github.io/posts/OnCreatingBenchmarkDatasetforAerialImageInterpretation) |
| Seasonal Contrast:Unsupervised Pre-Training from Uncurated Remote Sensing Data | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/SeasonalContrast:UnsupervisedPre-TrainingfromUncuratedRemoteSensingData) |
| Self-Supervised Learning of Remote Sensing Scene Representations Using Contrastive Multiview Coding | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/Self-SupervisedLearningofRemoteSensingSceneRepresentationsUsingContrastiveMultiviewCoding) |
| Advancing plain vision transformer toward remote sensing foundation model | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Advancingplainvisiontransformertowardremotesensingfoundationmodel) |
| Consecutive Pre-Training | Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/ConsecutivePre-Training) |
| Geographical Knowledge-Driven RepresentationLearning for Remote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/GeographicalKnowledge-DrivenRepresentationLearningforRemoteSensingImages) |
| Global and Local Contrastive Self-Supervised Learning for Semantic Segmentation of HR Remote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/GlobalandLocalContrastiveSelf-SupervisedLearningforSemanticSegmentationofHRRemoteSensingImages) |
| SatMAE | NeurIPS 2022 | [Link](https://irip-buaa.github.io/posts/SatMAE) |
| Self-Supervised Learning for Invariant Representations from Multi-Spectral and SAR Images | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Self-SupervisedLearningforInvariantRepresentationsfromMulti-SpectralandSARImages) |
| Self-Supervised Material and Texture Representation Learning for Remote Sensing Tasks | CVPR 2022 | [Link](https://irip-buaa.github.io/posts/Self-SupervisedMaterialandTextureRepresentationLearningforRemoteSensingTasks) |
| Self-supervised vision transformers for joint sar-optical representation learning | Arxiv 2022 | [Link](https://irip-buaa.github.io/posts/Self-supervisedvisiontransformersforjointsar-opticalrepresentationlearning) |
| Semantic segmentation of remote sensing images with self-supervised semantic-aware inpainting | IEEE Geoscience and Remote Sensing Letters 2022 | [Link](https://irip-buaa.github.io/posts/Semanticsegmentationofremotesensingimageswithself-supervisedsemantic-awareinpainting) |
| A billion-scale foundation model for remote sensing images | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Abillion-scalefoundationmodelforremotesensingimages) |
| A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion | IGARSS 2023 | [Link](https://irip-buaa.github.io/posts/ASelf-SupervisedCross-ModalRemoteSensingFoundationModelwithMulti-DomainRepresentationandCross-DomainFusion) |
| An Empirical Study of Remote Sensing Pretraining | IEEE Transactions on Geoscience and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/AnEmpiricalStudyofRemoteSensingPretraining) |
| Change-Aware Sampling and Contrastive Learning for Satellite Images | CVPR 2023 | [Link](https://irip-buaa.github.io/posts/Change-AwareSamplingandContrastiveLearningforSatelliteImages) |
| CMID | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/CMID) |
| CROMA | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/CROMA) |
| Cross-Scale MAE | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/Cross-ScaleMAE) |
| CtxMIM | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/CtxMIM) |
| DeCUR | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DeCUR) |
| DINO-MC | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DINO-MC) |
| EarthPT | NeurIPS CCAI workshop 2023 | [Link](https://irip-buaa.github.io/posts/EarthPT) |
| Feature Guided Masked Autoencoder for Self-supervised Learning in Remote Sensing | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/FeatureGuidedMaskedAutoencoderforSelf-supervisedLearninginRemoteSensing) |
| FoMo-Bench | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/FoMo-Bench) |
| Foundation Models for Generalist Geospatial Artificial Intelligence | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/FoundationModelsforGeneralistGeospatialArtificialIntelligence) |
| Lightweight, Pre-trained Transformers for Remote Sensing Timeseries | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Lightweight,Pre-trainedTransformersforRemoteSensingTimeseries) |
| Multi Modal Multi Objective Contrastive Learning for Sentinel 1-2 Imagery | CVPRW 2023 | [Link](https://irip-buaa.github.io/posts/MultiModalMultiObjectiveContrastiveLearningforSentinel1-2Imagery) |
| Predicting Gradient is Better | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/PredictingGradientisBetter) |
| RingMo-lite | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RingMo-lite) |
| Rsprompter | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Rsprompter) |
| SatlasPretrain | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/SatlasPretrain) |
| Scale-MAE | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/Scale-MAE) |
| TOV | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/TOV) |
| TOV: The Original Vision Model for Optical Remote Sensing Image Understanding via Self-Supervised Learning | IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/TOV: The Original VisionModelforOpticalRemoteSensingImageUnderstandingviaSelf-SupervisedLearning) |
| Towards Geospatial Foundation Models via Continual Pretraining | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/TowardsGeospatialFoundationModelsviaContinualPretraining) |
| USat | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/USat) |
| Generative ConvNet Foundation Model With Sparse Modeling and Low-Frequency Reconstruction for Remote Sensing Image Interpretation | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/GenerativeConvNetFoundationModelWithSparseModelingandLow-FrequencyReconstructionforRemoteSensingImageInterpretation) |
| Generic Knowledge Boosted Pre-training ForRemote Sensing Images | IEEE Transactions on Geoscience and Remote Sensing 2024 | [Link](https://irip-buaa.github.io/posts/GenericKnowledgeBoostedPre-trainingForRemoteSensingImages) |
| MTP | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MTP) |
| One for All | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/OneforAll) |
| Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/RethinkingTransformersPre-trainingforMulti-SpectralSatelliteImagery) |
| RingMo | IEEE Transactions on Geoscience and Remote Sensing 2024 | [Link](https://irip-buaa.github.io/posts/RingMo) |
| S2MAE | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/S2MAE) |
| Self-Supervised Spatio-Temporal Representation Learning of Satellite Image Time Series | JSTARS 2024 | [Link](https://irip-buaa.github.io/posts/Self-SupervisedSpatio-TemporalRepresentationLearningofSatelliteImageTimeSeries) |
| SkySense | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/SkySense) |
| SpectralGPT | TPAMI 2024 | [Link](https://irip-buaa.github.io/posts/SpectralGPT) |
| SwiMDiff | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SwiMDiff) |
| Multi-source remote sensing pretraining based on contrastive self-supervised learning | Remote Sensing 22 | [Link](https://irip-buaa.github.io/posts/Multi-sourceremotesensingpretrainingbasedoncontrastiveself-supervisedlearning) |

## Other

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Transforming remote sensing images to textual descriptions | INT J APPL EARTH OBS 2022 | [Link](https://irip-buaa.github.io/posts/Transformingremotesensingimagestotextualdescriptions) |
| CSP | ICML 2023 | [Link](https://irip-buaa.github.io/posts/CSP) |
| GeoCLIP | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/GeoCLIP) |
| Good at captioning, bad at counting | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Goodatcaptioning,badatcounting) |
| On the Promises and Challenges of Multimodal Foundation Models for Geographical, Environmental, Agricultural, and Urban Planning Applications | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/OnthePromisesandChallengesofMultimodalFoundationModelsforGeographical,Environmental,Agricultural,andUrbanPlanningApplications) |
| SatCLIP | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/SatCLIP) |
| The Potential of Visual ChatGPT for Remote Sensing | RS 2023 | [Link](https://irip-buaa.github.io/posts/ThePotentialofVisualChatGPTforRemoteSensing) |
| 遥感基础模型发展综述与未来设想 | 遥感学报 2023 | [Link](https://irip-buaa.github.io/posts/遥感基础模型发展综述与未来设想) |
| Bridging Remote Sensors with Multisensor Geospatial Foundation Models | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/BridgingRemoteSensorswithMultisensorGeospatialFoundationModels) |
| Charting New Territories | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/ChartingNewTerritories) |
| GeoLLM | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM) |
| LeMeViT | IJCAI 2024 | [Link](https://irip-buaa.github.io/posts/LeMeViT) |
| MMEarth | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MMEarth) |
| Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/NeuralPlasticity-InspiredFoundationModelforObservingtheEarthCrossingModalities) |
| On the Foundations of Earth and Climate Foundation Models | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/OntheFoundationsofEarthandClimateFoundationModels) |
| SARATR-X | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SARATR-X) |

## VLM

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Bootstrapping Interactive Image-Text Alignment for Remote Sensing Image Captioning | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/BootstrappingInteractiveImage-TextAlignmentforRemoteSensingImageCaptioning) |
| Language-aware domain generalization network for cross-scene hyperspectral image classification | IEEE Transactions on Geoscience and Remote Sensing 2023 | [Link](https://irip-buaa.github.io/posts/Language-awaredomaingeneralizationnetworkforcross-scenehyperspectralimageclassification) |
| Parameter-Efficient Transfer Learning for Remote Sensing Image-Text Retrieval | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/Parameter-EfficientTransferLearningforRemoteSensingImage-TextRetrieval) |
| RS5M and GeoRSCLIP | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RS5MandGeoRSCLIP) |
| S-CLIP | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/S-CLIP) |
| Vlca | J SYST ENG ELECTRON 2023 | [Link](https://irip-buaa.github.io/posts/Vlca) |
| Large Language Models for Captioning and Retrieving Remote Sensing Images | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/LargeLanguageModelsforCaptioningandRetrievingRemoteSensingImages) |
| Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/RemoteSensingVision-LanguageFoundationModelswithoutAnnotationsviaGroundRemoteAlignment) |
| RemoteCLIP | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/RemoteCLIP) |
| SkyScript | AAAI 2024 | [Link](https://irip-buaa.github.io/posts/SkyScript) |

## nan

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Changes to Captions | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/ChangestoCaptions) |
| Multi-source interactive stair attention for remote sensing image captioning | RS 2023 | [Link](https://irip-buaa.github.io/posts/Multi-sourceinteractivestairattentionforremotesensingimagecaptioning) |

## MLLM

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| RSGPT | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RSGPT) |
| EarthGPT | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/EarthGPT) |
| GeoChat | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoChat) |
| H2RSVLM | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/H2RSVLM) |
| LHRS-Bot | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/LHRS-Bot) |
| Popeye | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Popeye) |
| RS-LLaVA | RS 2024 | [Link](https://irip-buaa.github.io/posts/RS-LLaVA) |
| SkyEyeGPT | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SkyEyeGPT) |

## Agent

| Paper Name | Published in | Detailed Info |
|------------|--------------|---------------|
| Tree-GPT | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Tree-GPT) |
| Change-Agent | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Change-Agent) |
| Evaluating Tool-Augmented Agents in Remote Sensing Platforms | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/EvaluatingTool-AugmentedAgentsinRemoteSensingPlatforms) |
| GeoLLM-Engine | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM-Engine) |
| Remote Sensing ChatGPT | IGARSS 2024 | [Link](https://irip-buaa.github.io/posts/RemoteSensingChatGPT) |



