import cv2

img = cv2.imread('./images/profile.jpg')

level0 = cv2.pyrDown(img)
level1 = cv2.pyrDown(level0)
level2 = cv2.pyrDown(level1)

cv2.imshow('level 0 : ', level0)
cv2.imshow('level 1 : ', level1)
cv2.imshow('level 2 : ', level2)

cv2.waitKey(0)
cv2.destroyAllWindows()
