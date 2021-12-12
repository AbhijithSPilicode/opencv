#to get height,width,dimension of an image
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
print(f"shape is {img.shape}")
h=img.shape[0]
w=img.shape[1]
dimen=(h,w)
print(f"h={h} w={w} dimension={dimen}")
print(f"size is {img.size}")
print(f"dtype is {img.dtype}")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
