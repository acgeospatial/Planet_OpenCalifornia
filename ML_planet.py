#!/usr/bin/python
# -*- coding: utf-8 -*-
## Written by Andrew Cutts (unless stated above)

''' This code has been adapted from this video
https://youtu.be/KTeVOb8gaD4 please do check it out for more about SVM
and slso from
https://github.com/acgeospatial/SVM_digits/blob/master/SVM_pi.py

The sort method is taken from
https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python/12093993
'''


import matplotlib.pyplot as plt
import scipy.ndimage
import numpy as np
from sklearn import svm
#from sklearn.ensemble import RandomForestClassifier
import glob
from skimage import io
import os
import re
import pandas as pd
### path to data containing the labels for points
file = "../file_in.csv"
## read in the csv using pandas and create list
df = pd.read_csv(file)
flat_list = df['id'].tolist()


data = []
### helper method for sorting through the images in correct numerical order
## https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python/12093993
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

## loop through the the clipped rasters and read in with correct order using io.imread
for infile in sorted(glob.glob('D:/los_angeles/attempt5/*.jpg'), key=numericalSort):
	### print to make sure the correct order is being read
    #print "Current File Being Processed is: " + infile
    image = io.imread(infile)
    data.append(image)
		
## reshape the data 
dataset_size = len(data)
TwoDim_dataset = np.array(data).reshape(dataset_size,-1)

## the classifier (support vector machines)
clf=svm.SVC(gamma=0.0001, C=100)

## You could use RandomForestClassifier or any other ensemble method, will need import at top
## update 3rd Sept 2017 - I have found using RandomForestClassifer to be a significant improvement
#clf = RandomForestClassifier(n_estimators=500)

## the size of the data (everything minus the last 10 records)
x,y = TwoDim_dataset[:-10], flat_list[:-10]
## fit the data
clf.fit(x,y)

## Counter for number of correct predictions
count = 0

## build a dictionary of terrain/landuse types
d = {1:'Water', 2: 'Scrubland', 3: 'Building', 4: 'Road', 5: 'Trees', 6: 'Shadows', 7:'Grass'}

for i in range(0,10):
	## predict each one
	x = (clf.predict(TwoDim_dataset[[-i]]))
	print 'prediction: ', clf.predict(TwoDim_dataset[[-i]])
	print 'labelled: ' , flat_list[-i]
	label =  "Terrain type labelled: ", d[flat_list[-i]]
	pred =  "Predicted terrain: ", d[x.item(0)]
	value = x.item(0) == flat_list[-i]
	if value == True:
		count += 1
		sucess = 'correct prediction!'
	if value == False:
		sucess = 'incorrect prediction'
	## plot each one
	plt.imshow(data[-i], cmap=plt.cm.gray_r, interpolation="nearest")
	plt.annotate(label, (0,0), (0, 375), xycoords='axes fraction', textcoords='offset points', va='top')
	plt.annotate(pred, (0,0), (0, 360), xycoords='axes fraction', textcoords='offset points', va='top')
	plt.annotate(sucess, (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
	plt.show()
	
print "out of 10 samples " + str(count) + " were correct"
