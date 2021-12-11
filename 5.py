#gray image
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("output",img)
cv2.imshow("Gray output",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows() #clear all memory