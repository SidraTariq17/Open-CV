import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\kittens.jpg')
blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, ((img.shape[1]//2)-200, (img.shape[0]//2)-100), 100, 255, -1)

cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked', masked)
cv.imshow('Cat', img)
cv.waitKey(0)