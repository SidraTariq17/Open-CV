import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')
blank1 = np.zeros((500,500,3), dtype= 'uint8')
#cv.imshow('Blank', blank)

#1) paint the image a certain color
#[200:300] -> rows 300 exclusive (y-axis) [300:400] -> columns 400 exclusive (x-axis)
blank[200:300, 300:400] = 0,255,0
#cv.imshow('Green', blank)

#2) draw a rectangle (manually)
blank[200:300, 200:400] = 0,255,0
#cv.imshow('Green', blank)

#3) automatically
cv.rectangle(blank1, (0,0), (250,250), (0,255,0), thickness= cv.FILLED)
#cv.imshow('Rectangle', blank1)

#4) circle
cv.circle(blank1,(250,250),40, (0,0,255), thickness=cv.FILLED)
#cv.imshow('Circle', blank1)

#5) line self-drawn

# cv.rectangle(blank1, (0,399), (400,399), (255,0,0), thickness=2)
# cv.imshow('line', blank1)

#5) line with method
cv.line(blank1, (0,0), (250,250), (255,0,0), thickness=2)
#cv. imshow('line', blank1)

#6) write text on an image
cv.putText(blank1, ' SIDRA TARIQ', (250,250), cv.FONT_HERSHEY_TRIPLEX,1.0, (255,255,255), thickness= 2)
cv.imshow('text', blank1)

cv.waitKey(0)