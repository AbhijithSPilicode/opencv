#write an image to a place
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\8 to convert.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:\\Users\\user\\Desktop\\asap\\opencv images\\8 to convert.jpg",gray_img)
cv2.imshow("output",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
