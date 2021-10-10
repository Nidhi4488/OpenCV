#Mouse callback functions
import cv2
import numpy as np

def draw(event,x,y,flags,param):
    print("x:",x)
    print("y:",y)
    print("flags:",flags)
    print("param:",param)
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (456, 342, 43), 2)
    elif event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img, (x, y), (x+100, y+75), (54, 253, 76), 8)

cv2.namedWindow(winname="Result")
img=np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("Result",draw)
while True:
    cv2.imshow("Result", img)
    if cv2.waitKey(1)==27: #esc
        break
cv2.destroyAllWindows()