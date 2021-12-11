#Adding two images
#width and height of both image should be same
import cv2
img1=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
img2=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\9.jpg")
img2=cv2.resize(img2,(288,512)) #making both into samesize
dst=cv2.add(img1,img2)   #adding two images
cv2.imshow("Combine two image",dst)
dst2=cv2.addWeighted(img1,0.5,img2,0.9,0) #to make both image to a fixed proportion #0.5,0.9 is proportiobinality,0 is scaling factor indicate no change
cv2.imshow("Combine",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()