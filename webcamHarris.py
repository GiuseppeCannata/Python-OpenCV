import numpy as np
import cv2
import math

cap =cv2.VideoCapture(0)

while(True):
#capture frame-by-frame
    ret, frame = cap.read()

#Our operation on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(gray,(5, 5),0)
    sobelx = cv2.Sobel( img , cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel( img , cv2.CV_64F,0,1,ksize=5)
    x = cv2.convertScaleAbs (  sobelx ); 
    y = cv2.convertScaleAbs (  sobely );
    grad = cv2.addWeighted (  x ,  0.5 , y ,  0.3 ,  0 );
    ret1,th1 = cv2.threshold(grad,100,255,cv2.THRESH_BINARY)

   
#Display the resulting Frame
    cv2.imshow('Gray',gray)
    cv2.imshow('DerivataLungoX', x )
    cv2.imshow('DerivataLungoY', y )
    cv2.imshow('Intensità approssimata di Gradienti', grad)
    cv2.imshow('Threshold', th1)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   

#when everything done,release the capture
cap.release()
cv2.destroyAllWindows()

