#If 2 points clicked on screen,a line will be drawn between last 2 points.
import cv2
import numpy as np
co_points=[]
def lineEvent(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),4,(255,0,0),-1) #when click it create a point
        co_points.append((x,y))
        if len(co_points)>=2:
            cv2.line(img,co_points[-1],co_points[-2],(0,255,0),2) #it gets last 2 points
        cv2.imshow("image",img)

img=np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)
cv2.setMouseCallback("image",lineEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
