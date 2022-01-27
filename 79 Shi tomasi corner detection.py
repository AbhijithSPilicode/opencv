#shi tomasi is almost same as harris corner
#bad quality things are removed and good quality things will be focused more
#cv2.goodFeaturesToTrack(gray img,maxc,Q,minD)
#maxc is maximum number of corners we want
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\31.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original",gray)
out=cv2.goodFeaturesToTrack(gray,50,0.02,10) #50 is maximumcorner,if give -1 it will detect all corners
import numpy as np
out=np.int0(out) #int64
for i in out:
    x,y=i.ravel()
    cv2.circle(img,(x,y),4,(0,0,255),-1)
cv2.imshow("Shi tomasi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
