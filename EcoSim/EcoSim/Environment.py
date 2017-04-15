from Organism import *

class Node:
		
	def __init__(self, orgtype = OrgType.DIRT, organism = Organism()):
		# type of organism on the board
		self.orgtype = orgtype
		# actual organism on the board
		self.organism = organism

	def empty(self):
		return self.orgtype == OrgType.DIRT or self.orgtype == OrgType.GRASS

	def mySelf(self):
		if (self.orgtype == OrgType.DIRT):
			return '.'
		if (self.orgtype == OrgType.GRASS):
			return '#'
		else:
			return self.organism.name

class Environment:
		
	def __init__(self, boardSize = 20):
		# length of a side of the board
		self.boardSize = boardSize
		self.board = []

		self.buildBoard()

	# builds the board
	def buildBoard(self):
		for row in range(self.boardSize):
			self.board.append([])
			for col in range(self.boardSize):
				self.board[row].append(Node())

	def addPredator(self, name = '', number = 1, homeLoc = Point(0, 0)):
		emptyPoint = self.getEmptyPointNear(homeLoc)
	
	def getEmptyPointNear(self, loc = Point(0, 0)):
		return Point(0, 0)

	def printBoard(self):
		for row in range(self.boardSize):			
			for col in range(self.boardSize):
				print(self.board[row][col].mySelf())
			print()

	def updateEnvironment(self):
		self.printBoard()
	

		
			
