#PerspectiveTransformation
#convert topview to frontview
import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\10.png")
width,height=250,350

pts1=np.float32([[121,179],[194,216],[60,295],[137,330]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
warp_img=cv2.warpPerspective(img1,matrix,(width,height))
cv2.imshow("image",img1)
cv2.imshow("Warp image",warp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()