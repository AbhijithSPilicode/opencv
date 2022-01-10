#Image Pyramids
#2 type:Gaussian pyramid and laplacian pyraimd
#Gaussian Pyramid
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\9.jpg")
cv2.imshow("original",img)
gp_img1=cv2.pyrDown(img)
gp_img2=cv2.pyrDown(gp_img1) #it will reduce 1/4th of img
gp_img3=cv2.pyrDown(gp_img2)
gp_img4=cv2.pyrUp(img)
cv2.imshow("pyrDown1",gp_img1) #decrease the resolution of img
cv2.imshow("pyrDown2",gp_img2)
cv2.imshow("pyrDown3",gp_img3)
cv2.imshow("pyUp1",gp_img4) #increase the resolution of img
cv2.waitKey(0)
cv2.destroyAllWindows()