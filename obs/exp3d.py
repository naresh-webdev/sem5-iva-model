import cv2
import numpy as np

img = cv2.imread("./images/profile.jpg")

p1 = np.float32([[0, 0], [100, 0], [0, 100]])
p2 = np.float32([[50, 10], [120, 10], [10, 120]])

(h, w) = img.shape[:2]
M = cv2.getAffineTransform(p1, p2)
res = cv2.warpAffine(img, M, (w, h))

cv2.imshow('res : ', res)
cv2.waitKey(0)
cv2.destroyAllWindows()