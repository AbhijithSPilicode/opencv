#image thresholding
#it will seperate object from background
#it will help to get edges
#comparing each pixel with image with a predefinred threshold value

#inverse binary thresholding
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\15.jpg")
ret,th=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) #source,thresh,maxval
cv2.imshow("Image",img)
cv2.imshow("Inverse Binary thresh",th)
#each pixel will compared to 127,if pixel is less than 127,it will convert to maximum value which is 255
cv2.waitKey(0)
cv2.destroyAllWindows()
#here 0-127(black shade)
#127-255(white shade)
#black gradient become white,white gradient become black
