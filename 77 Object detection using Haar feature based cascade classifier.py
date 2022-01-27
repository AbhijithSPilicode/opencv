#face detection from an image
#eye detection in that face
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\23.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\asap\\opencv\\haarcascade_frontalface_default.xml") #importing the file having face features
eye_cascade=cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\asap\\opencv\\haarcascade_eye_tree_eyeglasses.xml") #eye in face detection #these 2 are a ML dataset already trained with around 6000 datas
faces=face_cascade.detectMultiScale(gray,1.1,4) #taking 1 pixel and search around 4 neighbours of it #face recognition
for (x,y,w,h) in faces:                 #1.1 is scaling factor
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #for face
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray) #for eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

