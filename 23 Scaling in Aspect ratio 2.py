#Scaling in Aspect ratio method 2
#in upscaling and downscaling,the image is seemed to be stretched too much , to avoid this we are using aspect ratio
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\12.jpeg")
print(img.shape)
h=img.shape[0]
w=img.shape[1]
asp_ratio=1.2
print(asp_ratio)
dimensions=(int(w*asp_ratio),int(h*asp_ratio))
print(dimensions)
resized=cv2.resize(img,dimensions)
cv2.imshow("output",img)
cv2.imshow("resized",resized)
print(resized.shape)
cv2.waitKey(0)
cv2.destroyAllWindows

