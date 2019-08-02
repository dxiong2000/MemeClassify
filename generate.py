"""
generate.py
generate training data using images in /templates/
"""

import numpy as np
import cv2
import os

MEME_PATH = "templates"
SCALE_SIZE = (2118, 2825)


def generate():

    meme_array = []
    for meme in os.listdir(MEME_PATH):
        img_array = cv2.imread(os.path.join(MEME_PATH, meme))
        scaled = cv2.resize(img_array, SCALE_SIZE)

        # stores scaled image and meme name without .jpg extension
        meme_array.append([scaled, meme[:-4]])

    return meme_array
