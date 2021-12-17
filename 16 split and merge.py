#split and merge

import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
b,g,r=cv2.split(img) #split we will get 3 image of blue,green,red shades
cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)
merged_img=cv2.merge((b,g,r))
cv2.imshow("merged image",merged_img) #merging back all the 3 bgr
cv2.waitKey(0)
cv2.destroyAllWindows()
