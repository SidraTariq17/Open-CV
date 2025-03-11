import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\park.jpg')


#TRANSLATION
def translate(img1, x, y):
    #Array:
    #[[1.0, 0.0 x]
    #[1.0, 1.0, y]]
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img1.shape[1], img1.shape[0])
    return cv.warpAffine(img1, transmat, dimensions)

# -x ---> left
# -y ---> Up
# +x ---> Right
# +y ---> Down

cv.imshow('Karachi', img)

translated = translate(img, -100, 100 )
#cv.imshow('Translated', translated)


#ROTATION from any point not just the centre

#The shape of the array is organized as (height, width, channels):

# img.shape[0]: Height of the image.
# img.shape[1]: Width of the image.
# img.shape[2]: Number of color channels (e.g., 3 for RGB images)

def rotate(img1, angle, rotpoint = None):
    (height, width) = img1.shape[0:2]
    # 0 -> height, 1 -> width

    if rotpoint == None:
        rotpoint = (width//2, height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    #Affine Transformation: It maps pixels from the input image to new locations in the output image based on the affine transformation matrix.
    return cv.warpAffine(img1, rotmat, dimensions)

rotated = rotate(img, -45 )
# -angle --> clockwise rotation
# +angle --> anti-clockwise rotation

#cv.imshow('Rotated', rotated)

#RESIZE
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC)
#cv.imshow('Resized', resized)


#FLIP
# 0: Flip vertically.
# 1: Flip horizontally.
# -1: Flip both vertically and horizontally.
flips = cv.flip(img, 1)
cv.imshow('FLIPPED', flips)

#CROPPING

cropped = img[50:200, 200:400]
cv.imshow('CROPPED', cropped)

cv.waitKey(0)