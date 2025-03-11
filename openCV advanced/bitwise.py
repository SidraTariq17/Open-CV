import cv2 as cv
import numpy as np

# Create a binary image
blank = np.ones((400, 400), dtype='uint8')

# Draw a rectangle and circle with different values
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 200, -1)  # Value 200
circle = cv.circle(blank.copy(), (200, 200), 200, 200, -1)  # Value 100

# Perform bitwise operations
bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_not = cv.bitwise_not(rectangle)
bitwise_xor = cv.bitwise_xor(rectangle, circle)

# Display results
cv.imshow('and', bitwise_and)
cv.imshow('or', bitwise_or)
cv.imshow('not', bitwise_not)
cv.imshow('xor', bitwise_xor)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

cv.waitKey(0)
cv.destroyAllWindows()
