import os
import sys
import numpy as np
from collections import defaultdict

if __name__ == '__main__':
	dataFileA = "./data/Day5_A.txt"
	dataFileB = "./data/Day5_B.txt"
	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		stack_drawing = []
		moves = []
		now_moves = False
		for l in lines:
			if l == '\n':
				now_moves = True
				continue
			if now_moves:
				moves.append(l)
			else:
				stack_drawing.append(l)

		# Creating the stack
		stackNumbers = [int(sn.replace('\n', '')) for sn in stack_drawing[-1].split(" ") if sn != '' and sn != '\n']
		stacks = {}
		for sn in stackNumbers:
			stacks[sn] = []
		stackValues = []
		for sd in stack_drawing[:-1]:
			l = sd.split('[')
			#print(l)
			nextIndex = 1
			for li, c in enumerate(l):
				c_good = c.replace(']', '').replace('\n', '')
				#print(c_good)
				if len(c_good) == 0:
					continue
				if c_good[0] == ' ':
					nextIndex += len(c_good) // 4
				else:
					stacks[nextIndex].append(c_good.replace(' ', ''))
					nextIndex += max(1, len(c_good) // 4 + 1)
		for s in stacks.keys():
			stacks[s] = list(reversed(stacks[s]))

		for m in moves:
			tokens = m.split(' ')
			qty = int(tokens[1])
			stack_from = int(tokens[3])
			stack_to = int(tokens[-1].replace('\n', ''))
			for q in range(qty):
				v = stacks[stack_from].pop()
				stacks[stack_to].append(v)

		res = ""
		for s in stacks.keys():
			res += stacks[s].pop()
		print(res)


	# Section B:
	with open(dataFileB) as fhB:
		lines = fhB.readlines()
		stack_drawing = []
		moves = []
		now_moves = False
		for l in lines:
			if l == '\n':
				now_moves = True
				continue
			if now_moves:
				moves.append(l)
			else:
				stack_drawing.append(l)

		# Creating the stack
		stackNumbers = [int(sn.replace('\n', '')) for sn in stack_drawing[-1].split(" ") if sn != '' and sn != '\n']
		stacks = {}
		for sn in stackNumbers:
			stacks[sn] = []
		stackValues = []
		for sd in stack_drawing[:-1]:
			l = sd.split('[')
			# print(l)
			nextIndex = 1
			for li, c in enumerate(l):
				c_good = c.replace(']', '').replace('\n', '')
				# print(c_good)
				if len(c_good) == 0:
					continue
				if c_good[0] == ' ':
					nextIndex += len(c_good) // 4
				else:
					stacks[nextIndex].append(c_good.replace(' ', ''))
					nextIndex += max(1, len(c_good) // 4 + 1)
		for s in stacks.keys():
			stacks[s] = list(reversed(stacks[s]))

		for m in moves:
			tokens = m.split(' ')
			qty = int(tokens[1])
			stack_from = int(tokens[3])
			stack_to = int(tokens[-1].replace('\n', ''))
			#print(qty, stack_from, stack_to)
			v = []
			for q in range(qty):
				v.append(stacks[stack_from].pop())
			for vi in reversed(v):
				stacks[stack_to].append(vi)
			#print(stacks)

		res = ""
		for s in stacks.keys():
			res += stacks[s].pop()
		print(res)

