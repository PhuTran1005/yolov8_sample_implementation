# import necessary library
from ultralytics import YOLO


# Load a model, nanno version
model_v8 = YOLO("yolov8n.pt")

# Train the model
train_results = model_v8.train(
    data="dataset/vehicles_dataset.yaml",  # path to dataset YAML
    epochs=20,  # number of training epochs
    imgsz=640,  # training image size
    batch=16, # batch size
    device="7",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)