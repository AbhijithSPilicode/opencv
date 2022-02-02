# Motion Tracking of a ball
import cv2
import numpy as np
c=[(0,0)]
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\video_ball.mp4")
ret,frame1=cap.read()
ret,frame2=cap.read()
img=np.zeros_like(frame1,np.uint8)
cv2.imshow("Image", img)
while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,100)
    dilated=cv2.dilate(canny,(3,3),iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        x,y,w,h=cv2.boundingRect(cnt)
        area=cv2.contourArea(cnt)
        if area<600:
            continue
        center=((2*x+w)//2,(2*y+h)//2)
        if c[-1]!= center:
            c.append(center)
        if len(c)>=2:
            cv2.line(frame1,c[-1],c[-2],(0,255,0),2)
            cv2.line(img, c[-1], c[-2], (0, 255, 0), 2)
        cv2.imshow("Image", img)
        cv2.imshow("Frame", frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(30)==ord('q'):
        break

print("Center :",c)
cap.release()
cv2.destroyAllWindows()