import numpy as np
import cv2

# Create a black image

img = np.zeros((512,512,3), np.uint8)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
img = cv2.rectangle(img,(11,0),(100,0),(0,255,0),3)
while 1:
    cv2.imshow('image',img)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
      break
