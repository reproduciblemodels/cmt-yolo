import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('runs/train/yolov8n/weights/best.pt') # select your model.pt path
    model.predict(source='v1/test/images',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                  # conf=0.2,
                  # iou=0.7,
                  # agnostic_nms=True,
                  # visualize=True, # visualize model features maps
                  line_width=6, # line width of the bounding boxes线框粗细
                  # show_conf=False, # do not show prediction confidence置信度
                  # show_labels=False, # do not show prediction labels标签
                  # save_txt=True, # save results as .txt file
                  # save_crop=True, # save cropped images with results
                )