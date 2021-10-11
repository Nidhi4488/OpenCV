#Blending means addition of two images
#in  opencv we have 2 functions cv2.add(),cv2.addWeight()
#to blend 2 images the size should be same


import cv2
import numpy as np
img1=cv2.imread("Liam.jpg")
img2=cv2.imread("robert.jpg")
img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))
#result=img1+img2  (numpy addition gives module between value hence pixels are damaged

#image blending
#result1=cv2.add(img1,img2)

#function to control blending
                          #weight1,   ,wt2 ,gama_value
                          #w1+w2=1
result1=cv2.addWeighted(img1,0.7,img2,0.3,0)


cv2.imshow("result1",img1)
cv2.imshow("result2",img2)
cv2.imshow("Blended",result1)
cv2.waitKey(0)
cv2.destroyAllWindows()
