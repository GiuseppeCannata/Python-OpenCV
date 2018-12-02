import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame =cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    
    
    dst1 = cv2.cornerHarris(gray,4,3,0.04)
    dst1 = cv2.dilate(dst1 , None)
    
    i = 0
    n = 0
    for n1 in dst1:
       i = i+1
       for pixel1 in n1:
           n = n+1
              if pixel1 > 0.08:
                print('True')
                
                
    
    cv2.imshow('Final', dst1)
    
    k = cv2.waitKey(0)
    if k==27:
      cv2.destroyAllWindows()
    
