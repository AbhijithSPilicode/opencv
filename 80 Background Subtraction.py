#Using MOG2
#eliminate the background from image
#extract moving foreground from static background
#by creating a mask of moving foreground
#it will find the things only moving
import cv2
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\25.avi")
fg=cv2.createBackgroundSubtractorMOG2() #detectShadows=False if no shadows also needed
while(cap.isOpened()):
    ret,frame=cap.read()
    if frame is None:
        break
    fgmask=fg.apply(frame)
    cv2.imshow("Mask",fgmask)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(30)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
