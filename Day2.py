import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day2_A.txt"
	dataFileB = "./data/Day2_B.txt"

	rules = {'X' : 1, 'A': 1, 'Y' : 2, 'B' : 2, 'Z' : 3, 'C' : 3}
	points = [0, 3, 6]  # loss, draw, win + shape


	win = [1, 2, 3, 1]
	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		rounds = np.array([[int(rules[l.split(' ')[0]]), int(rules[l.split(' ')[1].replace('\n', '')])] for l in lines])
		points = 0
		for r in rounds:
			points += r[1]
			loses_to = win[r[1]]
			if r[0] == r[1]:
				points += 3
			elif r[0] != loses_to:
				points += 6
		print(points)

	# Section B:
	new_win = { 1 : 0, 2 : 3, 3 : 6}
	loses_to = [3, 1, 2]
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		rounds = np.array([[int(rules[l.split(' ')[0]]), int(rules[l.split(' ')[1].replace('\n', '')])] for l in lines])
		points = 0
		for r in rounds:
			points_this_round = new_win[r[1]]
			this_round = 0
			if points_this_round == 0:
				this_round += loses_to[r[0]-1]
			elif points_this_round == 3:
				this_round += r[0]
			else:
				this_round += win[r[0]]
			#print(this_round, points_this_round, points)
			points += this_round + points_this_round
			#print(this_round, points_this_round, points)

		print(points)
