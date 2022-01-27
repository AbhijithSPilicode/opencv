#flat surface,small change
#change in intensity in all dirction will lead to an edge
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\31.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",gray)
import numpy as np
gray=np.float32(gray)
out=cv2.cornerHarris(gray,3,5,0.04) #img,blocksize,ksize,k - k for accuracy
#out=cv2.dilate(out,None)
cv2.imshow("Corner Harris",out)
img[out>0.01*out.max()]=[0,0,255]
cv2.imshow("Corner Harris",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
