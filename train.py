import warnings, os
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"   
warnings.filterwarnings('ignore')
from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('/home/ultralytics/cfg/models/v8/yolov8n.yaml') # loading pretrain weights
    model.train(data='v1/data.yaml',
                cache=False,
                imgsz=640,
                epochs=800,
                batch=32,
                close_mosaic=0,
                workers=8, # 
                optimizer='SGD', # using SGD
                device='0', #
                # patience=0, # set 0 to close earlystop.
                # resume=True, # 
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='new',
                )