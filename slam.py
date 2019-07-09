#!/usr/bin/env python3
import time
import cv2
from display import Display
from extractor import Extractor
import numpy as np

W = 1920//2
H = 1080//2
disp = Display(W,H)

F = 1
K = np.array([[F,0,W//2],[0,F,H//2],[0,0,1]])
# using W//3.9 and H//1.2 works
#K = np.array([[F,0,0],[0,F,0],[0,0,1]])

fe = Extractor(K)

def process_frame(img):
	img = cv2.resize(img, (W,H))
	matches = fe.extract(img)
	
	for pt1, pt2 in matches:
		# denormalise for display
		u1,v1 = fe.denormalise(pt1)
		u2,v2 = fe.denormalise(pt2)
		#u1,v1 = map(lambda x: int(round(x)), pt1)
		#u2,v2 = map(lambda x: int(round(x)), pt2)

		cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
		cv2.line(img, (u1, v1), (u2, v2), color=(255,0,0))

	disp.paint(img)

if __name__ == "__main__":
	cap = cv2.VideoCapture("test.mp4")
	while cap.isOpened():
		ret, frame = cap.read()
		if ret == True:
			process_frame(frame)
		else:
			break
