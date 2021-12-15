#AffineTansform
#Image seeing on sideview will be implimented to top view.
import cv2
import numpy as np
img1=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
width,height=288,512
pts1=np.float32([[0,0],[width,0],[width,height]]) #pts1 is point1 is source coordination
pts2=np.float32([[10,100],[width,0],[width,height]]) #point2 is destination image
matrix=cv2.getAffineTransform(pts1,pts2) #now it is changed to rotation matrix
warp_img=cv2.warpAffine(img1,matrix,(width,height))
cv2.imshow("image",img1)
cv2.imshow("Warp image",warp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

