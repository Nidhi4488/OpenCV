#To capture video from webcam and storing it

import cv2
video=cv2.VideoCapture(0,cv2.CAP_DSHOW) #0 for webcam capture and 1 for external cam

#Video format : DIVX,XVID,MJPG,X264,WMV1,WMV2
fourcc= cv2.VideoWriter_fourcc(*"XVID")
#name,codec,fps,resolution,for grayscale 0
output1=cv2.VideoWriter("outputvideo1.avi",fourcc,20.0,(400,400))
output2=cv2.VideoWriter("outputvideo2.avi",fourcc,20.0,(400,400),0)
while video.isOpened():
    b,frame= video.read()
    if b==True:
        #frame=cv2.flip(frame,0)
        # frame=cv2.resize(frame,(400,400))
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("myvideo",frame)
        cv2.imshow("grayvideo",gray)
        output1.write(frame)
        output2.write(gray)
        k=cv2.waitKey(25)
        if k==ord('x'):
            break
video.release()
cv2.destroyAllWindows()
