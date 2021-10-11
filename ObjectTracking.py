#Object Tracking or color detection
#HSV Color spaces (Hue, Saturation, value)
#with HSV we simply separate the color information and color intensity
import cv2
import numpy as np

img=cv2.imread("ball.jpg")
img=cv2.resize(img,(500,400))
while True:
    hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    upperValue=np.array([227,145,255])
    lowerValue=np.array([166,1,255])
    #mask(filter that only keeps the to be kept and removes the rest)
    m=cv2.inRange(hsv,lowerValue,upperValue)

    #filter mask with image
    result=cv2.bitwise_and(img,img,mask=m)
    cv2.imshow("Result", img)
    cv2.imshow("result",result)
    cv2.imshow("mask",m)
    if cv2.waitKey(1)==27:
        break





cv2.destroyAllWindows()