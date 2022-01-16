#MOTION DETECTION IN VIDEOS
import cv2
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\25.avi")
ret,img1=cap.read() #frame 1
ret,img2=cap.read() #frame 2
while cap.isOpened():
    diff=cv2.absdiff(img1,img2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),1)
    ret,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,(3,3))
    contours,hierarchy=cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h=cv2.boundingRect(cnt)
        if cv2.contourArea(cnt)<900:
            continue
        else:
            cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow("Output",img1)
    img1=img2 #frame2 become frame1
    ret,img2=cap.read() #frame3 become frame2 and repeat until last frame
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


