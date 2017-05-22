# -*- coding: utf-8 -*-
import sys

class Life:
	"""This is
	fucking LIFE"""
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.createEmptyGrid()
		self.run()

	def createEmptyGrid(self):
		self.grid = [[False for x in range(self.cols)] for y in range(self.rows)]

	def isAlive(self, row, col):
		return self.grid[row][col]

	def setAlive(self, row, col, tf):
		self.grid[row][col] = tf
		return

	def getNumRows(self):
		return self.rows

	def getNumCols(self):
		return self.cols

	def printCurrentState(self):
		output = ''
		for y, row in enumerate(self.grid):
			for x, cell in enumerate(row):
				if self.grid[y][x]:
					output += ' ⬛'
				else:
					output += ' ⬜'
			output += '\r'

		#print output
		sys.stdout.write(output)

	def run(self):
		self.printCurrentState()
		sys.stdout.flush()
		#sys.stdout.write("\r  \r")

	def runTimeStep(self):
		return

l = Life(2, 2)
#print l.grid
#'⬜'
