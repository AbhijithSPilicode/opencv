#assignment
#Show current time on video
from datetime import datetime
import cv2

time=datetime.now()
timestring=time.strftime("%d-%m-%y %H:%M:%S")
print(timestring)

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0,capdshow for camera
while (cap.isOpened()):
    ret,img=cap.read() #ret for a boolean wheather it is reading image or not
    if ret==True:
     cv2.putText(img,timestring, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
     cv2.imshow("Output",img)
     if cv2.waitKey(1)==ord('q') :    #when press q it will quit,ord will give the ASCII of q # you can also use & 0xFF=ord('q') if any error comes
         break
    else:
        break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()


