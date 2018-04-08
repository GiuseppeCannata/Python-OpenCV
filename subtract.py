import cv2

img = cv2.imread('logo.jpg',0)
blur = cv2.GaussianBlur(img,(3,3),0)

dst = cv2.subtract(img,blur)

cv2.imshow('immagine', dst)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()