# CMT-YOLO: A Lightweight Defect Detection Framework for Low-Contrast Rubber Transmission-Belt Defects

This repository provides the implementation of **CMT-YOLO**, a lightweight object detector designed for **low-contrast rubber transmission-belt surface defect detection** under industrial conditions.

The method is built upon the YOLOv8 detection pipeline and introduces targeted modifications to the **backbone**, **neck**, and **detection head** to improve weak-defect representation, multi-scale feature interaction, and classification–localization coordination.

---

## Overview

Rubber transmission-belt defects are difficult to detect in practice because the captured images often exhibit:

- low contrast between defects and background,
- repetitive dark textures,
- weak boundaries,
- reflective interference,
- and large scale variation.

To address these challenges, CMT-YOLO introduces three main components:

- **C2f-CPMA**: enhances weak-defect representation by increasing receptive-field diversity while preserving an identity path;
- **MSFFB**: strengthens lightweight cross-scale feature fusion in the neck;
- **TADDH**: improves classification–localization coordination through task decomposition, deformable regression alignment, and spatial confidence modulation.

---

## Framework

<p align="center">
  <img src="assets/overall_framework.png" width="900"/>
</p>

**Figure 1.** Overall architecture of CMT-YOLO.

> Please place your framework figure in `assets/overall_framework.png`.

---

## Main Results

The proposed method achieves a favorable balance between detection accuracy and model efficiency on the transmission-belt defect dataset.

| Method | mAP@0.5 (%) | mAP@0.5:0.95 (%) | P (%) | R (%) | Params (M) | GFLOPs | Size (MB) | FPS | Latency (ms) |
|--------|-------------:|-----------------:|------:|------:|-----------:|-------:|----------:|----:|-------------:|
| YOLOv5n | 67.3 | 25.2 | 77.2 | 61.6 | 1.76 | 4.1 | 3.7 | 86.7 | 11.5 |
| YOLOv7 | 67.5 | 19.3 | 59.6 | 58.8 | 36.5 | 103.2 | 141.9 | 41.5 | 24.1 |
| YOLOv8n | 69.3 | 27.3 | 75.7 | 62.6 | 3.0 | 8.1 | 6.0 | 52.6 | 19.0 |
| YOLOv10n | 65.7 | 27.2 | 61.7 | 65.4 | 2.3 | 6.5 | 5.5 | 46.3 | 21.6 |
| YOLOv11n | 68.6 | 26.6 | 79.4 | 62.8 | 2.6 | 6.3 | 5.2 | 76.4 | 13.1 |
| YOLOv12n | 68.2 | 27.0 | 73.4 | 63.6 | 2.5 | 5.8 | 5.2 | 61.9 | 16.2 |
| **CMT-YOLO** | **75.4** | **29.0** | **77.6** | **73.5** | **2.1** | **8.5** | **4.4** | **72.7** | **13.7** |


##1
## Main Results

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


## Main Results

CMT-YOLO achieves a favorable balance between detection accuracy and efficiency compared with both conventional detectors and recent lightweight baselines.

<p align="center">
  <img src="assets/main_comparison_table.png" width="1000"/>
</p>

**Figure 2.** Comparison of CMT-YOLO with representative detection baselines on the transmission-belt defect dataset.



> If you prefer, this table can also be replaced or supplemented by a figure image placed in `assets/main_results_table.png`.


## Repository Structure


