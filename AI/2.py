import cv2
import numpy as np

img = cv2.imread('D:\\Github\\Game\\AI\\1.jpg')
img = cv2.resize(img, (500, 500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)  
img = cv2.Canny(img, 100, 200)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()