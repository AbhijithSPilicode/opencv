import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0,capdshow for camera
ar=[]
while (cap.isOpened()):
    ret,frame= cap.read()
    if ret==True:
     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
     l_b = np.array([96, 100, 100])  # lowerbound of blue #finding using colorpicker from site AlloyUI #firstone/2,100,100
     u_b = np.array([138, 255, 255])  # upperbound of blue #100 and 255 will be same for all colours
     mask = cv2.inRange(hsv,l_b,u_b)  # mask of blue
     res = cv2.bitwise_and(frame,frame, mask=mask)
     gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (5, 5), 0)
     canny = cv2.Canny(blur, 50, 100)
     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
     dilated = cv2.dilate(canny,kernel, iterations=3)
     contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
     for cnt in contours:
         x, y, w, h = cv2.boundingRect(cnt)
         ar.append((x + (w // 2), y + (h // 2)))
         for i in range(1, len(ar)):
             cv2.line(frame,ar[i - 1],ar[i], (255, 0, 0), 5)
             cv2.imshow('frame', frame)
             cv2.imshow("Image",mask)
             cv2.imshow("Blue colour detected",res)
     if cv2.waitKey(1)==ord('q') :    #when press q it will quit,ord will give the ASCII of q # you can also use & 0xFF=ord('q') if any error comes
         break
    else:
        break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()