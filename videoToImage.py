from datetime import timedelta
import cv2
import numpy as np
import os

infile = 'static/heroes/videos/muerta.webm'
outfile = 'static/heroes/images/muerta.jpg'
cap = cv2.VideoCapture(infile)
count = 0
is_read, frame = cap.read()
if is_read:
    cv2.imwrite(outfile, frame)
