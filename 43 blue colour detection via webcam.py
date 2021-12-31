#colour detection via webcam
#read video with present time,put time inside rectangle and change video to hsv (here blue object detect)
from datetime import datetime
import cv2
import numpy as np

time=datetime.now()
timestring=time.strftime("%d-%m-%y %H:%M:%S")
print(timestring)

def printVal(x):
    print(x)


cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0,capdshow for camera
while (cap.isOpened()):
    ret,img=cap.read() #ret for a boolean wheather it is reading image or not

    if ret==True:
     cv2.rectangle(img, (45,20), (400,60), (255, 0, 0), 3)
     cv2.putText(img,timestring, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
     hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
     l_b = np.array([96, 100, 100])  # lowerbound of blue #finding using colorpicker from site AlloyUI #firstone/2,100,100
     u_b = np.array([138, 255, 255])  # upperbound of blue #100 and 255 will be same for all colours
     mask = cv2.inRange(hsv,l_b,u_b)  # mask of blue
     res = cv2.bitwise_and(img, img, mask=mask)
     cv2.imshow("Image",mask)
     cv2.imshow("Output",img)
     cv2.imshow("Blue colour detected",res)
     if cv2.waitKey(1)==ord('q') :    #when press q it will quit,ord will give the ASCII of q # you can also use & 0xFF=ord('q') if any error comes
         break
    else:
        break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()
