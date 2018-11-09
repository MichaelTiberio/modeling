# Copyright (c) 2018  Michael C. Tiberio  All rights reserved.

import csv

def write_data(filename, frames):
	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
		writer.writerows([['mctData', 'version=0.1'],
		                  ['grid_source=CALCULATED'],
		                  ['algorithm=2d_cartesian', 'x_count=' + str(len(frames[0])), 'y_count=' + str(len(frames[0][0])), 'dx=0.1', 'dy=0.1'],
		                  ['format=csv', 'time_steps=' + str(len(frames)), 'dt=0.01'],
		                  []]) # blank line

		for frame in frames:
			writer.writerow([y for x in frame for y in x])

if __name__ == '__main__':
	import numpy as np
	CSV_FILE = r'C:\src\plotter\output\small_data.csv'

	#data = [[[x for y in range(3)] for x in range(4)] for t in range(5)]
	#data = [[[y for y in range(3)] for x in range(4)] for t in range(5)]
	#data = [[[t for y in range(3)] for x in range(4)] for t in range(5)]
	data = [[[(t+x*10+y*100) for y in range(3)] for x in range(4)] for t in range(5)]
	write_data(CSV_FILE, np.array(data, dtype=float))

	# Ensure that the array is in the correct form
	#for t in range(5):
	#	for x in range(4):
	#		for y in range(3):
				#assert (data[t][x][y] == x)
				#assert (data[t][x][y] == y)
				#assert (data[t][x][y] == t)
