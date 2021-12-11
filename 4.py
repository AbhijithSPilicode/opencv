#picture into blue,green,red
import cv2
import numpy as np

img1=np.zeros((300,300,3))
img1[:]=(255,0,0)
cv2.imshow("blue",img1)

img2=np.zeros((300,300,3))
img2[:]=(0,255,0)
cv2.imshow("green",img2)

img3=np.zeros((300,300,3))
img3[:]=(0,0,255)
cv2.imshow("red",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()