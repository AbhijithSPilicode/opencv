#Hough transform is used to detect any shape if you can represent that shape in a mathematical form
#equation of line y=mx+c,p=xcos(Q)+ysin(Q)
#to detect a line in an image
#Line in an image is a dot in hough space
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\16.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,50,50)
lines=cv2.HoughLines(edge,1,np.pi/180,200)   #here angle=pi/180=1 degree
for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=rho*a
    y0=rho*b
    x1=int(x0+1000*(-b)) #2 points one in positive and one in negative direction
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#this houghlines is now started to use with houghlinesP

