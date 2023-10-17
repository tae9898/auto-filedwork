import cv2
from deepface import DeepFace
import os
import pandas as pd
from cv2 import VideoCapture
from cv2 import waitKey
data = {
    "Age":[],
    "Gender":[]
}
'''
img = cv2.imread("/make/test/111.jpg")
result = DeepFace.analyze(img, actions=("gender","age"))
data["Gender"].append(result[0]["dominant_gender"])


#df = pd.DataFrame(data)

print(result[0]["dominant_gender"])
'''
# opencv python 코딩 기본 틀
# 카메라 영상을 받아올 객체 선언 및 설정(영상 소스, 해상도 설정)
videosource = "/make/test/final.mp4"
txt_path = videosource
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(videosource)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if capture.isOpened():
     while True:
          
        ret, frame = capture.read()
          
               
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.2, minNeighbors=20, minSize=(20,20))
        if ret:
            cnt = 0
            age = 0
            male = 0
            female = 0
            if len(faces) :             
               for  x, y, w, h in faces :
                    cnt+=1
                    result = DeepFace.analyze(frame, actions=("gender","age"))
                    age+=result[0]["age"]
                    if(result[0]["dominant_gender"]=='Man'):
                          male+=1
                    else:
                          female+=1
            with open(f'{txt_path}.txt', 'a') as f:
                            
                            f.write(('%g %g %g %g') % (int(cnt) , int(male), int(female) ,int(age) )+ '\n')
            cv2.waitKey(10)
        else:

            break





capture.release()                   
cv2.destroyAllWindows()           
  