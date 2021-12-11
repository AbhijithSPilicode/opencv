#Reading from laptop camera
#camera number we are using,by default it is 0
# Reading and displaying videos
import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)#0,capdshow for camera
w=cap.get(3) #enum value of width is 3
h=cap.get(4) #enum value of width is 4
dimen=(h,w)
print(f"dimension is {dimen}")
while (cap.isOpened()):
    ret,img=cap.read() #ret for a boolean wheather it is reading image or not
    if ret==True:
     cv2.imshow("Output",img)
     if cv2.waitKey(1)==ord('q') :    #when press q it will quit,ord will give the ASCII of q # you can also use & 0xFF=ord('q') if any error comes
         break
    else:
        break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()
#waitKey(1) is used to change frame after frame
#cv2.waitKey(  ) increases the video will become slower
#camera will be on in only one instance
print(cv2.__version__)  #this is just to see the version of my opencv