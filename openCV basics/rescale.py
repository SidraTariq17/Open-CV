import cv2 as cv

def rescale_frame(frame, scale=0.75):
    #images, videos, live videos

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeres(width, height):
    #live videos only, coming directly from camera
    capture.set(3,width)
    capture.set(4, height)

#image reading

# img = cv.imread('C:\\Users\\USER\Desktop\\uni internship\cat.jpg')
# img_resized = rescale_frame(img)
# cv.imshow('cat', img)
# cv.imshow('resized', img_resized)
# cv.waitKey(0)

capture = cv.VideoCapture('C:\\Users\\USER\\Desktop\\uni internship\\videos\\dog.mp4')

frame_counter = 0  # Counter to create unique filenames

while True:
    isTrue, frame = capture.read()

    # Break the loop if there are no more frames
    if not isTrue:
        print("Finished reading the video or error occurred.")
        break

    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    frame_counter += 1  # Increment the counter for the next frame

    # Break the loop when 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
