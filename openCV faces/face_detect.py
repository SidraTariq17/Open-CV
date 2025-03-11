import cv2 as cv

img = cv.imread("C:\\Users\\USER\\Desktop\\uni internship\lady.jpg")
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_Lady', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#rect for rectangle
# Yes, the `detectMultiScale` function in OpenCV typically requires the image to be in grayscale. Here’s why:
# 1. **Simplifies the Data**: Grayscale images have only one color channel (shades of gray) instead of three (red, green, and blue) in a color image. This reduces the amount of data the algorithm has to process, making it faster and more efficient.
# 2. **Focus on Patterns**: Face detection relies on recognizing patterns, like the shape of eyes, nose, and mouth. These patterns are easier to detect in grayscale because color variations can add unnecessary complexity and noise.
# 3. **Consistency**: In grayscale, the algorithm only has to deal with brightness variations (light and dark areas), which helps it consistently recognize facial features regardless of the person’s skin tone or the lighting conditions.
# By using a grayscale image, the detection process becomes quicker and more reliable, focusing solely on the structure and shape of the face.

# scaleFactor controls the resizing of the image to detect faces of different sizes.
# Smaller values increase detection accuracy but slow down the process.
# Larger values make detection faster but may reduce accuracy, especially for smaller faces.
# In practice, you often start with a value around 1.1 and adjust based on the specific needs of your application.

# The `minNeighbors` parameter controls how certain the program needs to be before it says, "Yes, this is a face."
# - If you set `minNeighbors` to a low number (like 1), the program will be less picky and might detect more faces, but some might not be real faces (false positives).
# - If you set it to a higher number, the program will be more strict, only keeping detections that it’s more confident about. This reduces false positives but might miss some real faces.
# So, it balances between catching more faces and avoiding mistakes.
# Not exactly on the same pixel, but in the same general area. Here’s a simpler breakdown:
# - When the program looks for faces, it checks small regions of the image. If it finds something that might be a face in one region, it marks that area.
# - It then moves a little and checks the next region, which might overlap with the first region.
# - If it finds a potential face in this new, overlapping region, it counts that as a "neighbor."
# So, when you set `minNeighbors`, you're deciding how many of these overlapping regions (neighbors) need to show a face in roughly the same area before the program says, "Yes, this is a face." The overlaps don’t have to be on the exact same pixel but rather in close proximity.

face_rect = haar_cascade.detectMultiScale(gray, 2, 1)
print(f"NO OF FACES FOUND = {len(face_rect)}")
print(face_rect)

for (x,y,w,h) in face_rect:
     cv.rectangle(img, (x,y), ((x+w), (y+h)), (0,255,0), thickness= 2)
#(x, y): The coordinates of the top-left corner of the rectangle.
#((x + w), (y + h)): The coordinates of the bottom-right corner of the rectangle. This is calculated by adding the width w to x and the height h to y.


cv.imshow('Detected', img)
cv.waitKey(0)

### Modern Methods for Object Detection:

# Today, more advanced techniques have largely replaced Haar Cascades for object detection, especially for tasks like face detection. The most commonly used methods now include:
#
# 1. **Convolutional Neural Networks (CNNs)**:
#    - **How It Works**: CNNs are deep learning models specifically designed to recognize patterns in images. They can learn complex features through multiple layers of processing, making them highly effective for detecting and recognizing objects, including faces.
#    - **Examples**: Popular CNN architectures include AlexNet, VGG, ResNet, and Inception. These networks are often used as backbones for object detection models.
#
# 2. **Region-Based CNN (R-CNN)**:
#    - **How It Works**: R-CNN and its variations (Fast R-CNN, Faster R-CNN) combine region proposal methods with CNNs to detect objects. These models first generate potential bounding boxes (regions) where objects might be and then use a CNN to classify each region.
#    - **Why It's Better**: R-CNN models are more accurate because they focus on specific regions of interest and can handle complex backgrounds better than traditional methods.
#
# 3. **Single Shot Multibox Detector (SSD) and YOLO (You Only Look Once)**:
#    - **How It Works**: SSD and YOLO are real-time object detection models that predict bounding boxes and class probabilities in a single pass through the network, making them incredibly fast.
#    - **Why It's Better**: These models are designed for speed without compromising much on accuracy, making them suitable for applications like video surveillance, self-driving cars, and mobile apps.
#
# 4. **Face Detection with MTCNN (Multi-Task Cascaded Convolutional Networks)**:
#    - **How It Works**: MTCNN is a specialized model for face detection that uses a series of CNNs to detect faces at different scales and refine the detection by aligning facial landmarks.
#    - **Why It's Better**: MTCNN is particularly effective at handling faces at different angles, scales, and lighting conditions, offering superior accuracy compared to traditional methods.
#
# ### Why Haar Cascade is Less Used Today:

# 1. **Lower Accuracy**:
#    - Haar Cascades rely on simple, hand-crafted features, making them less accurate for complex images with varying lighting, angles, and backgrounds. Modern deep learning methods automatically learn more complex and robust features from data, leading to better performance.
#
# 2. **Limited Flexibility**:
#    - Haar Cascades struggle with detecting objects at different scales, angles, and poses. Modern techniques like CNNs and R-CNNs are better at handling these variations because they learn from large, diverse datasets.
#
# 3. **Speed vs. Accuracy**:
#    - Although Haar Cascades are fast, their accuracy is not competitive with modern methods. Techniques like SSD and YOLO offer both real-time speed and higher accuracy, making them preferable in most applications.
#
# 4. **Better Generalization**:
#    - Haar Cascades were trained on specific datasets and might not generalize well to new data, especially in different environments. Modern deep learning models are trained on much larger and more diverse datasets, allowing them to generalize better across different scenarios.
#
# ### Summary:
# - **Modern Methods**: Techniques like CNNs, R-CNN, SSD, and YOLO are now widely used for object detection due to their superior accuracy, flexibility, and ability to handle complex images.
# - **Haar Cascade**: Once popular for its speed and simplicity, Haar Cascades have been largely replaced because they cannot compete with the accuracy and robustness of modern deep learning approaches.