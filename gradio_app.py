import gradio as gr
from ultralytics import YOLO

model = YOLO("models/best.pt")

def predict(image):
    res = model.predict(image, conf=0.25)[0]
    return res.plot()

gr.Interface(fn=predict, inputs="image", outputs="image", title="YOLO Roadscene Detection").launch()
