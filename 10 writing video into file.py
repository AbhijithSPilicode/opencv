#writing video into a file
import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)  #0,capdshow for camera
fourcc=cv2.VideoWriter_fourcc('X','V','I','D') #default XVID for AVI
out=cv2.VideoWriter("C:\\Users\\user\\Desktop\\asap\\opencv images\\video write.avi",fourcc,20.0,(640,480))
while (cap.isOpened()): #while loop since image should came after image to make a video
    ret,img=cap.read() #ret for a boolean wheather it is reading image or not
    if ret==True:
     cv2.imshow("Output",img)
     out.write(img) #writing video to a file
     if cv2.waitKey(1) == ord('q'):  # when press q it will quit,ord will give the ASCII of q # you can also use & 0xFF=ord('q') if any error comes
         break
    else:
        break
cap.release() # it will release all frames inside
out.release()
cv2.destroyAllWindows()
