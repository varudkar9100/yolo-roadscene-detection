# 🚦 YOLO Roadscene Detection

This repository implements YOLOv8 for detecting objects in road scenes, including road, vehicles, pedestrians, signs, buildings, and sky.

## 📂 Structure
- training.ipynb – Training pipeline (Colab)
- infer.py – CLI inference
- gradio_app.py – Web demo with Gradio
- data.yaml – Dataset config
- requirements.txt – Dependencies
- docs/ – Project report (Word & PDF)
- results/ – Training plots (placeholders)
- sample_predictions/ – Example outputs (placeholders)
- models/ – Placeholder for trained weights

## 🚀 Usage
```bash
pip install -r requirements.txt
python infer.py --weights models/best.pt --source sample_predictions/sample1.jpg
python gradio_app.py
```
