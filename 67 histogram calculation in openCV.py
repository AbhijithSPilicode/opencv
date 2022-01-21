#histogram calculation in OpenCV in grayimage
#cv2.calcHist(images,channels,mask,histsize,ranges[,hist[,accumulate]])
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg",0) #0 for grayscale
hist=cv2.calcHist([img],[0],mask=None,histSize=[256],ranges=[0,256]) #hitsize=binsize=256 #[img] in bracket since converting to 1D array
plt.plot(hist)
plt.show()