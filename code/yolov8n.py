# from ultralytics import YOLO
#
# # Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
#
# # Use the model
# model.train(data="coco8.yaml", epochs=3)  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format

# from ultralytics import YOLO
#
# model = YOLO("yolov8n.pt") # pass any model type
# model.train(epochs=5)
#
# results = model.train(data=r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\yolo\yolo", epochs=100, imgsz=640)


import torch
from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    model_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\ultralytics-main\ultralytics\cfg\models\v8\yolov8n.yaml"

    data_yaml = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\yolo\yolo\mydata.yaml"

    # pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\yolov8n.pt"
    pre_model = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\runs\detect\train\weights\best.pt"
    model = YOLO(model_yaml, task='detect').load(pre_model)  # build from YAML and transfer weights
    model.cuda()
    # Train the model
    results = model.train(data=data_yaml, epochs=50, imgsz=640, batch=2, workers=1)

    # save_path = "best.pt"
    #
    # torch.save(model.state_dict(), save_path)




