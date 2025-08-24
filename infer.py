from ultralytics import YOLO
import argparse

def run(weights, source):
    model = YOLO(weights)
    model.predict(source=source, save=True, conf=0.25)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--weights", required=True)
    p.add_argument("--source", required=True)
    args = p.parse_args()
    run(args.weights, args.source)
