#BITWISE OPERATION
#create 2 windows ,one white inside black and second window white stacked after black horizontally

import cv2
import numpy as np
img1=np.zeros((250,500))
img1[0:200,150:350]=1
img2_t1=np.zeros((250,250))
img2_t2=np.ones((250,250))
img2=np.hstack((img2_t1,img2_t2))
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
bitAnd=cv2.bitwise_and(img1,img2)
cv2.imshow("Bitwise And",bitAnd)
bitOr=cv2.bitwise_or(img1,img2)
cv2.imshow("Bitwise Or",bitOr)
bitXor=cv2.bitwise_xor(img1,img2)
cv2.imshow("Bitwise xor",bitXor)
cv2.waitKey(0)
cv2.destroyAllWindows()
