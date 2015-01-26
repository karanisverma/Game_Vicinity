import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\Users\Karma_is_Bitch\Desktop\mail to mam\est.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
