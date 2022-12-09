import os
import sys
import numpy as np
from collections import defaultdict
import inspect
from typing import List

class Tree(object):
	parent = None
	name = None
	size = 0
	leaves = []

	def __init__(self, parent, name, size=0):
		self.parent = parent
		self.name = name
		self.leaves = []
		self.size = size

	def add_leaf(self, leaf, size):
		self.leaves.append(leaf)

	def has_child(self, name):
		for l in self.leaves:
			if l.name == name:
				return True
			else:
				l.has_child(name)
		return False

	def get_child(self, name, parentName):
		for l in self.leaves:
			if l.name == name and l.parent == parentName:
				return l
			else:
				child = l.get_child(name, parentName)
				if not (child is None):
					return child
		return None

	def add_leaf_to_child(self, leaf, child):
		for l in self.leaves:
			if l.name == child:
				l.leaves.append(leaf)
			else:
				l.add_leaf_to_child(leaf, child)

	def printTree(self, space):
		print(space + self.name + " " + str(self.size))
		for l in self.leaves:
			l.printTree(space + "\t")

	def get_size_of_dir(self, name, parentName):
		dirRoot = self if name == self.name else self.get_child(name, parentName)
		# if name == "2wzpth":
		# 	x = 0
		if dirRoot is None:
			return 0
		if dirRoot.leaves == []:
			return dirRoot.size

		dirSize = 0
		for l in dirRoot.leaves:
			if l.leaves == []:
				dirSize += l.size
			else:
				dirSize += dirRoot.get_size_of_dir(l.name, dirRoot.name)
		return dirSize



if __name__ == '__main__':
	dataFileA = "./data/Day7_A.txt"
	dataFileB = "./data/Day7_B.txt"
	# Section A:
	with open(dataFileA) as fhA:
		lines = fhA.readlines()
		fileTree = Tree(None, "/")
		'''
		fileTree.add_leaf(Tree("/", "a"), 0)
		fileTree.add_leaf(Tree("/", "b"), 0)
		fileTree.add_leaf(Tree("/", "c"), 100)

		fileTree.printTree("")
		fileTree.add_leaf_to_child(Tree("a", "d"), "a")
		fileTree.printTree("")
		'''
		dirs = set()
		depth = 0
		incrementer = 0
		currentDir = "/"
		#dirs.add(currentDir)
		dirOccs = defaultdict(int)
		currentNode = fileTree
		oldParent = "/"
		for line in lines[1:]:  # We know line 1 is cd /
			tokens = line.replace('\n', '').split(' ')
			if tokens[0] == "$":
				#fileTree.printTree("")
				if tokens[1] == "ls":
					pass
				elif tokens[1] == "cd":
					if tokens[2] != "..":
						depth += 1
						nextDir = tokens[2]
						if str(depth) + nextDir == "2d":
							x = 0
						newTree = Tree(currentNode.name, str(depth) + nextDir)
						if nextDir == "i":
							v = 0
						if depth > 1:
							fileTree.get_child(currentNode.name, currentNode.parent).add_leaf(newTree, 0)
						else:
							fileTree.add_leaf(newTree, 0)
						oldParent = currentNode.parent
						currentNode = newTree
						#currentDir = str(depth) + nextDir

						dirs.add((currentNode.name, currentNode.parent))
						dirOccs[(currentNode.name, currentNode.parent)] += 1
					else:
						depth -= 1
						#print(currentDir, currentNode.parent)
						#fileTree.printTree("")
						currentNode = fileTree.get_child(currentNode.parent, oldParent)#fileTree.get_child(currentDir, currentNode.parent).parent
						if currentNode is None:
							print("oldP:", oldParent)
						else:
							print("P", currentNode.parent, "oldP:", oldParent)

			else:  # "ls" must have just been called
				if currentNode.name == "/":
					if tokens[0] != "dir":
						if tokens[1] == "i":
							v = 0
						newTree = Tree(currentNode.name, tokens[1], int(tokens[0]))
						fileTree.add_leaf(newTree,  int(tokens[0]))
				else:
					if tokens[0] != "dir":
						if tokens[1] == "i":
							v = 0
						newTree = Tree(currentDir, tokens[1], int(tokens[0]))
						child = fileTree.get_child(currentNode.name, currentNode.parent)
						fileTree.get_child(currentNode.name, currentNode.parent).add_leaf(newTree, int(tokens[0]))

		fileTree.printTree("")
		validsums = []

		for d in dirs:
			tsize = fileTree.get_size_of_dir(d[0], d[1])
			if tsize == 0:
				print(d)
			#print(d, "size", tsize)
			if tsize <= 100000:
				validsums.append(tsize)
		print((validsums))
		print(sum(validsums))
		#print(dirOccs)
		for d in dirOccs:
			if dirOccs[d] > 1:
				#print(d, dirOccs[d])
				pass







	# Section B:
	with open(dataFileA) as fhB:
		pass
