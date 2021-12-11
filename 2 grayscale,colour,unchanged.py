#greyscale, color, unchanged
import cv2
un_img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg",-1)
cv2.imshow("Unchanged",un_img)
color_img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg",1)
cv2.imshow("color",color_img)
gray_img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg",0)
cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
