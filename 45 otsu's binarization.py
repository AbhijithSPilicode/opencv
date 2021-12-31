#Otsu's Binarization
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\16.png",0)
ret1,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur=cv2.GaussianBlur(img,(5,5),0)
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Orig',img)
cv2.imshow('Binary thresh',th1)
cv2.imshow('OTSU',th2)
cv2.imshow('Blur+OTSU',th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
