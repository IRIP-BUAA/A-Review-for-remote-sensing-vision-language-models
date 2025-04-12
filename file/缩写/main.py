import re
import json

# LaTeX 表格的字符串内容
latex_text = r"""\begin{figure*}[t]
    \centering
    \resizebox{\textwidth}{!}{
    \begin{forest}
        forked edges, 
        for tree={
            grow=east, 
            reversed=true, 
            anchor=base west, 
            parent anchor=east, 
            child anchor=west, 
            base=left, 
            font=\small, 
            rectangle, 
            draw=hidden-draw, 
            rounded corners, 
            align=left, 
            minimum width=4em, 
            edge+={darkgray,  line width=1pt}, 
            s sep=3pt, 
            inner xsep=2pt, 
            inner ysep=3pt, 
            ver/.style={rotate=90,  child anchor=north,  parent anchor=south,  anchor=center}, 
        }, 
        where level=1{text width=6.3em, font=\scriptsize, }{}, 
        where level=2{text width=7.3em, font=\scriptsize, }{}, 
        where level=3{text width=9.5em, font=\scriptsize, }{}, 
        where level=4{text width=8.0em, font=\scriptsize, }{}, 
        [Remote Sensing Foundation Model,  ver,  color=carminepink!100,  fill=carminepink!15,  text=black
            % First Child Node
            [Architecture,  color=5!100,  fill=5!100,  text=black
                [Vision Models,  color=1!100,  fill=1_1!100,  text=black
                    [CNN-based,  color=1!100,  fill=1_1!100,  text=black
                        [{\,  SMLFR \cite{10378718} and MMEarth \cite{nedungadi2024mmearth}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Transformer-Based,  color=1!100,  fill=1_1!100,  text=black
                        [ {\,  SkySense \cite{guo2024skysense},  Prithvi \cite{jakubik2023foundationmodelsgeneralistgeospatial},  Presto \cite{tseng2024lightweight},  EarthPT \cite{smith2024earthpt},  USat \cite{irvin2023usat},  OFA-Net \cite{xiong2024all},  DOFA \cite{xiong2024neural},   \\ \,  RSPrompter \cite{chen2023rsprompter},  LeMeViT \cite{jiang2024lemevit} ,  HyperSIGMA \cite{wang2024hypersigma}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [CNN-Transformer Hybrid,  color=1!100,  fill=1_1!100,  text=black
                        [{\,  U-BARN \cite{10414422},  RingMo-lite \cite{wang2023ringmolite}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
                [Multimodal Models,  color=2!100,  fill=2_1!100,  text=black
                    [CLIP-based Models,  color=2!100,  fill=2_1!100,  text=black
                        [{\,   RemoteCLIP\cite{remoteclip},  Skyscript\cite{skyscript},  GeoRSCLIP\cite{georsclip},  S-CLIP\cite{s-clip},  RS-CLIP\cite{rs-clip},  Mall et al.\cite{remoteWoAnn},  \\ \, Yang et al.\cite{bootstrapping},  GeoCLIP\cite{geoclip},  SatCLIP\cite{satclip},  AddressCLIP\cite{xu2024addressclip},  StreetCLIP\cite{haas2023learning},  GeoCLAP\cite{geoclap}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Diffusion-based Models,  color=2!100,  fill=2_1!100,  text=black
                        [{\,  RSDiff\cite{sebaq2023rsdiff},  DiffusionSat\cite{diffusionsat},  CRS-Diff\cite{Crs-diff},  MetaEarth\cite{metaearth}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [MLLM,  color=2!100,  fill=2_1!100,  text=black
                        [{\,  LHRS-Bot\cite{lhrs-bot},  H2RSVLM\cite{h2rsvlm},  Geochat\cite{geochat}, Skysensegpt\cite{skysensegpt},  RSGPT\cite{rsgpt},  SkyEyeGPT\cite{skyeyegpt},  \\ \, EarthGPT\cite{earthgpt},   Popeye\cite{popeye},  RS-CapRet\cite{rs-cap},  RSGPT\cite{rsgpt},  RS-LLaVA\cite{rs-llava}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [LLM-based Agent,  color=2!100,  fill=2_1!100,  text=black
                        [{\,  Tree-GPT\cite{treegpt},  Remote Sensing ChatGPT\cite{remote-sense-chatgpt},  Change-Agent\cite{change-agent},  RS-Agent\cite{rs-agent}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
            ]
            [Training Method,  color=6!100,  fill=6!100,  text=black
                [Vision Models,  color=3!100,  fill=3_1!100,  text=black
                    [Contrastive Method,  color=3!100,  fill=3_1!100,  text=black
                        [{\,  CMC-RSSR \cite{Stojnic_2021_CVPR},  DINO-MC \cite{Wanyan_2024_CVPR},  CACo\cite{Mall_2023_CVPR}, GASSL \cite{Ayush_2021_ICCV},  SeCo \cite{Manas_2021_ICCV}, MATTER \cite{Akiva_2022_CVPR}, \\ \, DINO-MC \cite{Wanyan_2024_CVPR},   SSLTransformerRS \cite{Scheibenreif_2022_CVPR},  DINO-MM \cite{wang2022selfsupervised},  RSBYOL \cite{rs_byol_2022},  IaI-SimCLR \cite{Prexl_2023_CVPR},\\ \,  DeCUR \cite{wang2023decurdecouplingcommon},  SkySense \cite{han2024bridging}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Generative Method,  color=3!100,  fill=3_1!100,  text=black
                        [ {\,  Scale-MAE \cite{10377166},  SatMAE++ \cite{noman2024rethinking},  SMLFR \cite{10453587},  SAR-JEPA \cite{li2024predictinggradientbetterexploring}, SatMAE \cite{satmae2022},  RingMo \cite{ringmo_2023},  \\ \, RingMo-Sense \cite{10254320},  CtxMIM \cite{zhang2024ctxmimcontextenhancedmaskedimage},  S2MAE \cite{Li_2024_CVPR},  SpectralGPT \cite{10490262}, FG-MAE \cite{wang2023feature},  msGFM \cite{han2024bridging}, \\ \, A2-MAE \cite{zhang20242}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Contrastive-Generative \\ Hybrid,  color=3!100,  fill=3_1!100,  text=black
                        [{\,  CMID \cite{10105625},  Cross-Scale MAE \cite{tang2024cross},  CROMA \cite{fuller2024croma},  MSFE \cite{10282433}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Geographic Knowledge,  color=3!100,  fill=3_1!100,  text=black
                        [{\,  GeoKR \cite{geokr_2022},  GeCo \cite{geco_2022},  MTP \cite{wang2024mtp},  GeRSP \cite{10400411},  TOV \cite{10110958},  SoftCon \cite{Wang2024MultiLabelGS},  SwiMDiff \cite{10453587},\\ \, CSPT \cite{rs14225675}, GFM \cite{Mendieta_2023_ICCV},  MMEarth \cite{nedungadi2024mmearth},  SARATR-X \cite{yang2024saratr}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
                [Multimodal Models,  color=4!100,  fill=4_1!100,  text=black
                    [Contrastive Learning,  color=4!100,  fill=4_1!100,  text=black
                        [{\,  RemoteCLIP\cite{remoteclip},  Skyscript\cite{skyscript},  GeoRSCLIP\cite{georsclip},  S-CLIP\cite{s-clip},  RS-CLIP\cite{rs-clip},  Mall et al.\cite{remoteWoAnn}, \\ \, Yang et al.\cite{bootstrapping},   GeoCLIP\cite{geoclip},  SatCLIP\cite{satclip},  AddressCLIP\cite{xu2024addressclip},  StreetCLIP\cite{haas2023learning},  GeoCLAP\cite{geoclap}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                    % [Diffusion Training,  color=4!100,  fill=4_1!100,  text=black
                    %     [{\,  SMLFR \cite{10378718} and MMEarth \cite{nedungadi2024mmearth}},  cause_leaf,  text width=34.0em
                    %     ]
                    % ]
                    [Auto Regressive Learning,  color=4!100,  fill=4_1!100,  text=black
                        [{\,  LHRS-Bot\cite{lhrs-bot},  H2RSVLM\cite{h2rsvlm},  Geochat\cite{geochat}, Skysensegpt\cite{skysensegpt},  RSGPT\cite{rsgpt},  SkyEyeGPT\cite{skyeyegpt},  \\ \,EarthGPT\cite{earthgpt},   Popeye\cite{popeye},  RS-CapRet\cite{rs-cap},  RSGPT\cite{rsgpt},  RS-LLaVA\cite{rs-llava}},  cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
            ]
            [Training Dataset,  color=7!100,  fill=7!100,  text=black
                [Vision Models,  color=8!100,  fill=8!100,  text=black
                    [Custom Collected,  color=8!100,  fill=8!100,  text=black
                        [{\,  Seco \cite{Manas_2021_ICCV},  U-BARN \cite{10414422},  MATTER \cite{Akiva_2022_CVPR},  Levir-KR \cite{geokr_2022},  SkySense \cite{guo2024skysense},  GeoSense \cite{10378718},\\ \,  MMEarth \cite{nedungadi2024mmearth},   RingMo \cite{ringmo_2023},  TOV-RS \cite{10110958}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Publicly Available,  color=8!100,  fill=8!100,  text=black
                        [{\, MillionAID \cite{millionaid},  SAMRS \cite{wang2024samrs},  Sen12MS \cite{sen12ms},  BigEarthNet-MM \cite{bigearthnetmm},  SSL4EO \cite{ssl4eo},\\ \,  SatlasPretrain \cite{satlaspretrain},  fMoW \cite{fmow},  fMoW-S2 \cite{satmae2022},  BigEarthNet-S2 \cite{sumbul2019bigearthnet},  MSAR \cite{chen2022large}, \\ \, SAR-Ship \cite{wang2019sar},  SARSim \cite{ kusk2016synthetic},  SAMPLE \cite{lewis2019sar}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
                [Multimodal Models,  color=9!100,  fill=9!100,  text=black
                    [VLM,  color=9!100,  fill=9!100,  text=black
                        [{\, UCM-Caption \cite{qu2016deep},  RSICD \cite{lu2017exploring},  RSITMD \cite{yuan2022exploring},  DOTA \cite{dota},  DIOR \cite{dior},  fMoW \cite{fmow},  \\ \, MillionAID \cite{millionaid},  UCM \cite{yang2010bag},  NWPU-RESISC45 \cite{cheng2017remote},  SkyScript \cite{skyscript},  RS5M \cite{georsclip}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                    [MLLM,  color=9!100,  fill=9!100,  text=black
                        [{\, UCM \cite{yang2010bag},  NWPU-RESISC45 \cite{cheng2017remote},  UCM-Caption \cite{qu2016deep},  Sydney-Caption \cite{qu2016deep}, RSICD \cite{lu2017exploring}, \\ \,   NWPU-Caption \cite{cheng2022nwpu},   RSITMD \cite{yuan2022exploring},  RSVQA-LR \cite{lobry2020rsvqa},  RSVQA-HR \cite{lobry2020rsvqa},  RSIVQA \cite{zheng2021mutual}, \\ \,   FloodNet \cite{rahnemoonfar2021floodnet},  DOTA \cite{dota},  DIOR \cite{dior},  FAIR1M \cite{fair1m},  fMoW \cite{fmow},  MillionAID \cite{millionaid},  RSVG \cite{sun2022visual}, \\ \,   DIOR-RSVG \cite{zhan2023rsvg},  RSICap \cite{rsgpt},  LHRS-Align \cite{lhrs-bot},  LHRS-Instruct \cite{lhrs-bot}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                ]    
            ]
            [Evaluation,  color=10!100,  fill=10!100,  text=black
                [Vision Models,  color=11!100,  fill=11!100,  text=black
                    [Downstream Tasks,  color=11!100,  fill=11!100,  text=black
                        [{\,  Scene Classification  (Section \ref{sec: task_vis_cls}),  Object Detection  (Section \ref{sec: task_vis_object}),  \\ \, Semantic Segmentation  (Section \ref{sec: task_vis_segmen}),  Change Detection (Section \ref{sec: task_vis_change})}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Evaluation Datasets,  color=11!100,  fill=11!100,  text=black
                        [{\,  NWPU-RESISC45 \cite{cheng2017remote},  EuroSAT \cite{helber2019eurosat},  AID \cite{xia2017aid},  Xview \cite{xview},  DIOR \cite{dior},  DIOR-R \cite{diorr},  FAIR1M \cite{fair1m}, \\ \,  DOTA \cite{dota},  SpaceNetv1 \cite{spacenet},  LoveDA \cite{loveda},  iSAID \cite{isaid},  Dyna.-Pla. \cite{dynamicearthnet},  Dyna.-S2 \cite{dynamicearthnet},\\ \,   OSCD \cite{daudt2018urban},  LEVIR \cite{chen2020spatial}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                ]
                [Multimodal Models,  color=12!100,  fill=12!100,  text=black
                    [Downstream Tasks,  color=12!100,  fill=12!100,  text=black
                        [{\, Scene Classification (Section \ref{sec: task_mllm_scene}), Image Captioning (Section \ref{sec: task_mllm_caption}),  \\ \, Visual Question Answering (Section \ref{sec: task_mllm_vqa}), Visual Grounding (Section \ref{sec: task_mllm_grounding}), \\ \, Cross-Modal Retrieval (Section \ref{sec: task_mllm_retrieval})}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                    [Evaluation Datasets,  color=12!100,  fill=12!100,  text=black
                        [{\,  EuroSAT \cite{helber2019eurosat},  NWPU-RESISC45 \cite{cheng2017remote},  WHU-RS19 \cite{dai2010satellite},  AID \cite{isaid},  SIRI-WHU \cite{zhao2015dirichlet}, \\ \, UCM-Caption \cite{qu2016deep},   Sydney-Caption \cite{qu2016deep},  RSICD \cite{lu2017exploring},  NWPU-Captions \cite{cheng2022nwpu},  RSITMD \cite{yuan2022exploring}, \\ \, RSVQA \cite{lobry2020rsvqa}, FloodNet \cite{rahnemoonfar2021floodnet},   RSIVQA \cite{zheng2021mutual},  RSVG,  DIOR-RSVG \cite{zhan2023rsvg}}
                        , cause_leaf,  text width=34.0em
                        ]
                    ]
                ]  
            ]
        ]
    \end{forest}
    }
    \caption{Organization and Taxonomy of this article.}
    \label{figure:categorization_of_survey}
\end{figure*}
"""

# 正则表达式匹配模式
# 这里匹配形如：<缩写> \cite{<bib_key>}
pattern = r"([\w-]+)\s*\\cite\{([^}]+)\}"

# 找出所有匹配的项，返回一个列表，每项为 (缩写, bib_key)
matches = re.findall(pattern, latex_text)

# 输出匹配结果（用于调试）
print("匹配到的缩写及 bib_key:", matches)

# 读取 paper.bib 文件内容
bib_filename = "paper.bib"
with open(bib_filename, "r", encoding="utf-8") as f:
    bib_content = f.read()

def get_title_for_key(key, bib_text):
    """
    根据给定的 bib 条目的 key，在 bib_text 中查找对应的 title 字段
    使用 re.DOTALL 来处理多行情况。
    """
    # 构造正则表达式，匹配 @article 或其他类型的条目中 key 对应的 entry，并提取 title 字段
    pattern = re.compile(
        r"@[\w]+\{" + re.escape(key) + r",.*?title\s*=\s*\{([^}]+)\}",
        re.DOTALL | re.IGNORECASE
    )
    match = pattern.search(bib_text)
    if match:
        return match.group(1).strip()
    else:
        return None

# 构建缩写与论文标题的映射
result_mapping = {}
for abbr, bib_key in matches:
    title = get_title_for_key(bib_key, bib_content)
    if title:
        result_mapping[abbr] = title
    else:
        result_mapping[abbr] = "未找到对应条目"  # 或者也可以将其省略

# 将结果保存为 JSON 文件
output_filename = "result.json"
with open(output_filename, "w", encoding="utf-8") as outfile:
    json.dump(result_mapping, outfile, ensure_ascii=False, indent=4)

print(f"结果已保存到 {output_filename}")
