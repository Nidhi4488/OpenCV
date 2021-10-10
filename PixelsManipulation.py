#Using split and merge function

import cv2
import numpy as np
img=cv2.imread("pikachu.jpg")
# img=cv2.resize(img,(400,500))
print("Shapes(rows,columns,channel):",img.shape)
print("No.of pixels:",img.size)
print("imageDatatype:",img.dtype)
print("Image Type:" ,type(img))

#Split function
#split returns 3 channel of our image which is blue,green,red
# print(cv2.split(img))
b,g,r=cv2.split(img)
# cv2.imshow("Blue",b)
# cv2.imshow("Green",g)
# cv2.imshow("RED",r)

#Merge function
m=cv2.merge((r,g,b))
m3=cv2.merge((b,r,g))
m2=cv2.merge((b,g,r)) #conventionally used by python
cv2.imshow("MergeRgbImage",m)
cv2.imshow("MergeBgrImage",m2)
cv2.imshow("MergeBrgImage",m3)



cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()