import os
import sys
import numpy as np
from collections import defaultdict

DATA = "./data/"

if __name__ == '__main__':
	dataFileA = "./data/Day1_A.txt"
	dataFileB = "./data/Day1_B.txt"
	sums = {}
	# Section A:
	with open(dataFileA) as fhA:
		lines = fhA.readlines()
		nextElf = 0
		currentCals = 0
		for l in lines:
			if l == "\n":
				sums[nextElf] = currentCals
				currentCals = 0
				nextElf = nextElf + 1
			else:
				cals = int(l)
				currentCals += cals
		sums[nextElf] = currentCals
		print(max(sums.values()))



	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		nextElf = 0
		currentCals = 0
		for l in lines:
			if l == "\n":
				sums[nextElf] = currentCals
				currentCals = 0
				nextElf = nextElf + 1
			else:
				cals = int(l)
				currentCals += cals
		if currentCals != 0:
			sums[nextElf] = currentCals
		print(sum(sorted(sums.values(), reverse=True)[:3]))

