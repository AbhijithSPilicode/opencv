#Flippimg - Mirror image
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\12.jpeg")
cv2.imshow("image",img)
hflipped=cv2.flip(img,1) #1 since horizontal flip
cv2.imshow("Horizontal Flip",hflipped)
vflipped=cv2.flip(img,0) #0 for vertical flip
cv2.imshow("vertical Flip",vflipped)
hvflipped=cv2.flip(img,-1) #-1 for vertical flip & horizontal at a same time
cv2.imshow("horizontally vertical Flip",hvflipped)
cv2.waitKey(0)
cv2.destroyAllWindows()