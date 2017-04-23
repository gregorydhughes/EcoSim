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
		self.homeLocs = []
		self.populatHomeLocs(boardSize / 10)

	# builds the board
	def buildBoard(self):
		for row in range(self.boardSize):
			self.board.append([])
			for col in range(self.boardSize):
				self.board[row].append(Node())

	def addPredator(self, name = '', number = 1, homeLoc = Point(0, 0)):
		self.board[int(homeLoc.row)][int(homeLoc.col)] = Predator(name, 1.0, 1.0, 1.0, homeLoc, homeLoc)
	
	def getEmptyPointNear(self, loc = Point(0, 0)):
		return Point(0, 0)

	def populatHomeLocs(self, totalLocs):
		self.homeLocs.append(Point(totalLocs, totalLocs))
		self.homeLocs.append(Point(totalLocs, self.boardSize - totalLocs))
		self.homeLocs.append(Point(self.boardSize - totalLocs, totalLocs))
		self.homeLocs.append(Point(self.boardSize - totalLocs, self.boardSize - totalLocs))
		

	def getHomeLoc(self):
		homeLoc = self.homeLocs[0]
		self.homeLocs.pop(0)
		return homeLoc	

	def printBoard(self):
		print(' ', end='')
		for row in range(self.boardSize):
			print("-", end='')
		print()
		for row in range(self.boardSize):
			print("|", end='');			
			for col in range(self.boardSize):
				print(self.board[row][col].mySelf(), end='')
			print("|")

		print(' ', end='')
		for row in range(self.boardSize):
			print("-", end='')
		print()
		print()

	def updateEnvironment(self):
		self.printBoard()
	

		
			
