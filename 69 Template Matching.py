#template matching
#searching and finding location of template image in a larger image
#one image in one face
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg")
template=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13_face.jpg")
w,h=template.shape[1],template.shape[0]
o_img=img.copy()
o_img=cv2.matchTemplate(o_img,template,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(o_img)  #we searched's image for messi's face
top_left=max_loc
bottom_right=(top_left[0]+w,top_left[1]+h)
cv2.rectangle(img,top_left,bottom_right,(255,0,0),2)
cv2.imshow("Gray image",o_img)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
