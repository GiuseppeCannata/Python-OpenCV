import numpy as np
import cv2

cap =cv2.VideoCapture(0)

while(True):
#capture frame-by-frame
    ret, frame = cap.read()

#Our operation on the frame come here
    #Threshold
    #ret1,th1 = cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    #AggiuntaImmagine
    #dst = cv2.addWeighted(img2,0.8,frame,0.7,0)
    #Gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Canny --> edge detector
    #piu diminuisco gli edge piu ho instabilità
    can = cv2.Canny(frame,100,200)
    
   
#Display the resulting Frame
    
    cv2.imshow('frame', can )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   

#when everything done,release the capture
cap.release()
cv2.destroyAllWindows()

