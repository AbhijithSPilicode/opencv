#Adaptive Thresholding
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\16.png",0)
th1=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
cv2.imshow("Image",img)
cv2.imshow("adaptive thresh mean",th1)
cv2.imshow("adaptive thresh gaussian",th2)
cv2.waitKey(0)
cv2.destroyAllWindows()