import cv2
import poseModule as pm
import numpy as np

cap = cv2.VideoCapture('/home/user/Desktop/Complete_fitness_tracker/Squart counter/squat.mp4')

detector = pm.poseDetector()

count = 0
dir = 0

while True:
#1.image preprocessing
    success ,image = cap.read()
    image = cv2.resize(image,(1280,720))

#2.find body  

    image = detector.findPose(image ,draw=False)
    # print(image)
    lmlist = detector.findPosition(image ,draw= False)
    # print(lmlist)

#3. find angles of specific landmark
    if len(lmlist)!=0:

        # angle=detector.findAngle(image,23,25,27)
        # print(angle)
        angle = detector.findAngle(image,24,26,28)
        # print(angle)

#4.counting 

    per = np.interp(angle,(45,170),(0,100))
    # print(per)

    # print(angle ,'---->', per)
    if per == 100:
        if dir == 0:
            count += 0.5
            dir = 1

    if per == 0:
        if dir == 1:
            count += 0.5
            dir = 0

    print(count)

    cv2.rectangle(image,(0,0),(150,150),(0,255,0),cv2.FILLED)
    cv2.putText(image,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),5)

    bar = np.interp(angle,(45,170),(700,100))

    print(bar)
    
    cv2.rectangle(image,(1100,100),(1200,700),(0,255,0),3)


    cv2.rectangle(image,(1100,int(bar)),(1200,700),(0,255,0),cv2.FILLED)

    cv2.putText(image,str(int(per)),(1078,75),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)


    cv2.imshow('squat counter', image)
    if cv2.waitKey(1) & 0xFF ==27:
        break
