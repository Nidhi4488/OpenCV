#Bitwise operation includes AND,OR,NOT and XOR
#it is very important and used for various purposes like masking finding roi of complex shapes
import cv2
import numpy as np

img1=np.zeros((250,250,3),np.uint8)
img1=cv2.rectangle(img1,(150,100),(200,250),(255,255,255),-1)
img2=np.zeros((250,250,3),np.uint8)
img2=cv2.rectangle(img2,(10,10),(170,190),(255,255,255),-1)


cv2.imshow("Result1",img1)
cv2.imshow("Result2",img2)

bitAnd=cv2.bitwise_and(img1,img2)
bitOR=cv2.bitwise_or(img1,img2)
bitNot=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)
bitXOR=cv2.bitwise_xor(img1,img2)
cv2.imshow("BITAND",bitAnd)
cv2.imshow("BITOR",bitOR)
cv2.imshow("BITNot",bitNot)
cv2.imshow("BITNot",bitNot2)
cv2.imshow("BITXOR",bitXOR)
cv2.waitKey(0)
cv2.destroyAllWindows()