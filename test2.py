import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
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
        angle = math.degrees()

