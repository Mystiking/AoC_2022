import os
import sys
import numpy as np
from collections import defaultdict


if __name__ == '__main__':
	dataFileA = "./data/Day9_A.txt"
	dataFileB = "./data/Day9_B.txt"

	class Rope(object):

		def __init__(self):
			self.positions_covered = defaultdict(int)
			self.H = [0, 0]
			self.T = [0, 0]
			self.positions_covered[(self.T[0], self.T[1])] = 1

		def move(self, direction):
			secondaryMoves = []
			if direction == "R":
				self.H[1] += 1
				if self.isNotAdjacent():
					if self.T[0] == self.H[0]:  # Same row
						self.T[1] += 1
						secondaryMoves = ["R"]
					else:
						if self.T[0] > self.H[0]:
							secondaryMoves = ["R", "U"]
						else:
							secondaryMoves = ["R", "D"]
						self.T = [self.H[0], self.H[1] - 1]

			elif direction == "L":
				self.H[1] -= 1
				if self.isNotAdjacent():
					if self.T[0] == self.H[0]:  # Same row
						self.T[1] -= 1
						secondaryMoves = ["L"]
					else:
						if self.T[0] > self.H[0]:
							secondaryMoves = ["L", "U"]
						else:
							secondaryMoves = ["L", "D"]
						self.T = [self.H[0], self.H[1] + 1]
			elif direction == "U":
				self.H[0] += 1
				if self.isNotAdjacent():
					if self.H[1] == self.T[1]:  # Same column
						self.T[0] += 1
						secondaryMoves = ["U"]
					else:
						if self.T[1] > self.H[1]:
							secondaryMoves = ["U", "L"]
						else:
							secondaryMoves = ["U", "R"]
						self.T = [self.H[0] - 1, self.H[1]]
			elif direction == "D":
				self.H[0] -= 1
				if self.isNotAdjacent():
					if self.H[1] == self.T[1]:  # Same column
						self.T[0] -= 1
						secondaryMoves = ["D"]
					else:
						if self.T[1] > self.H[1]:
							secondaryMoves = ["D", "L"]
						else:
							secondaryMoves = ["D", "R"]
						self.T = [self.H[0] + 1, self.H[1]]
			self.positions_covered[(self.T[0], self.T[1])] = 1
			return secondaryMoves

		def isNotAdjacent(self):
			return abs(self.H[0] - self.T[0]) > 1 or abs(self.H[1] - self.T[1]) > 1

		def printState(self, dim):
			grid = [["." for _ in range(-dim, dim)] for _ in range(-dim, dim)]
			grid[self.H[0]][self.H[1]] = "H"
			grid[self.T[0]][self.T[1]] = "T"
			grid_string = ""
			for row in grid:
				rowString = ""
				for col in row:
					rowString += col + " "
				grid_string += rowString + "\n"
			print(grid_string)


	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		rope = Rope()
		for l in lines:
			tokens = l.replace('\n', '').split(' ')
			numMoves = int(tokens[1])
			direction = tokens[0]
			for i in range(numMoves):
				rope.move(direction)
				#rope.printState(6)
		print(len(rope.positions_covered.keys()))


	class BrokenRope(object):

		def __init__(self):
			self.positions_covered = defaultdict(int)
			self.ropes = [Rope() for _ in range(9)]
			self.positions_covered[(self.ropes[-1].T[0], self.ropes[-1].T[1])] = 1  # Only by end of tail

		def move_tail(self, ropeIndex):
			# if is in same column, follow
			if not self.isNotAdjacent(ropeIndex):
				return
			r = self.ropes[ropeIndex]
			if r.H[1] == r.T[1]:
				if r.H[0] > r.T[0]:
					r.T[0] = r.H[0] - 1
				elif r.H[0] < r.T[0]:
					r.T[0] = r.H[0] + 1
			elif r.H[0] == r.T[0]:
				if r.H[1] > r.T[1]:
					r.T[1] = r.H[1] - 1
				elif r.H[1] < r.T[1]:
					r.T[1] = r.H[1] + 1
			else:
				# We need to perform a diagonal move
				if r.H[1] > r.T[1]:
					r.T[1] = r.T[1] + 1
				elif r.H[1] < r.T[1]:
					r.T[1] = r.T[1] - 1
				if r.H[0] > r.T[0]:
					r.T[0] = r.T[0] + 1
				elif r.H[0] < r.T[0]:
					r.T[0] = r.T[0] - 1
			self.ropes[ropeIndex] = r

		def move(self, direction):
			self.ropes[0].move(direction)
			for i in range(1, len(self.ropes)):
				self.ropes[i].H = self.ropes[i-1].T
				self.move_tail(i)

			self.positions_covered[(self.ropes[-1].T[0], self.ropes[-1].T[1])] = 1  # Only end of tail

		def isNotAdjacentToHead(self):
			return abs(self.H[0] - self.T[0][0]) > 1 or abs(self.H[1] - self.T[0][1]) > 1

		def isNotAdjacent(self, index):
			return abs(self.ropes[index].T[0] - self.ropes[index].H[0]) > 1 or abs(self.ropes[index].T[1] - self.ropes[index].H[1]) > 1

		def isDiagonalTo(self, index):
			return abs(self.T[index - 1][0] - self.T[index][0]) == 1 and abs(self.T[index-1][1] - self.T[index][1]) == 1

		def printState(self, dim):
			grid = [["." for _ in range(-dim, dim)] for _ in range(-dim, dim)]
			grid[self.ropes[0].H[0]][self.ropes[0].H[1]] = "H"
			grid[self.ropes[-1].T[0]][self.ropes[-1].T[1]] = "9"
			for ti in range(8, -1, -1):
				t = self.ropes[ti].H
				grid[t[0]][t[1]] = str(ti+1)

			grid_string = ""
			for row in grid:
				rowString = ""
				for col in row:
					rowString += col + " "
				grid_string += rowString + "\n"
			print(grid_string)

	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		rope = BrokenRope()
		for l in lines:
			tokens = l.replace('\n', '').split(' ')
			numMoves = int(tokens[1])
			direction = tokens[0]
			#print(l)
			for i in range(numMoves):
				rope.move(direction)
				#rope.printState(10)
		print(len(rope.positions_covered.keys()))
