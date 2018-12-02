import cv2
import numpy
import math
import time


cap = cv2.VideoCapture(0)
scheda = cv2.imread('scheda2.jpg', 0)
pallino = cv2.imread('Pallino_rosso.png',0)

orb = cv2.ORB_create()    
sift = cv2.xfeatures2d.SIFT_create()

MIN_MATCHES = 15
while(True):
    ret, frame =cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# ORB keypoint detector
# create brute force  matcher object
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)  
# Compute model keypoints and its descriptors
    kp_scheda, des_scheda = sift.detectAndCompute(scheda, None)  
# Compute scene keypoints and its descriptors
    kp_frame, des_frame = sift.detectAndCompute(gray, None)
# Match frame descriptors with model descriptors
    matches = bf.match(des_scheda, des_frame)
# Sort them in the order of their distance
    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) > MIN_MATCHES:
    # draw first 15 matches.
        img3 = cv2.drawMatches(scheda, kp_scheda, gray, kp_frame, matches[:10], 0, flags=2)
        i=0
        x=[]
        y=[]
        for n in matches:
            x.append(kp_frame[n.trainIdx].pt[0])
            y.append(kp_frame[n.trainIdx].pt[1])
            #print ("x="+str(x[i])+"-y="+str(y[i]))
            i+=1
        xs=0
        for nx in x:
            xs+=nx
        xm=xs/i
        #print("media x="+str(xm))

        ys=0
        for ny in y:
            ys+=ny
        ym=ys/i
        #print("media y="+str(ym))

      
        cv2.circle(frame, (int(xm), int(ym)), 30,(255,0,0),-1)

    # show result
        #cv2.imshow('frame',img3)
        cv2.imshow('Final', frame)
        #time.sleep(10)
        cv2.waitKey(0)
    else:
        print ("Not enough matches have been found - %d/%d" % (len(matches), MIN_MATCHES))