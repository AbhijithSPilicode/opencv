#when click on image,get what is red,blue,green value
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
cv2.imshow("image",img)
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_RBUTTONDOWN:
        b,g,r=cv2.split(img)
        img1[:]=img(b,g,r)
        cv2.imshow("image1",img1)
cv2.setMouseCallback("image",click_event)
img1=np.zeros((512,512,3),np.uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()