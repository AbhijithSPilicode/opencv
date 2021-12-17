#image Translation
#Move within one image from one position to other
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\12.jpeg")
width=img.shape[1]
height=img.shape[0]
#height,width=img.shape[:2]
tx=width/2 #the amount to be translated
ty=height/2 #translate to half of width and half of height of original image
translation_matrix=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) #whenever matrix comes we convert to float
t_img=cv2.warpAffine(img,translation_matrix,(width,height))
cv2.imshow("Translated image",t_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
