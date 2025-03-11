import cv2 as cv

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\kittens.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Thresholding is a technique in image processing where pixel values are converted into binary values based on a specified threshold. Pixels with values above the threshold are set to one value (e.g., white), and those below are set to another (e.g., black). This method is used to segment objects or features from the background in an image.

#SIMPLE THRESHOLDING
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#if pixel value above 150 --> white(255) else 0 or black
#thresh --> binarized image
#threshold --> your provided value i.e 150

count = 0
height, width = thresh.shape
for i in range(height):
    for j in range(width):
        if thresh[i][j] == 255:
            count += 1

print(count)



cv.imshow('threshold', thresh)

#ADAPTIVE THRESHOLDING
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, (13), 13)
cv.imshow('AdaptiveThresh', adaptive_thresh)

cv.waitKey(0)