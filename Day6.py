import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day6_A.txt"
	dataFileB = "./data/Day6_B.txt"
	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()

		for l in lines:
			chars = set([])
			count = 0
			prevSetSize = 0

			for i in range(0, len(l)):
				marker = set(l[i:i+4])
				if len(marker) == 4:
					print(i+4)
					break

	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()

		for l in lines:
			chars = set([])
			count = 0
			prevSetSize = 0

			for i in range(0, len(l)):
				marker = set(l[i:i + 14])
				#print(marker)
				if len(marker) == 14:
					print(i + 14)
					break
