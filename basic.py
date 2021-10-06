import cv2

print(cv2.__version__)
#to read images
img=cv2.imread("first.png",0) #0 for gray scale 1 for colored , -1 unchanged (increases saturation sligthly)
#image resizing
img=cv2.resize(img,(1200,600)) #width and heigth
img=cv2.flip(img,0) #takes 3 parameters 0,1,-1, to flip in different directions
print(img)
#to display images
cv2.imshow('Nidhi',img)
cv2.waitKey() #0=for infinity time is by default, 1000(ms)=1sec
cv2.destroyAllWindows() #to free up all the memories used
#write images or to store images
cv2.imwrite('nihi.jpg',img)
