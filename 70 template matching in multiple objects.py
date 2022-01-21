#in previous probelm of template matching search image for messi's face which occurs only once in image,
#here we are searching for object which has multiple occurances
import cv2
import numpy as np
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\28.jpg")
cv2.imshow("img",img)
template=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\28_cut.png")
w,h=template.shape[1],template.shape[0]
o_img=img.copy()
o_img=cv2.matchTemplate(o_img,template,cv2.TM_CCORR_NORMED)
threshold=0.8
loc=np.where(o_img>threshold) #where will give location
print(loc)
for pt in zip(*loc[::-1]):  #zip will return into a tuple
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)
cv2.imshow("Founded coin",img)
cv2.imshow("gray",o_img)
cv2.waitKey(0)
cv2.destroyAllWindows()