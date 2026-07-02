from ultralytics import YOLOv10

model = YOLOv10(model='/home/speechless/Desktop/HintonAI/yoloV10/yolov10/bottles/004-1_27-28_50-202407174/weights/best.pt')

model.train(data='bottles.yaml', epochs=60, batch=8, nbs=64, imgsz=1216, optimizer='SGD', amp=False, box=15, cls=0.5, dfl=0.0, device='cpu', save_period=1, val_period=1, project='bottles', name='yolov10trained_model_', flipud=0.3, fliplr=0.3, mosaic=0.1)
