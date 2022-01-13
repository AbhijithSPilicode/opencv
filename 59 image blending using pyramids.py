#So we have to change that image stitching to a blending
#image blending using pyramids
import cv2
import numpy as np
apple=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\21.jpg")
orange=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\22.jpg")
#generate gaussian pyramid for apple
apple_copy=apple.copy()
gp_apple=[apple_copy]
for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
#generate gaussian pyramid for orange
orange_copy=orange.copy()
gp_orange=[orange_copy]
for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#laplacian for apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_apple[i])
    lap=cv2.subtract(gp_apple[i-1],gaussian_extended)
    lp_apple.append(lap)

#laplacian for orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp_orange[i])
    lap=cv2.subtract(gp_orange[i-1],gaussian_extended)
    lp_orange.append(lap)

#going to make the pyramid from half from orange and half from apple
apple_orange_pyramid=[]
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    laplacian=np.hstack((apple_lap[:,:apple_lap.shape[1]//2],orange_lap[:,orange_lap.shape[1]//2:]))
    apple_orange_pyramid.append(laplacian)
#constructing image from each layer to single layer
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)
cv2.imshow("apple_orange",apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
