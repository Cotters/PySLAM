#!/usr/bin/env python3
import time
import cv2
from display import Display

W = 1920//2
H = 1080//2

d = Display(W,H)

if __name__ == "__main__":
	cap = cv2.VideoCapture("test.mp4")
	while cap.isOpened():
		ret, frame = cap.read()
		if ret == True:
			d.paint(frame)
		else:
			break
