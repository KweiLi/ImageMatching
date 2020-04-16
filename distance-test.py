from classes import image, matcher,utils
import cv2 as cv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy 
import math,os

absolute_path = os.path.join(os.getcwd(), 'data-image', 'data')

img1 = image.Image()
img1.read(absolute_path+ "/sofa_query.jpeg")
kp_query,des_query = img1.kp_sift()
img2 = image.Image()
img2.read(absolute_path+ "/sofa6.jpeg")
kp_train,des_train = img2.kp_sift()

matches = matcher.Matcher()
good_matches = matches.flann(des_query, des_train)
# print(good_matches)

img3 = cv.drawMatchesKnn(img1.gray,kp_query,img2.gray,kp_train,good_matches,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()

# pts_query = []
# pts_train = []
# for i in xrange(len(good_matches)):
#     pts_query.append(kp_query[good_matches[i][0].queryIdx].pt)
#     pts_train.append(kp_train[good_matches[i][0].trainIdx].pt)
# print(pts_query)
# print(pts_train)

# w_query, w_train = [],[]
# w_query = utils.d_mat(pts_query)
# w_train = utils.d_mat(pts_train)
# print(w_query, len(w_query))
# print(w_train, len(w_train))

# w_ratio_sum, w_ratio_ave = 0, 0
# count = 0
# for i in xrange(len(w_query)):
#     if w_query[i]== 0:
#         count = count + 1
#     else:
#         w_ratio_sum = w_train[i]/w_query[i] + w_ratio_sum
# w_ratio_ave = w_ratio_sum/(len(w_query)-count)
# print(w_ratio_ave)

# angle_query, angle_train = [], []
# dim_query = numpy.linalg.norm(numpy.shape(img1.gray)) 
# dim_train = numpy.linalg.norm(numpy.shape(img2.gray)) 
# print(dim_query, dim_train)

# camera_aov = utils.aov(4.25, 7)
# print(camera_aov)
# for i in xrange(len(w_query)):
#     angle_query.append(w_query[i]*camera_aov/dim_query)
#     angle_train.append(w_train[i]*camera_aov/dim_train)

# print(angle_query)
# print(angle_train)


# d_query, d_train = [], []
# for i in xrange(len(w_query)):
#     d_query.append((w_query[i]/2)/math.tan(math.radians(angle_query[i]/2)))
#     d_train.append((w_train[i]/2)/math.tan(math.radians(angle_train[i]/2)))

# print(d_query, d_train)

# distance_ratio = []
# count = 0
# for i in xrange(len(distance_query)):
#     if distance_query[i]== 0:
#         count = count + 1
#     else:
#         distance_ratio.append(math.tan(math.radians(angle_query[i]/2))*distance_train[i]/(math.tan(math.radians(angle_train[i]/2))*distance_query[i]))

# print(distance_ratio)