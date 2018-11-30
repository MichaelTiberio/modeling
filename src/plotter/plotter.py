# Copyright (c) 2018  Michael C. Tiberio  All rights reserved.

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import datafile

# Download ffmpeg from their website. It is an xcopy install on Windows. DO NOT USE pip!!!
plt.rcParams['animation.ffmpeg_path'] = r'C:\Software\ffmpeg\bin\ffmpeg.exe'

# Parameters to control the simulation.
X = 100
Y = 100
T = 500

# Fully qualified output file for writing the movie to.
PATH       = r'C:\src\modeling\output'
MOVIE_FILE = PATH + r'\movie.mp4'
CSV_FILE   = PATH + r'\data.csv'

# Plot a single frame.
#		frame: The data to plot.
def show_plot(frame):
	print('Preparing frame.\n')
	plt.pcolormesh(frame)
	plt.show()

# Plot out an entire animation.
#		frames: The data to plot.
#		target: The destination
#			'anim': On screen animation.
#			'file': Write to file specified in FILENAME
def show_movie(frames, target):
	print('Preparing animation.\n\ttarget:', target, '\n')
	fig = plt.figure()
	ims = []
	for frame in frames:
	    im = plt.imshow(frame, animated=True)
	    ims.append([im])

	ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)#, repeat_delay=1000)
	
	if target == 'anim':
		plt.show()
	elif target == 'file':
		print('Writing to file:', FILENAME, '\n')
		writer = animation.FFMpegWriter()
		ani.save(MOVIE_FILE, writer)

# The function to plot.
def f(t, x, y):
	return np.sin(x/10 - t/10*np.pi) + np.sin(y/5 + t*x/20*np.pi)

# Build a single frame of f() at time t. x and y range over X and Y, respectfully.
def build_static_frame(t):
	return [[f(t, x, y) for y in range(Y)] for x in range(X)]

# Build all the frames for the entire anumation. The time ranges over T.
def build_movie_frames():
	return [build_static_frame(t) for t in range(T)]

# main function
#		plot_type:
#			'frame': A single static frame.
#			'movie': An animated movie.
#		param: Interpretation is dependent on plot_type
#			for 'frame': An integer that represents the time t at which to generate the frame.
#			for 'movie': The target of the rendered plot. See target parameter on show_movie().
def main(plot_type, param):
	print('Preparing data to plot.\n\tplot_type:', plot_type, '\n\tparam:', param, '\n')
	if plot_type == 'frame':
		show_plot(np.array(build_static_frame(param), dtype=float))
	elif plot_type == 'movie':
		show_movie(np.array(build_movie_frames(), dtype=float), param)
	print('Complete.\n')

if __name__ == '__main__':
	#main('frame', 100)
	#main('movie', 'anim')
	#main('movie', 'file')
	datafile.write_data(CSV_FILE, np.array(build_movie_frames(), dtype=float))
 