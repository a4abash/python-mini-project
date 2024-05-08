# image resizer
# for this we need to install ( pip install opencv-python )
import cv2

source = cv2.imread("sample.jpg") #source image should be in the same directory
# cv2.imshow('outputImage',source)
# cv2.waitKey(0)

scale_percent = 50

new_width = int(source.shape[1] * scale_percent / 100) #divides image in half in width
new_height = int(source.shape[0] * scale_percent / 100) #divides image in half in height

new_size = (new_width,new_height)

output = cv2.resize(source,new_size)
cv2.imwrite('resizedImage.jpg',output)
# cv2.imshow('outputImage',output) # uncomment this to display image
cv2.waitKey(0)