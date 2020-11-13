import cv2

img1 = cv2.imread('president.jpg')
img2 = cv2.imread('park.jpg')

height, width = img1.shape[:2]
img2[100:height+100, 100:100 + width] = img1

cv2.imwrite('new.jpg', img2)