#CANNY EDGE DETECTION using trackbars
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\23.jpg")
def callback(x):
 pass
cv2.namedWindow('image')
cv2.createTrackbar('trackbar1','image',100,255,callback)
cv2.createTrackbar('trackbar2','image',1,255,callback)
tb1 = cv2.getTrackbarPos('trackbar1', 'image')
tb2 = cv2.getTrackbarPos('trackbar2', 'image')

canny=cv2.Canny(img,tb1,tb2)
cv2.imshow("original",img)
cv2.imshow("image",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.Canny