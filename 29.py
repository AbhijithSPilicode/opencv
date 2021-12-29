#when click on image,get what is red,blue,green value
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
cv2.imshow("image",img)
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=[y,x,1]
        r=[y,x,2]
        strbgr="("+str(b)+","+str(g)+","+str(r)+")"
        cv2.putText(img,strbgr,(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)
        cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()