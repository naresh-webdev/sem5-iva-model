import cv2

# Read the image and convert it to grayscale
image = cv2.imread('../images/profile1.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel Edge Detection (combined X and Y gradients)
sobel_edges = cv2.Sobel(image, -1, 1, 1, 3)

# Display the result
cv2.imshow('Sobel Edge Detection', sobel_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
