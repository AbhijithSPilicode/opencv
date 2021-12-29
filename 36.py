#trackbar in hsv
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\14.jpeg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #hsv image
#only blue color will take from it using bitwise operation
def printVal(x):   #to get value from trackbar
    print(x)
l_b1=cv2.createTrackbar("l_b1","image",0,255,printVal) #name,window,start value,end value to
l_b2=cv2.createTrackbar(switch,"image",0,100,printVal)
l_b3=cv2.createTrackbar(switch,"image",0,100,printVal)
u_b1=cv2.createTrackbar("u_b1","image",0,255,printVal) #name,window,start value,end value to
u_b2=cv2.createTrackbar(switch,"image",0,255,printVal)
u_b3=cv2.createTrackbar(switch,"image",0,255,printVal)
l_b=np.array([l_b1,100,100]) #lowerbound of blue #finding using colorpicker from site AlloyUI #firstone/2,100,100
u_b=np.array([u_b1,255,255]) #upperbound of blue #100 and 255 will be same for all colours
mask=cv2.inRange(hsv,l_b,u_b) #mask of blue
#if hsv and mask bitwise and done,it will give mask only,which is blue
res=cv2.bitwise_and(img,img,mask=mask) #img as it is,2nd img is img+mask
cv2.imshow("image",img)
cv2.imshow("blue mask",mask)
cv2.imshow("Output",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
