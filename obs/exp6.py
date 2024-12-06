import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('./images/man.mp4')



while True:
    _, cur_frame = cap.read()
    
    cur_gray = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(cur_gray, 1.1, 2)

    for (x, y, h, w) in faces:
        cv2.rectangle(cur_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("res : ", cur_frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

