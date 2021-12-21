#Mouse Click Event
#to print all events present in opencv
#Eg:mousemove,mousewheel

#import cv2
#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

#now when click we have to get the position of mouse
import cv2
import numpy as np

def click_event(event,x,y,flags,p): #coordinate where we clicked,p is extra parameter
    if event==cv2.EVENT_LBUTTONDOWN:
        cor="("+str(x)+","+str(y)+")" #(10,10)
        cv2.putText(img,cor,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
        cv2.imshow("image",img)


img=np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event) #window name,function to be called #when click something something should be called
cv2.waitKey(0)
cv2.destroyAllWindows()