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


## Main Results

CMT-YOLO achieves a favorable balance between detection accuracy and efficiency compared with both conventional detectors and recent lightweight baselines.

<p align="center">
  <img src="assets/main_comparison_table.png" width="1000"/>
</p>

**Figure 2.** Comparison of CMT-YOLO with representative detection baselines on the transmission-belt defect dataset.



> If you prefer, this table can also be replaced or supplemented by a figure image placed in `assets/main_results_table.png`.

---

## Repository Structure


