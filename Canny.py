# Edge detector

import cv2
import numpy as np

img = cv2.imread('Lena.jpg',0)
edges = cv2.Canny(img,100,200)

cv2.imshow('Canny',edges)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
