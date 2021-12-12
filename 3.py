# Black and white 
import cv2
import numpy as np
black=np.zeros((288,512))
cv2.imshow("black",black)
white=np.ones((288,512))
cv2.imshow("white",white)
cv2.waitKey(0)
cv2.destroyAllWindows()
