#basic project of converting coloured into grayscale
import cv2
path=input("Enter the path or name of the image:")
print("This is your entered path: ",path)
img=cv2.imread(path, 0)
img=cv2.resize(img,(200,400))
cv2.imshow("Input image",img)
k=cv2.waitKey()
if k==ord("s"): #press key s to execute this
    cv2.imwrite("result.jpg",img)
else:
    cv2.destroyAllWindows()
