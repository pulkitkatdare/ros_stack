import imutils
import numpy as np

#
# Computes mean square error between two n-d matrices. Lower = more similar.
#
def meanSquareError(img1, img2):
	assert img1.shape == img2.shape, "Images must be the same shape."
	error = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
	error = error/float(img1.shape[0] * img1.shape[1] * img1.shape[2])
	return error

def compareImages(img1, img2):
	return 1/meanSquareError(img1, img2)


def pyramid(image, scale = 1.5, minSize = 30, maxSize = 1000):
	yield image
	while True:
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width = w)
		if(image.shape[0] < minSize or image.shape[1] < minSize):
			break
		if (image.shape[0] > maxSize or image.shape[1] > maxSize):
			continue
		yield image

def sliding_window(image, stepSize, windowSize):
	for y in xrange(0, image.shape[0], stepSize):
		for x in xrange(0, image.shape[1], stepSize):
			yield (x, y, image[y:y+windowSize[1], x:x+windowSize[1]])


import cv2
import time

def Stop_sign_detection(targetImage):
	prototypeImg = cv2.imread('/home/katdare2/Desktop/catkin_ws/src/mp0/src/stopPrototype.png')


	stop_sign_detect = False

	return stop_sign_detect
