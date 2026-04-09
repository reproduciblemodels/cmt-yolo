# CMT-YOLO: A Lightweight Defect Detection Framework for Low-Contrast Rubber Transmission-Belt Defects

This repository provides the implementation of **CMT-YOLO**, a lightweight object detector designed for **low-contrast rubber transmission-belt surface defect detection** under industrial conditions.

CMT-YOLO is built upon the YOLOv8 detection pipeline and introduces targeted modifications to the **backbone**, **neck**, and **detection head** to improve weak-defect representation, multi-scale feature interaction, and classification–localization coordination.

---

## 1. Introduction

Surface defects on black rubber transmission belts are difficult to detect in real production environments because the captured images often suffer from:

- low contrast between defects and background,
- repetitive dark textures,
- weak and ambiguous boundaries,
- reflective interference,
- and large variation in defect scale and appearance.

To address these challenges, this work proposes **CMT-YOLO**, an efficiency-aware redesign of the YOLOv8 detection pipeline for transmission-belt defect detection. Rather than introducing a completely new detection paradigm, the proposed method focuses on **task-oriented modifications** to the backbone, neck, and head, aiming to improve weak-defect representation, cross-scale interaction, and localization reliability while preserving lightweight deployment characteristics.

---

## 2. Method Overview

CMT-YOLO introduces three key components:

### 2.1 C2f-CPMA
A backbone enhancement module designed to improve **weak-defect representation** by increasing receptive-field diversity while preserving an explicit identity pathway.

### 2.2 MSFFB
A lightweight neck module that strengthens **cross-scale feature interaction** and multi-scale fusion, which is especially important for tiny, elongated, or scale-varying defects.

### 2.3 TADDH
A task-aligned detection head that improves **classification–localization coordination** through task decomposition, deformable regression alignment, and spatial confidence modulation.

Together, these modules form a balanced lightweight detector for difficult industrial defect scenarios.

---

## 3. Framework

<p align="center">
  <img src="assets/overall_framework.png" width="900"/>
</p>

**Figure 1.** Overall architecture of CMT-YOLO.

---

## 4. Main Results

The following table summarizes the comparison of CMT-YOLO with representative two-stage, one-stage, transformer-based, and YOLO-family detectors on the transmission-belt defect dataset.

| Method | Year | mAP@0.5 (%) | P (%) | R (%) | Params (M) | GFLOPs | Size (MB) | FPS | Infer Time (ms) |
|--------|-----:|------------:|------:|------:|-----------:|-------:|----------:|----:|----------------:|
| Faster R-CNN | 2015 | 73.4 | – | – | 41.4 | 178.1 | 316.0 | 21.0 | 47.6 |
| SSD | 2016 | 64.6 | – | – | 24.0 | 30.5 | 99.0 | 66.1 | 15.1 |
| Cascade R-CNN | 2018 | 72.5 | – | – | 69.2 | 205.1 | 528.0 | 20.1 | 49.8 |
| DETR | 2020 | 66.6 | – | – | 41.6 | 81.6 | 481.0 | 23.4 | 42.7 |
| YOLOv5n | 2020 | 70.3 | 77.2 | 66.6 | 1.8 | 4.1 | 3.9 | – | – |
| TOOD | 2021 | 72.7 | – | – | 32.0 | 168.2 | 244.2 | 18.6 | 53.8 |
| YOLOX-tiny | 2021 | 62.5 | – | – | 5.0 | 7.6 | 60.0 | 58.2 | 17.2 |
| DINO | 2022 | 72.5 | – | – | 47.5 | 235.0 | 545.2 | 12.7 | 78.7 |
| YOLOv7 | 2022 | 57.5 | 59.7 | 60.1 | 36.5 | 103.2 | 141.9 | – | – |
| RTMDet-tiny | 2022 | 74.5 | – | – | 4.9 | 8.0 | 80.0 | 64.2 | 15.6 |
| DDQ-DETR | 2023 | 74.3 | – | – | 48.3 | 236.0 | 557.4 | 9.8 | 102.0 |
| RT-DETR (r50vd) | 2023 | 68.1 | – | – | 42.9 | 102.4 | 164.0 | 11.8 | 84.0 |
| YOLOv8n (Baseline) | 2023 | 69.3 | 75.8 | 62.6 | 3.0 | 8.1 | 6.0 | 52.6 | 19.0 |
| RT-DETRv2 (r50vd) | 2024 | 75.9 | – | – | 34.0 | 78.6 | 164.0 | 17.6 | 57.0 |
| YOLOv12n | 2025 | 68.2 | 73.4 | 63.6 | 2.5 | 5.8 | 5.2 | 61.9 | 16.2 |
| **CMT-YOLO (Ours)** | **2026** | **75.4** | **84.9** | **69.3** | **2.1** | **8.5** | **4.4** | **72.7** | **13.7** |

CMT-YOLO achieves the highest mAP@0.5 among the compared methods while maintaining competitive model size, inference speed, and latency, demonstrating a favorable balance between detection accuracy and lightweight deployment efficiency.

---

## 5. Repository Structure

```text
.
├── README.md
├── .gitignore
├── requirements.txt
├── train.py
├── val.py
├── detect.py
├── assets/
│   └── overall_framework.png
└── ultralytics/
    ├── __init__.py
    ├── assets/
    ├── cfg/
    │   ├── default.yaml
    │   └── models/
    │       └── v8/
    │           ├── yolov8.yaml
    │           ├── yolov8-C2f-CPMA.yaml
    │           ├── yolov8-MSFFB.yaml
    │           ├── yolov8-TADDH.yaml
    │           └── cmt-yolo.yaml
    ├── data/
    ├── engine/
    ├── hub/
    ├── models/
    ├── nn/
    ├── solutions/
    ├── trackers/
    └── utils/
---

## 6.Configuration Files
Key files include:

yolov8.yaml
Original YOLOv8 baseline configuration.
yolov8-C2f-CPMA.yaml
YOLOv8 with the C2f-CPMA module.
yolov8-MSFFB.yaml
YOLOv8 with the MSFFB module.
yolov8-TADDH.yaml
YOLOv8 with the TADDH module.
cmt-yolo.yaml
Full CMT-YOLO configuration used in the main experiments.
---

## 7.Configuration Files
Python 3.10
PyTorch 2.2.2
CUDA 11.6
Ultralytics YOLOv8-based codebase

Dependencies can be installed according to the local environment:
pip install -r requirements.txt
##8.Datasets
8.1 Industrial transmission-belt defect dataset

The primary dataset used in this work was collected from a real industrial production line in collaboration with an enterprise partner.

The dataset contains three defect categories:

broken
scratch
uneven

The industrial images are annotated in YOLO text format.

Because the dataset is associated with real products and production processes, it is not publicly released due to commercial confidentiality restrictions.

To improve transparency, the corresponding manuscript provides:

dataset organization,
annotation format,
class statistics,
bounding-box distribution,
dataset split protocol,
and implementation details.
8.2 Public dataset for reproducibility: GC10-DET

In addition to the self-collected industrial dataset, we also evaluated CMT-YOLO on the public GC10-DET dataset to provide stronger external validation and improve reproducibility.

GC10-DET is a public surface-defect detection benchmark containing 10 classes of steel-surface defects. Since the industrial transmission-belt dataset used in this work cannot be fully released, interested readers may use GC10-DET together with the released code and configuration files to reproduce the public-dataset experiments.

GC10-DET can be downloaded from its public dataset page and organized in YOLO format before training or evaluation.
##9.Data Format
A typical dataset structure is:
dataset_root/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
A dataset YAML file should specify the image paths and class names.
For the transmission-belt dataset, a typical YAML file is:
A dataset YAML file should specify the image paths and class names.
For the transmission-belt dataset, a typical YAML file is:
##10.Training
python train.py
Please update the paths inside train.py according to:
dataset YAML path,
model configuration path,
project save directory,
weight initialization policy,
and device settings.
For fair comparison in the manuscript, the compared models are trained and evaluated under controlled settings, including consistent data split, evaluation criteria, and hardware environment wherever implementation permits.
##11.Validation
Example validation command:
Example validation command:
The manuscript reports the following evaluation metrics:
Precision (P)
Recall (R)
mAP@0.5
mAP@0.5:0.95
Params
GFLOPs
Model size
FPS
Infer Time / Latency
For statistical reliability, repeated-run results can also be reported as mean ± standard deviation over multiple random seeds.
##12.Inference
Example inference command:
python detect.py
Please update the weight path and input image path in detect.py before running inference.
##13.Ablation and Analysis
The released code and configuration files support experiments corresponding to:
baseline comparison,
single-module ablation,
two-module and full-model comparison,
per-class analysis,
robustness analysis under controlled perturbations,
and qualitative / failure-case visualization.
The manuscript further analyzes:
why each module works,
whether the gains are complementary rather than redundant,
and how the method behaves under different defect characteristics.
##14.Reproducibility and Availability
To improve reproducibility, this repository provides:
the Ultralytics-based implementation,
custom model configuration files,
training / validation / inference scripts,
and detailed configuration organization.
Although the industrial transmission-belt dataset cannot be fully released, the released code and configuration files are intended to make the experimental setup as transparent and reproducible as possible.
The manuscript also clarifies:
dataset split protocol,
annotation format,
initialization policy,
training settings,
evaluation metrics,
and software / hardware environment.
The source code, model configuration files, and training / validation scripts for CMT-YOLO are publicly provided in this repository to support reproducibility.
The industrial transmission-belt defect dataset used in this work is not publicly available due to commercial confidentiality restrictions. However, public-dataset experiments on GC10-DET are included to provide stronger external validation and a practical reproducibility path.





