#Lane detection in an image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_method(image):
    blur=cv2.GaussianBlur(image,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def region_of_interest(image):
    tri=np.array([[(200,700),(1100,700),(650,250)]]) #these points get from matplotlib where center of road comes
    mask=np.zeros_like(image)#zeros like will make a black image same as resolution of the original image
    cv2.fillPoly(mask,tri,255)
    cv2.imshow("mask",mask)
    masked_img=cv2.bitwise_and(image,mask)
    cv2.imshow("Masked img",masked_img)
    return masked_img

img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\29.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny=canny_method(gray)
plt.imshow(canny)
cropped_img=region_of_interest(canny)
lines=cv2.HoughLinesP(cropped_img,1,np.pi/180,200,minLineLength=40,maxLineGap=10)
for line in lines:
    (x1,y1,x2,y2)=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,255,0),12)
cv2.imshow("Lane Detection Output",img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


