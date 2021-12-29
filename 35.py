#multiple ROIs , #continuation of problem 27
import cv2
img=cv2.imread("C:\\Users\\user\\Desktop\\asap\\opencv images\\7.jpg")
rois=cv2.selectROIs("Original",img)
crop=1
for r in rois:
    cropped=img[(r[1]):(r[1]+r[3]),(r[0]):(r[0]+r[2])]
    cv2.imshow(f'Cropped {crop}',cropped)
    crop+=1
cv2.waitKey(0)
cv2.destroyAllWindows()
#enter space button after selecting a place,repeat as much crop needed,
#enter escape button to exit from window