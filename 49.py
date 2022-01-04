#Morphological Operations with masking blue colour
#Erosion and dilation
import cv2
import numpy as np
from matplotlib import pyplot as plt
bgr=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\14.jpeg")
img=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
l_b=np.array([96,100,100])
u_b=np.array([138,255,255])
mask=cv2.inRange(hsv,l_b,u_b)
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("image",bgr)
cv2.imshow("bluemask",res)

kernel=np.ones((5,5),np.uint8) #5x5 is kernel size,try to use odd kernel size
erodeimg=cv2.erode(res,kernel,iterations=3)#iteration increases = boundary will decrease more,shrink more
dilatedimg=cv2.dilate(res,kernel,iterations=3) #iteration increase =boundary increas,more thicker
morphOpen=cv2.morphologyEx(res,cv2.MORPH_OPEN,kernel) #erosion followed by dilation
morphClose=cv2.morphologyEx(res,cv2.MORPH_CLOSE,kernel) #dilation followed by erosion
morphGradient=cv2.morphologyEx(res,cv2.MORPH_GRADIENT,kernel) #difference between dilation and erosion
morphTopHat=cv2.morphologyEx(res,cv2.MORPH_TOPHAT,kernel) #difference between input image and opening of input image
morphBlackHat=cv2.morphologyEx(res,cv2.MORPH_BLACKHAT,kernel) #difference between input image and closing of input image

titles=['Original','Erosion','Dilate','Opening','closing','gradient','tophat','blackhat']
images=[img,erodeimg,dilatedimg,morphOpen,morphClose,morphGradient,morphTopHat,morphBlackHat]
for i in range(len(titles)):
    plt.subplot(2,4,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],"gray") #gray because to convert colour images, you have to convert from BGR to RGB since cv2 support BGR, matplotlib supports RGB
    plt.xticks()
    plt.yticks()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

