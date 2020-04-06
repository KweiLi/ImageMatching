from classes import image, matcher, database
import os


class Tester(object):
    def __init__(self, database):
        self.database = database
        pass

    def match_test(self, path, name):
        img = image.Image()
        img.read(path)
        kp, des = img.kp_sift()

        matched = {"name":"", "num": 0}

        matches = matcher.Matcher()
        for i in self.database:
            good_matches = matches.flann(des, self.database[i]["des"])
            if len(good_matches) > matched["num"]:
                matched["num"] = len(good_matches)
                matched["name"] = i

        return matched["name"] == name