from sklearn.metrics import mean_squared_error
import numpy as np
from scipy import average
from generate import generate_exemplars
from generate import generate_test_data
import cv2

def distance(exemplar, input):
    return mean_squared_error(exemplar, input)

def one_nearest_neighbor(input):
    """
    :param input: meme to be classified
    :return: list of distances of the meme to each class
    """
    dists = []
    exemplars = generate_exemplars()

    # convert input image into 2D array of intensities
    input = average(input, -1)

    for meme in exemplars:
        # extract image and class from exemplar
        img = meme["img"]
        cls = meme["class"]
        # convert exemplar image into 2D array of intensities
        img = average(img, -1)
        # calculate difference in intensities
        d = distance(img, input)
        dists.append((d, cls))

    # sort by least distance and return list
    dists.sort()
    return dists

img = cv2.imread("test1.jpg")
img = cv2.resize(img, (500, 750))
dists = one_nearest_neighbor(img)

print(dists[0])
