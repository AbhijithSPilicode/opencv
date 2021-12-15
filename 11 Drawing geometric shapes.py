#Drawing geometric Shapes
#Drawing a line,rectangle,circle,arrowed line in an image
import cv2
img=np.zeros((500,500,3)) #creating a black window
cv2.line(img,(100,100),(200,200),(255,0,0),2)#this is a sloped line #starting point,end point,colour,thickness
cv2.line(img,(20,150),(50,150),(0,255,0),2) #this is a horizontal line since y axis of start and end point are same.
cv2.arrowedLine(img,(40,200),(40,400),(0,0,255),7)
cv2.rectangle(img,(100,100),(200,200),(0,255,0),5) #creating a rectangle
cv2.rectangle(img,(200,200),(400,400),(255,0,0),-1) #-1 since it will fill the rectangle with colour
cv2.circle(img,(50,50),50,(0,210,123),3) #window,center,radius,colour,thickness
cv2.circle(img,(450,450),50,(0,210,123),-1) #-1 fill
cv2.putText(img,"Hello",(300,150),cv2.FONT_HERSHEY_COMPLEX,2,(120,120,30),3) #window,text content,position,font,size,color,thickness
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

