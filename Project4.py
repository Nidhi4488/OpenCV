#Create a function which help to find cordinate of any pixel and its color
import cv2
import numpy as np
def mouse_event(event,x,y,flags,param):
    print("x:", x)
    print("y:", y)
    print("flags:", flags)
    print("param:", param)
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,",",y)
        cord="Coordinate"+str(x)+","+str(y)
        cv2.putText(img, cord, (x, y), font, 1, (234, 123, 165), 1)
        #cv2.imshow('Image',img)

    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0] #0 for blue channel
        g=img[y,x,1] #1 for green channel
        r=img[y,x,2] #2 for red channel

        color_bgr="PixelColor:"+ str(b)+ ","+ str(g) + ","+ str(r)
        cv2.putText(img,color_bgr , (x, y), font, 1, (234, 123, 165), 1)
        #cv2.imshow('Image', img)

cv2.namedWindow(winname="Result")
# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("first.png")
cv2.setMouseCallback("Result",mouse_event)
while True:
    cv2.imshow("Result", img)
    if cv2.waitKey(1)==27: #esc
        break
cv2.destroyAllWindows()