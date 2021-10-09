#capture video from youtube
import pafy
import cv2
url="https://www.youtube.com/watch?v=5qIJ7tQ2QbM&list=RDGMEM916WJxafRUGgOvd6dVJkeQVM5qIJ7tQ2QbM&start_radio=1"
data=pafy.new(url)
data=data.getbest(preftype="mp4")
video=cv2.VideoCapture(0, cv2.CAP_DSHOW) #0 for webcam capture and 1 for external cam
video.open(data.url)
print(video.isOpened())

while video.isOpened():
    b,frame= video.read()
    if b==True:
        #frame=cv2.flip(frame,0)
        frame=cv2.resize(frame,(400,400))

        cv2.imshow("myvideo",frame)

        # output1.write(frame)

        k=cv2.waitKey(25)
        if k==ord('x'):
            break
video.release()
cv2.destroyAllWindows()
