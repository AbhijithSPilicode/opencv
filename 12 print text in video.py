#printing a text in a video
import cv2
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\vid2.mp4")
cap.set(3,1000)
cap.set(4,1000)
while True:
    ret,img=cap.read()#ret for a boolean
    cv2.putText(img, "Hello", (300, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (120, 120, 30), 3)
    cv2.imshow("Output",img)
    if cv2.waitKey(25)==ord('q') :    #when press q it will quit,ord will give the ASCII of q
         break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()
