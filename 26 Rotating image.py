#Rotating image
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\12.jpeg")
h=img.shape[0]
w=img.shape[1]
center=(w/2,h/2)
rot_matrix=cv2.getRotationMatrix2D(center,90,0.5) #90 degree rotation,0.5 for scaling factor that is half of size of original image
#angle is positive(eg:+90) anticlockwise,angle is negative(eg:-90) clockwise rotation
rot_img=cv2.warpAffine(img,rot_matrix,(w,h))
cv2.imshow("Anticlockwise Rotated image",rot_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
