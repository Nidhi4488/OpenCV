#Screen Recording
import cv2
import pyautogui as p
import numpy as np

#create resolution
rs=p.size()
filename=input("Enter the file name or path:")
fps=60.0
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(filename,fourcc,fps,rs)

cv2.namedWindow("LiveRecording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("LiveRecording",(600,400))

while True:
    img=p.screenshot()
    f=np.array(img)
    f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Result",f)
    if cv2.waitKey(1)==ord("x"):
        break

output.release()
cv2.destroyAllWindows()
