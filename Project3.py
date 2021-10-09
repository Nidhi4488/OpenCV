#To break a video into multiple images and storing in a folder
import cv2

vid=cv2.VideoCapture("video1.mp4")
ret,image=vid.read() #read the video
count=0
while True:
    if ret==True:
        cv2.imwrite("img%d.jpg"%count, image)
        #video capturing speed
        vid.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image=vid.read()
        cv2.imshow("Result",image)
        print(count)

        count+=1
        if cv2.waitKey(1)==ord("x"):
            break
            cv2.destroyAllWindows()

vid.release()
cv2.destroyAllWindows()
