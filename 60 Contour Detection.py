#Contour Detection
#It will helpful to understand which shape it is
#A curve joining all continuous points along the boundary
#Application:Motion Detection,object detection
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\19.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imggray,100,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("no of contours",len(contours))
cv2.drawContours(img,contours,-1,(0,255,0),3) #-1 for all contours
cv2.drawContours(img,contours[3],0,(255,0,0),3) #this is for a particular contour,you can see it in the green as a blue dot,it may be a point or it may be a curve
cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
