import argparse
import csv
import string

parser = argparse.ArgumentParser(description='Welcome to a humble version of Conway\'s Game of Life. Enjoy!')
parser.add_argument('-f', '--file', help='Path or filename for your .csv configuration file. Defaults to "Blinker.csv".', default='Blinker.csv')
args = parser.parse_args()

class Cycle:

	num_cols = 0
	num_rows = 0
	prevState = []

	def __init__(self, stateFile):
		self.stateFile = stateFile
		self.loadStateFromFile()
		try:
			while(True):
				self.parcour()
		except KeyboardInterrupt:
			pass

	def loadStateFromFile(self):
		with open(self.stateFile, 'r') as csvfile:
			readerObject = csv.reader(csvfile, delimiter=',')
			for row in readerObject:
				if self.num_cols == 0: self.num_cols = len(row)
				self.num_rows += 1
				self.prevState.append(map(int, row))

	def parcour(self):
		# We assume a new, empty state the same size
		self.nextState = None
		self.nextState = [[0 for y in range(self.num_rows)] for x in range(self.num_cols)]
		for y, row in enumerate(self.prevState):
			for x, cell in enumerate(row):
				"""
				a List of all eight neighbors,
				ordered clockwise from top left:
				0 1 2
				7 c 3
				6 5 4
				"""
				neighbors = None
				neighbors = [0] * 8
				# We determine the neighbors' respective
				# state, case by case.
				# first
				if y - 1 < 0 or x - 1 < 0:
					neighbors[0] = 0
				else:
					neighbors[0] = self.prevState[y-1][x-1]
				# second
				if y -1 < 0:
					neighbors[1] = 0
				else:
					neighbors[1] = self.prevState[y-1][x]
				# third
				if y - 1 < 0 or x + 2 > self.num_cols:
					neighbors[2] = 0
				else:
					neighbors[2] = self.prevState[y-1][x+1]
				# fourth
				if x + 2 > self.num_cols:
					neighbors[3] = 0
				else:
					neighbors[3] = self.prevState[y][x+1]
				# fifth
				if y + 2 > self.num_rows or x + 2 > self.num_cols:
					neighbors[4] = 0
				else:
					neighbors[4] = self.prevState[y+1][x+1]
				# sixth
				if y + 2 > self.num_rows:
					neighbors[5] = 0
				else:
					neighbors[5] = self.prevState[y+1][x]
				# seventh
				if y + 2 > self.num_rows or x - 1 < 0:
					neighbors[6] = 0
				else:
					neighbors[6] = self.prevState[y+1][x-1]
				# eigth
				if x - 1 < 0:
					neighbors[7] = 0
				else:
					neighbors[7] = self.prevState[y][x-1]
				# We now determine this cell's next state.
				liveNeighbors = 0
				liveNeighbors = sum(neighbors)
				if cell == 1 and liveNeighbors < 2:
					self.nextState[y][x] = 0
				if cell == 1 and liveNeighbors == 2 or liveNeighbors == 3:
					self.nextState[y][x] = 1
				if cell == 1 and liveNeighbors > 3:
					self.nextState[y][x] = 0
				if cell == 0 and liveNeighbors == 3:
					self.nextState[y][x] = 1
		self.printStates()

	def printStates(self):
		print self.prevState
		print self.nextState
		self.prevState = None
		self.prevState = self.nextState

Cycle(args.file)
