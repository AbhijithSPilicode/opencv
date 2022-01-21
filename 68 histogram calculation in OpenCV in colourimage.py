#histogram calculation in OpenCV for colourimage
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg") #no grayscale,colouredimage itself
color=("b","g","r")
for i,col in enumerate(color):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.show()