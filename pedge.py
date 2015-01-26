import cv2
import numpy as np
from matplotlib import pyplot as plt
val1=255
val=127
def nothing(x):
	pass
img = cv2.imread('C:\Users\Karma_is_Bitch\Desktop\mail to mam\cc1.jpg')
# edges = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#            cv2.THRESH_BINARY,11,6)
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)


# val= cv2.getTrackbarPos('R','image')
# val1= cv2.getTrackbarPos('G','image')
edges = cv2.Canny(img,50,190)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.show()
