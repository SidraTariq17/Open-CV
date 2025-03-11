import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\kittens.jpg')
cv.imshow('Cats', img)

#histograms allow you to view the pixel intensity distributions in the image
#possible for both grayscale and rgb
# histogram is a graphical representation of the distribution of pixel values in an image. It shows how frequently each pixel intensity occurs.

# Grayscale Images:
# In a grayscale image, each pixel has an intensity value ranging from 0 (black) to 255 (white).
# A histogram counts how many pixels have each intensity value.
# For example, if many pixels are dark, the histogram will have a tall bar near the 0 value.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# #Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#masking
blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, ((img.shape[1]//2)-200, (img.shape[0]//2)-100), 100, 255, -1)

cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('masked', masked)

# gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
colors = ('b' , 'g', 'r')

for i, col in enumerate (colors):
    #i is the index (0 for Blue, 1 for Green, 2 for Red), and col is the corresponding color name
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    #In matplotlib, when you pass 'b' as the value for the color parameter in plt.plot(), it automatically understands that 'b' stands for blue. Similarly, 'g' stands for green, and 'r' stands for red.
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)


# histograms can be used in traffic signal detection for autonomous vehicles. Here's how:
#
# ### Using Histograms for Traffic Signal Detection:
#
# 1. **Color Detection**:
#    - **Histograms of Color Channels**: You can analyze the histograms of color channels (e.g., Red, Green, Blue) to detect the presence of traffic lights. For instance, a histogram of the red channel can help determine if a red light is present.
#
# 2. **Intensity and Distribution**:
#    - **Red Channel Analysis**: If a traffic signal is red, the red channel histogram will show a peak in the red intensity range. Similarly, green or yellow signals will have peaks in the corresponding color channels.
#    - **Thresholding**: By analyzing the histograms, you can set thresholds to detect if the red channel (for a red light) surpasses a certain intensity level, indicating a red signal.
#
# 3. **Region of Interest (ROI)**:
#    - **Masking**: You can use histograms along with image masking to focus on specific regions of the image where traffic lights are likely to appear. This helps in isolating and analyzing traffic signals from the rest of the scene.
#
# 4. **Pattern Recognition**:
#    - **Pattern Analysis**: Histograms can help in understanding the distribution of colors in the image. Combined with pattern recognition techniques, this can help in identifying the shape and color of traffic signals.
#
# ### Summary:
# Histograms are useful for analyzing color distributions and detecting specific features like traffic signals in autonomous driving systems. They provide a way to quantify and visualize the color information in an image, which is crucial for accurate traffic signal detection.