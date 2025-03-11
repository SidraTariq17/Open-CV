import cv2 as cv
from numpy.ma.core import resize

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\cat.jpg')
cv.imshow('Cat', img)

#convert to black and white or grayscale to check for the color intensity
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('BW_Cat', gray)

#blur
#kernel is the intensity of the blur
blur =  cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT )
#cv.imshow('Blur', blur)

#Edge Cascade -> Find the edges in an image
#In the cv.Canny function, the numbers 125 and 175 are the lower and upper thresholds for edge detection. Here's what they do:
# Lower Threshold (125):
# Any gradient value below this threshold is considered not an edge, so those pixels are discarded.
# Upper Threshold (175):
# Any gradient value above this threshold is considered a strong edge, so those pixels are kept as edges.
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', canny)
#The edges decrease when passing a blur image
canny1 = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Lesser Edges', canny1)

#Dilate the image -> Using Canny Edges (Dilation is a morphological operation in image processing that enlarges bright regions in a binary or grayscale image)
dilated = cv.dilate(canny1, (3,3), iterations= 1 )
#cv.imshow('dilated', dilated)

#kernel basicallay brightens the intensity, iterations increase the number if times the lines are repeated
dilated1 = cv.dilate(canny1, (7,7) ,iterations= 3)
#cv.imshow('dilated1', dilated1)

#Eroded -> Erosion is a morphological operation in image processing that shrinks bright regions in a binary or grayscale image.
#opposite to dilation
# dilation-> increases the intensity of white area
# Erosion -> decreases the intensity of white area
eroded = cv.erode(dilated1, (7,7), iterations = 3)
#cv.imshow('Eroded', eroded)

#Resize
#Interpolation in image resizing refers to the method used to calculate the pixel values in the resized image.

#cv.INTER_AREA: This interpolation method is generally used for shrinking images.
resized = cv.resize(img, (700, 700), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resized)

#cv.INTER_LINEAR: It's the default method and is often used for enlarging images, providing a good balance between quality and speed.
resized1 = cv.resize(img, (700, 700), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resizedcubic', resized1)

#cv.INTER_CUBIC: It provides higher quality results than linear interpolation, especially when enlarging images, but is slower due to the more complex calculations.
resized2 = cv.resize(img, (700, 700), interpolation=cv.INTER_LINEAR)
#cv.imshow('Resizedlinear', resized2)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)