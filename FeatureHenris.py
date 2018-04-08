import cv2
import numpy as np

filename1 ='scacchiera.jpg'
filename2 = 'rot.jpg'
img1 = cv2.imread(filename1)
img2 = cv2.imread(filename2)

#Single precision float: sign bit, 8 bit exp, 23 bit mantissa
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray1 = np.float32(gray1)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray2 = np.float32(gray2)

# img - input image, grayscale and float32
#blocksize - It is the size of neighbourhood considered for corner detection
#ksize - Aperture parameter of Sobel derivate used
#k - Harris  detector free paramter in the equation.
dst1 = cv2.cornerHarris(gray1,4,3,0.04)
dst2 = cv2.cornerHarris(gray2,4,3,0.04)


#result is dilated for making the corners , not important
dst1 =cv2.dilate(dst1 , None)
dst2 = cv2.dilate(dst2 , None)


#Threshold for an optimal value, it may very depending on the image


i = 0
x= 0
for n1 in dst1:
    i = i+1
    print(i)
    for n2 in dst2:
       x =x+1
       for pixel1 in n1:
          for pixel2 in n2:
              if (pixel1 > 0.08) & (pixel1 == pixel2):
                print('True')
                pixel1 = pixel1*10
                pixel2 = pixel2*10
                break
            
img1[dst1>0.08*dst1.max()]=[0,0,255]
img2[dst2>0.08*dst2.max()]=[0,0,255]
                
                


cv2.imshow('prova1',img1)
cv2.imshow('prova2',img2)

k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()

#TO DO 

#Mathcing 2 images (report on pY)
#using distance metric
