#Smoothing images
#Removing noise, reducing the grains
#kernel is given by user like 3x3 or 5x5 or 7x7 some odd matrices near a pixel
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\19.png")

kernel=np.ones((5,5),np.float32)/25 #/25 because kernel is 5x5 so 5*5
dst=cv2.filter2D(img,-1,kernel) #-1 for 2D #homogenous filtering #edge is blured
blurImg=cv2.blur(img,(5,5)) #averaging bluring
g_blur=cv2.GaussianBlur(img,(5,5),0) #Gaussian Bluring
m_blur=cv2.medianBlur(img,5)
bi_blur=cv2.bilateralFilter(img,5,75,75) #d=kernel=5,sigmacolor and sigmavalue any value>75

titles=['image','filre2d','average bluring','Gaussian blur','median blur','bilateral blur']
images=[img,dst,blurImg,g_blur,m_blur,bi_blur]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()