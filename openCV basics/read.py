import cv2 as cv

#image reading

# img = cv.imread('cat.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0)

# video Reading
capture = cv.VideoCapture('videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    # Break the loop if there are no more frames
    if not isTrue:
        print("Finished reading the video or error occurred.")
        break

    cv.imshow('Video', frame)

    # Break the loop when 'd' is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
