from classes import estimater, image, utils
import math
import os, functools

absolute_path = os.path.join(os.getcwd(), 'data-image', 'data')

img1 = image.Image()
img1.read(absolute_path+ "/sofa_query.jpeg")

for i in range(1,7):
    name = "/sofa"+str(i)+".jpeg"
    img2 = image.Image()
    img2.read(absolute_path+ name)
    es = estimater.Estimater(img1)

    pts = es.confidence(img2)
    sh = list(img2.shape)

    score = 0 
    for x in xrange(len(pts)):
        score = score + math.exp((-( (pts[x][0]-sh[1]) **2+ (pts[x][1]-sh[0]) **2))/100000)

    print(name, len(pts), score)