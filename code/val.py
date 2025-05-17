import torch
from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\ultralytics-main\ultralytics\cfg\models\v8\yolov8n.yaml"

    data_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\test\test.yaml"

    # pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\yolov8n.pt"
    pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\runs\detect\train2\weights\best.pt"

    model = YOLO(model_yaml, task='detect').load(pre_model)  # build from YAML and transfer weights

    model.cuda()

    metrics = model.val(data=data_yaml, batch=1, workers=1)

    # 【目标检测】YOLOV8实战入门（四）模型验证