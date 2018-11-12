# Copyright (c) 2018  Michael C. Tiberio  All rights reserved.

import csv

def write_data(filename, frames, dt, dx, dy, precision = None):
	have_precision = isinstance(precision, int)
	if have_precision:
		format = '{{:.{}e}}'.format(precision + 1)
	else:
		format = '{}e'

	with open(filename, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
		
		line1 = [ 'mctField      ',
		          '00.00.01',
		          'TEXT  ' ]
		line2 = [ 'grid_source=CALCULATED' ]
		line3 = [ 'algorithm=cartesian2d',
		          'x_count={}'.format(len(frames[0])),
		          'y_count={}'.format(len(frames[0][0])),
		          'dx={}'.format(dx),
		          'dy={}'.format(dy) ]
		line4 = [ 'format=csv',
		          'data_type=float1',
		          'time_steps=' + str(len(frames)),
		          'dt={}'.format(dt) ]

		if have_precision:
			line4.insert(2, 'precision={}'.format(precision))

		writer.writerows([line1, line2, line3, line4 , []]) # blank line at end

		for frame in frames:
			writer.writerow([(format.format(y)) for x in frame for y in x])

if __name__ == '__main__':
	import numpy as np
	CSV_FILE = r'C:\src\modeling\output\small_data.csv'

	def f(t, x, y):
		m = (x*10.0+y*100.0+1)*np.pi
		e = ((t-2.5))
		r = np.power(m, e)
		return r

	#data = [[[x for y in range(3)] for x in range(4)] for t in range(5)]
	#data = [[[y for y in range(3)] for x in range(4)] for t in range(5)]
	#data = [[[t for y in range(3)] for x in range(4)] for t in range(5)]
	data = [[[f(t, x, y) for y in range(3)] for x in range(4)] for t in range(5)]
	write_data(CSV_FILE, np.array(data, dtype=float), dt = 0.01, dx = 0.15, dy = 0.2, precision = 3)

	# Ensure that the array is in the correct form
	#for t in range(5):
	#	for x in range(4):
	#		for y in range(3):
				#assert (data[t][x][y] == x)
				#assert (data[t][x][y] == y)
				#assert (data[t][x][y] == t)
