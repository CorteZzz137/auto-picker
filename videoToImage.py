import cv2
import os

in_folder = 'public/heroes/videos/'
out_folder = 'public/heroes/images/'
names = []
for root, dirs, files in os.walk(in_folder):
    for filename in files:
        names.append(filename.split('.webm')[0])

for name in names:
    cap = cv2.VideoCapture(in_folder + name + '.webm')
    is_read, frame = cap.read()
    if is_read:
        cv2.imwrite(out_folder + name + '/avatar.jpg', frame)
