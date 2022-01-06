#image gradient using 64F
import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\20.jpg")
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3) #64F will also there ,but there will be some lose of infromation
lap=np.uint8(abs(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0) #8U uses less memory than 64F,64F is signed and 8U is unsigned
sobelx=np.uint8(abs(sobelx))  #since 64F contains signed or positive values,abs help to use negative values also
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
sobely=np.uint8(abs(sobely))
sobelxy=cv2.bitwise_or(sobelx,sobely)

scharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
scharrx=np.uint8(abs(scharrx))
scharry=cv2.Scharr(img,cv2.CV_64F,0,1)
scharry=np.uint8(abs(scharry))
scharrxy=cv2.bitwise_or(scharrx,scharry)

titles=["orig","Laplacian","Sobelx","sobely","soblexy","scharrx","scharry","scharrxy"]
images=[img,lap,sobelx,sobely,sobelxy,scharrx,scharry,scharrxy]
for i in range(len(titles)):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()