#truncate thresholding
#apply maxvalue if greater than thrash,else pixel value itself
#here 0-127 no change,127-255 it will give 255
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\15.jpg")
ret,th=cv2.threshold(img,127,255,cv2.THRESH_TRUNC) #source,thresh,maxval
cv2.imshow("Image",img)
cv2.imshow("truncate thresh",th)
cv2.waitKey(0)
cv2.destroyAllWindows()