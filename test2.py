from pyexpat.errors import codes
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np
# from math import atan
import math

cap = cv.VideoCapture(0)

detector = HandDetector(detectionCon=0.8,minTrackCon=0.8)

while True:
    ret,frame = cap.read()
    hands,img  = detector.findHands(frame)
    if hands:
        left = hands[0]
        lmlist = left['lmList']
        bbox = left['bbox']
        fingers = detector.fingersUp(left)
        # angle = math.degrees()
        # tip
        x,y,w,h = bbox
        mask = img[x:x+w,y:y+h]
        size = mask.shape
        white = np.ones(size)
        # cut = cv.bitwise_or()
        new_img = cv.bitwise_and(img,img,mask=mask)
    cv.imshow('img',new_img)
    # if cv.waitKey(5) or 0xFF ==27:
    #     break
    key = cv.waitKey(5)
    if key == 27:
        break
cap.release()
cv.destroyAllWindows()Test codes
