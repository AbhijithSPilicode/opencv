#subplot in matplot
#cv2 support BGR, matplotlib supports RGB
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\16.png")
ret1,th1=cv2.threshold(img,200,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
ret3,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
ret4,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
ret5,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)
titles=['image','binary','inverse binary','truncate','tozero','inverse to zero']
images=[img,th1,th2,th3,th4,th5]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) #to remove anything in x axis
    plt.yticks([]) #to remove anything in y axis
plt.show()
 #to convert colour images, you have to convert from BGR to RGB
