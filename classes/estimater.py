from classes import utils, matcher, image,utils

class Estimater(object):
    def __init__(self, image):
        self.image = image

    # def scale_ratio(self):
    #     distance = []
    #     for i in self.good_matches:
    #         print(i[0].queryIdx,i[1].trainIdx)
    #         self.kp_source[]

    def confidence(self, reference_image):
        kp_query,des_query = self.image.kp_sift()
        kp_reference,des_reference = reference_image.kp_sift()
        matches = matcher.Matcher()
        good_matches = matches.flann(des_query, des_reference)
        pts_reference = []
        for i in xrange(len(good_matches)):
            pts_reference.append(kp_reference[good_matches[i][0].trainIdx].pt)
        return pts_reference