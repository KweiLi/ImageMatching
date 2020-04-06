import math
def distance(pt1, pt2):
    math.sqrt((pt2[1]-pt1[1])^2+(pt2[0]-pt1[0])^2)

def aov(flen, ccd_dim):
    return 2*math.atan(ccd_dim/(flen*2))

    