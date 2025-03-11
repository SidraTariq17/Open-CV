import cv2 as cv

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\cat.jpg')
cv.imshow('cats', img)

#KERNEL
#A kernel in image processing is a small matrix (usually 3x3, 5x5, etc.) that is used to apply effects like blurring, sharpening, edge detection, and more. It is slid over the image, and for each position, the kernel values are multiplied by the corresponding pixel values in the image. The results are summed and usually normalized to produce the new pixel value in the output image.

#Averaging
#Average Blur: A blurring technique in OpenCV that smooths an image by averaging the pixel values within a defined kernel size. This results in a uniform blur, reducing noise and detail.
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#Gaussianblur
#Gaussian Blur: A blurring technique that applies a Gaussian function to the image, giving more weight to the central pixels in the kernel. This creates a natural, smooth blur effect, often used to reduce image noise and detail more effectively than average blur.
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Guass', gauss)

#Medianblur
#Median Blur: Replaces each pixel with the median value of its neighbors. It’s great for removing salt-and-pepper noise while preserving edges.
#this works better for smaller kernel sizes
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#bilateral Blurring
#retains the edges when blurring the image
bilateral = cv.bilateralFilter(img, 15, 35, 25)
# In cv.bilateralFilter(img, 15, 35, 25):
# img: The input image.
# 15: Diameter of the pixel neighborhood.
# 35: Standard deviation of the color space (larger values mean more smoothing).
# 25: Standard deviation of the coordinate space (controls spatial distance influence).
# This function smooths the image while preserving edges.
cv.imshow('bilateral', bilateral)

#for bilateral and median higher value for kernel and sigma results in a smudged image.
cv.waitKey(0)

#USES:
#Average Blur: Use for general smoothing and noise reduction. It averages the pixel values in a neighborhood, which can blur edges and details.
# Gaussian Blur: Use when you want to smooth an image while maintaining more of the image’s details compared to average blur. It uses a Gaussian function to weigh nearby pixels more heavily, producing a smooth effect with less distortion of edges.
# Median Blur: Use to remove salt-and-pepper noise or other types of noise while preserving edges. It’s effective for reducing noise in images without blurring edges too much.
# Bilateral Blur: Use when you need to smooth an image while preserving edges. It’s great for reducing noise and details while keeping the boundaries between different regions sharp.