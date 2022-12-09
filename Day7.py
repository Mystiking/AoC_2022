import os
import sys
import numpy as np
from collections import defaultdict
import inspect
from typing import List


class Directory(object):
	name = None
	parent = None
	children = []
	size = 0

	def __init__(self, parent, name, size=0):
		self.parent = parent
		self.name = name
		self.children = []
		self.size = size

	def printTree(self, space = ""):
		print(space + self.name + ":" + str(self.size))
		for c in self.children:
			c.printTree(space + "\t")


def getDirectorySize(node):
	size = 0
	for c in node.children:
		if c.children == []:
			size += c.size
		else:
			size += getDirectorySize(c)
	return size

def getSubNodes(node, subNodes):
	for c in node.children:
		if c.children != []:
			subNodes.append(getDirectorySize(c))
	for c in node.children:
		if c.children != []:
			getSubNodes(c, subNodes)

	return subNodes


def getDirectorySizesCountOnce(node):
	size = node.size
	for c in node.children:
		if c.children != []:
			#print(c.size)
			size += getDirectorySizesCountOnce(c)
	return size

def computeDirSizes(node):
	for c in node.children:
		if c.children == []:  # i.e. not a directory
			node.size += c.size
		else:
			computeDirSizes(c)

def computeActualDirSizes(node):
	for c in node.children:
		if c.children == []:
			c.parent.size += c.size
		else:
			computeActualDirSizes(c)
			c.parent.size += c.size


if __name__ == '__main__':
	dataFileA = "./data/Day7_A.txt"
	dataFileB = "./data/Day7_B.txt"
	# Section A:
	with open(dataFileB) as fhA:
		lines = fhA.readlines()
		rootDir = Directory(None, "/")
		currentDir = rootDir
		for line in lines[1:]:
			tokens = line.replace('\n', '').split(" ")
			if tokens[0] == "$":
				# Command
				if tokens[1] == "ls":
					pass
				elif tokens[1] == "cd":
					#print(currentDir.name, currentDir.parent)
					if tokens[2] == "..":
						currentDir = currentDir.parent
					else:
						newDir = Directory(currentDir, tokens[2])
						currentDir.children.append(newDir)
						currentDir = newDir
			else: # We have just called "ls"
				if tokens[0] == "dir":
					pass
				else:
					currentDir.children.append(Directory(currentDir, tokens[1], int(tokens[0])))

#		rootDir.printTree()
		nodes = getSubNodes(rootDir, [getDirectorySize(rootDir)])
		print("answer", sum([n for n in nodes if n <= 100000]))
		space_used = nodes[0]
		space_needed = 30000000
		total_space = 70000000
		unused_space = total_space - space_used
		total_space_needed = space_needed - unused_space
		print("total space needed", space_needed - unused_space)
		print(nodes)
		for n in sorted(nodes):
			if n >= total_space_needed:
				print(n)
				break
#		print(getDirectorySizesCountOnce(rootDir))
		#computeDirSizes(rootDir)
		computeActualDirSizes(rootDir)
		nodes = getSubNodes(rootDir, [getDirectorySize(rootDir)])

		#rootDir.printTree()

		#size = rootDir.size
		#print(getDirectorySizesCountOnce(rootDir))



	# Section B:
	with open(dataFileA) as fhB:
		pass
