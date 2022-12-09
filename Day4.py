import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day4_A.txt"
	dataFileB = "./data/Day4_B.txt"
	# Section A:
	def isContainedInside(rA, rB):
		return rA[0] >= rB[0] and rA[1] <= rB[1]

	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		overlaps = 0
		for l in lines:
			rA = l.split(',')[0]
			rB = l.split(',')[1]
			rA = [int(rA.split('-')[0]), int(rA.split('-')[1])]
			rB = [int(rB.split('-')[0]), int(rB.split('-')[1])]
			if isContainedInside(rA, rB) or isContainedInside(rB, rA):
				overlaps += 1

		print(overlaps)

	def isContainedInside(rA, rB):
		As = list(range(rA[0], rA[1]+1))
		Bs = list(range(rB[0], rB[1]+1))
		for a in As:
			if a in Bs:
				return True
		return False
	#...123...
	#.....345
	#......4..
	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		overlaps = 0
		for l in lines:
			rA = l.split(',')[0]
			rB = l.split(',')[1]
			rA = [int(rA.split('-')[0]), int(rA.split('-')[1])]
			rB = [int(rB.split('-')[0]), int(rB.split('-')[1])]
			if isContainedInside(rA, rB):
				overlaps += 1

		print(overlaps)
