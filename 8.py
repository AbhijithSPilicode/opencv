# Reading and displaying videos
import cv2
cap=cv2.VideoCapture("C:\\Users\\user\\Desktop\\asap\\opencv images\\vid1.mp4")
cap.set(3,3840)
cap.set(4,2160)
print(f"dimension is {cap.get(3)},{cap.get(4)}")
while True:
    ret,img=cap.read() #ret for a boolean
    cv2.imshow("Output",img)
    if cv2.waitKey(25)==ord('q') :    #when press q it will quit,ord will give the ASCII of q
         break
cap.release()  #it will release all frames inside
cv2.destroyAllWindows()
#waitKey(1) is used to change frame after frame
#cv2.waitKey(  ) increases the video will become slower