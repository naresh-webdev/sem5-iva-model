#shearing
import cv2
import numpy as np

img = cv2.imread('./images/profile.jpg')

(h, w) = img.shape[:2]
M = np.float32([[1, 0.5, 0], [0, 1, 0]])
res = cv2.warpAffine(img, M, (w, h))

cv2.imshow("result : ", res)

cv2.waitKey(0)
cv2.destroyAllWindows()