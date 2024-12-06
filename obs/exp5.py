import cv2

cap = cv2.VideoCapture('./images/test.mp4')

ret, prev_frame = cap.read()

prev_gray = cv2.Canny(cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY), 100, 200)
while True:
    ret, cur_frame = cap.read()
    if not ret:
        exit()
    
    cur_gray = cv2.Canny(cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY), 100, 200)

    motion = cv2.absdiff(cur_gray, prev_gray)

    _, threshold = cv2.threshold(motion, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow('motion : ', threshold)

    if cv2.countNonZero(threshold) > 0.1 * threshold.size:
        print('Motion detected')
    
    prev_gray = cur_gray    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



