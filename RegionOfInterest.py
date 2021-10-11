import cv2

img=cv2.imread("Liam.jpg")
img2=cv2.imread("robert.jpg ")
#Region of interest
#334,50 and 551,280
#[(y1:y2),(x1:x2)]
#y=230 x= 217 (difference)
roi=img[50:280,334:551]
#now passing data into img
img[50:280,116:333]=roi

#439,132
img2[132:362,439:656]=roi

print(img.shape)
cv2.imshow("Result2",img2)
cv2.imshow("Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()