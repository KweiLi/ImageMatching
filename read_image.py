from classes import utils, image
import numpy as np

img = image.Image()
keys =img.metadata("bottle_query.jpeg")
print([i for i in keys])
img.read("bottle_query.jpeg")
print(img.gray)
print(np.shape(img.gray))