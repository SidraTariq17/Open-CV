import cv2 as cv
# import matplotlib.pyplot as plt

#BGR: Blue, Green, Red channels;
img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\park.jpg')
cv.imshow('Boston', img)
# plt.imshow(img)
# plt.show()

#BGR TO grayscale
#Grayscale: Single channel representing intensity; ranges from black (0) to white (255), eliminating color information.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR TO HSV
#HSV: Hue, Saturation, Value; separates color information (hue) from intensity (value), useful for color-based filtering.
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR TO LAB
#LAB: Lightness (L) and color-opponent dimensions (A and B); designed to be perceptually uniform, meaning equal changes in values correspond to equal changes in perceived color.
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

lab1 = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB1',lab1)

#BGR TO RGB
#RGB: Red, Green, Blue channels;
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)