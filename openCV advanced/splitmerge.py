from heapq import merge

import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\park.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

#lighter images show higher saturation of that particular color
#darker regions show lesser or no concentration of that particular color
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
print(b)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

cv.waitKey(0)