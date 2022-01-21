#read a colour image and find histogram
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\9.jpg")
b,g,r=cv2.split(img)
plt.hist(b.ravel(),256,[0,256]) #converting the image pixel to 1D array
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
