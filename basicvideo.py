import cv2
vid=cv2.VideoCapture("video1.mp4")
while True:
    b,frame=vid.read() #two variables one to store boolean and other frame
    frame=cv2.resize(frame,(600,600))
    #gray scale video
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #0,1,-1 only used when using imread
    cv2.imshow("MyVideo",frame)
    cv2.imshow('GrayVideo',gray)
    k=cv2.waitKey(25) #the lesser the value is the video will be faster
    if k==ord("x"):
        break
vid.release()
cv2.destroyAllWindows()
