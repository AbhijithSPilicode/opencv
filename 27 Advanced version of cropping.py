#ROI(Region of Interest)
#Advance version of cropping image
#no need to give the coordinates of points to be cropped
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg")
r=cv2.selectROI(img)
cropped=img[(r[1]):(r[1]+r[3]),(r[0]):(r[0]+r[2])]
#img[288:342,335:391]
print(r[0],r[1],r[2],r[3])
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
