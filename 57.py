#Image Blending Using Pyramids
import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\21.jpg")
img2=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\22.jpg")
hstackimg=np.hstack((img1[:,0:img1.shape[1]//2],img2[:,img2.shape[1]//2:])) #half of first image and half of second image
cv2.imshow("Stacked",hstackimg)
cv2.waitKey(0)
cv2.destroyAllWindows()