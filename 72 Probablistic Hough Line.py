#Probablistic Hough Line
#HoughLineP
#it doesn't take all point for consideration,it takes only a random subset of points which is sufficient for detection
#important in self driving cars
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\16.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,50,150)
cv2.imshow("canny",canny)
lines=cv2.HoughLinesP(canny,1,np.pi/180,80,None,100,maxLineGap=60) #image,row value,theta in radians,thrshold,lines,minimumlinelength,maximumlinegap
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
