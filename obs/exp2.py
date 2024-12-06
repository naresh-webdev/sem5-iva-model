import cv2
import numpy as np

img = cv2.imread('./images/profile.jpg', cv2.IMREAD_GRAYSCALE)

def quad_tree(x, y, size):
    if y+size > img.shape[0] or x+size > img.shape[1]:
        return 
    if size <= 1 or np.all(img[y: y+size, x: x+size] == img[y, x]):
        cv2.rectangle(img, (x,y), (x+size, y+size), (0,255,0), 1)
    else:
        #split the image
        half = size // 2

        quad_tree(x, y, half)
        quad_tree(x+half, y, half)
        quad_tree(x, y+half, half)
        quad_tree(x+half, y+half, half)

    
quad_tree(0, 0, min(img.shape))

cv2.imshow("result : ", img)

cv2.waitKey(0)
cv2.destroyAllWindows()