import cv2
import poseModule as pm
import numpy as np

cap = cv2.VideoCapture('/home/user/Desktop/Complete_fitness_tracker/Push_up_counter/slow_motion_video.mp4')

detector = pm.poseDetector()

count = 0
flage = 0

while True:

#1.image preprocessing
    success ,image = cap.read()
    # image = cv2.resize(image,(1280,720))

#2.find body  

    image = detector.findPose(image ,draw=False)
    # print(image)
    lmlist = detector.findPosition(image ,draw=False)
    # print(lmlist)

#3. find angles of specific landmark
    if len(lmlist) != 0:

        # angle=detector.findAngle(image,23,25,27)
        # print(angle)
        distance = detector.findDistace(image,32,27)
        print(distance)

#4.counting

        percentage = np.interp(distance,(90,190),(0,100))
        print(percentage)

        if percentage ==100:
            if flage == 0:
                count = count+ 1
                flage = 1
        if percentage == 0:
            if flage ==1:
                count = count +1
                flage = 0
        print(count)
        # Count the counts of push ups
        cv2.rectangle(image,(0,0),(150,150),(131, 0, 42),cv2.FILLED)
        cv2.putText(image,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),5)

        # Percentage bar for drawing
        bar = np.interp(distance,(190,310),(700,100))
        
        canvas = np.zeros((900, 800,3), dtype=np.uint8)

        cv2.rectangle(image,(1100,100),(1200,700),(0,255,0),3)


        cv2.rectangle(image,(1100,int(bar)),(1200,700),(131, 0, 42),cv2.FILLED)

        cv2.putText(image,str(int(percentage)),(1078,75),cv2.FONT_HERSHEY_COMPLEX,2,(131, 0, 42),3)

        # Canvas operations


        cv2.rectangle(canvas,(0,0),(150,150),(131, 0, 42),cv2.FILLED)

        cv2.putText(canvas,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)

        # cv2.circle(canvas,(361,446),50,(0,255,0),2)
        # forbar = np.interp(distance,(100,200),(446,361))
        # cv2.circle(canvas,(500,446),int(forbar),(0,255,0),cv2.FILLED)


        # cv2.rectangle(canvas,(500,int(bar)),(900,700),(131, 0, 42),cv2.FILLED)




    cv2.imshow('squat counter', image)
    # cv2.imshow('Details',canvas)
    if cv2.waitKey(1) & 0xFF ==27:
        break
