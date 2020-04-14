import cv2 as cv

class Matcher(object):
    def __init__(self):
        pass

    def bf(self,img1_des,img2_des):
        # BFMatcher with default params
        bf = cv.BFMatcher()
        matches = bf.knnMatch(img1_des,img2_des,k=2)
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append([m])
        return good


    def flann(self,img1_des,img2_des):
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(img1_des,img2_des,k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append([m])
        return good
