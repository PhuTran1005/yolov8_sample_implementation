# import necessary library
from ultralytics import YOLO


# Load pretrained model, nanno version
model_v8 = YOLO("runs/detect/train/weights/best.pt")

results = model_v8.predict(
    source="dataset/test/images", 
    save=True, 
    conf=0.5
    )