from classes import utils

class Estimater(object):
    def __init__(self, good_matches, kp_source, kp_target):
        self.good_matches = good_matches
        self.des_source = des_source
        self.des_target = des_target

    def scale_ratio(self):
        distance = []
        for i in self.good_matches:
            print(i[0].queryIdx,i[1].trainIdx)
            self.kp_source[]
