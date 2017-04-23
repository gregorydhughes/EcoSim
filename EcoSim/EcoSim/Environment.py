from Organism import *

class Node:
		
	def __init__(self, orgtype = OrgType.DIRT, organism = Organism()):
		# type of organism on the board
		self.orgtype = orgtype
		# actual organism on the board
		self.organism = organism
		self.moved = False

	def empty(self):
		return self.orgtype == OrgType.DIRT or self.orgtype == OrgType.GRASS

	def mySelf(self):
		if (self.orgtype == OrgType.DIRT):
			return '.'
		if (self.orgtype == OrgType.GRASS):
			return '*'
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
				chansu = random.random()
				if chansu >= 0.5:
					self.board[row].append(Node())
				else:
					self.board[row].append(Node(OrgType.GRASS))

	def addPredator(self, name = '', number = 1, homeLoc = Point(1, 1)):		
		surroundingLocs = self.getSurroundingLocs(homeLoc)
		totalLocs = 7
		for pred in range(number):
			spot = random.randint(0, totalLocs)
			totalLocs -= 1

			currLoc = surroundingLocs[spot]
			surroundingLocs.pop(spot)

			self.board[int(currLoc.row)][int(currLoc.col)].orgtype = OrgType.PRED
			self.board[int(currLoc.row)][int(currLoc.col)].organism = Predator(name, 1.0, 1.0, 1.0, homeLoc, currLoc)
	
	def addGrass(self, number = 1, baseLoc = Point(1,1)):
		surroundLocs = self.getSurroundingLocs(baseLoc)
		totalLocs = 7
		for loc in range(number):
			index = random.randint(0, totalLocs)
			totalLocs -= 1
			
			currLoc = surroundLocs[index]
			surroundLocs.pop(index)
			
			self.board[int(currLoc.row)][int(currLoc.col)].orgtype = OrgType.GRASS

	def getSurroundingLocs(self, loc = Point(1, 1)):
		locs = []
		locs.append(Point(loc.row - 1, loc.col - 1))
		locs.append(Point(loc.row - 1, loc.col))
		locs.append(Point(loc.row - 1, loc.col + 1))
		locs.append(Point(loc.row, loc.col - 1))
		locs.append(Point(loc.row, loc.col + 1))
		locs.append(Point(loc.row + 1, loc.col - 1))
		locs.append(Point(loc.row + 1, loc.col))
		locs.append(Point(loc.row + 1, loc.col + 1))

		for loc in locs:
			if loc.row < 0:
				loc.row = self.boardSize - 1
			if loc.row >= self.boardSize:
				loc.row = 0
			if loc.col < 0:
				loc.col = self.boardSize - 1
			if loc.col >= self.boardSize:
				loc.col = 0

		return locs



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
		for row in range(self.boardSize):
			for col in range(self.boardSize):
				self.update(self.board[row][col], row, col)

		for row in range(self.boardSize):
			for col in range(self.boardSize):
				self.board[row][col].moved = False

		self.printBoard()

	def update(self, curNode = Node(None, None), row = 1, col = 1):
		if (curNode.orgtype != OrgType.DIRT and curNode.orgtype != OrgType.GRASS):
			locations = self.getSurroundingLocs(curNode.organism.currLoc)
			newLoc = curNode.organism.Move(locations)
			while not self.board[newLoc.row][newLoc.col].empty():
				newLoc = curNode.organism.Move(locations)

			self.board[newLoc.row][newLoc.col].organism = curNode.organism
			self.board[newLoc.row][newLoc.col].organism.currLoc = newLoc
			self.board[newLoc.row][newLoc.col].orgtype = curNode.orgtype			
			self.board[newLoc.row][newLoc.col].moved = True
			curNode.organism = None
			curNode.orgtype = OrgType.DIRT

		if (curNode.orgtype == OrgType.GRASS):
			locations = self.getSurroundingLocs(Point(row,col))
			for loc in locations:
				rand = random.random()
				if self.board[loc.row][loc.col].orgtype == OrgType.DIRT and rand >= 0.6:
					self.board[loc.row][loc.col].orgtype = OrgType.GRASS