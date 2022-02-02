import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\user\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\27.jpg")
cv2.imshow("image",img)
text = pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()