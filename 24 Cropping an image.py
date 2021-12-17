#Cropping an image
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg")
cv2.imshow("original image",img)
crop=img[285:338,333:386] #coordinates of point to be cropped
img[285:338,108:161]=crop
cv2.imshow("added img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

