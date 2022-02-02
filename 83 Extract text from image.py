import pytesseract
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\user\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\27.jpg")
cv2.imshow("Original",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh= cv2.threshold(gray,100, 255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,20)) #to get rectangular kernel
dilation = cv2.dilate(thresh,kernel, iterations=1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt) #xcoordinate,ycoordinate,width,height
    rect = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cropped = img[y:y+h,x:x+w]
    text = pytesseract.image_to_string(cropped)
    print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()