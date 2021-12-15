#downscaling and upscaling
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
cv2.imshow("image",img)
#downscaling
d_w=150
d_h=300
d_d=(d_w,d_h)
downscale=cv2.resize(img,d_d,interpolation=cv2.INTER_AREA)
cv2.imshow("Downscaled Image",downscale)
#upscale
u_w=750
u_h=700
u_d=(u_w,u_h)
upscale=cv2.resize(img,u_d,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Upscaled Image",upscale)
cv2.waitKey()
cv2.destroyAllWindows()
