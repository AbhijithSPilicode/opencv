#Laplacian pyramid
#formed from gaussian pyramid
#Difference between current laplacian and laplacian of upper
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\9.jpg")
cv2.imshow("original",img)

#Gaussian pyramid layers
layer=img.copy()
gp=[layer]  #gaussian
for i in range(5):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow("Gp"+str(i),layer)

last_image=gp[5]
lp=[last_image]   #laplacian
for i in range(5,0,-1):  #increase the resolution
    gaussian_extended=cv2.pyrUp(gp[i])
    lap=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow("Laplacian"+str(i),lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
