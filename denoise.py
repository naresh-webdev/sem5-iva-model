import cv2
import numpy as np

# Read the grayscale image
gray_image = cv2.imread('../images/profile1.jpg', cv2.IMREAD_GRAYSCALE)

# Standardize
mean, std = gray_image.mean(), gray_image.std()
standardized_image = (gray_image - mean) / std

print(standardized_image)  # Prints standardized values
