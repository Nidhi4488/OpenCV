#Drawing functions for videos
import cv2
import datetime

vid=cv2.VideoCapture("vanilla.mp4")
print("Width:",vid.get(3)) #for width
print("Height:",vid.get(4)) #for height
while True:
    ret,frame=vid.read()
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    text="Height:"+str(vid.get(4))+"Width:"+str(vid.get(3))
    date="Date:"+ str(datetime.datetime.now())
    frame=cv2.putText(frame,text,(170,270),font,1,(234,123,165),1,cv2.LINE_AA)
    frame=cv2.putText(frame,date,(100,200),font,1,(234,23,65),1,cv2.LINE_AA)
    frame = cv2.rectangle(frame, (110, 10), (200, 100), (54, 253, 76), 8)
    cv2.imshow("Result",frame)
    if cv2.waitKey(25)==ord("x"):
        break

vid.release()
cv2.destroyAllWindows()