from classes import image
import os

class Database(object):

    def __init__(self, path):
        self.path = path
        self.database = dict()

    def create_database_sift(self):
        for filename in os.listdir(self.path):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                file_path = self.path + "/" + filename
                img = image.Image()
                img.read(file_path)
                kp, des = img.kp_sift()
                self.database[filename] = {"kp": kp, "des": des}
    
    def create_database_surf(self):
        for filename in os.listdir(self.path):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                file_path = self.path + "/" + filename
                img = image.Image()
                img.read(file_path)
                kp, des = img.kp_surf()
                self.database[filename] = {"kp": kp, "des": des}
                