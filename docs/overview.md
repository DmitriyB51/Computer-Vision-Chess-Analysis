# Project Overview

## Purpose
This project implements a **computer vision–based chess analysis system** that recognizes the state of a physical chessboard from a live camera feed and suggests the best move using the Stockfish chess engine.

---

## High-Level Pipeline
1. Capture live video from a camera
2. Calibrate chessboard corners and generate square bounding boxes
3. Detect chess pieces using a YOLOv8 model
4. Map detections to board squares
5. Convert board state to FEN notation
6. Analyze position with Stockfish
7. Visualize results in a graphical user interface

---

## System Architecture

### Calibration Layer
- Manual selection of **9×9 chessboard corner points**
- Points are saved and reused across runs
- From the points, **64 square bounding boxes** (8×8) are generated

---

<p align="center">
  <img src="images/calibration.png" width="600">
</p>



### Vision Layer
- YOLOv8 model detects chess pieces in each frame
- Each detection provides class label and bounding box
- Detection center is mapped to a board square using calibrated boxes

---

### Board Representation
- Board state is stored as an **8×8 matrix**
- Empty cells are marked with `.`
- Detected pieces are placed using chess notation (`p`, `P`, `k`, etc.)
- Board is rotated to match correct chess orientation
- Final board state is converted to a **FEN string**

---

### Chess Engine Layer
- FEN position is passed to **Stockfish**
- Engine calculates the best move with a fixed time limit
- Best move is returned in UCI format (e.g. `e2e4`)

---

### Visualization Layer (GUI)
- Implemented using **Tkinter**
- Two live views:
  - Raw camera feed with highlighted best move
  - YOLO-detected frame with bounding boxes
- Best move is displayed and visually marked on the board

---

## Design Characteristics
- Real-time processing
- Single-camera setup
- Modular pipeline (vision → logic → engine → GUI)
- Calibration-based robustness
- Designed for experimentation and analysis

---

## Project Scope
The system is intended for **analysis and training purposes** and demonstrates the integration of computer vision, chess logic, and a classical chess engine in a real-time application.
