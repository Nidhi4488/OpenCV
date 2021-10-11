#working on pixel color values
import cv2
img=cv2.imread("pikachu.jpg")
img=cv2.resize(img,(500,500))
cv2.imshow("Result",img)
print("Shapes(rows,columns,channel):",img.shape)
print("No.of pixels:",img.size)
print("imageDatatype:",img.dtype)
print("Image Type:" ,type(img))
#to access a pixel value by its row and column coordinates
px=img[220,220]
print("The pixel of that coordinate:",px) #gives color value at that coordinate
#trying to find selected channel value from coordinate
#three channel=0,1,2
blue=img[250,260,0]
green=img[250,260,1]
red=img[250,260,2]
print("The pixel having blue color:",blue)
print("The pixel having green color:",green)
print("The pixel having red color:",red)

cv2.waitKey(0)
cv2.destroyAllWindows()