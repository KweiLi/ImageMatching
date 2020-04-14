from classes import image,database,matcher
import cv2, time, os

start = time.time()
absolute_path = os.path.join(os.getcwd(), 'data-image', 'data')
database = database.Database(absolute_path)
database.create_database_sift()
print(time.time()-start)

for i in range(7,10):
    img = image.Image()
    img.read(absolute_path+"/stairs"+str(i)+".jpeg")
    kp, des = img.kp_sift()

    matched = {"name":"", "num": 0}

    matched_temp= {}

    matches = matcher.Matcher()
    for i in database.database:
        good_matches = matches.flann(des, database.database[i]["des"])
        if len(good_matches) > matched["num"]:
            matched_temp["name"] = matched["name"]
            matched_temp["num"] = matched["num"]
            matched["num"] = len(good_matches)
            matched["name"] = i
    print(matched_temp, matched)


for i in range(12,21):
    img = image.Image()
    img.read(absolute_path+"/living"+str(i)+".jpeg")
    kp, des = img.kp_sift()

    matched = {"name":"", "num": 0}

    matched_temp= {}

    matches = matcher.Matcher()
    for i in database.database:
        good_matches = matches.flann(des, database.database[i]["des"])
        if len(good_matches) > matched["num"]:
            matched_temp["name"] = matched["name"]
            matched_temp["num"] = matched["num"]
            matched["num"] = len(good_matches)
            matched["name"] = i
    print(matched_temp, matched)