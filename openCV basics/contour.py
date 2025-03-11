import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\cat.jpg')
blank = np.zeros(img.shape, dtype='uint8')


cv.imshow('Cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Cat_BW', gray)

# Edges:
# Definition: The boundaries where there is a significant change in intensity or color in an image.
#Purpose: Helps in identifying and highlighting boundaries between different regions or objects in an image.
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('BLUR', blur)

ret, thresh = cv.threshold(gray, 125, 255,  cv.THRESH_BINARY)
cv.imshow('THRESH', thresh)


# Contours:
# Definition: Curves or lines that connect continuous points along the boundary of an object.
# Purpose: Used to analyze and understand shapes, sizes, and the structure of objects within an image. They provide a detailed outline of objects.
contours, heirarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)