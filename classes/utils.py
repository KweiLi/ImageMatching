import math
import numpy as np

def distance(pt1, pt2):
    math.sqrt((pt2[1]-pt1[1])^2+(pt2[0]-pt1[0])^2)

def aov(flen, ccd_dim):
    return 2*math.atan(ccd_dim/(flen*2))*180/math.pi

def d_mat(pts):
    d = []
    for i in xrange(len(pts)):
        x = i + 1
        while x<len(pts):
            dist = np.linalg.norm(np.array(pts[i])-np.array(pts[x]))
            d.append(dist)
            x = x+1
    return d
        