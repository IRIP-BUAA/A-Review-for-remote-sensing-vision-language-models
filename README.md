# A-Review-for-remote-sensing-vision-language-models
This is a repository for ...
## Overleaf
https://www.overleaf.com/5469324254jsdvcqwcsmzz#0edfd1

## Table of Contents
- [A-Review-for-remote-sensing-vision-language-models](#a-review-for-remote-sensing-vision-language-models)
  - [Overleaf](#overleaf)
  - [Table of Contents](#table-of-contents)
- [Types of Remote Sensing Vision Language Models](#types-of-remote-sensing-vision-language-models)
  - [1](#1)
  - [2](#2)
- [Dataset](#dataset)
  - [汇总](#汇总)
  - [分类](#分类)
  - [检测](#检测)
  - [分割](#分割)
  - [变化检测](#变化检测)
  - [目标跟踪](#目标跟踪)
  - [图像生成](#图像生成)
  - [单模态预训练](#单模态预训练)
  - [评估](#评估)
  - [VQA](#vqa)
  - [图文对](#图文对)
  - [视觉定位](#视觉定位)
  - [多模态预训练](#多模态预训练)



# Types of Remote Sensing Vision Language Models
## 1
<table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.09712'>SkyEyeGPT: Unifying Remote Sensing Vision-Language Tasks via Instruction Tuning with Large Language Model</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1.遥感领域的视觉语言指令数据集（SkyEye968k），包括单任务和多任务对话指令，包括968k条样本的指令跟随数据集2. 提出SkyEyeGPT模型，通过一个对齐层将RS视觉特征投影到语言领域后，它们与任务特定的指令一起被馈送到基于LLM的RS解码器中；设计了一个两阶段微调方法，第一阶段是遥感图文对齐，第二阶段是多任务对话微调</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：EVA-CLIPText Encoder：LLaMA2-chat</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption, Visual Grounding, RS VQA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ZhanYang-nwpu/SkyEyeGPT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2311.15826'>GeoChat: Grounded Large Vision-Language Model for Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. RS多模态数据集：多模态数据集，且提出了一个生成数据的pipeline2. GeoChat：利用已有的数据微调LLaVA-1.5，利用lora微调；除了能够处理自然语言问题之外，用户还可以提供视觉提示（bounding box），并且模型能够回答有关ROI（指定感兴趣区域）的问题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP-ViTText Encoder： Vicuna-v1.5</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, RS VQA, Visual Grounding</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/mbzuai-oryx/geochat</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>CVPR 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2307.15266'>RSGPT: A Remote Sensing Vision Language Model and Benchmark</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 提出RSICap数据集，基于 DOTA 目标检测数据集构建了 RSICap2. 提出RSIEval评估集3. RSGPT模型，现成的冻结的预训练图像编码器（EVA-G）和大型语言模型（vicuna7b，vicuna13b）构成了该模型的基础，并通过微调Q-Former和线性层结构</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：EVAText Encoder：Vicuna</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption, RS VQA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2306.11029'>RemoteCLIP: A Vision Language Foundation Model for Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>CNN, Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>(CLIP)Vision Encoder:ResNet-50/ViT-Base/ViT-LargeText Encoder：Transformer Architecture</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image-text Retrieval, Scene Classification, Object Counting</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ChenDelong1999/RemoteCLIP</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>awesome-remote-sensing-vision-language-models</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>TGRS 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.06960'>Remote Sensing Vision-Language Foundation Models without Annotations via Ground Remote Alignment</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>介绍了一种在不使用任何文本注释，为遥感图像训练视觉语言模型的方法。关键是利用地面上拍摄的共同位置的互联网图像作为连接遥感图像和语言的中介</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-B</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, RS VQA, Semantic Segmentation, Image-text Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>提出了一种训练遥感图像的视觉-语言模型的方法</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>ICLR 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.09083'>Remote Sensing ChatGPT: Solving Remote Sensing Tasks with ChatGPT and Visual Models</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Agent</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 在chatgpt的基础上构建了remote sensing chatgpt。工作流程包括提示模板生成、任务规划、任务执行和响应生成。    2. 针对LLM无法直接感知遥感图像，设计了visual cues，将视觉信息注入到chatgpt</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>gpt-3.5-turbo/gpt-4</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/HaonanGuo/Remote-Sensing-ChatGPT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>IGARSS 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.16822'>EarthGPT: A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 提出了一种同一集成各种多传感器遥感解释任务的MLLM，EarthGPT，提出了视觉增强感知机制和跨模态相互理解的方法，最后提出了一种遥感领域的多传感器多任务的统一指令微调方法 2. 构建了最大的多模态多传感器的遥感指令跟随数据集MMRS-1M，由超过100万个图像文本对组成，包括有光学、合成孔径雷达（SAR）和红外图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>CNN, Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：DINOv2 ViT-L/14、CLIP ConvNeXt-LText Encoder：LLaMA-2</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, Image Caption, Visual Grounding, RS VQA, Object Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/wivizhang/EarthGPT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.12856'>SkyScript: A Large and Semantically Diverse Vision-Language Dataset for Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>(CLIP)Vision Encoder: ViT-B/ViT-LText Encoder：Transformer Architecture</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, Image-text Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/wangzhecheng/SkyScript</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>主要是构建数据集</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>AAAI 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2402.02544'>LHRS-Bot: Empowering Remote Sensing with VGI-Enhanced Large Multimodal Language Model</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 提出LHRS-Align数据集：大规模遥感领域的图像文本数据集，使用开源的全球地理数据生成的。2. 提出了LHRS-Instruct数据集，是一个专门为遥感图像理解定制的多模态指令跟随数据集。3. 在此基础上，提出了LHRS-Bot模型，采用了新的bridging strategy，并利用课程学习的方法来充分挖掘数据集种的内在知识4. 提出LHRS-Bench，用于对遥感领域的MLLM进行评估，包含690个单选题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-LText Encoder：LLaMA-2</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, RS VQA, Visual Grounding</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/NJU-LHRS/LHRS-Bot</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2403.20213'>H2RSVLM: Towards Helpful and Honest Remote Sensing Large Vision Language Model</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 创建了HqDC-1.4M数据集，还构建了两个指令微调数据集HqDC-Instruct和RS-Specialized-Instruct    2. 针对幻觉问题，构建了第一个遥感self-awareness数据集，RSSA。包含一系列可回答和不可回答的任务    3. 基于上述数据，通过预训练和监督微调两个步骤，基于LLaVA模型训练了H2RSVLM模型（helpfulness 和 honesty）</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-LText Encoder：Vicuna-v1.5</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, RS VQA, Visual Grounding</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/opendatalab/H2RSVLM</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://www.mdpi.com/2072-4292/16/9/1477'>RS-LLaVA: Large Vision Language Model for Joint Captioning and Question Answering in Remote Sensing Imagery</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 通过集成caption和VQA数据集，提出了一个遥感领域的指令微调数据集2. 基于LLaVA模型，通过使用遥感数据对模型进行预训练和lora微调得到了了RS-LLaVA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-LText Encoder：Vicuna-v1.5</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption, RS VQA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/BigData-KSU/RS-LLaVA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>RS 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2305.14095'>S-CLIP: Semi-supervised Vision-Language Learning using Few Specialist Captions</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>提出了一种半监督学习方法，用于在少量专家标注的字幕情况下训练CLIP模型。S-CLIP利用额外的未配对图像，并通过两种伪标签策略增强对比学习和语言模态的训练。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>(CLIP)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, Image-text Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/alinlab/s-clip</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>awesome-remote-sensing-vision-language-models</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>NeurIPS 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2306.11300'>RS5M and GeoRSCLIP: A Large Scale Vision-Language Dataset and A Large Vision-Language Model for Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>(CLIP)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification, Image-text Retrieval, Semantic Localization</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>awesome-remote-sensing-vision-language-models</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2305.01118'>CSP: Self-Supervised Contrastive Spatial Pre-Training for Geospatial-Visual Representations</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://gengchenmai.github.io/csp-website/</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>vision-location</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>ICML 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2309.16020'>GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-L</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/VicenteVivan/geo-clip</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>vision-location</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>NeurIPS 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2311.17179'>SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/microsoft/satclip</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>vision-location</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2310.04698'>Tree-GPT: Modular Large Language Model Expert System for Forest Remote Sensing Image Understanding and Interactive Analysis</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Agent</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>gpt-4</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2402.06475'>Large Language Models for Captioning and Retrieving Remote Sensing Images</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption, Image-text Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>Image Caption & Text-image Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2403.03790'>Popeye: A Unified Visual-Language Model for Multi-Source Ship Detection from Remote Sensing Imagery</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>MLLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>1. 设计了一种image-to-caption的方法来统一各种船只检测数据集，基于现有的公开数据集构建了一个多模态多源指令跟随数据集MMShip（统一标记范式）  2. 提出Popeye架构，主要包括四个部分，统一标记范式、跨模态图像解释方法（通过多尺度多模态特征融合模块和视觉-语言对齐调整模块实现视觉-语言对齐，在 COCO Caption 数据集上对齐）、knowledge adaption paradigm（在 MMShip 数据集上进行船只领域适应阶段的训练）、与 SAM（Segment Anything Model）的集成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-L、DINOv2 ViT-LText Encoder：LLaMA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Ship Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2209.02700'>Language-aware domain generalization network for cross-scene hyperspectral image classification</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：deep residual 3D CNN networkText Encoder：Transformer Architecture</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Scene Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>Vision-Language Models in Remote Sensing: Current Progress and Future Trends</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>IEEE Transactions on Geoscience and Remote Sensing 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2311.14656'>Charting New Territories: Exploring the Geographic and Geospatial Capabilities of Multimodal LLMs</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>评估MLLM在遥感领域的能力</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2310.06213'>GeoLLM: Extracting Geospatial Knowledge from Large Language Models</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>GeoLLM 提出了一种方法，可以从 LLMs 中提取大量的地理空间知识，并通过 OpenStreetMap 的辅助地图数据进行微调</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>RoBERTa、LLaMA-2、GPT-3.5</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/rohinmanvi/GeoLLM/</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>ICLR 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://www.sciencedirect.com/science/article/pii/S0303243422000678'>Transforming remote sensing images to textual descriptions</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>nan</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：ResNetText Encoder：Transformer Architecture</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>INT J APPL EARTH OBS 2022</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/abstract/document/10066217'>Vlca: vision-language aligning model with cross-modal attention for bilingual remote sensing image captioning</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>CNN, Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP（ResNet50/ViT）Text Encoder：GPT-2</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>J SYST ENG ELECTRON 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://www.mdpi.com/2072-4292/15/3/579'>Multi-source interactive stair attention for remote sensing image captioning</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>nan</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>RS 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2304.01091'>Changes to Captions: An Attentive Network for Remote Sensing Change Captioning</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>nan</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/shizhenchang/chg2cap</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.01191'>Bootstrapping Interactive Image-Text Alignment for Remote Sensing Image Captioning</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>Vision Encoder：CLIP ViT-LText Encoder：OPT-2.7B</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/yangcong356/BITA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2403.19646'>Change-Agent: Towards Interactive Comprehensive Remote Sensing Change Interpretation and Analysis</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Agent</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Change Detection, Change Caption</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/Chen-Yang-Liu/Change-Agent</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2405.00709'>Evaluating Tool-Augmented Agents in Remote Sensing Platforms</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Agent</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>提出了一个新的基准测试GeoLLM-QA，用于评估和理解工具增强型LLMs在遥感平台上的性能和潜力</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>评估</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>ICLR 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2404.15500'>GeoLLM-Engine: A Realistic Environment for Building Geospatial Copilots</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Agent</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>gpt-3.5-turbo/gpt-4</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>CVPR 2024</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2308.12509'>Parameter-Efficient Transfer Learning for Remote Sensing Image-Text Retrieval</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>VLM</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>构建了一个新颖的PETL框架，用于RS图像-文本检索任务，其中包括预训练的CLIP、多模态遥感adapter和混合多模态对比（HMMC）学习目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>Image-text Retrieval</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ZhanYang-nwpu/PE-RSITR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>偏向PETL方向</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>TGRS 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2405.04285.pdf'>On the Foundations of Earth and Climate Foundation Models</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://www.mdpi.com/2072-4292/15/13/3232'>The Potential of Visual ChatGPT for Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>设计实验对Visual Chatgpt在遥感领域的能力进行了测试评估</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>评估</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>RS 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.17600'>Good at captioning, bad at counting: Benchmarking GPT-4V on Earth observation data</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>提出了一个benchmark，用于评估VLMs在地球观测数据上的表现，特别是在场景理解、定位和计数以及变化检测任务上</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://vleo.danielz.ch/</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>评估</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='9' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.17016'>On the Promises and Challenges of Multimodal Foundation Models for Geographical, Environmental, Agricultural, and Urban Planning Applications</a></td>
    <td style='text-align: left; width:10%;'>Tag</td>
    <td style='text-align: left; width:20%;'>Other</td>
    <td rowspan='9' style='text-align: left; width:40%;word-wrap: break-word;'>评估GPT-4V模型在地理、环境科学、农业和城市规划多个领域的能力</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Visual Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Text Encoder</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Model Details</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Task</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>评估</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Published in</td>
    <td style='text-align: left;'>Arxiv 2023</td>
  </tr>
</table>
## 2
<table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2204.02825'>An Empirical Study of Remote Sensing Pretraining</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>提出了RS pretraining的概念。测试了CNN和VIT模型和一些增强方式。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ViTAE-Transformer/ViTAE-Transformer-Remote-Sensing</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>有监督预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2103.16607'>Seasonal Contrast:Unsupervised Pre-Training from Uncurated Remote Sensing Data</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR 2021</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>利用未标记数据进行遥感表示的领域内预训练。首先，是一个有原则的程序，用于收集大规模、未标记且未筛选的遥感数据集，其中包含来自不同地点、不同时间戳的图像。其次，是一种自监督算法，利用时间和位置的不变性来学习可转移的遥感应用表示。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ElementAI/seasonal-contrast</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，利用未标注数据</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://www.mdpi.com/2072-4292/14/18/4632'>Multi-source remote sensing pretraining based on contrastive self-supervised learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Remote Sensing 22</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>研究了基于对比自监督学习（CSSL）方法的预训练模型在SAR-光学遥感分类中的有效性</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，利用未标注数据</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2011.09980'>Geography-aware self-supervised learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>ICCV 21</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>利用随时间空间对齐的图像构建了对比学习中的时间正样本对，并利用地理定位设计了预文本任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/sustainlab-group/geography-aware-ssl</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，利用未标注数据</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/1805.02855'>Tile2Vec: Unsupervised representation learning for spatially distributed data</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>AAAI 19</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>主要目标是从未标记的数据中学习语义上有意义的表示，类似于自然语言处理中的词向量。Tile2Vec 利用分布假设，其中假设地理邻居具有相似的语义和表示。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ermongroup/tile2vec</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>半监督，利用未标记数据</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/document/9913413'>Semantic segmentation of remote sensing images with self-supervised semantic-aware inpainting</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Geoscience and Remote Sensing Letters 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>通过基于对抗学习的掩码和重建学习更适配语义分割的预训练特征</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/JasmineBJTU/self-supervised_RSSS</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，用于语意分割</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2204.04716'>TOV: The Original Vision Model for Optical Remote Sensing Image Understanding via Self-Supervised Learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 23</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>通过大量未标记的光学数据沿着类似人类的自监督学习(SSL)路径进行训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/abstract/document/9844015'>RingMo: A Remote Sensing Foundation Model With Masked Image Modeling </a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>提出了一种针对遥感图像中密集小目标的PIMask采样策略，即对遮挡补丁进行二次像素采样以暴露小目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>-</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>利用 生成式自监督学习 进行预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2208.03987'>Advancing plain vision transformer toward remote sensing foundation model</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ViTAE-Transformer/Remote-Sensing-RVSA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督掩码图像建模方法MAE对网络进行预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2306.16269'>Rsprompter: Learning to prompt for remote sensing instance segmentation based on visual foundation model</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv 2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>考虑基于 SAM 基础模型设计一种自动化实例分割方法，该方法将语义类别信息纳入其中，用于遥感图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://kyanchen.github.io/RSPrompter</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2311.07113'>SpectralGPT: Spectral Foundation Model</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>TPAMI2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>虽然大多数基础模型都是为了有效地处理各种视觉任务的RGB图像而定制的，但在光谱数据方面的研究存在明显的差距。采用MAE架构构建，多目标重建策略；generative pretrained transformer(GPT)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/danfenghong/IEEE_TPAMI_SpectralGPT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督MAE，以渐进式训练方式在多个数据集上进行训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2401.04614'>Generic Knowledge Boosted Pre-training ForRemote Sensing Images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/floatingstarZ/GeRSP</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督遥感+有监督自然图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2403.13430'>MTP: Advancing Remote Sensing FoundationModel via Multi-Task Pretraining</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv 2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>共享backbone+多任务头</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ViTAE-Transformer/MTP</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多任务监督预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://www.mdpi.com/2072-4292/14/22/5675'>Consecutive Pre-Training: A Knowledge Transfer Learning Strategy with Relevant Unlabeled Data for Remote Sensing Domain</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Remote Sensing 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>（1）在大规模未标记数据集（如ImageNet [18]）上进行自监督预训练；（2）在与任务相关的未标记遥感数据上进一步进行自监督预训练；（3）在多样化的下游任务上进行微调。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/ZhAnGToNG1/transfer_learning_cspt</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督+持续预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/1711.07846'>Functional Map of the World</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR 18</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>主要在数据集，没有特殊的训练方法</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/fMoW</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据集+有监督训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/1902.06148'>BIGEARTHNET: A LARGE-SCALE BENCHMARK ARCHIVE FOR REMOTE SENSINGIMAGE UNDERSTANDING</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE International Geoscience and Remote Sensing Symposium 2019</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>主要在数据集，没有特殊的训练方法</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/jerpint/bigearthnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据集+有监督训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2006.12485'>On Creating Benchmark Dataset for Aerial Image Interpretation: Reviews, Guidances, and Million-AID</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2021</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>首个与imagenet量级相当的数据集。主要在数据集，没有特殊的训练方法</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://captain-whu.github.io/DiRS/0</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据集+有监督训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2304.05215'>A billion-scale foundation model for remote sensing images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv 2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>研究参数量对预训练模型质量的影响</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2312.10115'>SkySense: A Multi-Modal Remote Sensing Foundation Model Towards Universal Interpretation for Earth Observation Imagery</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR 2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>通用的十亿级模型，在包含 2150 万个时间序列的多模态遥感图像 (RSI) 数据集上进行了预训练。通过多粒度对比学习对分解后的编码器进行预训练，从不同的模态和空间粒度构造特征。此外，我们提出了地理环境原型学习，从给定地理位置的RSI特征生成区域原型。该方法通过利用隐藏在大量未标记RSI中的区域上下文线索来增强多模态时空表征学习。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督多粒度对比学习，关注多模态和区域上下文</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2204.05381'>Self-supervised vision transformers for joint sar-optical representation learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>基于DINO，一种最先进的SSL算法，从输入图像的两个增强视图中提取知识，我们通过将所有通道连接到统一的输入来结合SAR和光学图像。随后，我们随机屏蔽掉一种模态的通道作为数据增强策略。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/zhu-xlab/DINO-MM</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，EMA, SAR+RGB多模态</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2107.05276'>Geographical Knowledge-Driven RepresentationLearning for Remote Sensing Images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/flyakon/Geographical-Knowledge-driven-Representaion-Learning</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，利用地理信息（地表覆盖种类）构建正负样本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2104.07070'>Self-Supervised Learning of Remote Sensing Scene Representations Using Contrastive Multiview Coding</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR 2021</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/vladan-stojnic/CMC-RSSR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多视图对比学习，用同一张图像的不同view（L，ab）作为正样本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2207.08051'>SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite Imagery</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>NeurIPS 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/sustainlab-group/SatMAE</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，MAE</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2205.02049'>Self-Supervised Learning for Invariant Representations from Multi-Spectral and SAR Images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，BYOL只使用正样本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2112.01715'>Self-Supervised Material and Texture Representation Learning for Remote Sensing Tasks</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2204.04716'>TOV: The original vision model for optical remote sensing image understanding via self-supervised learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing 2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>先学习网络上的自然图片，然后学习未标记RSI图片，</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>CNN(Resnet-50)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, Object Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>scene classification, object detection and semantic segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2010.00882'>Remote Sensing Image Scene Classification with Self-Supervised Paradigm under Limited Labeled Samples</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Geoscience and Remote Sensing Letters 2020</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>the first time to use the SSL mechanism in the RSI scene classification; 分别测试了image inpainting, predicting relative position, and instance-wise contrastive learning </td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2106.10605'>Global and Local Contrastive Self-Supervised Learning for Semantic Segmentation of HR Remote Sensing Images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IEEE Transactions on Geoscience and Remote Sensing 2022</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>基于对比学习对于像素级别的任务适配不好，改论文提出了一种基于全局和局部对比学习的方法，以更好的适应像素级任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/GeoX-Lab/G-RSIM</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，对比学习</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2304.09670'>CMID: A Unified Self-Supervised Learning Framework for Remote Sensing Image Understanding</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>TGRS2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>对图片一个做增强一个做mask，经过网络后同时计算两个分支的contrastive loss和mask分支的regression loss。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/NJU-LHRS/official-CMID</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，通过蒸馏将对比学习和掩码结合在一起</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer, CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>architecture-agnostic(CNN/Transformer)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, Object Detection, Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>scene classification, semantic segmentation, object detection, and change detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Prexl_Multi-Modal_Multi-Objective_Contrastive_Learning_for_Sentinel-12_Imagery_CVPRW_2023_paper.html'>Multi-Modal Multi-Objective Contrastive Learning for Sentinel-1/2 Imagery</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPRW2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>构建模态内和模态间相似度损失函数，通过地理编码获取更难的对比学习负样本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，对比学习，多模态</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>CNN(ResNet18)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Regression</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>Classification(Land-cover,Crop type mapping,), Regression (Biomass estimation)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://openaccess.thecvf.com/content/CVPR2023/html/Mall_Change-Aware_Sampling_and_Contrastive_Learning_for_Satellite_Images_CVPR_2023_paper.html'>Change-Aware Sampling and Contrastive Learning for Satellite Images</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>季节变化损失与SeCo相同，使用同一地点几个月时间内的图片作为正样本，其他地点的图片作为负样本。长时间变化用几个月内的做正样本，长时间后的图片做负样本。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/utkarshmall13/CACo</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，对比学习</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>CNN（ResNet-18, ResNet-50）</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Change Detection, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>Classification（Landcover classification），Change detection，Semantic segmentation，Change Events</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2211.15660'>SatlasPretrain: A Large-Scale Dataset for Remote Sensing Image Understanding</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>ICCV2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>主要是数据集，说明在这个数据集上进行预训练能够得到更好的效果</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/allenai/satlas</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据集，</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Swin Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>Swin Transformer Backbone，UNet Head</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, Instance Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>8 classification，semantic segmentation, and instance segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2302.04476'>Towards Geospatial Foundation Models via Continual Pretraining</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>ICCV2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>改论文注意到了地理空间数据集的多样性对MIM预训练十分重要。为了增加纹理细节，我们确保了各种地面采样距离（GSD），包括比Sentinel-2（GSD为10米）高得多分辨率的图像。此外，选择的标签数据集涵盖了广泛的通用遥感场景类，确保样本间的视觉多样性。通过蒸馏的方式让学生网络学习到ImageNet pretrain的特征。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/mmendiet/GFM</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据集，自监督掩码+蒸馏，持续预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Swin Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>Swin transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Change Detection, Classification, Semantic Segmentation, Super-resolution</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>change detection, classification, multi-label classification, semantic segmentation, and super-resolution</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2212.14532'>Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation Learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>ICCV2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>原始ViT的位置编码与相机高度无关，Scale-MAE引入了基于地面采样距离（GSD）的位置编码，该编码与图像中土地面积成比例缩放，而不考虑图像的分辨率。此外，Scale-MAE还在MAE框架中引入了拉普拉斯金字塔解码器，以鼓励网络学习多尺度表示。来自ViT编码器的嵌入被解码为捕捉低频信息的低分辨率图像和捕捉高频信息的高分辨率图像。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/bair-climate-initiative/scale-mae</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>MAE，对位置编码和解码器进行了优化</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>ViT-Large</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>基于KNN的分类，linear classi-fication，Semantic segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2303.06670'>DINO-MC: Self-supervised Contrastive Learning for Remote Sensing Imagery with Multi-sized Local Crops</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv 2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/WennyXY/DINO-MC</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，DINO，使用时间对比任务和多尺度裁剪对比</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet, ViT, Swin Transformer, WRN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>ResNet-50，WRN-50-2，ViT-small，Swin-tiny</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification，Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/pdf/2311.00566'>CROMA: Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>NeurIPS2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>分别编码被遮盖的多光谱光学和合成孔径雷达样本，这些样本在空间和时间上是对齐的，并执行跨模态对比学习。另一个编码器融合这些传感器，生成联合多模态编码，然后通过一个轻量级解码器预测被遮盖的补丁。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/antofuller/CROMA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习+重建，多光谱+孔径雷达</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>ViT-B/ViT-L</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>Classification,Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://openreview.net/pdf?id=5oEVdOd6TV'>Cross-Scale MAE: A Tale of Multiscale Exploitation in Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>NeurIPS2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>在预训练过程中，Cross-Scale MAE采用了尺度增强技术，并通过对比损失和生成损失实施跨尺度一致性约束，以确保一致且有意义的表示，适用于广泛的下游任务。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/aicip/Cross-Scale-MAE</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>MAE+对比学习</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>ViT-L</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification and segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2309.05300'>DeCUR: decoupling common & unique representations for multimodal self-supervision</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>在不同模态间分离了通用和独特的表示，增强了模态内和跨模态的学习。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/zhu-xlab/DeCUR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多模态，对比学习</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>ResNet50 </td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification and segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2304.14065'>Lightweight, Pre-trained Transformers for Remote Sensing Timeseries</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>一种在遥感像素时间序列数据上预训练的模型</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/nasaharvest/presto</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多模态，单像素时间序列掩码，关注时间序列</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>Presto</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2310.00022'>CtxMIM: Context-Enhanced Masked Image Modeling for Remote Sensing Image Understanding</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>CtxMIM将原始图像块形式化为重建模板，并采用Siamese框架处理两组图像块。引入了一个上下文增强的生成分支，通过重建中的上下文一致性约束提供上下文信息。通过这种简单且优雅的设计，CtxMIM鼓励预训练模型在大规模数据集上学习对象级或像素级特征，而无需特定的时间或地理约束。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，掩码</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Swin Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>Swin-B</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, Object Detection, Instance Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification, semantic segmentation, object detection, instance segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2310.18653'>Feature Guided Masked Autoencoder for Self-supervised Learning in Remote Sensing</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>MAE往往过度关注像素细节，从而限制了模型的语义理解能力，特别是对于噪声较大的SAR图像。提出了特征引导掩码自动编码器（FG-MAE）：重建多光谱图像的方向梯度直方图（HOG）和归一化差异指数（NDI）的组合，以及重建SAR图像的HOG。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/zhu-xlab/FGMAE</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多模态，掩码</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'> ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2310.18660'>Foundation Models for Generalist Geospatial Artificial Intelligence</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>对ViT架构的主要修改是3D位置嵌入和3D补丁嵌入，以处理时空数据</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://huggingface.co/ibm-nasa-geospatial</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>MAE, HLS多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Cloud Gap Imputation/Flood Mapping/Wildfire Scar Mapping/Crop Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2309.09003'>RingMo-lite: A Remote Sensing Multi-task Lightweight Network with CNN-Transformer Hybrid Framework</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>RingMo-lite，这是一种具有CNN-Transformer混合框架的RS多任务轻量级网络，能够有效利用RS的频域特性来优化解释过程。它结合了变压器模块作为低通滤波器，通过双分支结构提取RS图像的全局特征，以及CNN模块作为堆叠的高通滤波器来有效提取细粒度细节。此外，在预训练阶段，设计的频域掩码图像建模（FD-MIM）结合了每个图像补丁的高频和低频特性，有效捕捉了RS数据中的潜在特征表示。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>掩码（FD-MIM），轻量化</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱, RGB</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>CNN-Transformer hybrid</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Object Detection, Semantic Segmentation, Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/abstract/document/10282433'>A Self-Supervised Cross-Modal Remote Sensing Foundation Model with Multi-Domain Representation and Cross-Domain Fusion</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IGARSS2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>然而，多模态数据在传感器种类、成像机制、分辨率和光谱信息上具有独特性。现有方法主要针对单一模态数据，特别是光学遥感图像，直接将其应用于多模态数据很难平衡提取各模态特征，并突破单一模态数据的性能上限。一种基于多域表示和跨域融合概念的模型架构.对于多模态遥感输入数据，MSFE首先在相应的特征空间中学习各种特征，即在欧几里得空间中学习光学和红外数据，在双曲空间中学习高光谱数据，在复数空间中学习SAR数据。然后，基于自监督损失，MMFH通过多模态特征对齐和交互学习跨模态互补信息，从而提高基础模型对多模态遥感数据的解释性能。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多模态，对比学习+重建</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>single-modal interpretation/multi-modal interpretation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2309.07207'>EarthPT: a foundation model for Earth Observation</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>NeurIPS2023 CCAI workshop</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>与Lightweight, Pre-trained Transformers forRemote Sensing Timeseries相似，用了更大的数据集</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/aspiaspace/EarthPT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>关注时间序列，单像素时间预测</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Future data generation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.02199'>USat: A Unified Self-Supervised Encoder for Multi-Sensor Satellite Imagery</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>遥感数据包含多传感器、多光谱和时间信息，提供了大量可用于自监督预训练的自标注数据,开发了一种新的编码器架构，称为 USat，可以输入来自多个传感器的多光谱数据进行自监督预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/stanfordmlgroup/USat</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>新的USat backbone，多光谱，MAE预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2312.10114'>FoMo-Bench: a multi-modal, multi-scale and multi-task Forest Monitoring Benchmark for remote sensing foundation models</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/RolnickLab/FoMo-Bench</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>森林监测基准，多模态</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>多光谱</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2311.15153v4'>Predicting Gradient is Better: Exploring Self-Supervised Learning for SAR ATR with a Joint-Embedding Predictive Architecture</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>发现像素采样不适用于SAR图像，因为SAR图像的单个像素包含乘性噪声。因此更倾向于使用局部补丁进行遮挡，而不是整个图像或像素级别。工作旨在通过局部补丁在目标层次上挖掘语义信息，而不是场景层次，工作发现梯度比率比HOG的差分梯度在乘性斑点噪声下更适合目标形状信息提取。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/waterdisappear/SAR-JEPA</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>自监督，类似JEPA的框架，固定student生成梯度特征</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>SAR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Target Recognition</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/document/10414422'>Self-Supervised Spatio-Temporal Representation Learning of Satellite Image Time Series</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>JSTARS2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>先生成patch编码。预训练任务旨在重建原始时间序列中被掩盖的一些输入补丁。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://src.koda.cnrs.fr/iris.dumeur/ssl_ubarn</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>类似Bert的自监督预训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>SITS</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.05093'>SwiMDiff: Scene-wide Matching Contrastive Learning with Diffusion Constraint for Remote Sensing Image</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>以往的CL忽略了细粒度特征和负样本中的潜在联系，SwiMDiff采用场景范围的匹配方法，有效地重新校准标签，将来自同一场景的数据识别为假负样本。此调整使CL更适用于遥感的细微差别。此外，SwiMDiff将CL与扩散模型无缝集成。通过实施像素级别的扩散约束，我们增强了编码器捕捉图像的全局语义信息和细粒度特征的能力。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>对比学习，用同一场景下的图片构建了一个FNS，并用一个基于Diffussion的图像恢复任务做辅助任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Resnet</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2401.07527'>One for All: Toward Unified Foundation Models for Earth Vision</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>目前的遥感基础模型通常专注于单一模态或特定的空间分辨率范围，这限制了它们在下游数据集中的通用性。尽管已经有开发多模态遥感基础模型的尝试，但它们通常为每种模态或空间分辨率采用单独的视觉编码器，需根据输入数据切换不同的骨干网络。为了解决这一问题，我们提出了一种简单而有效的方法，称为OFA-Net（One-For-All网络）：使用单一的共享Transformer骨干网络来处理不同空间分辨率的多种数据模态。通过使用掩码图像建模机制，我们在一个精心策划的多模态数据集上预训练单一的Transformer骨干网络。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>---</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>掩码，在主干前加了不同模态的编码器，解码器也是各个模态独立的</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>RGB, SAR, 多光谱, NIR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://ieeexplore.ieee.org/abstract/document/10378718'>Generative ConvNet Foundation Model With Sparse Modeling and Low-Frequency Reconstruction for Remote Sensing Image Interpretation</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>TGRS2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>https://github.com/HIT-SIRS/SMLFR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models/blob/main'>S2MAE: A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>GeoSense的大型数据集，设计了一个稀疏建模和低频重建（SMLFR）框架，用于ConvNet基础模型的自监督表示学习。具体而言，在遮罩图像建模（MIM）中提出了一种稀疏建模策略，使ConvNet能够通过将未遮罩的补丁视为体素并对编码器进行稀疏化来处理可变长度序列。此外，我们设计了一个低频重建目标，引导模型关注遥感图像中的重要地物特征，同时减轻不必要的细节干扰。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ConvNext</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Object Detection, Semantic Segmentation, Change Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2403.05419'>Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>Pretrain</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>执行多尺度预训练，并利用基于卷积的上采样块在更高尺度上重建图像，使其可以扩展到更多尺度。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>RGB</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer, CNN</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2404.01260'>Bridging Remote Sensors with Multisensor Geospatial Foundation Models</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>CVPR2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>通过使用遮罩图像建模技术可以学习到对应传感器之间的联合表示吗？针对该问题提出了msGFM（多传感器地理空间基础模型），该模型有效整合了四种关键传感器模式的数据。msGFM特别擅长处理配对和非配对的传感器数据。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>跨传感器的掩码方式。每个传感器有独立的embedding提取器，为每个传感器设置单独的解码器和跨传感器预测。例如，当模型被馈送来自DSM的遮罩图像时，它可以预测自身的遮罩补丁或RGB对应的图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>SAR, RGB, DSM</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Swin Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation, cloud removal, pan-sharpening</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='https://arxiv.org/abs/2403.15356'>Neural Plasticity-Inspired Foundation Model for Observing the Earth Crossing Modalities</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>这是通过设计的基于超网络的动态权重生成器实现的，该生成器适应每个通道的光谱波长。通过将具有不同通道数量的图像嵌入到统一的特征空间中，模型利用共享Transformer块来学习模态共享表示。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>将各种数据模态自适应地集成到一个单一框架中，这种动态超网络，能够调整到不同的波长，使得一个多功能Transformer能够在来自五个传感器的数据上进行联合训练</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>RGB, NIR, 多光谱, SAR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>Transformer</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Semantic Segmentation</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='nan'>MMEarth: Exploring Multi-Modal Pretext Tasks For Geospatial Representation Learning</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>多预文本遮罩自编码器，解码器包括重建和一些下游任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>ConvNext</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='nan'>SARATR-X: A Foundation Model for Synthetic Aperture Radar Images Target Recognition</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>MAE，两阶段预训练（ImageNet-SAR），使用多尺度梯度特征（MGF）[这个文档里的49]来抑制斑点噪声并提取目标形状</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>SAR</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>HiViT</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>Classification, Object Detection</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='nan'>LeMeViT: Efficient Vision Transformer with Learnable Meta Tokens for Remote Sensing Image Interpretation</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>IJCAI2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>改网络结构，加速</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='nan'>On the Foundations of Earth and Climate Foundation Models</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>Arxiv2024</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>有一些问题：1. 专注于预训练数据集的策划，往往过度采样城市等人口稠密地区，而在雨林、极地和海洋等人口稀少地区采样不足 2. 预训练数据集往往专注于中高分辨率的RGB和MSI，很少有大规模的数据集用于SAR、HSI或Lidar数据，或用于非常高或低分辨率的图像。像DOFA这样的多传感器模型很少见，大多数模型需要在每次遇到新的成像平台时从头训练 3. 时间序列地球观测建模也处于起步阶段，少有模型能够处理具有不规则间隔的可变长度图像序列。在地球观测中整合不确定性量化和物理一致性仍未得到充分探索。未来的发展：1.具有条件计算的动态编码器 2.多尺度的空间-时间分析 3.多模态学习框架 4.与大型语言模型的对齐 ...</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>针对地球和气候科学</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table><table style="width:100%;">
<tr>
<td>Paper</td>
<td>key</td>
<td>value</td>
<td>Short Summary</td>
</tr>
  <tr>
    <td rowspan='11' style='text-align: left; width:30%;'><a href='nan'>遥感基础模型发展综述与未来设想</a></td>
    <td style='text-align: left; width:10%;'>Published in</td>
    <td style='text-align: left; width:20%;'>遥感学报2023</td>
    <td rowspan='11' style='text-align: left; width:40%;word-wrap: break-word;'>对比学习、生成式学习；图像，时间序列</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Type</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Code/Project</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>备注</td>
    <td style='text-align: left;'>数据、方法和应用</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数据类型</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Backbone 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>下游任务 1</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>Survey Inclusion</td>
    <td style='text-align: left;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>other</td>
    <td style='text-align: left;'>nan</td>
  </tr>
</table>


# Dataset
## 汇总
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/MBZUAI/GeoChat_Instruct'>GeoChat_Instruct</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感多模态大模型指令微调</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>318k个图像指令对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>UCM-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>该图像数据是从USGS国家地图城市区域影像集合中提取的，包含2,100张RGB航拍图像，覆盖21个类别。每张图像配有5条描述性文字，总计有2032条独特标注。图像分辨率为256×256像素，空间分辨率为1英尺。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像、每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7546397</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>Sydney-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>悉尼数据集包含来自谷歌地球的澳大利亚悉尼的图像。它包含属于7个类别的613个图像。图像是(500,500) RGB，并为每个图像提供5个caption。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>613张图像，每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7546397</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>RSICD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>超过一万张遥感图像是从谷歌地球、百度地图、MapABC、天地图等平台收集而来的。这些图像被固定为 224X224 像素，具有不同的分辨率。总共有 10921 张遥感图像，每张图像配有5句描述，共有18,190条独特标注。据我们所知，这个数据集是用于remote sensing image caption任务中最大的数据集。数据集中的样本图像具有高类内多样性和低类间差异性。包含30种类型的遥感地物类型</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10921张图像，每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1712.07835</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/xiaoyuan1996/AMFMN'>RSITMD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感多模态检索</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSITMD（遥感图像-文本匹配数据集）是Yuan等人提出的一个细粒度且富有挑战性的遥感数据集，适用于遥感多模态检索任务。相比其他遥感图像-文本配对数据集，它具有描述物体间关系的详细说明。此外，该数据集还包含了关键词属性（每张图像1至5个关键词），可用于基于关键词的遥感文本检索任务。该数据集中共有4,743张图像跨越32个场景，共包含23,715条标注，其中21,829条为非重复标注。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4743张图像，23715条标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2204.09868</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ZhanYang-nwpu/RSVG-pytorch'>DIOR_RSVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>是Zhan等人于2022年引入的一个全面的遥感视觉定位基准数据集（Remote Sensing Visual Grounding, RSVG）。RSVG任务专注于在遥感图像中定位由查询语句所指的对象。该数据集建立在最初设计用于目标检测的DIOR遥感图像数据集基础之上。RSVGD包含38,320对遥感图像-文本对以及17,402张遥感图像，平均表达长度为7.47，词汇表规模为100。图像分辨率为800×800像素，空间分辨率范围从0.5米到30米。文本描述是根据模板和预定义规则合成生成的。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>38320对遥感图像-文本对以及17402张遥感图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2210.12634</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/Zilun/RS5M'>RS5M</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图文匹配</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>图像-文本配对的数据集RS5M，其中包含500万张带有英文描述的遥感图像。该数据集是通过筛选公开可用的图像-文本配对数据集并用预训练的视觉-语言模型标注仅具有标签的遥感数据集得到的。这构成了第一个大规模的遥感图像-文本配对数据集。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>500万张带有英文描述的遥感图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2306.11300</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/HaiyanHuang98/NWPU-Captions'>NWPU-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>NWPU-Captions包含了157,500个句子，所有31,500张图片都由七名经验丰富的志愿者手动注释。NWPU-Captions相对于当前公开可用的基准数据集的优越性不仅在于其更大的规模，还在于其对复杂场景的更广泛覆盖以及描述词汇的丰富多样性。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>157,500个句子，31,500张图片</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1703.00121</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/fMoW/dataset'>fMoW</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>数据集由来自200多个国家的100多万张图像组成。对于每张图像，提供至少一个包含63个类别之一的边界框注释，其中包括一个“错误检测”类别。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100 多万张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018/papers/Christie_Functional_Map_of_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://weegee.vision.ucmerced.edu/datasets/landuse.html'>UCMerced_LandUse</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含21种土地利用类型的遥感影像，提取自 USGS National Map，由University of California, Merced于2010年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2010</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://dl.acm.org/doi/abs/10.1145/1869790.1869829</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/BED4RS/'>WHU RS19</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含19种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2012年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>950张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/palewithout/RSSCN7'>RSSCN7</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2015年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2800张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://mvr.whu.edu.cn/pubs/2015-IEEE_GRSL.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.researchgate.net/publication/271647282_RS_C11_Database'>RS_C11</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种土地利用类型的遥感影像，提取自Google Earth，由中科院于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1232张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://gcheng-nwpu.github.io/#Datasets'>NWPU-RESISC45</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含45种土地利用类型的遥感影像，提取自Google Earth，由西北工业大学于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>31500张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7891544/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/AID/'>AID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含30种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7907303/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/RSIA-LIESMARS-WHU/RSD46-WHU'>RSD46-WHU</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含46种土地利用类型的遥感影像，提取自Google Earth、天地图，由武汉大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>117000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7827088/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的secenClass部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种土地利用类型的遥感影像，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset'>PatternNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含38种土地利用类型的遥感影像，提取自Google Map，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1706.03424</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/phelber/eurosat'>EuroSAT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种土地利用类型的遥感影像，提取自哨兵2，由德国凯泽斯劳滕大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>27000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8736785</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://drive.google.com/open?id=1Fk9a0DW8UyyQsR8dP2Qdakmr69NVBhq9'>OPTIMAL-31</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含21种土地利用类型的遥感影像，提取自Google Earth，由西北工业大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1860张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8454883</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/lehaifeng/CLRS'>Continual Learning Benchmark for Remote</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含25种土地利用类型的遥感影像，提取自Google Earth, Bing Map, Google Map, and Tianditu，由中南大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>15000张图片</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/1424-8220/20/4/1226</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.msadc.cn/main/setsubDetail?id=1369487569196158978; http://www.jors.cn/jrs/ch/reader/create_pdf.aspx?file_no=20209323&flag=1'>TG1HRSSC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含全色谱段(PAN)、可见近红外(VNI)、短波红外谱段(SWI)，包含9种土地利用类型的遥感影像，提取自天宫一号，由中国科学院空间应用工程与技术中心于2021年发布，包含波段:0.5—0.8μm、1band(PAN), 0.4—1.0μm、54band((VNI), 1.0—2.5μm、52band((SWI),</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>204张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.msadc.cn/main/setsubDetail?id=1370312964720037889； http://www.msadc.cn/group1/M00/00/08/CgId02Bio4KAazc6AEZR3GfuVic489.pdf
'>NaSC-TG2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物类型，
提取自天宫二号，
包含波段范围：0.40–1.04 µm，
由中国科学院空间应用工程与技术中心于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://csc.lsu.edu/~saikat/deepsat/'>SAT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>SAT数据集，包括SAT-4、SAT-6，2个数据子集，分别包含4种、6种土地利用类型的遥感影像，提取自the National Agriculture Imagery Program (NAIP) dataset，由路易斯安那州立大学与NASA于2015年发布，采用MATLAB的.mat数据存储格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>405000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.lmars.whu.edu.cn/prof_web/zhongyanfei/Code/Google_Dataset/Google%20dataset%20of%20SIRI-WHU_earth_im_tiff.7z'>SIRI-WHU</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>SIRI-WHU数据集，包括 google image、USGS image2个数据子集，分别包含12种、4种土地利用类型的遥感影像，分别提取自Google Earth、USGS，由武汉大学于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7329997</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/lehaifeng/RSI-CB'>RSI-CB</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSI-CB数据集，包括RSI-CB128、RSI-CB256，2个数据子集，分别包含45种、35种土地利用类型的遥感影像，提取自多种数据，由中南大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>36000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/'>Multi-View Datasets中的CV-BrCT部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Multi-View Datasets数据集，CV-BrCT数据子集，包含8种土地利用类型的遥感影像，提取自航空影像及地面街景影像，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>48342张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/'>Multi-View Datasets中的AiRound部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Multi-View Datasets数据集，AiRound数据子集，包含11种土地利用类型的遥感影像，提取自Sentinel-2等多源数据，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13980张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://ai.stanford.edu/~gaheitz/Research/TAS/'>TAS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由斯坦福大学于2008年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2008</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sourceforge.net/projects/oirds/'>OIRDS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物目标，提取自USGS、DARPA、VIVID，由雷神公司等于2009年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2009</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>900张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://downloads.greyc.fr/vedai/'>VEDAI</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含9种类型的遥感地物目标，提取自Utah AGRC，由卡昂大学于2015年发布，采用oriented bounding boxes(OBB)标注格式
</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1210张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.kaggle.com/datasets/guofeng/hrsc2016'>HRSC2016</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含27种类型的遥感地物目标，提取自Google Earth，由西北工业大学于2016年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1061张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.dlr.de/eoc/en/desktopdefault.aspx/tabid-12760/22294_read-52777'>DLR3k</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物目标提取自无人机(Canon Eos 1Ds Mark III)由德国航天航空中心于2016年发布采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/CrazyStoneonRoad/TGRS-HRRSD-Dataset'>TGRS-HRRSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含13种类型的遥感地物目标，提取自Google Earth、百度地图，由中科院于2017年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>21761张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8676107</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://challenge.xviewdataset.org/data-download'>xView</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含60种类型的遥感地物目标，提取自WorldView 3，由DIUx、NGA于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1129张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://levir.buaa.edu.cn/Code.htm'>LEVIR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物目标，提取自Google Earth，由北京航天航空大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>22000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8106808</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.iuii.ua.es/datasets/masati/'>MASATI</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物目标，提取自Bing Maps，由阿利坎特大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>7389张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/4/511</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://research.utwente.nl/en/datasets/itcvd-dataset'>ITCVD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自航拍影像，由University of Twente Research Information于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>135张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8451454</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/iSAID/index.html'>iSAID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种类型的遥感地物目标，提取自Google Earth、JL-1、GF-2，由武汉大学于2019年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1905.12886</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2019/07/10/bridge-dataset/'>Bridge Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth、 OpenStreetMap，由Federal University of Minas Gerais于2019年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>500张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8876942</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cosmiqworks.org/RarePlanes/ https://www.graviti.cn/open-datasets/RarePlanes'>RarePlanes</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种飞机遥感影像，提取自WorldView-3，由In-Q-Tel、AI.Reverie于2020年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1507张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2006.02963</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/contestDetail?id=2&tab=data'>飞机目标识别-训练数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种飞机类型的遥感地物目标,提取自国产自主产权系列卫星，由中科院于2021年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>430张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/contestDetail?id=6&tab=data'>船只智能检测-训练数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自国产自主产权系列卫星
由中科院于2021年发布采用，oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>25张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-Detection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>32825张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2111.12960</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-DET</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10209张图象</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-VID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>288个视频片段</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>DroneCrowd</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像人群计数</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自无人机数据，由天津大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1807张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA1.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>15类，共188282个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA1.5</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>16类，共400000±个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA2.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'> 18类，共1,793,658个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>11268张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://opensar.sjtu.edu.cn/DataAndCodes.html'>OpenSARShip</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Sentinel-1，由上海交通大学于2017年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>41张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8067489</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/chaozhong2010/HRSID'>HRSID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Sentinel-1B、TerraSAR-X、TanDEM-X，由电子科技大学于2020年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5604张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9127939</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.usgs.gov/core-science-systems/nli/landsat/spatial-procedures-automated-removal-cloud-and-shadow-sparcs'>SPARCS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自 Landsat 8 OLI/TIRS，由University of Tennessee Knoxville于2014年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2014</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>80张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/6/6/4907stats?stats=v&utm_source=TrendMD&utm_medium=cpc&utm_campaign=Remote_Sens_TrendMD_0</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/record/1154821'>CITY-OSM</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6个城市，2种类别：街道和建筑，提取自Google Maps、OpenStreetMap，由ETH Zürich于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1671张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1707.06879</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0'>WHDLD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自UC Merced，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4940张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/6/964</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0'>DLRSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>基于UCMerced_LandUse数据集进行标注，包含17种类型的遥感地物类型标注数据，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/6/964</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ishann/aeroscapes'>Aeroscapes</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种类型的遥感地物类型，提取自航空影像，由Carnegie Mellon University于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3269张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8354272</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.airs-dataset.com/'>AIRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自LINZ Data Service，由 University of Tokyo等，于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1047张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1807.09532</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmkemker/RIT-18'>RIT-18</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含18种类型的遥感地物类型，提取自Tetracam Micro-MCA6，包含7波段，由Rochester Institute of Technology于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271618301229</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1AsdnO2-nadxTaq9_9Mo3Eg?pwd=tftf#list/path=%2F'>HSODBIT-V1</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>高光谱显著性目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>319幅高光谱图像及对应的伪彩色图像和像素级标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>323张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/satellogic/EarthView/tree/main'>EarthView</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感模型预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>外网不会下</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>300万张高分辨率训练数据集</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/dronedeploy/dd-ml-segmentation-benchmark'>DroneDeploy</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自航空影像drones，由DroneDeploy于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>55张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/mitroadmaps/roadtracer/'>RoadTracer</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google earth、OSM，由MIT于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://roadmaps.csail.mit.edu/roadtracer/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/Bijie_pages.html'>Bijie Landslide Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种土地利用类型的遥感影像，提取自TripleSat，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>770张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/article/10.1007/s10346-020-01353-2</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/3DFGC_pages.html'>GF2 Dataset for 3DFGC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种土地利用类型的遥感影像，提取自GF2，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>11张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.tandfonline.com/doi/abs/10.1080/01431161.2019.1699973</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://project.inria.fr/aerialimagelabeling/'>Semantic Drone Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含22种土地利用类型的遥感影像，提取自航拍影像，由Graz University of Technology于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://inria.hal.science/hal-01468452/document</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_Cloud_Dataset.html'>WHU Cloud Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种土地利用类型的遥感影像，提取自Landsat 8，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>859张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9099032</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://landcover.ai.linuxpolska.com/'>landcover_ai</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物类型，提取自  public geodetic resource，由linuxpolska等于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>41张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2005.02264</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.uavid.nl/'>UAVid</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自航空影像，由University of Twente于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>300张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.10438</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.datafountain.cn/competitions/457/datasets'>全国人工智能大赛AI遥感影像</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>一级大类8种，二级子类17种，数据为0.1米-4米分辨率的高分一、二、六号，高景二号，北京二号，以及部分航空等数据源的可见光、多光谱载荷图像，由鹏城实验室和协办单位合作采集、标注、构建；</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.datafountain.cn/competitions/475'>BDCI2020</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，由BDCI于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>145981</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Junjue-Wang/LoveDA'>LoveDA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自Google Earth，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5987张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.researchgate.net/publication/355390292_LoveDA_A_Remote_Sensing_Land-Cover_Dataset_for_Domain_Adaptive_Semantic_Segmentation</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.grss-ieee.org/community/technical-committees/2022-ieee-grss-data-fusion-contest/'>MiniFrance-DFC22</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种土地利用类型的遥感影像，提取自航空影像，由IADF TC于2022年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2322张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cs.toronto.edu/~vmnih/data/'>Massachusetts Roads</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由University of Toronto于2013年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2013</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>804张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.cs.toronto.edu/~vmnih/docs/Mnih_Volodymyr_PhD_Thesis.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cs.toronto.edu/~vmnih/data/'>Massachusetts Builds</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由University of Toronto于2013年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2013</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>151张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.cs.toronto.edu/~vmnih/docs/Mnih_Volodymyr_PhD_Thesis.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://deepglobe.org/challenge.html'>DeepGlobe Land Cover Classificat</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自DigitalGlobe，由CVPR于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>803张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Demir_DeepGlobe_2018_A_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://deepglobe.org/challenge.html'>DeepGlobe Road Detection Challen</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自DigitalGlobe，由CVPR于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>6226张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Demir_DeepGlobe_2018_A_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html'>WHU Building Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>总共三部分，global cities、East Asia、Aerial imagery datase，包含1种类型的遥感地物类型，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>25781张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8444434</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmcong/ORSSD-dataset'>ORSSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自 Google Earth，由北京交通大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>800张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1906.08462</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmcong/EORSSD-dataset'>EORSSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自Google Earth，由北京交通大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2011.13144</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/SorourMo/38-Cloud-A-Cloud-Segmentation-Dataset'>38-Cloud</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Landsat 8，由Simon Fraser University于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集中有 8400 个图像块，38个训练场景，测试集中有 9201 个图像块，20个测试场景。每个图像块包含 4 个相应的光谱通道，分别是红色（波段 4）、绿色（波段 3）、蓝色（波段 2）和近红外（波段 5）。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1901.10077</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/SorourMo/95-Cloud-An-Extension-to-38-Cloud-Dataset'>95-Cloud</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Landsat 8，由Simon Fraser University于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集中有 34701个图像块，95个训练场景，测试集中有 9201 个图像块，20个测试场景。每个图像块包含 4 个相应的光谱通道，分别是红色（波段 4）、绿色（波段 3）、蓝色（波段 2）和近红外（波段 5）。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://deepai.org/publication/cloud-net-a-cloud-segmentation-cnn-for-landsat-8-remote-sensing-imagery-optimized-with-filtered-jaccard-loss-function</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的Fine部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种类型的遥感地物类型，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的Large-scale部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物类型，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>150张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/MarcWong/UDD'>Urban Drone Dataset(UDD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包括UDD5、UDD6两个数据子集，分别包含5、6种类型的遥感地物类型，提取自无人机数据（DJI Phantom 4），由北京大学于2018年发布

</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集120张图像，测试集40张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/chapter/10.1007/978-3-030-03398-9_30</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/'>BH-POOLS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 水池分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>各包含1种类型的遥感地物类型，提取自GoogleEarth，由Federal University of Minas Gerais于2020年发布
</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由8个不同街区的200张4K图像组成(每个街区25张图像)，包含3980个带注释的水池</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/'>BH-WATERTANKS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 水箱分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>各包含1种类型的遥感地物类型，提取自GoogleEarth，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由6个社区的150张4K图像组成(每个社区25张图像)，包含16216个带注释的水箱。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>这个和上面那个是一个,和一起叫"BH-DATASET"</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://web.eee.sztaki.hu/remotesensing/airchange_benchmark.html'>SZTAKI-INRIA AirChange</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，由MTA SZTAKI于2009年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2009</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/iel5/36/4358825/05169964.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/gistairc/ABCDdataset'>AIST Building Change Detection(ABCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型提取自 aerial images 由National Institute of Advanced Industrial Science and Technology (AIST)于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含fixed-scale、resized 2个子集，分别有4,253 * 2、4,223 * 2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7986759</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html'>WHU Building Change Detection Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8444434</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://paperswithcode.com/dataset/cdd-dataset-season-varying'>CDD Dataset (season-varying)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 季节变化</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种变化类型，提取自Google Earth (DigitalGlobe)，由GosNIIAS于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集10000, 验证集3000, 测试集3000</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://paperswithcode.com/paper/change-detection-in-remote-sensing-images</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rcdaudt.github.io/oscd/'>Onera Satellite Change Detection (OSCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Sentinel-2，由Universit´e Paris-Saclay、 T´el´ecom ParisTech于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>14×2张训练，10×2张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.08468</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://sigma.whu.edu.cn/newspage.php?q=2019_03_26'>Multi-temporal Scene WuHan (MtS-WH)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 多时相场景变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含9种土地利用类型的遥感影像，提取自IKONOS传感器，由武汉大学2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>每个时相训练集包括190张影像，测试集包括1920张影像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/GeoZcx/A-deeply-supervised-image-fusion-network-for-change-detection-in-remote-sensing-images/tree/master/dataset'>DSIFN Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自GoogleEarth，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练数据集中有3600对图像，验证数据集中有340对图像，测试数据集中有48对图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271620301532</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rcdaudt.github.io/hrscd/'>High Resolution Semantic Change (HRSCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自 IGS’s BD ORTHO database，由ETH Zürich / EcoVision Lab于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>291×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.08452</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://xview2.org/dataset'>xBD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 灾害前后变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含全球六种不同类型自然灾害，每种灾害四种变化状态</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>22068张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPRW_2019/html/cv4gc/Gupta_Creating_xBD_A_Dataset_for_Assessing_Building_Damage_from_Satellite_CVPRW_2019_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/daifeng2016/Change-Detection-Dataset-for-High-Resolution-Satellite-Imagery'>Change-Detection-dataset-for-High-resolution-Satellite-Image</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，由ieee于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'> 20张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9161009</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://chenhao.in/LEVIR/'>LEVIR-CD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，由北京航空航天大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>637张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/12/10/1662</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rs.sensetime.com/competition/index.html#/info'>SenseEarth ChangeDetection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种变化类型的遥感地物类型，由商汤科技于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练2968张, 验证847张</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/SCD/'>SEmantic Change detectiON Data(SECOND)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自航空影像，由ETH Zürich / EcoVision Lab于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4662×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://captain-whu.github.io/SCD/SCD_files/Semantic_Change_Detection.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/records/4280482'>Sentinel-2 Multitemporal Cities Pairs</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Sentinel-2，由Wageningen University于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1520×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2101.08122</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/liumency/SYSU-CD'>Sun Yat-Sen University (SYSU)-CD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型变化信息，提取自 aerial image，由中山大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20000×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9467555</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=30'>S2Looking</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自国产自主产权系列卫星，由中科院于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3500对训练图像，500对验证图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=27'>LEVIR-CD2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，基于LEVIR-CD数据集，由中科院于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2800对训练图像、840对验证图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://gitlab.citius.usc.es/hiperespectral/ChangeDetectionDataset'>Change Detection Dataset(CDD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物类型，包含224波段，提取自HYPERION,AVIRIS sensor，于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3对图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection/data'>Dstl Satellite Imagery Feature Detection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感实例分割 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自WorldView 3，由DigitalGlobe于2017年发布，采用MultiPolygons标注格式，波段范围：全色450-800 nm，3波段；多光谱 (red, red edge, coastal, blue, green, yellow, near-IR1 and near-IR2)400 nm - 1040 nm，8波段；短波红外 1195 nm - 2365 nm，8波段</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集25张图像，测试集32张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.crowdai.org/challenges/mapping-challenge'>Mapping Challenge</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感实例分割 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Map，由crowdAI于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集280741张图像，验证集60317张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.frontiersin.org/articles/10.3389/frai.2020.534696/full</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://competitions.codalab.org/competitions/20100'>2018 Open AI Tanzania Building Footprint</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感实例分割 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由SUZA等于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/record/4172871'>Sentinel-2 Cloud Mask Catalogue</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感实例分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物类型，提取自Sentinel-2，于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>513张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=16'>CASIA-aircraft</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感目标检测 飞机检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由中科院于2021年发布，采用json标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含29093个训练数据，11603个验证数据，17425个测试数据，共计58121个</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://aistudio.baidu.com/datasetdetail/131586'>CASIA-Ship</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感目标检测 船体检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由中科院于2021年发布，采用json标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含571个训练数据，220个验证数据，327个测试数据，共计1118个</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://data.mendeley.com/datasets/7j9bv9vwsx/2'>MLRSNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多标签分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含46种土地利用类型的遥感影像，提取自Google Earth，由中国地质大学于2020年发布，最大标签数13</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>109161张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271620302677</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://aistudio.baidu.com/datasetdetail/91853'>UAV123</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>UAV123数据集，包含3个子集，子集1包含103个序列，子集2包含12个序列，子集3包含8个序列，提取自 UAV (DJIS1000)、UAV simulator，由King Abdullah University of Science and Technology于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共包含123个视频序列和超过110K帧</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/chapter/10.1007/978-3-319-46448-0_27</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.csdata.org/p/387/'>地/空背景下红外图像弱小飞机目标检测跟踪数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标跟踪 红外图像弱小飞机目标检测跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自航拍影像，由国防科技大学于2019年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>共计22段数据、30条航迹、16177帧图像、16944个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://www.csdata.org/p/387/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.scidb.cn/en/detail?dataSetId=808025946870251520'>复杂背景下红外弱小运动目标检测数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标检测、跟踪 复杂背景下红外弱小运动目标</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自航拍影像，由国防科技大学于2021年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含350个视频，150185个图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.scidb.cn/en/detail?dataSetId=808025946870251520</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-SOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频单目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>167段视频序列，1393000帧</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9573394</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-MOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频多目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集56段视频，24201帧, 验证集7段视频,2819帧 测试集33段视频，12968帧 </td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9573394</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-SOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频单目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100段视频序列，32,825帧图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9625976</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-MOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频多目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100段视频序列，32,825帧图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9625976</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/phillipi/pix2pix'>Aerial to Map</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 风格迁移</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自Google Maps，由UC Berkeley于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集1096张图像 ，验证集1098 张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.dropbox.com/s/k2i3p7puuwl2g59/Haze1k.zip?dl=0'>SateHaze1k</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 图像去噪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自GF-2、GF-3，由清华大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>400×3张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_WACV_2020/papers/Huang_Single_Satellite_Optical_Imagery_Dehazing_using_SAR_Image_Prior_Based_WACV_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html'>WHU Multi-view Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自航拍影像，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>21600张训练，6800张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_A_Novel_Recurrent_Encoder-Decoder_Structure_for_Large-Scale_Multi-View_Stereo_Reconstruction_CVPR_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html'>WHU Stereo Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自航拍影像，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>16632张训练，5236 张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_A_Novel_Recurrent_Encoder-Decoder_Structure_for_Large-Scale_Multi-View_Stereo_Reconstruction_CVPR_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu_tlc.html'>WHU TCL SatMVS dataset1.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自ZY3，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>173张训练，127张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/ICCV2021/html/Gao_Rational_Polynomial_Camera_Model_Warping_for_Deep_Learning_Based_Satellite_ICCV_2021_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu_tlc.html'>WHU TCL SatMVS dataset2.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自ZY3，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5011张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/ICCV2021/html/Gao_Rational_Polynomial_Camera_Model_Warping_for_Deep_Learning_Based_Satellite_ICCV_2021_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1dIFOm4V2pM_AjhmkD1-Usw?pwd=SARD'>SARDet-100K</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测 合成孔径雷达目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>涵盖六个不同的类别,由南开大学2024年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含约117K张图像和246K个对象实例</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2403.06534.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Chen-Yang-Liu/LEVIR-CC-Dataset'>LEVIR-CC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕 变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>每对图像包括变化前和变化后的，五句描述变化的话，由北京航空航天大学于2022年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含10077对双时态遥感图像和50385个描述图像之间差异的句子</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9934924</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://opendatasharing.s3.us-west-2.amazonaws.com/SkyScript'>SkyScript</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>涵盖超过29K个不同的语义标签</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>520万对遥感图像-文本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2312.12856</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA-LR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 低分辨率</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>使用哨兵2号的图像和来自OSM的问题和答案</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>772张图像、77232个问题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2003.07333</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA-HR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 高分辨率</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>USGS的高分辨率(15.24cm)正校正图像和OSM的问答</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10659张图像、955664个问题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2003.07333</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA×BEN</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>从BigEarthNet数据集中提取图像/问题/答案</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含近1500万个样本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9553307</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/spectralpublic/RSIVQA'>RSIVQA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSIVQA的图像来自三个RSI分类数据集(UCM、Sydney和AID)和两个RSI目标检测数据集(HRRSD和DOTA)。基于图像生成问题和答案，形成图像-问题-答案三元组。问题、答案及其对应关系可以在此存储库的txt文件中找到。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>有37264张图像和111693张图像-问答三元组</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9444570</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/YZHJessica/CDVQA'>CDVQA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>选择现有的语义变化检测数据集SECOND作为基础数据，自动生成CDVQA数据集。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含2968对航拍图像和超过122000对对应的问答</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2112.06343</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/jonathan-roberts1/SATIN'>SATIN</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类 场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>一个元数据集，包含27个卫星和航空图像数据集，涵盖6个不同的任务:土地覆盖、土地利用、分层土地利用、复杂场景、罕见场景和假彩色场景。这些图像是全球分布的，由跨越5个数量级的分辨率、多个视图大小和250多个不同的类标签组成。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2304.11619</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/blanchon/FAIR1M'>FAIR1M</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像目标检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含37种类型的遥感地物目标，共100 0000+个目标，提取自Gaofen satellites、Google Earth，由中科院等于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>15000+张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2103.05569</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021'>FloodNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类、分割、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>无人机收集，总共2343张图像，10个语义类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共2343张图像，用于分类和分割的测试集有400张，测试集有1050张图像，用于VQA的有1450张图像、4511给问答对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2012.02951</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/mikonvergence/LAION-EO'>LAION-5B</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像文本对</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>LAION-5B的子集，卫星图像文本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>版本0有24,933张图像、版本1有112,985张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2309.15535</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://lcmou.github.io/ERA_Dataset/'>CapERA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>25个类别，每个视频五个字幕</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2864个5秒的视频，每秒24帧，14,320个字幕</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/15/8/2139</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Lavender105/RSGPT'>RSICap</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像文本对</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>该数据集为每张图像提供了详细的描述，包括场景描述(例如，住宅区、机场或农田)以及物体信息(例如，颜色、形状、数量、绝对位置等)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2585对具有高质量人工注释字幕的图像-文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2307.15266</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Lavender105/RSGPT'>RSIEval</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100个人工注释的标题和936个视觉问答对，包含丰富的信息和开放式的问题和答案。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2307.15266</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/like413/OPT-RSVG'>OPT-RSVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>14个类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含25,452张图像和48,952对图像查询</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.researchgate.net/publication/373146282_LaLGA_Multi-Scale_LanguageAware_Visual_Grounding_on_Remote_Sensing_Data</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sunyuxi.github.io/publication/GeoVG'>GeoVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4,239张图片，包括5,994个对象实例和7,933个指代表达</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://dl.acm.org/doi/abs/10.1145/3503161.3548316</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://mediatum.ub.tum.de/1474000'>SEN12MS </a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类、用于土地覆盖制图的语义分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>所有块都以10米的地面采样距离进行完全地理参考，并覆盖所有有人居住的大陆和所有气象季节</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由180,662个双极合成孔径雷达（SAR）图像块、多光谱Sentinel-2图像块和MODIS土地覆盖地图三元组组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1906.07789</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://bigearth.net/'>BigEarthNet-MM</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检索和分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>由BigEarthNet-S1和S2组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含 590,326 对 Sentinel-1 和 Sentinel-2 图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2105.07921</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DiRS/'>MillionAID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Million-AID的场景类别采用三级树的层次分类网络进行组织，51个叶节点在第二级分为28个父节点，在第一级分为8个节点，分别代表农业用地、商业用地、工业用地、公共服务用地、住宅用地、交通用地、未利用用地和水域8个底层场景类别。场景分类网络为数据集提供了良好的场景分类关系组织和可扩展性。每个场景类别的图像数量在2000到45000张之间，使数据集具有长尾分布的特性。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含100万个场景分类实例、有51个语义场景类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2006.12485</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ServiceNow/seasonal-contrast'>SeCo</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像无监督预训练  不同季节的图像</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>从Sentinel-2收集的，其原则是收集大规模、未标记和未经整理的遥感数据集，这些数据集包含来自不同时间戳的多个地球位置的图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>两个版本有一个100K的，有一个1M的</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2103.16607</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/sustainlab-group/SatMAE'>FMoWS2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>nan</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练图像712874张，验证图像84939张，测试图像84966张</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2207.08051</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1'>TOV-RS-balanced</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含31个类别的50万个样本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/10110958</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zhu-xlab/SSL4EO-S12'>SSL4EO-S12</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像无监督/自监督预训练 用于地球观测的大规模多模态多时相数据集</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>该数据集由来自全球251079个地点的未标记的三元组(Sentinel-1双极化SAR, Sentinel-2大气顶部多光谱，Sentinel-2表面反射率多光谱)组成，每个patch覆盖2640mx2640m，包括四个季节时间戳。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2211.07044</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/allenai/satlas-pretrain/tree/main/dataset'>SatlasPretrain</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>超过30 TB的卫星图像与137个标签类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2211.15660</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/utkarshmall13/CACo'>CACo</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像自监督预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>超过100万图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/CVPR2023/html/Mall_Change-Aware_Sampling_and_Contrastive_Learning_for_Satellite_Images_CVPR_2023_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ViTAE-Transformer/SAMRS'>SAMRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含三个子集：SOTA子集17480张图像，18个类；SIOR子集23463张图像，20个类；FAST子集64147张图像，37个类</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2305.02034</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ServiceNow/geo-bench'>GEO-Bench</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感数据上预训练模型评估</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>六个分类和六个分割任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2306.03831</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zhu-xlab/ChatEarthNet'>ChatEarthNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像图文对</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由ChatGPT-3.5生成的163,488对带有标题的图像-文本对和ChatGPT-4V(vision)生成的另外10,000对带有标题的图像-文本对组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2402.11325</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/vishalned/MMEarth-data'>MMEarth</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多模态预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含分布在世界各地的120万个地点的数据，在每个地点，收集了12个地理对齐模态的数据，分为像素级和图像级模式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2405.02771</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/162-hpJIlstgqTyC8SSFPcw#list/path=%2F'>全国shp数据汇总</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>用于地理学、城市规划、环境科学、交通管理等领域的研究</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>中国地理信息数字化的集大成者。它汇总了从中国湖泊、县界、公路、河流、铁路、国界线、经纬线、省会城市、省级行政区、县城驻地到线状省界的全方位地理信息。这些数据集以Shapefile（shp）格式提供，是GIS中最常用的地理数据格式之一。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>矢量</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1OLoK0pGHxbwpLSYrGzlQ6w (提取码:8ju2)'>东亚建筑物矢量数据</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>用于推动城市方面的大尺度研究</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>该数据集从0.5米分辨率的谷歌影像中提取获得</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>矢量</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>共计2.8亿个建筑矢量，涵盖中国、日本、韩国、朝鲜和蒙古5个国家。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1hfzASlI8qpubcKwrLdnkyw?pwd=8888 '>SinoLC-1</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>中国首套1m分辨率的全国土地覆盖数据集</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>盖中国全境约960万平方公里的1米分辨率土地</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/boranhan/Geospatial_Foundation_Models'>GeoPile-2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多模态预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>整合了四种关键遥感器模态的数据——RGB、Sentinel-2、SAR和DSM；整合四个数据集：SEN12MS、MDAS、GeoPile、MillionAID</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>四种模态、约两百万张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://arxiv.org/abs/2404.01260</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/mit-ll/tornet'>TorNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>AI预测龙卷风</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>每个风暴或龙卷风的样本包括两组六幅雷达图像。这两组图像对应于不同的雷达扫描角度。这六幅图像展示了不同的雷达数据产品，如反射率（显示降水强度）或径向速度（指示风是向雷达移动还是远离雷达）。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>该数据集包含超过200,000幅雷达图像，其中13,587幅描绘了龙卷风。其余的图像是非龙卷风的，来自两种类别的风暴：随机选择的严重风暴或误报风暴（导致预报员发出警告但没有产生龙卷风的风暴）</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2401.16437</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/records/7936885'>CACD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>用于农情监测、粮食安全评估、气候变化研究、生物多样性保护</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>中国1986-2021年30米分辨率的年度耕地数据集，每年1个tif文件</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://zenodo.org/records/7936885</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ennauata/buildings2vec'>Vectorizing World Buildings</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>提取建筑轮廓</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2001 张 256×256 像素的航空影像，训练集有 1601 张，测试集有 400 张</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ennauata.github.io/buildings2vec/page.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu-mix%20(vector)/whu_mix(vector).html'>WHU-Mix (vector) building dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 建筑物分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包括超过 64,000 张图像和 754,000 个单独的建筑实例，总地理面积约为 1100 平方公里。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/10104584</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/romainloiseau/EarthParserDataset'>Earth Parser Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 无监督实例分割和语义分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>涵盖了七个不同的场景，总面积超过7.7平方公里，包含约9800万个三维点</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://arxiv.org/abs/2304.09704</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zk2172-columbia/constellation-dataset'>Constellation</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像目标检测 高海拔下的目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含了从城市交通路口高海拔摄像头获取的13K图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2404.16944v1</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='未开源'>TextRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像图文匹配</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>https://www.mdpi.com/2072-4292/12/3/405</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2144张图像，从AID、Merced、PatternNet 和 NWPU 数据集收集图像，每个图像都由五个不同的句子注释。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='未开源'>VQA-TextRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像VQA</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>https://www.tandfonline.com/doi/abs/10.1080/01431161.2022.2145583</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>VQA-TextRS是一个由来自四个源数据集的2,144张RS图像组成的数据集，每个图像
有2-3对英语问答，共计6245对，分为4个问题类。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx'>ISPRS Vaihingen</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含33幅不同大小的遥感图像，6个最常见的土地覆盖类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://isprs-annals.copernicus.org/articles/I-3/293/2012/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx'>ISPRS Potsdam</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含28幅相同size的图像，6个最常见的土地覆盖类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://isprs-annals.copernicus.org/articles/I-3/293/2012/</td>
  </tr>
</table>

## 分类
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://weegee.vision.ucmerced.edu/datasets/landuse.html'>UCMerced_LandUse</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含21种土地利用类型的遥感影像，提取自 USGS National Map，由University of California, Merced于2010年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2010</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://dl.acm.org/doi/abs/10.1145/1869790.1869829</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/BED4RS/'>WHU RS19</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含19种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2012年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>950张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/palewithout/RSSCN7'>RSSCN7</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2015年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2800张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://mvr.whu.edu.cn/pubs/2015-IEEE_GRSL.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.researchgate.net/publication/271647282_RS_C11_Database'>RS_C11</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种土地利用类型的遥感影像，提取自Google Earth，由中科院于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1232张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://gcheng-nwpu.github.io/#Datasets'>NWPU-RESISC45</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含45种土地利用类型的遥感影像，提取自Google Earth，由西北工业大学于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>31500张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7891544/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/AID/'>AID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含30种土地利用类型的遥感影像，提取自Google Earth，由武汉大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7907303/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/RSIA-LIESMARS-WHU/RSD46-WHU'>RSD46-WHU</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含46种土地利用类型的遥感影像，提取自Google Earth、天地图，由武汉大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>117000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7827088/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的secenClass部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种土地利用类型的遥感影像，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset'>PatternNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含38种土地利用类型的遥感影像，提取自Google Map，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1706.03424</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/phelber/eurosat'>EuroSAT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种土地利用类型的遥感影像，提取自哨兵2，由德国凯泽斯劳滕大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>27000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8736785</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://drive.google.com/open?id=1Fk9a0DW8UyyQsR8dP2Qdakmr69NVBhq9'>OPTIMAL-31</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含21种土地利用类型的遥感影像，提取自Google Earth，由西北工业大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1860张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8454883</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/lehaifeng/CLRS'>Continual Learning Benchmark for Remote</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含25种土地利用类型的遥感影像，提取自Google Earth, Bing Map, Google Map, and Tianditu，由中南大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>15000张图片</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/1424-8220/20/4/1226</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.msadc.cn/main/setsubDetail?id=1369487569196158978; http://www.jors.cn/jrs/ch/reader/create_pdf.aspx?file_no=20209323&flag=1'>TG1HRSSC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含全色谱段(PAN)、可见近红外(VNI)、短波红外谱段(SWI)，包含9种土地利用类型的遥感影像，提取自天宫一号，由中国科学院空间应用工程与技术中心于2021年发布，包含波段:0.5—0.8μm、1band(PAN), 0.4—1.0μm、54band((VNI), 1.0—2.5μm、52band((SWI),</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>204张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.msadc.cn/main/setsubDetail?id=1370312964720037889； http://www.msadc.cn/group1/M00/00/08/CgId02Bio4KAazc6AEZR3GfuVic489.pdf
'>NaSC-TG2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物类型，
提取自天宫二号，
包含波段范围：0.40–1.04 µm，
由中国科学院空间应用工程与技术中心于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://csc.lsu.edu/~saikat/deepsat/'>SAT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>SAT数据集，包括SAT-4、SAT-6，2个数据子集，分别包含4种、6种土地利用类型的遥感影像，提取自the National Agriculture Imagery Program (NAIP) dataset，由路易斯安那州立大学与NASA于2015年发布，采用MATLAB的.mat数据存储格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>405000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.lmars.whu.edu.cn/prof_web/zhongyanfei/Code/Google_Dataset/Google%20dataset%20of%20SIRI-WHU_earth_im_tiff.7z'>SIRI-WHU</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>SIRI-WHU数据集，包括 google image、USGS image2个数据子集，分别包含12种、4种土地利用类型的遥感影像，分别提取自Google Earth、USGS，由武汉大学于2016年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7329997</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/lehaifeng/RSI-CB'>RSI-CB</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSI-CB数据集，包括RSI-CB128、RSI-CB256，2个数据子集，分别包含45种、35种土地利用类型的遥感影像，提取自多种数据，由中南大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>36000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/'>Multi-View Datasets中的CV-BrCT部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Multi-View Datasets数据集，CV-BrCT数据子集，包含8种土地利用类型的遥感影像，提取自航空影像及地面街景影像，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>48342张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2020/07/22/multi-view-datasets/'>Multi-View Datasets中的AiRound部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Multi-View Datasets数据集，AiRound数据子集，包含11种土地利用类型的遥感影像，提取自Sentinel-2等多源数据，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13980张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://data.mendeley.com/datasets/7j9bv9vwsx/2'>MLRSNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多标签分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含46种土地利用类型的遥感影像，提取自Google Earth，由中国地质大学于2020年发布，最大标签数13</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>109161张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271620302677</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/jonathan-roberts1/SATIN'>SATIN</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类 场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>一个元数据集，包含27个卫星和航空图像数据集，涵盖6个不同的任务:土地覆盖、土地利用、分层土地利用、复杂场景、罕见场景和假彩色场景。这些图像是全球分布的，由跨越5个数量级的分辨率、多个视图大小和250多个不同的类标签组成。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2304.11619</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021'>FloodNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类、分割、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>无人机收集，总共2343张图像，10个语义类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共2343张图像，用于分类和分割的测试集有400张，测试集有1050张图像，用于VQA的有1450张图像、4511给问答对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2012.02951</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://mediatum.ub.tum.de/1474000'>SEN12MS </a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类、用于土地覆盖制图的语义分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>所有块都以10米的地面采样距离进行完全地理参考，并覆盖所有有人居住的大陆和所有气象季节</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由180,662个双极合成孔径雷达（SAR）图像块、多光谱Sentinel-2图像块和MODIS土地覆盖地图三元组组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1906.07789</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://bigearth.net/'>BigEarthNet-MM</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检索和分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>由BigEarthNet-S1和S2组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含 590,326 对 Sentinel-1 和 Sentinel-2 图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2105.07921</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DiRS/'>MillionAID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>Million-AID的场景类别采用三级树的层次分类网络进行组织，51个叶节点在第二级分为28个父节点，在第一级分为8个节点，分别代表农业用地、商业用地、工业用地、公共服务用地、住宅用地、交通用地、未利用用地和水域8个底层场景类别。场景分类网络为数据集提供了良好的场景分类关系组织和可扩展性。每个场景类别的图像数量在2000到45000张之间，使数据集具有长尾分布的特性。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含100万个场景分类实例、有51个语义场景类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2006.12485</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/GeoX-Lab/G-RSIM/tree/main/TOV_v1'>TOV-RS-balanced</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含31个类别的50万个样本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/10110958</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/allenai/satlas-pretrain/tree/main/dataset'>SatlasPretrain</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>超过30 TB的卫星图像与137个标签类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2211.15660</td>
  </tr>
</table>

## 检测
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://ai.stanford.edu/~gaheitz/Research/TAS/'>TAS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由斯坦福大学于2008年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2008</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>30张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sourceforge.net/projects/oirds/'>OIRDS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物目标，提取自USGS、DARPA、VIVID，由雷神公司等于2009年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2009</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>900张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://downloads.greyc.fr/vedai/'>VEDAI</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含9种类型的遥感地物目标，提取自Utah AGRC，由卡昂大学于2015年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2015</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1210张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.kaggle.com/datasets/guofeng/hrsc2016'>HRSC2016</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含27种类型的遥感地物目标，提取自Google Earth，由西北工业大学于2016年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1061张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.dlr.de/eoc/en/desktopdefault.aspx/tabid-12760/22294_read-52777'>DLR3k</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物目标提取自无人机(Canon Eos 1Ds Mark III)由德国航天航空中心于2016年发布采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/CrazyStoneonRoad/TGRS-HRRSD-Dataset'>TGRS-HRRSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含13种类型的遥感地物目标，提取自Google Earth、百度地图，由中科院于2017年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>21761张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8676107</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://challenge.xviewdataset.org/data-download'>xView</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含60种类型的遥感地物目标，提取自WorldView 3，由DIUx、NGA于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1129张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://levir.buaa.edu.cn/Code.htm'>LEVIR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物目标，提取自Google Earth，由北京航天航空大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>22000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8106808</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.iuii.ua.es/datasets/masati/'>MASATI</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物目标，提取自Bing Maps，由阿利坎特大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>7389张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/4/511</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://research.utwente.nl/en/datasets/itcvd-dataset'>ITCVD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自航拍影像，由University of Twente Research Information于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>135张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8451454</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/iSAID/index.html'>iSAID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种类型的遥感地物目标，提取自Google Earth、JL-1、GF-2，由武汉大学于2019年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1905.12886</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.patreo.dcc.ufmg.br/2019/07/10/bridge-dataset/'>Bridge Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth、 OpenStreetMap，由Federal University of Minas Gerais于2019年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>500张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8876942</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cosmiqworks.org/RarePlanes/ https://www.graviti.cn/open-datasets/RarePlanes'>RarePlanes</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种飞机遥感影像，提取自WorldView-3，由In-Q-Tel、AI.Reverie于2020年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1507张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2006.02963</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/contestDetail?id=2&tab=data'>飞机目标识别-训练数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种飞机类型的遥感地物目标,提取自国产自主产权系列卫星，由中科院于2021年发布，采用oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>430张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/contestDetail?id=6&tab=data'>船只智能检测-训练数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自国产自主产权系列卫星
由中科院于2021年发布采用，oriented bounding boxes(OBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>25张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-Detection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>32825张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2111.12960</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-DET</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10209张图象</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-VID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>288个视频片段</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>DroneCrowd</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像人群计数</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自无人机数据，由天津大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1807张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2001.06303</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA1.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>15类，共188282个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA1.5</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>16类，共400000±个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2806张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/DOTA/index.html'>DOTA2.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'> 18类，共1,793,658个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>11268张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1711.10398</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://opensar.sjtu.edu.cn/DataAndCodes.html'>OpenSARShip</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Sentinel-1，由上海交通大学于2017年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>41张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8067489</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/chaozhong2010/HRSID'>HRSID</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Sentinel-1B、TerraSAR-X、TanDEM-X，由电子科技大学于2020年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5604张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9127939</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/fMoW/dataset'>fMoW</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>数据集由来自200多个国家的100多万张图像组成。对于每张图像，提供至少一个包含63个类别之一的边界框注释，其中包括一个“错误检测”类别。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100 多万张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018/papers/Christie_Functional_Map_of_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1AsdnO2-nadxTaq9_9Mo3Eg?pwd=tftf#list/path=%2F'>HSODBIT-V1</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>高光谱显著性目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>319幅高光谱图像及对应的伪彩色图像和像素级标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>323张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=16'>CASIA-aircraft</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感目标检测 飞机检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由中科院于2021年发布，采用json标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含29093个训练数据，11603个验证数据，17425个测试数据，共计58121个</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://aistudio.baidu.com/datasetdetail/131586'>CASIA-Ship</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感目标检测 船体检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自Google Earth，由中科院于2021年发布，采用json标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含571个训练数据，220个验证数据，327个测试数据，共计1118个</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://pan.baidu.com/s/1dIFOm4V2pM_AjhmkD1-Usw?pwd=SARD'>SARDet-100K</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检测 合成孔径雷达目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>涵盖六个不同的类别,由南开大学2024年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含约117K张图像和246K个对象实例</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2403.06534.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/blanchon/FAIR1M'>FAIR1M</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像目标检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含37种类型的遥感地物目标，共100 0000+个目标，提取自Gaofen satellites、Google Earth，由中科院等于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>15000+张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2103.05569</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zk2172-columbia/constellation-dataset'>Constellation</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像目标检测 高海拔下的目标检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含了从城市交通路口高海拔摄像头获取的13K图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2404.16944v1</td>
  </tr>
</table>

## 分割
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.usgs.gov/core-science-systems/nli/landsat/spatial-procedures-automated-removal-cloud-and-shadow-sparcs'>SPARCS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自 Landsat 8 OLI/TIRS，由University of Tennessee Knoxville于2014年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2014</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>80张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/6/6/4907stats?stats=v&utm_source=TrendMD&utm_medium=cpc&utm_campaign=Remote_Sens_TrendMD_0</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/record/1154821'>CITY-OSM</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6个城市，2种类别：街道和建筑，提取自Google Maps、OpenStreetMap，由ETH Zürich于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1671张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1707.06879</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0'>WHDLD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自UC Merced，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4940张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/6/964</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0'>DLRSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>基于UCMerced_LandUse数据集进行标注，包含17种类型的遥感地物类型标注数据，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/10/6/964</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ishann/aeroscapes'>Aeroscapes</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含11种类型的遥感地物类型，提取自航空影像，由Carnegie Mellon University于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3269张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/8354272</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.airs-dataset.com/'>AIRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自LINZ Data Service，由 University of Tokyo等，于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1047张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1807.09532</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmkemker/RIT-18'>RIT-18</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含18种类型的遥感地物类型，提取自Tetracam Micro-MCA6，包含7波段，由Rochester Institute of Technology于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271618301229</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/dronedeploy/dd-ml-segmentation-benchmark'>DroneDeploy</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自航空影像drones，由DroneDeploy于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>55张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/mitroadmaps/roadtracer/'>RoadTracer</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google earth、OSM，由MIT于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://roadmaps.csail.mit.edu/roadtracer/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/Bijie_pages.html'>Bijie Landslide Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种土地利用类型的遥感影像，提取自TripleSat，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>770张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/article/10.1007/s10346-020-01353-2</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/3DFGC_pages.html'>GF2 Dataset for 3DFGC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种土地利用类型的遥感影像，提取自GF2，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>11张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.tandfonline.com/doi/abs/10.1080/01431161.2019.1699973</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://project.inria.fr/aerialimagelabeling/'>Semantic Drone Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含22种土地利用类型的遥感影像，提取自航拍影像，由Graz University of Technology于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>400张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://inria.hal.science/hal-01468452/document</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_Cloud_Dataset.html'>WHU Cloud Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种土地利用类型的遥感影像，提取自Landsat 8，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>859张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9099032</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://landcover.ai.linuxpolska.com/'>landcover_ai</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物类型，提取自  public geodetic resource，由linuxpolska等于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>41张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2005.02264</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.uavid.nl/'>UAVid</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自航空影像，由University of Twente于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>300张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.10438</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.datafountain.cn/competitions/457/datasets'>全国人工智能大赛AI遥感影像</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>一级大类8种，二级子类17种，数据为0.1米-4米分辨率的高分一、二、六号，高景二号，北京二号，以及部分航空等数据源的可见光、多光谱载荷图像，由鹏城实验室和协办单位合作采集、标注、构建；</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.datafountain.cn/competitions/475'>BDCI2020</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，由BDCI于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>145981</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Junjue-Wang/LoveDA'>LoveDA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自Google Earth，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5987张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.researchgate.net/publication/355390292_LoveDA_A_Remote_Sensing_Land-Cover_Dataset_for_Domain_Adaptive_Semantic_Segmentation</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.grss-ieee.org/community/technical-committees/2022-ieee-grss-data-fusion-contest/'>MiniFrance-DFC22</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种土地利用类型的遥感影像，提取自航空影像，由IADF TC于2022年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2322张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cs.toronto.edu/~vmnih/data/'>Massachusetts Roads</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由University of Toronto于2013年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2013</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>804张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.cs.toronto.edu/~vmnih/docs/Mnih_Volodymyr_PhD_Thesis.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.cs.toronto.edu/~vmnih/data/'>Massachusetts Builds</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由University of Toronto于2013年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2013</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>151张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.cs.toronto.edu/~vmnih/docs/Mnih_Volodymyr_PhD_Thesis.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://deepglobe.org/challenge.html'>DeepGlobe Land Cover Classificat</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含7种类型的遥感地物类型，提取自DigitalGlobe，由CVPR于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>803张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Demir_DeepGlobe_2018_A_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://deepglobe.org/challenge.html'>DeepGlobe Road Detection Challen</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自DigitalGlobe，由CVPR于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>6226张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w4/Demir_DeepGlobe_2018_A_CVPR_2018_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html'>WHU Building Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>总共三部分，global cities、East Asia、Aerial imagery datase，包含1种类型的遥感地物类型，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>25781张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8444434</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmcong/ORSSD-dataset'>ORSSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自 Google Earth，由北京交通大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>800张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1906.08462</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/rmcong/EORSSD-dataset'>EORSSD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含8种类型的遥感地物类型，提取自Google Earth，由北京交通大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2000张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2011.13144</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/SorourMo/38-Cloud-A-Cloud-Segmentation-Dataset'>38-Cloud</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Landsat 8，由Simon Fraser University于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集中有 8400 个图像块，38个训练场景，测试集中有 9201 个图像块，20个测试场景。每个图像块包含 4 个相应的光谱通道，分别是红色（波段 4）、绿色（波段 3）、蓝色（波段 2）和近红外（波段 5）。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1901.10077</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/SorourMo/95-Cloud-An-Extension-to-38-Cloud-Dataset'>95-Cloud</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Landsat 8，由Simon Fraser University于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集中有 34701个图像块，95个训练场景，测试集中有 9201 个图像块，20个测试场景。每个图像块包含 4 个相应的光谱通道，分别是红色（波段 4）、绿色（波段 3）、蓝色（波段 2）和近红外（波段 5）。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://deepai.org/publication/cloud-net-a-cloud-segmentation-cnn-for-landsat-8-remote-sensing-imagery-optimized-with-filtered-jaccard-loss-function</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的Fine部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含15种类型的遥感地物类型，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://x-ytong.github.io/project/GID.html'>WHU_GID中的Large-scale部分</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物类型，提取自高分2卫星，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>150张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0034425719303414</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/MarcWong/UDD'>Urban Drone Dataset(UDD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 地物类型分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包括UDD5、UDD6两个数据子集，分别包含5、6种类型的遥感地物类型，提取自无人机数据（DJI Phantom 4），由北京大学于2018年发布

</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集120张图像，测试集40张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/chapter/10.1007/978-3-030-03398-9_30</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/'>BH-POOLS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 水池分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>各包含1种类型的遥感地物类型，提取自GoogleEarth，由Federal University of Minas Gerais于2020年发布
</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由8个不同街区的200张4K图像组成(每个街区25张图像)，包含3980个带注释的水池</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://patreo.dcc.ufmg.br/2020/07/29/bh-pools-watertanks-datasets/'>BH-WATERTANKS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 水箱分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>各包含1种类型的遥感地物类型，提取自GoogleEarth，由Federal University of Minas Gerais于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由6个社区的150张4K图像组成(每个社区25张图像)，包含16216个带注释的水箱。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>这个和上面那个是一个,和一起叫"BH-DATASET"</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection/data'>Dstl Satellite Imagery Feature Detection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自WorldView 3，由DigitalGlobe于2017年发布，采用MultiPolygons标注格式，波段范围：全色450-800 nm，3波段；多光谱 (red, red edge, coastal, blue, green, yellow, near-IR1 and near-IR2)400 nm - 1040 nm，8波段；短波红外 1195 nm - 2365 nm，8波段</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集25张图像，测试集32张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.crowdai.org/challenges/mapping-challenge'>Mapping Challenge</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Map，由crowdAI于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集280741张图像，验证集60317张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.frontiersin.org/articles/10.3389/frai.2020.534696/full</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://competitions.codalab.org/competitions/20100'>2018 Open AI Tanzania Building Footprint</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由SUZA等于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/record/4172871'>Sentinel-2 Cloud Mask Catalogue</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 云体分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含3种类型的遥感地物类型，提取自Sentinel-2，于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>513张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021'>FloodNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类、分割、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>无人机收集，总共2343张图像，10个语义类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共2343张图像，用于分类和分割的测试集有400张，测试集有1050张图像，用于VQA的有1450张图像、4511给问答对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2012.02951</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://mediatum.ub.tum.de/1474000'>SEN12MS </a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像场景分类、用于土地覆盖制图的语义分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>所有块都以10米的地面采样距离进行完全地理参考，并覆盖所有有人居住的大陆和所有气象季节</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由180,662个双极合成孔径雷达（SAR）图像块、多光谱Sentinel-2图像块和MODIS土地覆盖地图三元组组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1906.07789</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ViTAE-Transformer/SAMRS'>SAMRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含三个子集：SOTA子集17480张图像，18个类；SIOR子集23463张图像，20个类；FAST子集64147张图像，37个类</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2305.02034</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu-mix%20(vector)/whu_mix(vector).html'>WHU-Mix (vector) building dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 建筑物分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包括超过 64,000 张图像和 754,000 个单独的建筑实例，总地理面积约为 1100 平方公里。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/10104584</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/romainloiseau/EarthParserDataset'>Earth Parser Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割 无监督实例分割和语义分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>涵盖了七个不同的场景，总面积超过7.7平方公里，包含约9800万个三维点</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://arxiv.org/abs/2304.09704</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx'>ISPRS Vaihingen</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含33幅不同大小的遥感图像，6个最常见的土地覆盖类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://isprs-annals.copernicus.org/articles/I-3/293/2012/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx'>ISPRS Potsdam</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分割</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2012</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含28幅相同size的图像，6个最常见的土地覆盖类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://isprs-annals.copernicus.org/articles/I-3/293/2012/</td>
  </tr>
</table>

## 变化检测
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://web.eee.sztaki.hu/remotesensing/airchange_benchmark.html'>SZTAKI-INRIA AirChange</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，由MTA SZTAKI于2009年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2009</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>13×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/iel5/36/4358825/05169964.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/gistairc/ABCDdataset'>AIST Building Change Detection(ABCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型提取自 aerial images 由National Institute of Advanced Industrial Science and Technology (AIST)于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含fixed-scale、resized 2个子集，分别有4,253 * 2、4,223 * 2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7986759</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://study.rsgis.whu.edu.cn/pages/download/building_dataset.html'>WHU Building Change Detection Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自航空影像，由武汉大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/8444434</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://paperswithcode.com/dataset/cdd-dataset-season-varying'>CDD Dataset (season-varying)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 季节变化</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种变化类型，提取自Google Earth (DigitalGlobe)，由GosNIIAS于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集10000, 验证集3000, 测试集3000</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://paperswithcode.com/paper/change-detection-in-remote-sensing-images</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rcdaudt.github.io/oscd/'>Onera Satellite Change Detection (OSCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Sentinel-2，由Universit´e Paris-Saclay、 T´el´ecom ParisTech于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>14×2张训练，10×2张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.08468</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://sigma.whu.edu.cn/newspage.php?q=2019_03_26'>Multi-temporal Scene WuHan (MtS-WH)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 多时相场景变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含9种土地利用类型的遥感影像，提取自IKONOS传感器，由武汉大学2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>每个时相训练集包括190张影像，测试集包括1920张影像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/GeoZcx/A-deeply-supervised-image-fusion-network-for-change-detection-in-remote-sensing-images/tree/master/dataset'>DSIFN Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自GoogleEarth，由武汉大学于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练数据集中有3600对图像，验证数据集中有340对图像，测试数据集中有48对图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.sciencedirect.com/science/article/pii/S0924271620301532</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rcdaudt.github.io/hrscd/'>High Resolution Semantic Change (HRSCD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自 IGS’s BD ORTHO database，由ETH Zürich / EcoVision Lab于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>291×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/1810.08452</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://xview2.org/dataset'>xBD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 灾害前后变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含全球六种不同类型自然灾害，每种灾害四种变化状态</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>22068张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPRW_2019/html/cv4gc/Gupta_Creating_xBD_A_Dataset_for_Assessing_Building_Damage_from_Satellite_CVPRW_2019_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/daifeng2016/Change-Detection-Dataset-for-High-Resolution-Satellite-Imagery'>Change-Detection-dataset-for-High-resolution-Satellite-Image</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，由ieee于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'> 20张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9161009</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://chenhao.in/LEVIR/'>LEVIR-CD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，由北京航空航天大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>637张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/12/10/1662</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rs.sensetime.com/competition/index.html#/info'>SenseEarth ChangeDetection</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种变化类型的遥感地物类型，由商汤科技于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练2968张, 验证847张</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://captain-whu.github.io/SCD/'>SEmantic Change detectiON Data(SECOND)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含6种类型的遥感地物类型，提取自航空影像，由ETH Zürich / EcoVision Lab于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4662×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://captain-whu.github.io/SCD/SCD_files/Semantic_Change_Detection.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://zenodo.org/records/4280482'>Sentinel-2 Multitemporal Cities Pairs</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Sentinel-2，由Wageningen University于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>1520×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2101.08122</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/liumency/SYSU-CD'>Sun Yat-Sen University (SYSU)-CD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型变化信息，提取自 aerial image，由中山大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>20000×2张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9467555</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=30'>S2Looking</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自国产自主产权系列卫星，由中科院于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3500对训练图像，500对验证图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.rsaicp.com/portal/dataDetail?id=27'>LEVIR-CD2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 建筑物</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物类型，提取自Google Earth，基于LEVIR-CD数据集，由中科院于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2800对训练图像、840对验证图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://gitlab.citius.usc.es/hiperespectral/ChangeDetectionDataset'>Change Detection Dataset(CDD)</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感变化检测 遥感地物类型</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含5种类型的遥感地物类型，包含224波段，提取自HYPERION,AVIRIS sensor，于2019年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>3对图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/YZHJessica/CDVQA'>CDVQA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>选择现有的语义变化检测数据集SECOND作为基础数据，自动生成CDVQA数据集。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含2968对航拍图像和超过122000对对应的问答</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2112.06343</td>
  </tr>
</table>

## 目标跟踪
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://aistudio.baidu.com/datasetdetail/91853'>UAV123</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>UAV123数据集，包含3个子集，子集1包含103个序列，子集2包含12个序列，子集3包含8个序列，提取自 UAV (DJIS1000)、UAV simulator，由King Abdullah University of Science and Technology于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共包含123个视频序列和超过110K帧</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://link.springer.com/chapter/10.1007/978-3-319-46448-0_27</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://www.csdata.org/p/387/'>地/空背景下红外图像弱小飞机目标检测跟踪数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标跟踪 红外图像弱小飞机目标检测跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含1种类型的遥感地物目标，提取自航拍影像，由国防科技大学于2019年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2019</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>共计22段数据、30条航迹、16177帧图像、16944个目标</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://www.csdata.org/p/387/</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.scidb.cn/en/detail?dataSetId=808025946870251520'>复杂背景下红外弱小运动目标检测数据集</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频目标检测、跟踪 复杂背景下红外弱小运动目标</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自航拍影像，由国防科技大学于2021年发布，采用Chip标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含350个视频，150185个图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.scidb.cn/en/detail?dataSetId=808025946870251520</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-SOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频单目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>167段视频序列，1393000帧</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9573394</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/VisDrone/VisDrone-Dataset'>VisDrone2019-MOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频多目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含10种类型的遥感地物目标，提取自无人机数据，由天津大学于2018年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2018</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集56段视频，24201帧, 验证集7段视频,2819帧 测试集33段视频，12968帧 </td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9573394</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-SOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频单目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100段视频序列，32,825帧图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9625976</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://satvideodt.github.io/'>VISO-MOT</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频多目标跟踪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>包含4种类型的遥感地物目标，提取自JL1，由国防科技大学于2021年发布，采用horizontal bounding boxes (HBB)标注格式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100段视频序列，32,825帧图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/9625976</td>
  </tr>
</table>

## 图像生成
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/phillipi/pix2pix'>Aerial to Map</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 风格迁移</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自Google Maps，由UC Berkeley于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>训练集1096张图像 ，验证集1098 张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://www.dropbox.com/s/k2i3p7puuwl2g59/Haze1k.zip?dl=0'>SateHaze1k</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 图像去噪</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>提取自GF-2、GF-3，由清华大学于2017年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>400×3张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_WACV_2020/papers/Huang_Single_Satellite_Optical_Imagery_Dehazing_using_SAR_Image_Prior_Based_WACV_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html'>WHU Multi-view Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自航拍影像，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>21600张训练，6800张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_A_Novel_Recurrent_Encoder-Decoder_Structure_for_Large-Scale_Multi-View_Stereo_Reconstruction_CVPR_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/WHU_MVS_Stereo_dataset.html'>WHU Stereo Dataset</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自航拍影像，由武汉大学于2020年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>16632张训练，5236 张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content_CVPR_2020/papers/Liu_A_Novel_Recurrent_Encoder-Decoder_Structure_for_Large-Scale_Multi-View_Stereo_Reconstruction_CVPR_2020_paper.pdf</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu_tlc.html'>WHU TCL SatMVS dataset1.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自ZY3，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>173张训练，127张测试</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/ICCV2021/html/Gao_Rational_Polynomial_Camera_Model_Warping_for_Deep_Learning_Based_Satellite_ICCV_2021_paper.html</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='http://gpcv.whu.edu.cn/data/whu_tlc.html'>WHU TCL SatMVS dataset2.0</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像生成 三维重建</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>用于重建DSM，提取自ZY3，由武汉大学于2021年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>5011张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/ICCV2021/html/Gao_Rational_Polynomial_Camera_Model_Warping_for_Deep_Learning_Based_Satellite_ICCV_2021_paper.html</td>
  </tr>
</table>

## 单模态预训练
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/satellogic/EarthView/tree/main'>EarthView</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感模型预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>300万张高分辨率训练数据集</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ServiceNow/seasonal-contrast'>SeCo</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像无监督预训练  不同季节的图像</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>从Sentinel-2收集的，其原则是收集大规模、未标记和未经整理的遥感数据集，这些数据集包含来自不同时间戳的多个地球位置的图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>两个版本有一个100K的，有一个1M的</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2103.16607</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/utkarshmall13/CACo'>CACo</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像自监督预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>超过100万图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://openaccess.thecvf.com/content/CVPR2023/html/Mall_Change-Aware_Sampling_and_Contrastive_Learning_for_Satellite_Images_CVPR_2023_paper.html</td>
  </tr>
</table>

## 评估
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ServiceNow/geo-bench'>GEO-Bench</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感数据上预训练模型评估</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>六个分类和六个分割任务</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2306.03831</td>
  </tr>
</table>

## VQA
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA-LR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 低分辨率</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>使用哨兵2号的图像和来自OSM的问题和答案</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>772张图像、77232个问题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2003.07333</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA-HR</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 高分辨率</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>USGS的高分辨率(15.24cm)正校正图像和OSM的问答</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10659张图像、955664个问题</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2003.07333</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://rsvqa.sylvainlobry.com/#dataset'>RSVQA×BEN</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>从BigEarthNet数据集中提取图像/问题/答案</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含近1500万个样本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9553307</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/spectralpublic/RSIVQA'>RSIVQA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSIVQA的图像来自三个RSI分类数据集(UCM、Sydney和AID)和两个RSI目标检测数据集(HRRSD和DOTA)。基于图像生成问题和答案，形成图像-问题-答案三元组。问题、答案及其对应关系可以在此存储库的txt文件中找到。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>有37264张图像和111693张图像-问答三元组</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9444570</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/YZHJessica/CDVQA'>CDVQA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像问答 变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>选择现有的语义变化检测数据集SECOND作为基础数据，自动生成CDVQA数据集。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含2968对航拍图像和超过122000对对应的问答</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2112.06343</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/BinaLab/FloodNet-Challenge-EARTHVISION2021'>FloodNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像分类、分割、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>无人机收集，总共2343张图像，10个语义类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>总共2343张图像，用于分类和分割的测试集有400张，测试集有1050张图像，用于VQA的有1450张图像、4511给问答对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2012.02951</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Lavender105/RSGPT'>RSIEval</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100个人工注释的标题和936个视觉问答对，包含丰富的信息和开放式的问题和答案。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2307.15266</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='nan'>VQA-TextRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像VQA</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>https://www.tandfonline.com/doi/abs/10.1080/01431161.2022.2145583</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>VQA-TextRS是一个由来自四个源数据集的2,144张RS图像组成的数据集，每个图像
有2-3对英语问答，共计6245对，分为4个问题类。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>nan</td>
  </tr>
</table>

## 图文对
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/xiaoyuan1996/AMFMN'>RSITMD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感多模态检索</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>RSITMD（遥感图像-文本匹配数据集）是Yuan等人提出的一个细粒度且富有挑战性的遥感数据集，适用于遥感多模态检索任务。相比其他遥感图像-文本配对数据集，它具有描述物体间关系的详细说明。此外，该数据集还包含了关键词属性（每张图像1至5个关键词），可用于基于关键词的遥感文本检索任务。该数据集中共有4,743张图像跨越32个场景，共包含23,715条标注，其中21,829条为非重复标注。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4743张图像，23715条标注</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2204.09868</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/Zilun/RS5M'>RS5M</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图文匹配</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>图像-文本配对的数据集RS5M，其中包含500万张带有英文描述的遥感图像。该数据集是通过筛选公开可用的图像-文本配对数据集并用预训练的视觉-语言模型标注仅具有标签的遥感数据集得到的。这构成了第一个大规模的遥感图像-文本配对数据集。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>500万张带有英文描述的遥感图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2306.11300</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://huggingface.co/datasets/mikonvergence/LAION-EO'>LAION-5B</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像文本对</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>LAION-5B的子集，卫星图像文本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>版本0有24,933张图像、版本1有112,985张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2309.15535</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Lavender105/RSGPT'>RSICap</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕、图文检索</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>该数据集为每张图像提供了详细的描述，包括场景描述(例如，住宅区、机场或农田)以及物体信息(例如，颜色、形状、数量、绝对位置等)</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2585对具有高质量人工注释字幕的图像-文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2307.15266</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://bigearth.net/'>BigEarthNet-MM</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像检索和分类</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>由BigEarthNet-S1和S2组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2021</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含 590,326 对 Sentinel-1 和 Sentinel-2 图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2105.07921</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zhu-xlab/ChatEarthNet'>ChatEarthNet</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像图文对</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>由ChatGPT-3.5生成的163,488对带有标题的图像-文本对和ChatGPT-4V(vision)生成的另外10,000对带有标题的图像-文本对组成</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2402.11325</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='nan'>TextRS</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像图文匹配</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2020</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2144张图像，从AID、Merced、PatternNet 和 NWPU 数据集收集图像，每个图像都由五个不同的句子注释。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/12/3/405</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>UCM-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>该图像数据是从USGS国家地图城市区域影像集合中提取的，包含2,100张RGB航拍图像，覆盖21个类别。每张图像配有5条描述性文字，总计有2032条独特标注。图像分辨率为256×256像素，空间分辨率为1英尺。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2100张图像、每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7546397</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>Sydney-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>悉尼数据集包含来自谷歌地球的澳大利亚悉尼的图像。它包含属于7个类别的613个图像。图像是(500,500) RGB，并为每个图像提供5个caption。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2016</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>613张图像，每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/abstract/document/7546397</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/201528014227051/RSICD_optimal'>RSICD</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕、图文检索</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>超过一万张遥感图像是从谷歌地球、百度地图、MapABC、天地图等平台收集而来的。这些图像被固定为 224X224 像素，具有不同的分辨率。总共有 10921 张遥感图像，每张图像配有5句描述，共有18,190条独特标注。据我们所知，这个数据集是用于remote sensing image caption任务中最大的数据集。数据集中的样本图像具有高类内多样性和低类间差异性。包含30种类型的遥感地物类型</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2017</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>10921张图像，每张图像5条描述</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1712.07835</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/HaiyanHuang98/NWPU-Captions'>NWPU-Captions</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>NWPU-Captions包含了157,500个句子，所有31,500张图片都由七名经验丰富的志愿者手动注释。NWPU-Captions相对于当前公开可用的基准数据集的优越性不仅在于其更大的规模，还在于其对复杂场景的更广泛覆盖以及描述词汇的丰富多样性。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>157,500个句子，31,500张图片</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/1703.00121</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Chen-Yang-Liu/LEVIR-CC-Dataset'>LEVIR-CC</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕 变化检测</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>每对图像包括变化前和变化后的，五句描述变化的话，由北京航空航天大学于2022年发布</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含10077对双时态遥感图像和50385个描述图像之间差异的句子</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://ieeexplore.ieee.org/document/9934924</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://opendatasharing.s3.us-west-2.amazonaws.com/SkyScript'>SkyScript</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>涵盖超过29K个不同的语义标签</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>520万对遥感图像-文本对</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2312.12856</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://lcmou.github.io/ERA_Dataset/'>CapERA</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视频字幕</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>25个类别，每个视频五个字幕</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>视频、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>2864个5秒的视频，每秒24帧，14,320个字幕</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.mdpi.com/2072-4292/15/8/2139</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/Lavender105/RSGPT'>RSIEval</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像字幕、问答</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>100个人工注释的标题和936个视觉问答对，包含丰富的信息和开放式的问题和答案。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2307.15266</td>
  </tr>
</table>

## 视觉定位
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/ZhanYang-nwpu/RSVG-pytorch'>DIOR_RSVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>是Zhan等人于2022年引入的一个全面的遥感视觉定位基准数据集（Remote Sensing Visual Grounding, RSVG）。RSVG任务专注于在遥感图像中定位由查询语句所指的对象。该数据集建立在最初设计用于目标检测的DIOR遥感图像数据集基础之上。RSVGD包含38,320对遥感图像-文本对以及17,402张遥感图像，平均表达长度为7.47，词汇表规模为100。图像分辨率为800×800像素，空间分辨率范围从0.5米到30米。文本描述是根据模板和预定义规则合成生成的。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>38320对遥感图像-文本对以及17402张遥感图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/pdf/2210.12634</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/like413/OPT-RSVG'>OPT-RSVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>14个类别</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2023</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含25,452张图像和48,952对图像查询</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://www.researchgate.net/publication/373146282_LaLGA_Multi-Scale_LanguageAware_Visual_Grounding_on_Remote_Sensing_Data</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://sunyuxi.github.io/publication/GeoVG'>GeoVG</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像视觉定位</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>4,239张图片，包括5,994个对象实例和7,933个指代表达</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://dl.acm.org/doi/abs/10.1145/3503161.3548316</td>
  </tr>
</table>

## 多模态预训练
<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/zhu-xlab/SSL4EO-S12'>SSL4EO-S12</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像无监督/自监督预训练 用于地球观测的大规模多模态多时相数据集</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2022</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>该数据集由来自全球251079个地点的未标记的三元组(Sentinel-1双极化SAR, Sentinel-2大气顶部多光谱，Sentinel-2表面反射率多光谱)组成，每个patch覆盖2640mx2640m，包括四个季节时间戳。</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2211.07044</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/vishalned/MMEarth-data'>MMEarth</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多模态预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>nan</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像、文本</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>包含分布在世界各地的120万个地点的数据，在每个地点，收集了12个地理对齐模态的数据，分为像素级和图像级模式</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>https://arxiv.org/abs/2405.02771</td>
  </tr>
</table>

<table style="width:100%;">
<tr>
<td>数据集名称</td>
<td>key</td>
<td>value</td>
<td>备注</td>
</tr>
  <tr>
    <td rowspan='6' style='text-align: left; width:10%;'><a href='https://github.com/boranhan/Geospatial_Foundation_Models'>GeoPile-2</a></td>
    <td style='text-align: left; width:10%;'>任务</td>
    <td style='text-align: left; width:20%;white-space: normal;'>遥感图像多模态预训练</td>
    <td rowspan='6' style='text-align: left; width:40%;word-wrap: break-word;white-space: normal;'>整合了四种关键遥感器模态的数据——RGB、Sentinel-2、SAR和DSM；整合四个数据集：SEN12MS、MDAS、GeoPile、MillionAID</td>
  </tr>
  <tr>
    <td style='text-align: left;'>发布时间/Project</td>
    <td style='text-align: left;white-space: normal;'>2024</td>
  </tr>
  <tr>
    <td style='text-align: left;'>模态</td>
    <td style='text-align: left;white-space: normal;'>图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>数量</td>
    <td style='text-align: left;white-space: normal;'>四种模态、约两百万张图像</td>
  </tr>
  <tr>
    <td style='text-align: left;'>链接</td>
    <td style='text-align: left;white-space: normal;'>http://arxiv.org/abs/2404.01260</td>
  </tr>
</table>

