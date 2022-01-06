#Image Gradients using 8U
#sudden change in the intensity or colours in adjascent pixels
#derivative gives the speed of that change
#3 type of gradient filters- High pass filters -Sobel,Scharr and Laplacian
import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\20.png")
lap=cv2.Laplacian(img,cv2.CV_8U,ksize=3) #64F will also there ,but there will be some lose of infromation

sobelx=cv2.Sobel(img,cv2.CV_8U,1,0) #8U uses less memory than 64F,64F is signed and 8U is unsigned
sobely=cv2.Sobel(img,cv2.CV_8U,0,1)
sobelxy=cv2.bitwise_or(sobelx,sobely)

scharrx=cv2.Scharr(img,cv2.CV_8U,1,0)
scharry=cv2.Scharr(img,cv2.CV_8U,0,1)
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


