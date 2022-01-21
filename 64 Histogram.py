#Histogram
#bins
#to portray the intensity
#Draw a dark image and find intensity
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=np.zeros((200,200),np.uint8)
cv2.imshow("Orig",img)
plt.hist(img.ravel(),256,[0,256]) #ravel is image to 1D array,256 colours
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

