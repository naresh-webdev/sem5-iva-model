import cv2
import numpy as np

# Open the video source (0 for webcam or file path)
cap = cv2.VideoCapture("../images/traffic.mp4")

while cap.isOpened():
    # Read two consecutive frames
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges1 = cv2.Canny(gray1, 100, 200)
    edges2 = cv2.Canny(gray2, 100, 200)

    # Subtract edges to find motion
    diff = cv2.absdiff(edges1, edges2)

    # Apply binary threshold
    _, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

    # Check the percentage of non-zero pixels
    non_zero_count = np.count_nonzero(thresh)
    total_pixels = thresh.size
    motion_percentage = (non_zero_count / total_pixels) * 100

    if motion_percentage > 10:  # Adjust threshold as needed
        print("Motion detected!")

    # Display the result
    cv2.imshow('Motion Detection', thresh)

    # Break on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
