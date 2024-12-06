import cv2

# Load the pre-trained Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

img = cv2.imread("./images/plate_num.jpg")
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plates = plate_cascade.detectMultiScale(gray_scale, 1.1, 4)


for (x, y, h, w) in plates:
    cv2.rectangle(img, (x, y), (x+h, y+w), (255, 0, 0), 2)

cv2.imshow('res: ', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
