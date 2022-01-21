#Circle: (x-a)^2+(y-b)^2=r^2
#Hough Gradient Method
#cv2.houghCircles(image,method,dp(resolution),mindist between centers,[,threshold of param1 of sobel derivative)
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\14.jpeg")
img=cv2.medianBlur(img,5)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,circles=None,param1=60,param2=30,minRadius=0,maxRadius=0)
circles=np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),3) #x,y,radius,colour,thickness
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),-1)
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


