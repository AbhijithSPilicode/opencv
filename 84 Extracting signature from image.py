import numpy as np
import cv2

img = cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\32.jpg")

h=img.shape[0]
w=img.shape[1]
asp_ratio=1500/w
dimensions=(int(w*asp_ratio),int(h*asp_ratio))
resized=cv2.resize(img,dimensions)

image = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
lower = np.array([90, 38, 0])
upper = np.array([145, 255, 255])
mask = cv2.inRange(image, lower, upper)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1) #erosion follwed by dilation
close = cv2.morphologyEx(open, cv2.MORPH_CLOSE, kernel, iterations=1) #dilation followed by erosion
contours,heirarchy = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

boxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    boxes.append([x,y, x+w,y+h])

boxes = np.asarray(boxes) #converting input to array
left = np.min(boxes[:,0])
top = np.min(boxes[:,1])
right = np.max(boxes[:,2])
bottom = np.max(boxes[:,3])

image[close==0] = (255,255,255)
ROI =image[top:bottom, left:right].copy()
cv2.rectangle(image, (left,top), (right,bottom), (36, 255, 12), 2)
cv2.imshow("image",resized)
cv2.imshow('result',image)
cv2.imshow('close', close)
cv2.waitKey(0)
cv2.destroyAllWindows()
