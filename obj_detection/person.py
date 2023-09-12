from ultralytics import YOLO
import cvzone
import cv2
import math

cap=cv2.VideoCapture(0)

model=YOLO(r"yolov8n.pt")
cap.set(3,1280)
cap.set(4,620)

className=["person","bicycle","car","motorbike","aeroplane","bus","train","truck","boat","traffic light","fire hydrant","stop sign","parking meter","bench,bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]

while True:
    success,img=cap.read()
    
    results=model(img, stream=True) #uses generators which are more efficient

    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2=box.xyxy[0] #getting the xy xy value of the chosen box
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            
            conf=(math.ceil(box.conf[0]*100))/100
            conf=round(conf,2)
            cls=int(box.cls[0])
            if className[cls]=="person" and conf > 0.3:
                cvzone.putTextRect(img,f'{conf},{className[cls]}',(max(0,x1),max(35,y1)))
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)




    cv2.imshow("image",img)
    cv2.waitKey(1)