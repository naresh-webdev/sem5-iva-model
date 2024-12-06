import cv2

img = cv2.imread('./images/profile.jpg')

res = cv2.resize(img, None, fx=0.5, fy=0.5)

cv2.imshow("result : ", res)

cv2.waitKey(0)
cv2.destroyAllWindows()