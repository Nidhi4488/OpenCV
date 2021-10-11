#Image blending using Trackbars
import cv2
import numpy as np
img1=cv2.imread("Liam.jpg")
img2=cv2.imread("robert.jpg")
img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))
# cv2.imshow("result1",img1)
# cv2.imshow("result2",img2)

def blend(x):
    pass
img=np.zeros((400,400,3),np.uint8)
cv2.namedWindow('Window') #creating trackbar windows
cv2.createTrackbar('alpha','Window',1,100,blend)
s1="0:OFF \n 1:ON"
cv2.createTrackbar(s1,"Window",0,1,blend)

while True:
    s=cv2.getTrackbarPos(s1,'Window')
    a=cv2.getTrackbarPos('alpha','Window')
    n=float(a/100)
    print(n)
    if s==0:
        dst=img[:]

    else:
        dst=cv2.addWeighted(img1,n,img2,(1-n),0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,125,255),2)

    cv2.imshow("Result",dst)
    if cv2.waitKey(1)==27:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
