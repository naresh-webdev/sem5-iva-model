import cv2
import numpy as np

# Read the image
image = cv2.imread('./../images/profile1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection with specified thresholds
edges = cv2.Canny(image, 100, 200)

# Display the edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
