#BITWISE OPERATION
#create 2 windows ,one white inside black and second window white stacked after black horizontally
import cv2
import numpy as np
img1=np.zeros((250,500,3))
cv2.rectangle(img1,(150,0),(350,150),(255,255,255),-1)
cv2.imshow("img1",img1)

img2=np.zeros((250,250,3)) #blackwindow
img3=np.ones((250,250,3))  #white window
img4=np.hstack((img2,img3)) #stacking vertically blackwindow after whitewindow
cv2.imshow("img4",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
