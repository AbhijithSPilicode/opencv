#Hue
#In RGB no control over brighness or intensity,contrast,etc.. it only work on light
#saturation says depth of colour
#value is the intensity
#HSV colorspace- Hue,Saturation,Value
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\14.jpeg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #hsv image
#only blue color will take from it using bitwise operation
l_b=np.array([96,100,100]) #lowerbound of blue #finding using colorpicker from site AlloyUI #firstone/2,100,100
u_b=np.array([138,255,255]) #upperbound of blue #100 and 255 will be same for all colours
mask=cv2.inRange(hsv,l_b,u_b) #mask of blue
#if hsv and mask bitwise and done,it will give mask only,which is blue
res=cv2.bitwise_and(img,img,mask=mask) #img as it is,2nd img is img+mask
cv2.imshow("image",img)
cv2.imshow("blue mask",mask)
cv2.imshow("Output",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

