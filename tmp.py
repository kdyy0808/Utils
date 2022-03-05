import cv2
from cv2 import IMREAD_GRAYSCALE
import numpy as np
import os
import cv2
from cv2 import IMREAD_COLOR

path = "/media/piai202/53387bcd-1a4a-4370-8c74-abf0c7811ab0/Segmentation_data/ALL_train_data/test/mask_img/"
img=cv2.imread(path+"DY2_183.png",IMREAD_COLOR)
img2=cv2.imread(path+"DY2_183.png",IMREAD_GRAYSCALE)
img[img[:][:][0]>0]=(255,255,255)
#img[img2==133] = (0,255,0)

cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()