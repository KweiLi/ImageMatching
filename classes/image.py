import cv2 as cv
import exifread

class Image(object):
    def __init__(self):
        self.color= []
        self.gray = []
        self.kp = []
        self.des = []

    def read(self, path):
        self.color = cv.imread(path)
        self.gray= cv.cvtColor(self.color,cv.COLOR_BGR2GRAY)

    def kp_sift(self):
        sift = cv.xfeatures2d.SIFT_create()
        self.kp, self.des = sift.detectAndCompute(self.gray,None)
        return self.kp, self.des

    def kp_surf(self):
        surf = cv.xfeatures2d.SURF_create()
        self.kp, self.des = surf.detectAndCompute(self.gray,None)
        return self.kp, self.des

    def metadata(self,path):
        f = open(path, 'rb')
        tags = exifread.process_file(f)
        return tags