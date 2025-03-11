import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\kittens.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#LAPLACION

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#SOBEL
#computes the gradients/edges in two axises

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('SOBELX', sobelx)
cv.imshow('SOBELY', sobely)
cv.imshow('COMBINED', combined_sobel)

canny = cv.Canny(gray, 150, 175)
# Strong Edges: If a pixel's gradient value is above the upper threshold, it is considered a strong edge.
# Weak Edges: If a pixel's gradient value is between the lower and upper thresholds, it is considered a weak edge and is included only if it is connected to a strong edge.
# Non-Edges: Pixels below the lower threshold are discarded as non-edges.
cv.imshow('Canny', canny)

cv.waitKey(0)
