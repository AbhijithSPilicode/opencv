#thresh to zero
#compare with 127,if less than 127 apply 0,remaining no change
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\15.jpg")
ret,th=cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #source,thresh,maxval
cv2.imshow("Image",img)
cv2.imshow("truncate thresh",th)
cv2.waitKey(0)
cv2.destroyAllWindows()
#black gradient become black till 127 that is half,white gradient no change which is greater than 127.
