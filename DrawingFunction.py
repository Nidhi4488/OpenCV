#Drawing functions
import numpy as np
import cv2
# img=cv2.imread("first.png")
# img=cv2.resize(img,(400,400))
#black screen height,width,channel, uint8=8 bit unsigned integer(0-255)
# img=np.zeros([512,512,3],np.uint8)*255
#white screen
img=np.ones([512,512,3],np.uint8)*255



#Line accepts 5 parameters (img,starting,ending,color,thickness)
img=cv2.line(img,(0,0),(400,0),(54,253,76),8) #color format BGR(range 0-255)\use "online color picker in google"
img=cv2.line(img,(0,0),(0,400),(54,253,76),8)
img=cv2.line(img,(0,400),(400,400),(54,253,76),8)
img=cv2.line(img,(400,400),(400,0),(54,253,76),8)
#arrowed line
img=cv2.arrowedLine(img,(0,0),(100,100),(54,253,76),8)
#rectangle            starting cord,ending cord,color,thickness
img=cv2.rectangle(img,(110,10),(200,100),(54,253,76),8)
img=cv2.rectangle(img,(110,110),(200,200),(54,253,76),-8) #minus for filling rectangle
#circle             centre,radius,color, thickness
img=cv2.circle(img,(150,300),50,(456,342,43),2)
img=cv2.circle(img,(270,300),50,(456,342,43),-2)

#text               text,startingCord,font,fontsize,color,thickness,linetype
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"IPL",(170,270),font,2,(234,123,165),8,cv2.LINE_AA)

#Ellipse           startingCord,(length,height),rotationPoint,rotationPoint,degree,color,thickness)
img=cv2.ellipse(img,(200,200),(100,50),0,0,180,(123,234,256),2)



cv2.imshow("Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
