import cv2

img = cv2.imread('lena.jpg',0)

ret1,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('threshold1',th1)
#cv2.imshow('threshold2',th2)
#cv2.imshow('blur',blur)
#cv2.imshow('threshold3',th3)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()