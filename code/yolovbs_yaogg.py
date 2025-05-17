from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\ultralytics-main\ultralytics\cfg\models\v8\yolov8s.yaml"

    data_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\yolo\yolo\mydata.yaml"

    pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\yolov8s.pt"
    # pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\runs\detect\train\weights\best.pt"
    model = YOLO(model_yaml, task='detect').load(pre_model)  # build from YAML and transfer weights

    model.cuda()

    # Train the model
    results = model.train(data=data_yaml, epochs=100, imgsz=640, batch=1, workers=1)