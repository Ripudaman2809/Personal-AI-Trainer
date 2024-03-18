import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)

detector = pm.poseDetector()

while True:
    # success,img = cap.read()
    # img = cv2.resize(img,(960,720))
    img = cv2.imread('PoseVideos/img2.jpg')
    img = cv2.resize(img,(0,0),fx=0.1,fy=0.1)
    img = detector.findPose(img,False)
    lmList = detector.findPosition(img,False)
    
    if len(lmList)!=0:
        
        detector.findAngle(img,11,13,15)
        print('\n')
    cv2.imshow('Image',img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()