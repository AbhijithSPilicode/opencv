import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\24.jpg")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imggray,(5,5),1)#source,kernel size
canny=cv2.Canny(imgBlur,50,100) #Canny
cv2.imshow("Canny",canny)
contours,heirarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #contour
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #cornerpoints
    n=len(approx) #no.of edges
    x,y,w,h=cv2.boundingRect(approx)
    if n==3:
        obj="Triangle"
    elif n==4:
        asp_ratio=w/h
        if asp_ratio>=0.95 and asp_ratio<=1.05:
            obj = "Square"
        else:
            obj="rectangle"
    elif n==5:
        obj="Hexagon"
    elif n==16:
        obj="Circle"
    else:
        obj="Ellipse" #n=14
    cv2.drawContours(img,[approx],0,255,3)  #it will find contours
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.putText(img,obj,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1) #give a text with which shape it is
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()