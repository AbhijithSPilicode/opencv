#Morphological Operations
#Erosion and dilation
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\18.jpeg",0)

kernel=np.ones((5,5),np.uint8) #5x5 is kernel size,try to use odd kernel size
erodeimg=cv2.erode(img,kernel,iterations=1)#iteration increases = boundary will decrease more,shrink more
dilatedimg=cv2.dilate(img,kernel,iterations=1) #iteration increase =boundary increas,more thicker
morphOpen=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #erosion followed by dilation
morphClose=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) #dilation followed by erosion
morphGradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) #difference between dilation and erosion
morphTopHat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel) #difference between input image and opening of input image
morphBlackHat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel) #difference between input image and closing of input image

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