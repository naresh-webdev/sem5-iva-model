import cv2
import numpy as np

# Read the image
image = cv2.imread('../images/profile1.jpg')

# Convert the image to a NumPy array
image_array = np.array(image)

# Invert the image colors (simple manipulation)
inverted_image = 255 - image_array

# Display the original and inverted image
cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
