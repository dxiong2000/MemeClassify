"""
generate.py
generate training data using images in /templates/
"""

import numpy as np
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import cv2
import os
import argparse

chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


class GenerateMeme:

    def __init__(self, batch_size):
        # do stuff



