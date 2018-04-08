import cv2
img1 = cv2.imread('immagine.jpg',0)
img2 = cv2.imread('logo.jpg',0)
#somme pesate per la sovrapposizione
dst = cv2.addWeighted(img1,0.8,img2,0.7,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()