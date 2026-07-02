A trained model using yolov10 that detects empty spaces and tubes in a centrifuge.

Forked yolov10 directory: https://github.com/THU-MIG/yolov10#
Pretrained yolov10n: https://github.com/THU-MIG/yolov10/releases

Model is located in /yoloV10/yolov10/bottles. The latest model is named 004-1_27-28_50-202407176
Pictures used to train the model are found in /yoloV10/yolov10/ultralytics/cfg/datasets/bottles with the corresponding boxes located in txt files in the corresponding labels folder.
Labels were made using CVAT found here: https://github.com/cvat-ai/cvat

Model was trained using lx-train.py (run python lx-train.py in conda env). You can change the number of epochs in the same file in 'epochs='

Labels can be changed in ultralytics/cfg/datasets/bottles.yaml
Note that you will need to change file paths if you would like to follow along.
