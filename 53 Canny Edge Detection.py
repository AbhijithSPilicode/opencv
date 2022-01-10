#CANNY EDGE DETECTION
#multistage algorithm have smoothing(gaussian),gradient(Sobel),Non-maximum suppression
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\20.jpg")
canny=cv2.Canny(img,100,200)
cv2.imshow("original",img)
cv2.imshow("Canny output",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
