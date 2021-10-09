import cv2
url="http://192.168.1.87:8080/video "
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(url)
print(cap.isOpened())
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("result.avi",fourcc, 20.0,(400,400))
while (cap.isOpened()):
    b,frame=cap.read()
    if b==True:
        frame=cv2.resize(frame,(400,400))
        cv2.imshow("Result",frame)
        output.write(frame)
        k =cv2.waitKey(1)
        if k==ord("x"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()