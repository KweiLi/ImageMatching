from classes import utils, image
import numpy as np,os

absolute_path = os.path.join(os.getcwd(), 'data-image', 'data')

img = image.Image()
keys =img.metadata(absolute_path+ "/sofa_query.jpeg")
print([i for i in keys])
img.read(absolute_path+ "/sofa_query.jpeg")
print(img.gray)
print(np.shape(img.gray))