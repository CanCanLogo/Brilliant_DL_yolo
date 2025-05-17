from collections import Counter
import json
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# def calculate_metrics(ground_truth, predictions):
#     all_labels = set()
#     for item in ground_truth:
#         all_labels.update(item['labels'])
#
#     # 初始化 true positives, false positives, 和 false negatives
#     tp = Counter()
#     fp = Counter()
#     fn = Counter(all_labels)
#
#     for gt_item, pred_item in zip(ground_truth, predictions):
#         gt_labels = set(gt_item['labels'])
#         pred_labels = set(pred_item['labels'])
#         print(gt_item['image'], pred_item['image'])
#         print(gt_labels, pred_labels)
#
#         # 更新 true positives 和 false positives
#         tp += Counter(gt_labels & pred_labels)
#         fp += Counter(pred_labels - gt_labels)
#
#         # 更新 false negatives
#         for label in gt_labels:
#             if label not in pred_labels:
#                 fn[label] -= 1
#
#     # 转换为常规字典以便后续计算
#     tp_dict = dict(tp)
#     fp_dict = dict(fp)
#     fn_dict = dict(fn)
#
#     # 计算精度、召回率和 F1 分数
#     precision = sum(tp_dict.values()) / max(sum(tp_dict.values()) + sum(fp_dict.values()), 1)
#     recall = sum(tp_dict.values()) / max(sum(tp_dict.values()) + sum(fn_dict.values()), 1)
#     f1_score = 2 * (precision * recall) / max(precision + recall, 1e-9)
#
#     return precision, recall, f1_score

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

    # 转换为常规字典以便后续计算
    # tp_dict = dict(tp)
    # fp_dict = dict(fp)
    # fn_dict = dict(fn)

    # 计算精度、召回率和 F1 分数
    # precision = sum(tp_dict.values()) / max(sum(tp_dict.values()) + sum(fp_dict.values()), 1)
    # recall = sum(tp_dict.values()) / max(sum(tp_dict.values()) + sum(fn_dict.values()), 1)
    # f1_score = 2 * (precision * recall) / max(precision + recall, 1e-9)

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