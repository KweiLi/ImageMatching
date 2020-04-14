from classes import image,database,matcher
import os
import cv2
import time

absolute_path = os.path.join(os.getcwd(), 'data-image', 'data')
database = database.Database(absolute_path)
database.create_database_sift()

start = time.time()
img = image.Image()
img.read("hallway2.jpeg")
kp, des = img.kp_sift()

matched = {"name":"", "num": 0}

matches = matcher.Matcher()
for i in database.database:
    good_matches = matches.bf(des, database.database[i]["des"])
    if len(good_matches) > matched["num"]:
        matched["num"] = len(good_matches)
        matched["name"] = i

print(matched)
print(time.time()-start)