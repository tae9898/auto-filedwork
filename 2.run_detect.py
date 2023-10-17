import os

os.system("python /make/yolov5/detect.py --source /make/test/final.mp4 --weights /make/yolov5/runs/train/human_results6/weights/best.pt --img 416 --conf 0.5 --save-txt")

#os.system("python detect.py --source /make/test/12.mp4 --weights /make/yolov5/runs/train/human_results6/weights/best.pt --img 416 --conf 0.4")

