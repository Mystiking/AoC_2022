import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day8_A.txt"
	dataFileB = "./data/Day8_B.txt"
	dataFileC = "./data/Day8_C.txt"
	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		numRows = len(lines)
		numCols = len(lines[0]) - 1
		grid = np.zeros((numRows, numCols), dtype=int)
		for li, l in enumerate(lines):
			grid[li] = [int(c) for c in l.replace('\n', '')]

		from_left_grid = np.zeros((numRows - 2, numCols - 2), dtype=int)
		from_right_grid = np.zeros((numRows - 2, numCols - 2), dtype=int)
		from_top_grid = np.zeros((numRows - 2, numCols - 2), dtype=int)
		from_bot_grid = np.zeros((numRows - 2, numCols - 2), dtype=int)
		print(numRows, numCols)
		# from left grid
		for row in range(1, numRows - 1):
			for col in range(1, numCols - 1):
				if col > 1:
					from_left_grid[row-1, col-1] = max(from_left_grid[row-1, col-2], grid[row, col-1])
				else:
					from_left_grid[row-1, col - 1] = grid[row, col - 1]
		# from right grid
		for row in range(1, numRows - 1):
			for col in range(numCols - 3, -1, -1):
				if col < numCols - 3:
					from_right_grid[row-1, col] = max(from_right_grid[row-1, col+1], grid[row, col+2])
				else:
					from_right_grid[row-1, col] = grid[row, col + 2]
		# from top
		for col in range(1, numCols - 1):
			for row in range(1, numRows - 1):
				if row > 1:
					from_top_grid[row - 1, col - 1] = max(from_top_grid[row-2, col-1], grid[row - 1, col])
				else:
					from_top_grid[row-1, col-1] = grid[row-1, col]
		# from bot
		for col in range(1, numCols - 1):
			for row in range(numRows - 3, -1, -1):
				if row < numRows - 3:
					from_bot_grid[row, col-1] = max(from_bot_grid[row+1, col-1], grid[row+2, col])
				else:
					from_bot_grid[row, col-1] = grid[row+2, col]

		# print(from_top_grid)
		# print(from_bot_grid)
		# print(from_left_grid)
		# print(from_right_grid)
		def stack(A):
			A = np.vstack([A, np.zeros((1, numCols - 2))])
			A = np.vstack([np.zeros((1, numCols - 2)), A])
			A = np.hstack([np.zeros((numRows, 1)), A])
			A = np.hstack([A, np.zeros((numRows, 1))])
			return A
		from_top_grid = stack(from_top_grid)
		from_bot_grid = stack(from_bot_grid)
		from_right_grid = stack(from_right_grid)
		from_left_grid = stack(from_left_grid)

		visible = np.zeros_like(grid)
		# Result
		numVisibleTrees = 0
		for row in range(1, numRows-1):
			for col in range(1, numCols-1):
				val = grid[row, col]

				if val > from_top_grid[row, col] or\
					val > from_bot_grid[row, col] or\
					val > from_left_grid[row, col] or\
					val > from_right_grid[row, col]:
					visible[row, col] = 1
					numVisibleTrees += 1
		numVisibleTrees += numRows * 2 + (numCols - 2) * 2
		print(numVisibleTrees)
		# Section B:
		def ScenicScore(row, col):
			val = grid[row, col]
			numTreesUp = 0
			if (row == 3 and col == 2):
				x = 0
			for r in range(row-1, -1, -1):
				if grid[r, col] < val:
					numTreesUp += 1
				elif grid[r, col] >= val:
					numTreesUp += 1
					break
				else:
					break
			numTreesDown = 0
			for r in range(row+1, numRows):
				if grid[r, col] < val:
					numTreesDown += 1
				elif grid[r, col] >= val:
					numTreesDown += 1
					break
				else:
					break
			numTreesLeft = 0
			for c in range(col-1, -1, -1):
				if grid[row, c] < val:
					numTreesLeft += 1
				elif grid[row, c] >= val:
					numTreesLeft += 1
					break
				else:
					break
			numTreesRight = 0
			for c in range(col+1, numCols):
				if grid[row, c] < val:
					numTreesRight += 1
				elif grid[row, c] >= val:
					numTreesRight += 1
					break
				else:
					break
			return numTreesRight * numTreesLeft * numTreesDown * numTreesUp

		scenic_grid = np.zeros_like(grid)
		for row in range(numRows):
			for col in range(numCols):
				sc = ScenicScore(row, col)
				#print(sc)
				scenic_grid[row, col] = sc
		print(scenic_grid.max())