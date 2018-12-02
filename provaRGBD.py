import cv2
import numpy as np

filename1 ='background.png'
filename2 ='frame.png'
img1 = cv2.imread(filename1, cv2.IMREAD_ANYDEPTH)
img2 = cv2.imread(filename2, cv2.IMREAD_ANYDEPTH)

dst = img2- img1
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.Canny(blur,100,200)

cv2.imshow('prova1',dst)
cv2.imshow('edges',edges)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()

