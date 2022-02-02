#MeanShift tracking algorithm
#take roi,when moving object,window also moves,when intensity matches,take histogram and backpropogate
#histogram helps to find how much pixel is used in every place
import cv2
import numpy as np
count=0
cap= cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\33.mp4")
ret,frame=cap.read()
cv2.imshow("frame",frame)
x,y,width,height=(300,200,40,50)
track_window=(x,y,width,height)
roi=frame[y:y+height,x:x+width]
cv2.imshow("ROI",roi)
hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv_roi,np.array((0,60,30)),np.array((180,255,255)))
roi_hist=cv2.calcHist([hsv_roi],[0],mask,[180],[0,180]) #taking histogram
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit=(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,1) #setup rermination criteria #10 times it will work and incriment by one and stops at 10
while(cap.isOpened()):
    count+=1
    ret,frame=cap.read()
    if ret is False:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dst=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1) #backpropogation,if intensity is matched
    ret,track_window=cv2.meanShift(dst,track_window,term_crit) #track window will have new x,y,w,h
    x,y,w,h=track_window
    f_img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Final image",f_img)
    print(count) #no.of total frames
    if cv2.waitKey(30)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#there is one more camShift instead of meanShift
