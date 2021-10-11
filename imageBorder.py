import cv2
import numpy
img=cv2.imread("first.png")
                             #borderWidth(top,bottom,right,left),border type,colorvalue
border=cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value=[255,0,125])
cv2.imshow("Result",border)
cv2.waitKey(0)
cv2.destroyAllWindows()
