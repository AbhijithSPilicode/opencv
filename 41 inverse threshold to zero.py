#inverse threshold to zero
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\15.jpg")
ret,th=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) #source,thresh,maxval
cv2.imshow("Image",img)
cv2.imshow("truncate thresh",th)
cv2.waitKey(0)
cv2.destroyAllWindows()
#black shade same,white shade black.
