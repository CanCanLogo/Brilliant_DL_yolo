# from ultralytics import YOLO
#
# # 读取模型，这里传入训练好的模型
# model = YOLO(r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\yolov8n.pt").cuda()
#
# # 模型预测，save=True 的时候表示直接保存yolov8的预测结果
# metrics = model.predict([r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\test\images\1.jpg", r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\test\images\2.jpg"], save=True)
# # 如果想自定义的处理预测结果可以这么操作，遍历每个预测结果分别的去处理
# for m in metrics:
#     # 获取每个boxes的结果
#     box = m.boxes
#     # 获取box的位置，
#     xywh = box.xywh
#     # 获取预测的类别
#     cls = box.cls
#
#     print(box, xywh, cls)

from ultralytics import YOLO
import json
import os
from collections import Counter

import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def calculate_metrics(ground_truth, predictions):
    # 创建一个字典，将图像名映射到其实际标签
    gt_map = {item['image']: set(item['labels']) for item in ground_truth}
    # 创建一个字典，将图像名映射到其预测标签
    pred_map = {item['image']: set(item['labels']) for item in predictions}

    all_labels = set().union(*gt_map.values())

    # print(len(all_labels)) # 34

    # 初始化 true positives, false positives, 和 false negatives
    # tp = Counter()
    # fp = Counter()
    # fn = Counter(all_labels)
    true = []
    pred = []

    # 遍历每个图像的实际标签
    for image, gt_labels in gt_map.items():
        pred_labels = pred_map.get(image, set())
        print(pred_labels, gt_labels)

        total_set = gt_labels | pred_labels
        print(total_set)

        gt_list = [1 if item in gt_labels else 0 for item in total_set]
        pr_list = [1 if item in pred_labels else 0 for item in total_set]

        print(gt_list, pr_list)
        true.extend(gt_list)
        pred.extend(pr_list)
        # # 更新 true positives 和 false positives
        # tp += Counter(gt_labels & pred_labels)
        # fp += Counter(pred_labels - gt_labels)
        # print(Counter(gt_labels & pred_labels), Counter(pred_labels - gt_labels))

        # 更新 false negatives
        # for label in gt_labels:
        #     if label not in pred_labels:
        #         fn[label] -= 1
        # for label in pred_labels:
        #     if label in gt_labels:
        #         tp[label] += 1
        #     if label not in gt_labels:
        #         fp[label] += 1
        # for label in gt_labels:
        #     if label not in gt_labels:
        #         tn[label] += 1
        # fn = 0
    print(true)
    print(pred)
    accuracy = accuracy_score(true, pred)
    # 计算精度
    precision = precision_score(true, pred, average='binary')
    # 计算召回率
    recall = recall_score(true, pred, average='binary')
    # 计算F1分数
    f1 = f1_score(true, pred, average='binary')

        # precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        # recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        # f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return accuracy, precision, recall, f1

# class_dic = {}

if __name__ == "__main__":
    test_path = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\test\images"

    # # 50
    # pth_path = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\runs\detect\train6\weights\best.pt"
    # # Load a model
    # # model = YOLO('yolov8n.pt')  # load an official model
    # model = YOLO(pth_path)  # load a custom model
    # # Predict with the model
    # results = model(test_path, save=True, conf=0.5, save_txt = True)  # predict on an image
    # # predict4


    # 50
    pth_path = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\Exp4\runs\detect\train2\weights\best.pt"
    model = YOLO(pth_path)  # load a custom model

    names = model.module.names if hasattr(model, 'module') else model.names  # 获取标签
    print(names)
    # Predict with the model
    results = model(test_path, save=True, conf=0.4, save_txt=True)  # predict on an image
    # predict

    test_result = []
    for result in results:
        single_data = {}
        # 提取图像路径
        img_path = result.path
        # img_path = img_path.strip("\\")[-1]
        filename = os.path.basename(img_path)
        single_data['image'] = filename
        # 提取检测到的物体
        objects = []
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls.item())
            if names[class_id] not in objects:
                objects.append(names[class_id])
        single_data['labels'] = objects
        test_result.append(single_data)
        print(single_data)
    # json.dumps(test_path, "test_result_140.json", ensure_ascii=False, indent=4) # 错了，这个是转字符串
    # json.dump(test_path, "test_result_140.json", ensure_ascii=False, indent=4)

    # with open("test_result_140.json", 'w', encoding='utf-8') as f:
    #     json.dump(test_result, f, ensure_ascii=False, indent=4)

    # 计算指标
    actual_data_path = r"D:\new_program\pythonProject\pytorchUse\DeepLearning\data_exp4\test\label.json"
    predictions_path = "test_result_140.json"

    with open(actual_data_path, 'r', encoding='utf-8') as file:
        actual_data = json.load(file)
    with open(predictions_path, 'r', encoding='utf-8') as file:
        predictions = json.load(file)

    acc, precision, recall, f1_score = calculate_metrics(actual_data, predictions)
    print(f"Accuracy: {acc}")
    print(f"Precsion: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1_score}")
'''
Accuracy: 0.6304347826086957
Precsion: 0.9666666666666667
Recall: 0.6444444444444445
F1 Score: 0.7733333333333334
'''



