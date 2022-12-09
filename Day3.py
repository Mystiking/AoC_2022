import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day3_A.txt"
	dataFileB = "./data/Day3_B.txt"

	score = {}

	letters = 'abcdefghijklmnopqrstuvwxyz'
	for li, l in enumerate(letters):
		score[l] = li + 1
		score[l.upper()] = li + 27

	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		rucksackCompartments = []
		sum = 0
		for l in lines:
			l = l.replace('\n', '')
			rucksackCompartments = [l[:int(len(l)/2)], l[int(len(l)/2):]]
			for rItem in rucksackCompartments[0]:
				if rItem in rucksackCompartments[1]:
					sum += score[rItem]
					break

		print(sum)


	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		rucksackCompartments = []
		sum = 0
		for i in range(0, len(lines), 3):
			l0 = lines[i]
			l1 = lines[i+1]
			l2 = lines[i+2]
			l0 = l0.replace('\n', '')
			l1 = l1.replace('\n', '')
			l2 = l2.replace('\n', '')

			items = defaultdict(int)
			for c in set(l0):
				items[c] += 1
			for c in set(l1):
				items[c] += 1
			for c in set(l2):
				items[c] += 1
			for k in items.keys():
				if items[k] == 3:
					sum += score[k]

		print(sum)