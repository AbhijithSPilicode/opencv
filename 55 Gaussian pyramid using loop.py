#Gaussian pyramid using loop
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\9.jpg")
cv2.imshow("original",img)
layer=img.copy()
gp=[layer]
for i in range(5):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow("Gp"+str(i),layer)
cv2.waitKey(0)
cv2.destroyAllWindows()
