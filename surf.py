import numpy as np
import cv2 as cv
import os
import time
from classes import image

start_time = time.time()
absolute_path = os.path.join(os.getcwd(), 'data-image', 'data', 'door1.jpeg')
img = image.Image()
img.read(absolute_path)
m,n = img.kp_surf()
image1=cv.drawKeypoints(img.gray,m,img.color,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift_keypoints.jpg',image1)
# print(len(m), len(n))
print("--- %s seconds ---" % (time.time() - start_time))