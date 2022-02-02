#watermark on image
import cv2
img = cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\13.jpeg")
watermark = cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\watermarker.png")
cv2.imshow('Org', img)

h = watermark.shape[0]
w = watermark.shape[1]
as_ratio = 0.2
dimensions = (int(w * as_ratio), int(h * as_ratio))
resized = cv2.resize(watermark, dimensions)

center_y = int(img.shape[0]/2) #image height/2
center_x = int(img.shape[1]/2)

top_y = center_y - int(resized.shape[0]/2) #image height/2 -
left_x = center_x - int(resized.shape[1]/2)
bottom_y = top_y + resized.shape[0]
right_x = left_x + resized.shape[1]

roi = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 0.2, resized, 0.9, 0)
img[top_y:bottom_y, left_x:right_x] = result

cv2.imshow("Resized Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()