# A Survey on Remote Sensing Foundation Models: From Vision to Multimodality
This is a repository for "A Survey on Remote Sensing Foundation Models: From Vision to Multimodality". 

🌏 Please check out our survey paper: [A Survey on Remote Sensing Foundation Models: From Vision to Multimodality](https://arxiv.org/abs/2503.22081)
## Detail page
You can see details of all papers and datasets here: [homepage](https://irip-buaa.github.io/)
## Table of Contents
- [Dataset](#Dataset)
  - [Image](#Image)
  - [Image+Text](#Image+Text)
  - [Video](#Video)
  <!-- - [视频、文本](#视频文本) -->
- [Model](#Model)
  - [Pretrain](#pretrain)
  - [VLM](#vlm)
  <!-- - [Nan](#nan) -->
  - [MLLM](#mllm)
  - [Agent](#agent)
  - [Other](#other)

# Dataset

## Image

| Dataset Name | Categories | Detailed Info |
|------------|------------|---------------|
| [TAS](http://ai.stanford.edu/~gaheitz/Research/TAS/) | Detection | [Link](https://irip-buaa.github.io/posts/TAS) |
| [OIRDS](https://sourceforge.net/projects/oirds/) | Detection | [Link](https://irip-buaa.github.io/posts/OIRDS) |
| [SZTAKI-INRIA AirChange](http://web.eee.sztaki.hu/remotesensing/airchange_benchmark.html) | Change Detection | [Link](https://irip-buaa.github.io/posts/SZTAKI-INRIA-AirChange) |
| [UCMerced_LandUse](http://weegee.vision.ucmerced.edu/datasets/landuse.html) | Classification | [Link](https://irip-buaa.github.io/posts/UCMerced_LandUse) |
| [ISPRS Potsdam](https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx) | Segmentation | [Link](https://irip-buaa.github.io/posts/ISPRS-Potsdam) |
| [ISPRS Vaihingen](https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx) | Segmentation | [Link](https://irip-buaa.github.io/posts/ISPRS-Vaihingen) |
| [WHU RS19](https://captain-whu.github.io/BED4RS/) | Classification | [Link](https://irip-buaa.github.io/posts/WHU-RS19) |
| [Massachusetts Builds](https://www.cs.toronto.edu/~vmnih/data/) | Segmentation | [Link](https://irip-buaa.github.io/posts/Massachusetts-Builds) |
| [Massachusetts Roads](https://www.cs.toronto.edu/~vmnih/data/) | Segmentation | [Link](https://irip-buaa.github.io/posts/Massachusetts-Roads) |
| [SPARCS](https://www.usgs.gov/core-science-systems/nli/landsat/spatial-procedures-automated-removal-cloud-and-shadow-sparcs) | Segmentation | [Link](https://irip-buaa.github.io/posts/SPARCS) |
| [RSSCN7](https://github.com/palewithout/RSSCN7) | Classification | [Link](https://irip-buaa.github.io/posts/RSSCN7) |
| [SAT](http://csc.lsu.edu/~saikat/deepsat/) | Classification | [Link](https://irip-buaa.github.io/posts/SAT) |
| [VEDAI](https://downloads.greyc.fr/vedai/) | Detection | [Link](https://irip-buaa.github.io/posts/VEDAI) |
| [DLR3k](https://www.dlr.de/eoc/en/desktopdefault.aspx/tabid-12760/22294_read-52777) | Detection | [Link](https://irip-buaa.github.io/posts/DLR3k) |
| [HRSC2016](https://www.kaggle.com/datasets/guofeng/hrsc2016) | Detection | [Link](https://irip-buaa.github.io/posts/HRSC2016) |
| [NWPU-RESISC45](https://gcheng-nwpu.github.io/#Datasets) | Classification | [Link](https://irip-buaa.github.io/posts/NWPU-RESISC45) |
| [RS_C11](https://www.researchgate.net/publication/271647282_RS_C11_Database) | Classification | [Link](https://irip-buaa.github.io/posts/RS_C11) |
| [SIRI-WHU](http://www.lmars.whu.edu.cn/prof_web/zhongyanfei/Code/Google_Dataset/Google%20dataset%20of%20SIRI-WHU_earth_im_tiff.7z) | Classification | [Link](https://irip-buaa.github.io/posts/SIRI-WHU) |
| [Aerial to Map](https://github.com/phillipi/pix2pix) | Image Generation | [Link](https://irip-buaa.github.io/posts/Aerial-to-Map) |
| [AID](https://captain-whu.github.io/AID/) | Classification | [Link](https://irip-buaa.github.io/posts/AID) |
| [AIST Building Change Detection(ABCD)](https://github.com/gistairc/ABCDdataset) | Change Detection | [Link](https://irip-buaa.github.io/posts/AIST-Building-Change-Detection(ABCD)) |
| [CITY-OSM](https://zenodo.org/record/1154821) | Segmentation | [Link](https://irip-buaa.github.io/posts/CITY-OSM) |
| [Dstl Satellite Imagery Feature Detection](https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection/data) | Segmentation | [Link](https://irip-buaa.github.io/posts/Dstl-Satellite-Imagery-Feature-Detection) |
| [OpenSARShip](https://opensar.sjtu.edu.cn/DataAndCodes.html) | Detection | [Link](https://irip-buaa.github.io/posts/OpenSARShip) |
| [RSD46-WHU](https://github.com/RSIA-LIESMARS-WHU/RSD46-WHU) | Classification | [Link](https://irip-buaa.github.io/posts/RSD46-WHU) |
| [RSI-CB](https://github.com/lehaifeng/RSI-CB) | Classification | [Link](https://irip-buaa.github.io/posts/RSI-CB) |
| [SateHaze1k](https://www.dropbox.com/s/k2i3p7puuwl2g59/Haze1k.zip?dl=0) | Image Generation | [Link](https://irip-buaa.github.io/posts/SateHaze1k) |
| [TGRS-HRRSD](https://github.com/CrazyStoneonRoad/TGRS-HRRSD-Dataset) | Detection | [Link](https://irip-buaa.github.io/posts/TGRS-HRRSD) |
| [2018 Open AI Tanzania Building Footprint](https://competitions.codalab.org/competitions/20100) | Segmentation | [Link](https://irip-buaa.github.io/posts/2018-Open-AI-Tanzania-Building-Footprint) |
| [Aeroscapes](https://github.com/ishann/aeroscapes) | Segmentation | [Link](https://irip-buaa.github.io/posts/Aeroscapes) |
| [AIRS](https://www.airs-dataset.com/) | Segmentation | [Link](https://irip-buaa.github.io/posts/AIRS) |
| [CDD Dataset (season-varying)](https://paperswithcode.com/dataset/cdd-dataset-season-varying) | Change Detection | [Link](https://irip-buaa.github.io/posts/CDD-Dataset-(season-varying)) |
| [DeepGlobe Land Cover Classificat](http://deepglobe.org/challenge.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/DeepGlobe-Land-Cover-Classificat) |
| [DeepGlobe Road Detection Challen](http://deepglobe.org/challenge.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/DeepGlobe-Road-Detection-Challen) |
| [DLRSD](https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0) | Segmentation | [Link](https://irip-buaa.github.io/posts/DLRSD) |
| [DOTA1.0](https://captain-whu.github.io/DOTA/index.html) | Detection | [Link](https://irip-buaa.github.io/posts/DOTA1.0) |
| [EuroSAT](https://github.com/phelber/eurosat) | Classification | [Link](https://irip-buaa.github.io/posts/EuroSAT) |
| [fMoW](https://github.com/fMoW/dataset) | Detection | [Link](https://irip-buaa.github.io/posts/fMoW) |
| [ITCVD](https://research.utwente.nl/en/datasets/itcvd-dataset) | Detection | [Link](https://irip-buaa.github.io/posts/ITCVD) |
| [LEVIR](http://levir.buaa.edu.cn/Code.htm) | Detection | [Link](https://irip-buaa.github.io/posts/LEVIR) |
| [Mapping Challenge](https://www.crowdai.org/challenges/mapping-challenge) | Segmentation | [Link](https://irip-buaa.github.io/posts/Mapping-Challenge) |
| [MASATI](https://www.iuii.ua.es/datasets/masati/) | Detection | [Link](https://irip-buaa.github.io/posts/MASATI) |
| [Onera Satellite Change Detection (OSCD)](https://rcdaudt.github.io/oscd/) | Change Detection | [Link](https://irip-buaa.github.io/posts/Onera-Satellite-Change-Detection-(OSCD)) |
| [PatternNet](https://sites.google.com/view/zhouwx/dataset) | Classification | [Link](https://irip-buaa.github.io/posts/PatternNet) |
| [RIT-18](https://github.com/rmkemker/RIT-18) | Segmentation | [Link](https://irip-buaa.github.io/posts/RIT-18) |
| [Urban Drone Dataset(UDD)](https://github.com/MarcWong/UDD) | Segmentation | [Link](https://irip-buaa.github.io/posts/Urban-Drone-Dataset(UDD)) |
| [VisDrone2019-DET](https://github.com/VisDrone/VisDrone-Dataset) | Detection | [Link](https://irip-buaa.github.io/posts/VisDrone2019-DET) |
| [WHDLD](https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHDLD) |
| [WHU Building Change Detection Dataset](https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html) | Change Detection | [Link](https://irip-buaa.github.io/posts/WHU-Building-Change-Detection-Dataset) |
| [The "Fine" part in WHU_GID](https://x-ytong.github.io/project/GID.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Fine部分) |
| [The "Large-scale" part in WHU_GID](https://x-ytong.github.io/project/GID.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHU_GID中的Large-scale部分) |
| [The "secenClass" part in WHU_GID](https://x-ytong.github.io/project/GID.html) | Classification | [Link](https://irip-buaa.github.io/posts/WHU_GID中的secenClass部分) |
| [xView](https://challenge.xviewdataset.org/data-download) | Detection | [Link](https://irip-buaa.github.io/posts/xView) |
| [38-Cloud](https://github.com/SorourMo/38-Cloud-A-Cloud-Segmentation-Dataset) | Segmentation | [Link](https://irip-buaa.github.io/posts/38-Cloud) |
| [Bijie Landslide Dataset](http://gpcv.whu.edu.cn/data/Bijie_pages.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/Bijie-Landslide-Dataset) |
| [Bridge Dataset](http://www.patreo.dcc.ufmg.br/2019/07/10/bridge-dataset/) | Detection | [Link](https://irip-buaa.github.io/posts/Bridge-Dataset) |
| [Change Detection Dataset(CDD)](https://gitlab.citius.usc.es/hiperespectral/ChangeDetectionDataset) | Change Detection | [Link](https://irip-buaa.github.io/posts/Change-Detection-Dataset(CDD)) |
| [DOTA1.5](https://captain-whu.github.io/DOTA/index.html) | Detection | [Link](https://irip-buaa.github.io/posts/DOTA1.5) |
| [DroneDeploy](https://github.com/dronedeploy/dd-ml-segmentation-benchmark) | Segmentation | [Link](https://irip-buaa.github.io/posts/DroneDeploy) |
| [DSIFN Dataset](https://github.com/GeoZcx/A-deeply-supervised-image-fusion-network-for-change-detection-in-remote-sensing-images/tree/master/dataset) | Change Detection | [Link](https://irip-buaa.github.io/posts/DSIFN-Dataset) |
| [GF2 Dataset for 3DFGC](http://gpcv.whu.edu.cn/data/3DFGC_pages.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/GF2-Dataset-for-3DFGC) |
| [High Resolution Semantic Change (HRSCD)](https://rcdaudt.github.io/hrscd/) | Change Detection | [Link](https://irip-buaa.github.io/posts/High-Resolution-Semantic-Change-(HRSCD)) |
| [iSAID](https://captain-whu.github.io/iSAID/index.html) | Detection | [Link](https://irip-buaa.github.io/posts/iSAID) |
| [Multi-temporal Scene WuHan (MtS-WH)](http://sigma.whu.edu.cn/newspage.php?q=2019_03_26) | Change Detection | [Link](https://irip-buaa.github.io/posts/Multi-temporal-Scene-WuHan-(MtS-WH)) |
| [OPTIMAL-31](https://drive.google.com/open?id=1Fk9a0DW8UyyQsR8dP2Qdakmr69NVBhq9) | Classification | [Link](https://irip-buaa.github.io/posts/OPTIMAL-31) |
| [ORSSD](https://github.com/rmcong/ORSSD-dataset) | Segmentation | [Link](https://irip-buaa.github.io/posts/ORSSD) |
| [RoadTracer](https://github.com/mitroadmaps/roadtracer/) | Segmentation | [Link](https://irip-buaa.github.io/posts/RoadTracer) |
| [Semantic Drone Dataset](https://project.inria.fr/aerialimagelabeling/) | Segmentation | [Link](https://irip-buaa.github.io/posts/Semantic-Drone-Dataset) |
| [SEN12MS](https://mediatum.ub.tum.de/1474000) | Segmentation | [Link](https://irip-buaa.github.io/posts/SEN12MS) |
| [WHU Building Dataset](https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHU-Building-Dataset) |
| [95-Cloud](https://github.com/SorourMo/95-Cloud-An-Extension-to-38-Cloud-Dataset) | Segmentation | [Link](https://irip-buaa.github.io/posts/95-Cloud) |
| [BDCI2020](https://www.datafountain.cn/competitions/475) | Segmentation | [Link](https://irip-buaa.github.io/posts/BDCI2020) |
| [BH-POOLS](http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/) | Segmentation | [Link](https://irip-buaa.github.io/posts/BH-POOLS) |
| [BH-WATERTANKS](http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/) | Segmentation | [Link](https://irip-buaa.github.io/posts/BH-WATERTANKS) |
| [Change-Detection-dataset-for-High-resolution-Satellite-Image](https://github.com/daifeng2016/Change-Detection-Dataset-for-High-Resolution-Satellite-Imagery) | Change Detection | [Link](https://irip-buaa.github.io/posts/Change-Detection-dataset-for-High-resolution-Satellite-Image) |
| [Continual Learning Benchmark for Remote](https://github.com/lehaifeng/CLRS) | Classification | [Link](https://irip-buaa.github.io/posts/Continual-Learning-Benchmark-for-Remote) |
| [DroneCrowd](https://github.com/VisDrone/VisDrone-Dataset) | Detection | [Link](https://irip-buaa.github.io/posts/DroneCrowd) |
| [EORSSD](https://github.com/rmcong/EORSSD-dataset) | Segmentation | [Link](https://irip-buaa.github.io/posts/EORSSD) |
| [HRSID](https://github.com/chaozhong2010/HRSID) | Detection | [Link](https://irip-buaa.github.io/posts/HRSID) |
| [landcover_ai](https://landcover.ai.linuxpolska.com/) | Segmentation | [Link](https://irip-buaa.github.io/posts/landcover_ai) |
| [LEVIR-CD](https://chenhao.in/LEVIR/) | Change Detection | [Link](https://irip-buaa.github.io/posts/LEVIR-CD) |
| [MLRSNet](https://data.mendeley.com/datasets/7j9bv9vwsx/2) | Classification | [Link](https://irip-buaa.github.io/posts/MLRSNet) |
| [The "AiRound" part in Multi-View Datasets](http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/) | Classification | [Link](https://irip-buaa.github.io/posts/Multi-View-Datasets中的AiRound部分) |
| [The "CV-BrCT" part in Multi-View Datasets](http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/) | Classification | [Link](https://irip-buaa.github.io/posts/Multi-View-Datasets中的CV-BrCT部分) |
| [RarePlanes](https://www.cosmiqworks.org/RarePlanes/) | Detection | [Link](https://irip-buaa.github.io/posts/RarePlanes) |
| [SEmantic Change detectiON Data(SECOND)](https://captain-whu.github.io/SCD/) | Change Detection | [Link](https://irip-buaa.github.io/posts/SEmantic-Change-detectiON-Data(SECOND)) |
| [SenseEarth ChangeDetection](https://rs.sensetime.com/competition/index.html#/info) | Change Detection | [Link](https://irip-buaa.github.io/posts/SenseEarth-ChangeDetection) |
| [Sentinel-2 Cloud Mask Catalogue](https://zenodo.org/record/4172871) | Segmentation | [Link](https://irip-buaa.github.io/posts/Sentinel-2-Cloud-Mask-Catalogue) |
| [Sentinel-2 Multitemporal Cities Pairs](https://zenodo.org/records/4280482) | Change Detection | [Link](https://irip-buaa.github.io/posts/Sentinel-2-Multitemporal-Cities-Pairs) |
| [UAVid](https://www.uavid.nl/) | Segmentation | [Link](https://irip-buaa.github.io/posts/UAVid) |
| [WHU Cloud Dataset](http://gpcv.whu.edu.cn/data/WHU_Cloud_Dataset.html) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHU-Cloud-Dataset) |
| [WHU Multi-view Dataset](http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html) | Image Generation | [Link](https://irip-buaa.github.io/posts/WHU-Multi-view-Dataset) |
| [WHU Stereo Dataset](http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html) | Image Generation | [Link](https://irip-buaa.github.io/posts/WHU-Stereo-Dataset) |
| [xBD](https://xview2.org/dataset) | Change Detection | [Link](https://irip-buaa.github.io/posts/xBD) |
| [全国人工智能大赛AI遥感影像](https://www.datafountain.cn/competitions/457/datasets) | Segmentation | [Link](https://irip-buaa.github.io/posts/全国人工智能大赛AI遥感影像) |
| [CASIA-aircraft](https://www.rsaicp.com/portal/dataDetail?id=16) | Detection | [Link](https://irip-buaa.github.io/posts/CASIA-aircraft) |
| [CASIA-Ship](https://aistudio.baidu.com/datasetdetail/131586) | Detection | [Link](https://irip-buaa.github.io/posts/CASIA-Ship) |
| [DOTA2.0](https://captain-whu.github.io/DOTA/index.html) | Detection | [Link](https://irip-buaa.github.io/posts/DOTA2.0) |
| [FAIR1M](https://huggingface.co/datasets/blanchon/FAIR1M) | Detection | [Link](https://irip-buaa.github.io/posts/FAIR1M) |
| [LEVIR-CD2](https://www.rsaicp.com/portal/dataDetail?id=27) | Change Detection | [Link](https://irip-buaa.github.io/posts/LEVIR-CD2) |
| [LoveDA](https://github.com/Junjue-Wang/LoveDA) | Segmentation | [Link](https://irip-buaa.github.io/posts/LoveDA) |
| [MillionAID](https://captain-whu.github.io/DiRS/) | Classification | [Link](https://irip-buaa.github.io/posts/MillionAID) |
| [NaSC-TG2](http://www.msadc.cn/main/setsubDetail?id=1370312964720037889) | Classification | [Link](https://irip-buaa.github.io/posts/NaSC-TG2) |
| [S2Looking](https://www.rsaicp.com/portal/dataDetail?id=30) | Change Detection | [Link](https://irip-buaa.github.io/posts/S2Looking) |
| [SeCo](https://github.com/ServiceNow/seasonal-contrast) | Single-modal Pre-training | [Link](https://irip-buaa.github.io/posts/SeCo) |
| [Sun Yat-Sen University (SYSU)-CD](https://github.com/liumency/SYSU-CD) | Change Detection | [Link](https://irip-buaa.github.io/posts/Sun-Yat-Sen-University-(SYSU)-CD) |
| [TG1HRSSC](http://www.msadc.cn/main/setsubDetail?id=1369487569196158978) | Classification | [Link](https://irip-buaa.github.io/posts/TG1HRSSC) |
| [VISO-Detection](https://satvideodt.github.io/) | Detection | [Link](https://irip-buaa.github.io/posts/VISO-Detection) |
| [WHU TCL SatMVS dataset1.0](http://gpcv.whu.edu.cn/data/whu_tlc.html) | Image Generation | [Link](https://irip-buaa.github.io/posts/WHU-TCL-SatMVS-dataset1.0) |
| [WHU TCL SatMVS dataset2.0](http://gpcv.whu.edu.cn/data/whu_tlc.html) | Image Generation | [Link](https://irip-buaa.github.io/posts/WHU-TCL-SatMVS-dataset2.0) |
| [MiniFrance-DFC22](https://www.grss-ieee.org/community/technical-committees/2022-ieee-grss-data-fusion-contest/) | Segmentation | [Link](https://irip-buaa.github.io/posts/MiniFrance-DFC22) |
| [SAMRS](https://github.com/ViTAE-Transformer/SAMRS) | Segmentation | [Link](https://irip-buaa.github.io/posts/SAMRS) |
| [TOV-RS-balanced](https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1) | Classification | [Link](https://irip-buaa.github.io/posts/TOV-RS-balanced) |
| [CACo](https://github.com/utkarshmall13/CACo) | Single-modal Pre-training | [Link](https://irip-buaa.github.io/posts/CACo) |
| [GEO-Bench](https://github.com/ServiceNow/geo-bench) | Evaluation | [Link](https://irip-buaa.github.io/posts/GEO-Bench) |
| [SATIN](https://huggingface.co/datasets/jonathan-roberts1/SATIN) | Classification | [Link](https://irip-buaa.github.io/posts/SATIN) |
| [SatlasPretrain](https://huggingface.co/allenai/satlas-pretrain/tree/main/dataset) | Classification | [Link](https://irip-buaa.github.io/posts/SatlasPretrain) |
| [WHU-Mix (vector) building dataset](http://gpcv.whu.edu.cn/data/whu-mix%20(vector)/whu_mix(vector).html) | Segmentation | [Link](https://irip-buaa.github.io/posts/WHU-Mix-(vector)-building-dataset) |
| [Constellation](https://github.com/zk2172-columbia/constellation-dataset) | Detection | [Link](https://irip-buaa.github.io/posts/Constellation) |
| [Earth Parser Dataset](https://github.com/romainloiseau/EarthParserDataset) | Segmentation | [Link](https://irip-buaa.github.io/posts/Earth-Parser-Dataset) |
| [EarthView](https://huggingface.co/datasets/satellogic/EarthView/tree/main) | Single-modal Pre-training | [Link](https://irip-buaa.github.io/posts/EarthView) |
| [GeoPile-2](https://github.com/boranhan/Geospatial_Foundation_Models) | Multimodal Pre-training | [Link](https://irip-buaa.github.io/posts/GeoPile-2) |
| [HSODBIT-V1](https://pan.baidu.com/s/1AsdnO2-nadxTaq9_9Mo3Eg?pwd=tftf#list/path=%2F) | Detection | [Link](https://irip-buaa.github.io/posts/HSODBIT-V1) |
| [SARDet-100K](https://pan.baidu.com/s/1dIFOm4V2pM_AjhmkD1-Usw?pwd=SARD) | Detection | [Link](https://irip-buaa.github.io/posts/SARDet-100K) |
| [SARSim](https://ieeexplore.ieee.org/document/7559326/) | Detection| - |

## Image+Text

| Dataset Name | Categories | Detailed Info |
|------------|------------|---------------|
| [Sydney-Captions](https://github.com/201528014227051/RSICD_optimal) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/Sydney-Captions) |
| [UCM-Captions](https://github.com/201528014227051/RSICD_optimal) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/UCM-Captions) |
| [RSICD](https://github.com/201528014227051/RSICD_optimal) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/RSICD) |
| [RSVQA-HR](https://rsvqa.sylvainlobry.com/#dataset) | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA-HR) |
| [RSVQA-LR](https://rsvqa.sylvainlobry.com/#dataset) | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA-LR) |
| [TextRS](N/A) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/TextRS) |
| [BigEarthNet-MM](https://bigearth.net/) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/BigEarthNet-MM) |
| [FloodNet](https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021) | VQA | [Link](https://irip-buaa.github.io/posts/FloodNet) |
| [RSIVQA](https://github.com/spectralpublic/RSIVQA) | VQA | [Link](https://irip-buaa.github.io/posts/RSIVQA) |
| [RSVQA×BEN](https://rsvqa.sylvainlobry.com/#dataset) | VQA | [Link](https://irip-buaa.github.io/posts/RSVQA×BEN) |
| [CDVQA](https://github.com/YZHJessica/CDVQA) | VQA | [Link](https://irip-buaa.github.io/posts/CDVQA) |
| [GeoVG](https://sunyuxi.github.io/publication/GeoVG) | Visual Localization | [Link](https://irip-buaa.github.io/posts/GeoVG) |
| [LEVIR-CC](https://github.com/Chen-Yang-Liu/LEVIR-CC-Dataset) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/LEVIR-CC) |
| [NWPU-Captions](https://github.com/HaiyanHuang98/NWPU-Captions) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/NWPU-Captions) |
| [RSITMD](https://github.com/xiaoyuan1996/AMFMN) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/RSITMD) |
| [SSL4EO-S12](https://github.com/zhu-xlab/SSL4EO-S12) | Multimodal Pre-training | [Link](https://irip-buaa.github.io/posts/SSL4EO-S12) |
| [VQA-TextRS](N/A) | VQA | [Link](https://irip-buaa.github.io/posts/VQA-TextRS) |
| [DIOR_RSVG](https://github.com/ZhanYang-nwpu/RSVG-pytorch) | Visual Localization | [Link](https://irip-buaa.github.io/posts/DIOR_RSVG) |
| [LAION-5B](https://huggingface.co/datasets/mikonvergence/LAION-EO) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/LAION-5B) |
| [OPT-RSVG](https://github.com/like413/OPT-RSVG) | Visual Localization | [Link](https://irip-buaa.github.io/posts/OPT-RSVG) |
| [RS5M](https://huggingface.co/datasets/Zilun/RS5M) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/RS5M) |
| [RSICap](https://github.com/Lavender105/RSGPT) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/RSICap) |
| [RSIEval](https://github.com/Lavender105/RSGPT) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/RSIEval) |
| [SkyScript](https://opendatasharing.s3.us-west-2.amazonaws.com/SkyScript) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/SkyScript) |
| [ChatEarthNet](https://github.com/zhu-xlab/ChatEarthNet) | Image-Text Pair | [Link](https://irip-buaa.github.io/posts/ChatEarthNet) |
| [MMEarth](https://github.com/vishalned/MMEarth-data) | Multimodal Pre-training | [Link](https://irip-buaa.github.io/posts/MMEarth) |

## Video

| Dataset Name | Categories | Detailed Info |
|------------|------------|---------------|
| [UAV123](https://aistudio.baidu.com/datasetdetail/91853) | Object Tracking | [Link](https://irip-buaa.github.io/posts/UAV123) |
| [VisDrone2019-MOT](https://github.com/VisDrone/VisDrone-Dataset) | Object Tracking | [Link](https://irip-buaa.github.io/posts/VisDrone2019-MOT) |
| [VisDrone2019-SOT](https://github.com/VisDrone/VisDrone-Dataset) | Object Tracking | [Link](https://irip-buaa.github.io/posts/VisDrone2019-SOT) |
| [VisDrone2019-VID](https://github.com/VisDrone/VisDrone-Dataset) | Detection | [Link](https://irip-buaa.github.io/posts/VisDrone2019-VID) |
| [地空背景下红外图像弱小飞机目标检测跟踪数据集](http://www.csdata.org/p/387/) | Object Tracking | [Link](https://irip-buaa.github.io/posts/地空背景下红外图像弱小飞机目标检测跟踪数据集) |
| [VISO-MOT](https://satvideodt.github.io/) | Object Tracking | [Link](https://irip-buaa.github.io/posts/VISO-MOT) |
| [VISO-SOT](https://satvideodt.github.io/) | Object Tracking | [Link](https://irip-buaa.github.io/posts/VISO-SOT) |
| [复杂背景下红外弱小运动目标检测数据集](https://www.scidb.cn/en/detail?dataSetId=808025946870251520) | Object Tracking | [Link](https://irip-buaa.github.io/posts/复杂背景下红外弱小运动目标检测数据集) |
| [CapERA](https://lcmou.github.io/ERA_Dataset/) | Video Caption | [Link](https://irip-buaa.github.io/posts/CapERA) |

# Model

## Pretrain

|Model Name| Paper Name | Published in | Detailed Info |
|------------|------------|--------------|---------------|
| fMoW | [Functional Map of the World](https://arxiv.org/pdf/1711.07846) | CVPR 2018 | [Link](https://irip-buaa.github.io/posts/Functional-Map-of-the-World) |
| - | [BIGEARTHNET A LARGE-SCALE BENCHMARK ARCHIVE FOR REMOTE SENSINGIMAGE UNDERSTANDING](https://arxiv.org/abs/1902.06148) | IGARSS 2019 | [Link](https://irip-buaa.github.io/posts/BIGEARTHNET-A-LARGE-SCALE-BENCHMARK-ARCHIVE-FOR-REMOTE-SENSINGIMAGE-UNDERSTANDING) |
| - | [Tile2Vec Unsupervised representation learning for spatially distributed data](https://arxiv.org/pdf/1805.02855) | AAAI 2019 | [Link](https://irip-buaa.github.io/posts/Tile2Vec-Unsupervised-representation-learning-for-spatially-distributed-data) |
| - | [Remote Sensing Image Scene Classification with Self-Supervised Paradigm under Limited Labeled Samples](https://arxiv.org/abs/2010.00882) | GRSL 2020 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-Image-Scene-Classification-with-Self-Supervised-Paradigm-under-Limited-Labeled-Samples) |
| GASSL | [Geography-aware self-supervised learning](https://arxiv.org/abs/2011.09980) | ICCV 2021 | [Link](https://irip-buaa.github.io/posts/Geography-aware-self-supervised-learning) |
| MillionAID | [On Creating Benchmark Dataset for Aerial Image Interpretation Reviews, Guidances, and Million-AID](https://arxiv.org/pdf/2006.12485) | JSTARS 2021 | [Link](https://irip-buaa.github.io/posts/On-Creating-Benchmark-Dataset-for-Aerial-Image-Interpretation-Reviews,-Guidances,-and-Million-AID) |
| Seco | [Seasonal ContrastUnsupervised Pre-Training from Uncurated Remote Sensing Data](https://arxiv.org/abs/2103.16607) | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/Seasonal-ContrastUnsupervised-Pre-Training-from-Uncurated-Remote-Sensing-Data) |
| CMC-RSSR | [Self-Supervised Learning of Remote Sensing Scene Representations Using Contrastive Multiview Coding](https://arxiv.org/abs/2104.07070) | CVPR 2021 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Learning-of-Remote-Sensing-Scene-Representations-Using-Contrastive-Multiview-Coding) |
| - | [Advancing plain vision transformer toward remote sensing foundation model](https://arxiv.org/abs/2208.03987) | TGRS 2022 | [Link](https://irip-buaa.github.io/posts/Advancing-plain-vision-transformer-toward-remote-sensing-foundation-model) |
| CSPT | [Consecutive Pre-Training A Knowledge Transfer Learning Strategy with Relevant Unlabeled Data for Remote Sensing Domain](https://www.mdpi.com/2072-4292/14/22/5675) | Remote Sensing 2022 | [Link](https://irip-buaa.github.io/posts/Consecutive-Pre-Training-A-Knowledge-Transfer-Learning-Strategy-with-Relevant-Unlabeled-Data-for-Remote-Sensing-Domain) |
| Levir-KR | [Geographical Knowledge-Driven RepresentationLearning for Remote Sensing Images](https://arxiv.org/pdf/2107.05276) | TGRS 2022 | [Link](https://irip-buaa.github.io/posts/Geographical-Knowledge-Driven-RepresentationLearning-for-Remote-Sensing-Images) |
| - | [Global and Local Contrastive Self-Supervised Learning for Semantic Segmentation of HR Remote Sensing Images](https://arxiv.org/abs/2106.10605) | TGRS 2022 | [Link](https://irip-buaa.github.io/posts/Global-and-Local-Contrastive-Self-Supervised-Learning-for-Semantic-Segmentation-of-HR-Remote-Sensing-Images) |
| SatMAE | [SatMAE Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery](https://arxiv.org/abs/2207.08051) | NeurIPS 2022 | [Link](https://irip-buaa.github.io/posts/SatMAE-Pre-training-Transformers-for-Temporal-and-Multi-Spectral-Satellite-Imagery) |
| RSBYOL | [Self-Supervised Learning for Invariant Representations from Multi-Spectral and SAR Images](https://arxiv.org/abs/2205.02049) | JSTARS 2022 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Learning-for-Invariant-Representations-from-Multi-Spectral-and-SAR-Images) |
| MATTER | [Self-Supervised Material and Texture Representation Learning for Remote Sensing Tasks](https://arxiv.org/abs/2112.01715) | CVPR 2022 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Material-and-Texture-Representation-Learning-for-Remote-Sensing-Tasks) |
| DINO-MM | [Self-supervised vision transformers for joint sar-optical representation learning](https://arxiv.org/abs/2204.05381) | Arxiv 2022 | [Link](https://irip-buaa.github.io/posts/Self-supervised-vision-transformers-for-joint-sar-optical-representation-learning) |
| - | [Semantic segmentation of remote sensing images with self-supervised semantic-aware inpainting](https://ieeexplore.ieee.org/document/9913413) | GRSL 2022 | [Link](https://irip-buaa.github.io/posts/Semantic-segmentation-of-remote-sensing-images-with-self-supervised-semantic-aware-inpainting) |
| - | [A billion-scale foundation model for remote sensing images](https://arxiv.org/abs/2304.05215) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/A-billion-scale-foundation-model-for-remote-sensing-images) |
| - | [A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion](https://ieeexplore.ieee.org/abstract/document/10282433) | IGARSS 2023 | [Link](https://irip-buaa.github.io/posts/A-Self-Supervised-Cross-Modal-Remote-Sensing-Foundation-Model-with-Multi-Domain-Representation-and-Cross-Domain-Fusion) |
| - | [An Empirical Study of Remote Sensing Pretraining](https://arxiv.org/pdf/2204.02825) | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/An-Empirical-Study-of-Remote-Sensing-Pretraining) |
| CACo | [Change-Aware Sampling and Contrastive Learning for Satellite Images](https://openaccess.thecvf.com/content/CVPR2023/html/Mall_Change-Aware_Sampling_and_Contrastive_Learning_for_Satellite_Images_CVPR_2023_paper.html) | CVPR 2023 | [Link](https://irip-buaa.github.io/posts/Change-Aware-Sampling-and-Contrastive-Learning-for-Satellite-Images) |
| CMID | [CMID A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding](https://arxiv.org/abs/2304.09670) | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/CMID-A-Unified-Self-Supervised-Learning-Framework-for-Remote-Sensing-Image-Understanding) |
| CROMA | [CROMA Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders](https://arxiv.org/pdf/2311.00566) | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/CROMA-Remote-Sensing-Representations-with-Contrastive-Radar-Optical-Masked-Autoencoders) |
| MAE | [Cross-Scale MAE A Tale of Multiscale Exploitation in Remote Sensing](https://openreview.net/pdf?id=5oEVdOd6TV) | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/Cross-Scale-MAE-A-Tale-of-Multiscale-Exploitation-in-Remote-Sensing) |
| CtxMIM | [CtxMIM Context-Enhanced Masked Image Modeling for Remote Sensing Image Understanding](https://arxiv.org/abs/2310.00022) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/CtxMIM-Context-Enhanced-Masked-Image-Modeling-for-Remote-Sensing-Image-Understanding) |
| DeCUR | [DeCUR decoupling common & unique representations for multimodal self-supervision](https://arxiv.org/abs/2309.05300) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DeCUR-decoupling-common-&-unique-representations-for-multimodal-self-supervision) |
| DINO-MC | [Extending Global-local View Alignment for Self-supervised Learning with Remote Sensing Imagery](https://arxiv.org/pdf/2303.06670) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/DINO-MC-Self-supervised-Contrastive-Learning-for-Remote-Sensing-Imagery-with-Multi-sized-Local-Crops) |
| EarthPT | [EarthPT a foundation model for Earth Observation](https://arxiv.org/abs/2309.07207) | NeurIPS CCAI workshop 2023 | [Link](https://irip-buaa.github.io/posts/EarthPT-a-foundation-model-for-Earth-Observation) |
| FG-MAE | [Feature Guided Masked Autoencoder for Self-supervised Learning in Remote Sensing](https://arxiv.org/abs/2310.18653) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Feature-Guided-Masked-Autoencoder-for-Self-supervised-Learning-in-Remote-Sensing) |
| - | [FoMo-Bench a multi-modal, multi-scale and multi-task Forest Monitoring Benchmark for remote sensing foundation models](https://arxiv.org/abs/2312.10114) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/FoMo-Bench-a-multi-modal,-multi-scale-and-multi-task-Forest-Monitoring-Benchmark-for-remote-sensing-foundation-models) |
| Prithvi | [Foundation Models for Generalist Geospatial Artificial Intelligence](https://arxiv.org/abs/2310.18660) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Foundation-Models-for-Generalist-Geospatial-Artificial-Intelligence) |
| Presto | [Lightweight, Pre-trained Transformers for Remote Sensing Timeseries](https://arxiv.org/abs/2304.14065) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Lightweight,-Pre-trained-Transformers-for-Remote-Sensing-Timeseries) |
| IaI-SimCLR | [Multi Modal Multi Objective Contrastive Learning for Sentinel 1-2 Imagery](https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Prexl_Multi-Modal_Multi-Objective_Contrastive_Learning_for_Sentinel-12_Imagery_CVPRW_2023_paper.html) | CVPRW 2023 | [Link](https://irip-buaa.github.io/posts/Multi-Modal-Multi-Objective-Contrastive-Learning-for-Sentinel-1-2-Imagery) |
| SAR-JEPA | [Predicting Gradient is Better Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2311.15153v4) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Predicting-Gradient-is-Better-Exploring-Self-Supervised-Learning-for-SAR-ATR-with-a-Joint-Embedding-Predictive-Architecture) |
| RingMo-lite | [RingMo-lite A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework](https://arxiv.org/abs/2309.09003) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RingMo-lite-A-Remote-Sensing-Multi-task-Lightweight-Network-with-CNN-Transformer-Hybrid-Framework) |
| RSPrompter | [Rsprompter Learning to prompt for remote sensing instance segmentation based on visual foundation model](https://arxiv.org/pdf/2306.16269) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Rsprompter-Learning-to-prompt-for-remote-sensing-instance-segmentation-based-on-visual-foundation-model) |
| SatlasPretrain | [SatlasPretrain A Large-Scale Dataset for Remote Sensing Image Understanding](https://arxiv.org/abs/2211.15660) | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/SatlasPretrain-A-Large-Scale-Dataset-for-Remote-Sensing-Image-Understanding) |
| - | [Scale-MAE A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning](https://arxiv.org/abs/2212.14532) | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/Scale-MAE-A-Scale-Aware-Masked-Autoencoder-for-Multiscale-Geospatial-Representation-Learning) |
| TOV-RS | [TOV The original vision model for optical remote sensing image understanding via self-supervised learning](https://arxiv.org/abs/2204.04716) | JSTARS 2023 | [Link](https://irip-buaa.github.io/posts/TOV-The-original-vision-model-for-optical-remote-sensing-image-understanding-via-self-supervised-learning) |
| TOV-RS | [TOV The Original Vision Model for Optical Remote Sensing Image Understanding via Self-Supervised Learning](https://arxiv.org/abs/2204.04716) | JSTARS 2023 | [Link](https://irip-buaa.github.io/posts/TOV The Original Vision-Model-for-Optical-Remote-Sensing-Image-Understanding-via-Self-Supervised-Learning) |
| GFM | [Towards Geospatial Foundation Models via Continual Pretraining](https://arxiv.org/abs/2302.04476) | ICCV 2023 | [Link](https://irip-buaa.github.io/posts/Towards-Geospatial-Foundation-Models-via-Continual-Pretraining) |
| USat | [USat A Unified Self-Supervised Encoder for Multi-Sensor Satellite Imagery](https://arxiv.org/abs/2312.02199) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/USat-A-Unified-Self-Supervised-Encoder-for-Multi-Sensor-Satellite-Imagery) |
| GeoSense | [Generative ConvNet Foundation Model With Sparse Modeling and Low-Frequency Reconstruction for Remote Sensing Image Interpretation](https://ieeexplore.ieee.org/abstract/document/10378718) | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/Generative-ConvNet-Foundation-Model-With-Sparse-Modeling-and-Low-Frequency-Reconstruction-for-Remote-Sensing-Image-Interpretation) |
| GeRSP | [Generic Knowledge Boosted Pre-training ForRemote Sensing Images](https://arxiv.org/pdf/2401.04614) | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/Generic-Knowledge-Boosted-Pre-training-ForRemote-Sensing-Images) |
| MTP | [MTP Advancing Remote Sensing FoundationModel via Multi-Task Pretraining](https://arxiv.org/pdf/2403.13430) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MTP-Advancing-Remote-Sensing-FoundationModel-via-Multi-Task-Pretraining) |
| OFA-Net | [One for All Toward Unified Foundation Models for Earth Vision](https://arxiv.org/abs/2401.07527) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/One-for-All-Toward-Unified-Foundation-Models-for-Earth-Vision) |
| - | [Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery](https://arxiv.org/abs/2403.05419) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/Rethinking-Transformers-Pre-training-for-Multi-Spectral-Satellite-Imagery) |
| RingMo | [RingMo A Remote Sensing Foundation Model With Masked Image Modeling](https://ieeexplore.ieee.org/abstract/document/9844015) | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/RingMo-A-Remote-Sensing-Foundation-Model-With-Masked-Image-Modeling) |
| S2MAE | [S2MAE A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models/blob/main) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/S2MAE-A-Spatial-Spectral-Pretraining-Foundation-Model-for-Spectral-Remote-Sensing-Data) |
| U-BARN | [Self-Supervised Spatio-Temporal Representation Learning of Satellite Image Time Series](https://ieeexplore.ieee.org/document/10414422) | JSTARS 2024 | [Link](https://irip-buaa.github.io/posts/Self-Supervised-Spatio-Temporal-Representation-Learning-of-Satellite-Image-Time-Series) |
| SkySense | [SkySense A Multi-Modal Remote Sensing Foundation Model Towards Universal Interpretation for Earth Observation Imagery](https://arxiv.org/pdf/2312.10115) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/SkySense-A-Multi-Modal-Remote-Sensing-Foundation-Model-Towards-Universal-Interpretation-for-Earth-Observation-Imagery) |
| SpectralGPT | [SpectralGPT Spectral Foundation Model](https://arxiv.org/pdf/2311.07113) | TPAMI 2024 | [Link](https://irip-buaa.github.io/posts/SpectralGPT-Spectral-Foundation-Model) |
| SwiMDiff | [SwiMDiff Scene-wide Matching Contrastive Learning with Diffusion Constraint for Remote Sensing Image](https://arxiv.org/abs/2401.05093) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SwiMDiff-Scene-wide-Matching-Contrastive-Learning-with-Diffusion-Constraint-for-Remote-Sensing-Image) |
| - | [Multi-source remote sensing pretraining based on contrastive self-supervised learning](https://www.mdpi.com/2072-4292/14/18/4632) | Remote Sensing 22 | [Link](https://irip-buaa.github.io/posts/Multi-source-remote-sensing-pretraining-based-on-contrastive-self-supervised-learning) |
| RSICap | [RSGPT: A Remote Sensing Vision Language Model and Benchmark](https://arxiv.org/abs/2307.15266) | Arxiv 2023 | - |
| HyperSIGMA | [HyperSIGMA: Hyperspectral Intelligence Comprehension Foundation Model](https://arxiv.org/abs/2406.11519) | IEEE TPAMI 2025 | [Link](https://github.com/WHU-Sigma/HyperSIGMA) |
| RS-CLIP | [RS-CLIP: Zero shot remote sensing scene classification via contrastive vision-language supervision](https://www.sciencedirect.com/science/article/pii/S1569843223003217) | International Journal of Applied Earth Observation and Geoinformation 2023 | [Link](https://github.com/lx709/RS-CLIP) |
| StreetCLIP   | [Learning generalized zero-shot learners for open-domain image geolocalization](https://arxiv.org/abs/2408.12345) | Arxiv 2024 | - |
| GeoCLAP      | [Learning Tri-modal Embeddings for Zero-Shot Soundscape Mapping](https://arxiv.org/abs/2408.23456) | Arxiv 2024 | - |
| RSDiff       | [Rsdiff: Remote sensing image generation from text using diffusion model](https://arxiv.org/abs/2408.34567) | Arxiv 2024 | - |
| DiffusionSat | [Diffusionsat: A generative foundation model for satellite imagery](https://arxiv.org/abs/2408.45678) | Arxiv 2024 | - |
| CRS-Diff     | [Crs-diff: Controllable generative remote sensing foundation model](https://arxiv.org/abs/2408.56789) | Arxiv 2024 | - |
| MetaEarth    | [Metaearth: A generative foundation model for global-scale remote sensing image generation](https://arxiv.org/abs/2408.67890) | Arxiv 2024 | - |
| Skysensegpt      | [Skysensegpt: A fine-grained instruction tuning dataset and model for remote sensing vision-language understanding](https://arxiv.org/abs/2409.00001) | Arxiv 2024                                              | -                                                             |
| RS-Agent         | [RS-Agent: Automating Remote Sensing Tasks through Intelligent Agents](https://arxiv.org/abs/2409.00002)                      | Arxiv 2024                                              | -                                                             |
| SSLTransformerRS | [Self-Supervised Vision Transformers for Land-Cover Segmentation and Classification](https://arxiv.org/abs/2409.00003)         | Arxiv 2023                                              | -                                                             |
| RingMo-Sense     | [RingMo-Sense: Remote Sensing Foundation Model for Spatiotemporal Prediction via Spatiotemporal Evolution Disentangling](https://arxiv.org/abs/2409.00004) | Arxiv 2023                                              | -                                                             |
| A2-MAE           | [A2-MAE: A spatial-temporal-spectral unified remote sensing pre-training method based on anchor-aware masked autoencoder](https://arxiv.org/abs/2409.00005) | Arxiv 2023                                              | -                                                             |
| MSFE             | [IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium](https://ieeexplore.ieee.org/document/10012345)  | IGARSS 2023                                             | -                                                             |
| GeCo             | [Geographical Supervision Correction for Remote Sensing Representation Learning](https://arxiv.org/abs/2409.00006)             | Arxiv 2023                                              | -                                                             |
| SoftCon          | [Multi-label Guided Soft Contrastive Learning for Efficient Earth Observation Pretraining](https://arxiv.org/abs/2409.00007)     | CVPR 2023                                               | -                                                             |
| Sen12MS          | [SEN12MS--A curated dataset of georeferenced multi-spectral sentinel-1/2 imagery for deep learning and data fusion](https://ieeexplore.ieee.org/document/8765432) | IEEE TGRS 2019                                         | -                                                             |
| BigEarthNet-S2   | [Bigearthnet: A large-scale benchmark archive for remote sensing image understanding](https://ieeexplore.ieee.org/document/8765433) | IEEE TGRS 2019                                         | -                                                             |
| MSAR       | [Large-scale multi-class SAR image target detection dataset-1.0](https://example.com/msar) | IEEE TGRS 2021 | - |
| SAR-Ship   | [SAR target recognition based on cross-domain and cross-task transfer learning](https://example.com/sar-ship) | IEEE Access 2020 | - |
| SAMPLE     | [A SAR dataset for ATR development: the Synthetic and Measured Paired Labeled Experiment (SAMPLE)](https://example.com/sample) | IEEE TGRS 2019 | - |
| DIOR-RSVG  | [Rsvg: Exploring data and models for visual grounding on remote sensing data](https://example.com/dior-rsvg) | IEEE Access 2021 | - |
| Xview      | [xview: Objects in context in overhead imagery](https://example.com/xview) | Arxiv 2017 | - |
| DIOR-R     | [Anchor-free oriented proposal generator for object detection](https://example.com/dior-r) | IEEE TGRS 2020 | - |
| SpaceNetv1 | [Spacenet: A remote sensing dataset and challenge series](https://example.com/spacenetv1) | IGARSS 2017 | - |
| -S2        | [Dynamicearthnet: Daily multi-spectral satellite dataset for semantic change segmentation](https://example.com/-s2) | Arxiv 2021 | - |

## VLM

| Model Name | Paper Name | Published in | Detailed Info |
| - |------------|--------------|---------------|
| - | [Bootstrapping Interactive Image-Text Alignment for Remote Sensing Image Captioning](https://arxiv.org/abs/2312.01191) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Bootstrapping-Interactive-Image-Text-Alignment-for-Remote-Sensing-Image-Captioning) |
| - | [Language-aware domain generalization network for cross-scene hyperspectral image classification](https://arxiv.org/pdf/2209.02700) | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/Language-aware-domain-generalization-network-for-cross-scene-hyperspectral-image-classification) |
| - | [Parameter-Efficient Transfer Learning for Remote Sensing Image-Text Retrieval](https://arxiv.org/abs/2308.12509) | TGRS 2023 | [Link](https://irip-buaa.github.io/posts/Parameter-Efficient-Transfer-Learning-for-Remote-Sensing-Image-Text-Retrieval) |
| RS5M | [RS5M and GeoRSCLIP A Large Scale Vision-Language Dataset and A Large Vision-Language Model for Remote Sensing](https://arxiv.org/abs/2306.11300) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RS5M-and-GeoRSCLIP-A-Large-Scale-Vision-Language-Dataset-and-A-Large-Vision-Language-Model-for-Remote-Sensing) |
| S-CLIP | [S-CLIP Semi-supervised Vision-Language Learning using Few Specialist Captions](https://arxiv.org/abs/2305.14095) | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/S-CLIP-Semi-supervised-Vision-Language-Learning-using-Few-Specialist-Captions) |
| - | [Vlca vision-language aligning model with cross-modal attention for bilingual remote sensing image captioning](https://ieeexplore.ieee.org/abstract/document/10066217) | J SYST ENG ELECTRON 2023 | [Link](https://irip-buaa.github.io/posts/Vlca-vision-language-aligning-model-with-cross-modal-attention-for-bilingual-remote-sensing-image-captioning) |
| RS-CapRet | [Large Language Models for Captioning and Retrieving Remote Sensing Images](https://arxiv.org/abs/2402.06475) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Large-Language-Models-for-Captioning-and-Retrieving-Remote-Sensing-Images) |
| - | [Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment](https://arxiv.org/abs/2312.06960) | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-Vision-Language-Foundation-Models-without-Annotations-via-Ground-Remote-Alignment) |
| RemoteCLIP | [RemoteCLIP A Vision Language Foundation Model for Remote Sensing](https://arxiv.org/abs/2306.11029) | TGRS 2024 | [Link](https://irip-buaa.github.io/posts/RemoteCLIP-A-Vision-Language-Foundation-Model-for-Remote-Sensing) |
| SkyScript | [SkyScript A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing](https://arxiv.org/abs/2312.12856) | AAAI 2024 | [Link](https://irip-buaa.github.io/posts/SkyScript-A-Large-and-Semantically-Diverse-Vision-Language-Dataset-for-Remote-Sensing) |


## MLLM

| Model Name | Paper Name | Published in | Detailed Info |
| - |------------|--------------|---------------|
| RSICap | [RSGPT A Remote Sensing Vision Language Model and Benchmark](https://arxiv.org/abs/2307.15266) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/RSGPT-A-Remote-Sensing-Vision-Language-Model-and-Benchmark) |
| EarthGPT | [EarthGPT A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain](https://arxiv.org/abs/2401.16822) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/EarthGPT-A-Universal-Multi-modal-Large-Language-Model-for-Multi-sensor-Image-Comprehension-in-Remote-Sensing-Domain) |
| Geochat | [GeoChat Grounded Large Vision-Language Model for Remote Sensing](https://arxiv.org/abs/2311.15826) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoChat-Grounded-Large-Vision-Language-Model-for-Remote-Sensing) |
| H2RSVLM | [H2RSVLM Towards Helpful and Honest Remote Sensing Large Vision Language Model](https://arxiv.org/abs/2403.20213) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/H2RSVLM-Towards-Helpful-and-Honest-Remote-Sensing-Large-Vision-Language-Model) |
| LHRS-Instruct | [LHRS-Bot Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model](https://arxiv.org/abs/2402.02544) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/LHRS-Bot-Empowering-Remote-Sensing-with-VGI-Enhanced-Large-Multimodal-Language-Model) |
| Popeye | [Popeye A Unified Visual-Language Model for Multi-Source Ship Detection from Remote Sensing Imagery](https://arxiv.org/abs/2403.03790) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Popeye-A-Unified-Visual-Language-Model-for-Multi-Source-Ship-Detection-from-Remote-Sensing-Imagery) |
| RS-LLaVA | [RS-LLaVA Large Vision Language Model for Joint Captioning and Question Answering in Remote Sensing Imagery](https://www.mdpi.com/2072-4292/16/9/1477) | RS 2024 | [Link](https://irip-buaa.github.io/posts/RS-LLaVA-Large-Vision-Language-Model-for-Joint-Captioning-and-Question-Answering-in-Remote-Sensing-Imagery) |
| SkyEyeGPT | [SkyEyeGPT Unifying Remote Sensing Vision-Language Tasks via Instruction Tuning with Large Language Model](https://arxiv.org/abs/2401.09712) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SkyEyeGPT-Unifying-Remote-Sensing-Vision-Language-Tasks-via-Instruction-Tuning-with-Large-Language-Model) |

## Agent

| Model Name | Paper Name | Published in | Detailed Info |
| - |------------|--------------|---------------|
| Tree-GPT | [Tree-GPT Modular Large Language Model Expert System for Forest Remote Sensing Image Understanding and Interactive Analysis](https://arxiv.org/abs/2310.04698) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Tree-GPT-Modular-Large-Language-Model-Expert-System-for-Forest-Remote-Sensing-Image-Understanding-and-Interactive-Analysis) |
| Change-Agent | [Change-Agent Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis](https://arxiv.org/abs/2403.19646) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Change-Agent-Towards-Interactive-Comprehensive-Remote-Sensing-Change-Interpretation-and-Analysis) |
| - | [Evaluating Tool-Augmented Agents in Remote Sensing Platforms](https://arxiv.org/abs/2405.00709) | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/Evaluating-Tool-Augmented-Agents-in-Remote-Sensing-Platforms) |
| - | [GeoLLM-Engine A Realistic Environment for Building Geospatial Copilots](https://arxiv.org/abs/2404.15500) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM-Engine-A-Realistic-Environment-for-Building-Geospatial-Copilots) |
| ChatGPT | [Remote Sensing ChatGPT Solving Remote Sensing Tasks with ChatGPT and Visual Models](https://arxiv.org/abs/2401.09083) | IGARSS 2024 | [Link](https://irip-buaa.github.io/posts/Remote-Sensing-ChatGPT-Solving-Remote-Sensing-Tasks-with-ChatGPT-and-Visual-Models) |

## Other

| Model Name | Paper Name | Published in | Detailed Info |
| - |------------|--------------|---------------|
| - | [Transforming remote sensing images to textual descriptions](https://www.sciencedirect.com/science/article/pii/S0303243422000678) | INT J APPL EARTH OBS 2022 | [Link](https://irip-buaa.github.io/posts/Transforming-remote-sensing-images-to-textual-descriptions) |
| - | [CSP Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations](https://arxiv.org/abs/2305.01118) | ICML 2023 | [Link](https://irip-buaa.github.io/posts/CSP-Self-Supervised-Contrastive-Spatial-Pre-Training-for-Geospatial-Visual-Representations) |
| GeoCLIP | [GeoCLIP Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization](https://arxiv.org/abs/2309.16020) | NeurIPS 2023 | [Link](https://irip-buaa.github.io/posts/GeoCLIP-Clip-Inspired-Alignment-between-Locations-and-Images-for-Effective-Worldwide-Geo-localization) |
| - | [Good at captioning, bad at counting Benchmarking GPT-4V on Earth observation data](https://arxiv.org/abs/2401.17600) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Good-at-captioning,-bad-at-counting-Benchmarking-GPT-4V-on-Earth-observation-data) |
| - | [On the Promises and Challenges of Multimodal Foundation Models for Geographical, Environmental, Agricultural, and Urban Planning Applications](https://arxiv.org/abs/2312.17016) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/On-the-Promises-and-Challenges-of-Multimodal-Foundation-Models-for-Geographical,-Environmental,-Agricultural,-and-Urban-Planning-Applications) |
| SatCLIP | [SatCLIP Global, General-Purpose Location Embeddings with Satellite Imagery](https://arxiv.org/abs/2311.17179) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/SatCLIP-Global,-General-Purpose-Location-Embeddings-with-Satellite-Imagery) |
| - | [The Potential of Visual ChatGPT for Remote Sensing](https://www.mdpi.com/2072-4292/15/13/3232) | RS 2023 | [Link](https://irip-buaa.github.io/posts/The-Potential-of-Visual-ChatGPT-for-Remote-Sensing) |
| - | [遥感基础模型发展综述与未来设想](N/A) | 遥感学报 2023 | [Link](https://irip-buaa.github.io/posts/遥感基础模型发展综述与未来设想) |
| msGFM | [Bridging Remote Sensors with Multisensor Geospatial Foundation Models](https://arxiv.org/abs/2404.01260) | CVPR 2024 | [Link](https://irip-buaa.github.io/posts/Bridging-Remote-Sensors-with-Multisensor-Geospatial-Foundation-Models) |
| - | [Charting New Territories Exploring the Geographic and Geospatial Capabilities of Multimodal LLMs](https://arxiv.org/abs/2311.14656) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Charting-New-Territories-Exploring-the-Geographic-and-Geospatial-Capabilities-of-Multimodal-LLMs) |
| - | [GeoLLM Extracting Geospatial Knowledge from Large Language Models](https://arxiv.org/abs/2310.06213) | ICLR 2024 | [Link](https://irip-buaa.github.io/posts/GeoLLM-Extracting-Geospatial-Knowledge-from-Large-Language-Models) |
| LeMeViT | [LeMeViT Efficient Vision Transformer with Learnable Meta Tokens for Remote Sensing Image Interpretation](N/A) | IJCAI 2024 | [Link](https://irip-buaa.github.io/posts/LeMeViT-Efficient-Vision-Transformer-with-Learnable-Meta-Tokens-for-Remote-Sensing-Image-Interpretation) |
| MMEarth | [MMEarth Exploring Multi-Modal Pretext Tasks For Geospatial Representation Learning](N/A) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/MMEarth-Exploring-Multi-Modal-Pretext-Tasks-For-Geospatial-Representation-Learning) |
| DOFA | [Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities](https://arxiv.org/abs/2403.15356) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/Neural-Plasticity-Inspired-Foundation-Model-for-Observing-the-Earth-Crossing-Modalities) |
| - | [On the Foundations of Earth and Climate Foundation Models](N/A) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/On-the-Foundations-of-Earth-and-Climate-Foundation-Models) |
| SARATR-X | [SARATR-X A Foundation Model for Synthetic Aperture Radar Images Target Recognition](N/A) | Arxiv 2024 | [Link](https://irip-buaa.github.io/posts/SARATR-X-A-Foundation-Model-for-Synthetic-Aperture-Radar-Images-Target-Recognition) |
| - | [Changes to Captions An Attentive Network for Remote Sensing Change Captioning](https://arxiv.org/abs/2304.01091) | Arxiv 2023 | [Link](https://irip-buaa.github.io/posts/Changes-to-Captions-An-Attentive-Network-for-Remote-Sensing-Change-Captioning) |
| - | [Multi-source interactive stair attention for remote sensing image captioning](https://www.mdpi.com/2072-4292/15/3/579) | RS 2023 | [Link](https://irip-buaa.github.io/posts/Multi-source-interactive-stair-attention-for-remote-sensing-image-captioning) |
