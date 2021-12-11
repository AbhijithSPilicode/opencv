#assignment
#converting video into grayscale
import cv2
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\vid2.mp4")
cap.set(3,1000)
cap.set(4,1000)
while True:
    ret,img=cap.read()#ret for a boolean
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Output",gray_img)
    if cv2.waitKey(25)==ord('q')  :
         break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()