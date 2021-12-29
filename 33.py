#read an image,create switch trackbar,if 1 set,display image,0 print gray scale of image
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
cv2.imshow("image",img)
def printVal(x):   #to get value from trackbar
    print(x)
switch='0-ON/1-OFF'
cv2.createTrackbar(switch,"image",0,1,printVal)
while(1):
    cv2.imshow("image",img)
    s=cv2.getTrackbarPos(switch,"image")
    if s==0:    #if switch=0 same image
        cv2.imshow("image",img)
    else:
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #grayscale if switch=1
        cv2.imshow("image",img1)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()