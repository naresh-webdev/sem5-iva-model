import cv2

img = cv2.imread("./images/profile.jpg")

(h, w) = img.shape[:2]
center = (h//2, w//2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)

rotatedimg = cv2.warpAffine(img, M, (w,h))

cv2.imshow('res', rotatedimg)

cv2.waitKey(0)
cv2.destroyAllWindows()