#Trackbars
#create black screen,create a switch,if switch=0 show black screen ,else show combination of b,g,r image
#help to adjust brightness,contrast while run time itself
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8) #black image
cv2.namedWindow("image") #window created
def printVal(x):   #to get value from trackbar
    print(x)
cv2.createTrackbar("B","image",0,255,printVal) #name,window,start value,end value to
cv2.createTrackbar("G","image",0,255,printVal)
cv2.createTrackbar("R","image",0,255,printVal)
switch='0-ON/1-OFF'
cv2.createTrackbar(switch,"image",0,1,printVal)
while(1):
    cv2.imshow('image',img)
    b=cv2.getTrackbarPos("B","image") #trackbar1
    g=cv2.getTrackbarPos("G","image") #trackbar2
    r=cv2.getTrackbarPos("R","image") #trackbar3
    s=cv2.getTrackbarPos(switch,"image")
    if s==0:    #if switch=0 only black window appear,if switch=1 it will show combination of image
        img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        img[:]=(b,g,r)  #to image curresponding to trackbars
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
