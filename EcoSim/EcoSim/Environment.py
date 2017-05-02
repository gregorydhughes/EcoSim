from Organism import *

class Node:
		
	def __init__(self, orgtype = OrgType.DIRT, organism = None):
		# type of organism on the board
		self.orgtype = None
		# what is the ground made of
		self.groundtype = orgtype
		# actual organism on the board
		self.organism = organism
		self.moved = False

	def empty(self):
		return self.organism == None

	def mySelf(self):
		if (self.organism == None):			
			if (self.groundtype == OrgType.GRASS):
				return '*'
			else:
				return '.'
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
					self.board[row].append(Node(OrgType.DIRT))
				else:
					self.board[row].append(Node(OrgType.GRASS))

	def addPredator(self, name = '', number = 1, startLoc = Point(1, 1)):		
		surroundingLocs = self.getSurroundingLocs(startLoc)
		totalLocs = 7
		for pred in range(number):
			spot = random.randint(0, totalLocs)
			totalLocs -= 1

			currLoc = surroundingLocs[spot]
			surroundingLocs.pop(spot)

			self.board[int(currLoc.row)][int(currLoc.col)].orgtype = OrgType.PRED
			self.board[int(currLoc.row)][int(currLoc.col)].organism = Predator(name, 1.0, 1.0, 1.0, startLoc)

	def addPrey(self, totalPreyToAdd = 1):
		for i in range(totalPreyToAdd):
			row = random.randint(0, self.boardSize - 1);
			col = random.randint(0, self.boardSize - 1);
			while (not self.board[row][col].empty()):
				row = random.randint(0, self.boardSize - 1);
				col = random.randint(0, self.boardSize - 1);
			self.board[row][col].organism = Prey(currLoc = Point(row, col))
			self.board[row][col].orgtype = OrgType.PREY

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

	def getEmptyLocs(self, locs = []):

		for loc in locs:
			if loc.row < 0:
				loc.row = self.boardSize - 1
			if loc.row >= self.boardSize:
				loc.row = 0
			if loc.col < 0:
				loc.col = self.boardSize - 1
			if loc.col >= self.boardSize:
				loc.col = 0
		
		size = 7
		while (size >= 0):
			if (not self.board[locs[size].row][locs[size].col].empty()):
				locs.pop(size)
			size -= 1		
		return locs

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

		if curNode.moved == True:
			return

		if (not curNode.empty()):
			if (int(curNode.organism.hungry) > 50):
				print("Hunger: {}". format(curNode.organism.hungry))
			curNode.organism.hunger()
			if (curNode.organism.hungry > 100):
				curNode.orgtype = None
				curNode.organism = None
				return
		
		if (curNode.orgtype == OrgType.PREY):
			self.preyMove(curNode)
			
		
		elif (curNode.orgtype == OrgType.PRED):
			self.predMove(curNode);
			

		if (curNode.groundtype == OrgType.GRASS):
			locations = self.getSurroundingLocs(Point(row, col))
			for loc in locations:
				rand = random.random()
				if rand >= 0.6:
					self.board[loc.row][loc.col].groundtype = OrgType.GRASS

	# PREYMOVE
	# Parameters: curNode - the current Node that we are at
	# Post-Condition: establishes what the prey does for its move
	def preyMove(self, curNode = Node(None, None)):
		locations = self.getSurroundingLocs(curNode.organism.currLoc)
		newLoc = curNode.organism.Move(locations)

		if (self.board[newLoc.row][newLoc.col].orgtype == OrgType.PREY):
			emptyLocs = self.getEmptyLocs(self.getSurroundingLocs(curNode.organism.currLoc))
			if (len(emptyLocs) > 0):
				babyLoc = emptyLocs[random.randint(0, len(emptyLocs) - 1)]
				self.board[babyLoc.row][babyLoc.col].organism = curNode.organism
				self.board[babyLoc.row][babyLoc.col].organism.currLoc = babyLoc
				self.board[babyLoc.row][babyLoc.col].orgtype = curNode.orgtype
				self.board[babyLoc.row][babyLoc.col].moved = True
			
		elif (self.board[newLoc.row][newLoc.col].empty()):
			if (self.board[newLoc.row][newLoc.col].orgtype == OrgType.GRASS):
				curNode.organism.Eat()
			self.board[newLoc.row][newLoc.col].organism = curNode.organism
			self.board[newLoc.row][newLoc.col].organism.currLoc = newLoc
			self.board[newLoc.row][newLoc.col].orgtype = curNode.orgtype
			self.board[newLoc.row][newLoc.col].groundtype = OrgType.DIRT
			self.board[newLoc.row][newLoc.col].moved = True								
			curNode.organism = None
			curNode.orgtype = None

	# PREDMOVE
	# Parameters: curNode - the current Node that we are at
	# Post-Condition: establishes what the predator does for its move
	def predMove(self, curNode = Node(None, None)):

		locations = self.getSurroundingLocs(curNode.organism.currLoc)
		newLoc = curNode.organism.Move(locations)

		if (self.board[newLoc.row][newLoc.col].orgtype == OrgType.PRED):
			if (curNode.organism.name == self.board[newLoc.row][newLoc.col].organism.name):								
				emptyLocs = self.getEmptyLocs(self.getSurroundingLocs(curNode.organism.currLoc))
				if (len(emptyLocs) > 0):
					babyLoc = emptyLocs[random.randint(0, len(emptyLocs) - 1)]
					self.board[babyLoc.row][babyLoc.col].organism = curNode.organism
					self.board[babyLoc.row][babyLoc.col].organism.currLoc = babyLoc
					self.board[babyLoc.row][babyLoc.col].orgtype = curNode.orgtype
					self.board[babyLoc.row][babyLoc.col].moved = True
			else:
				pred1 = curNode.organism.Fight()
				pred2 = self.board[newLoc.row][newLoc.col].organism.Fight()
				if (pred1 == 0):
					curNode.organism = None
					curNode.orgtype = OrgType.DIRT
				else:
					curNode.moved = True
					curNode.organism.Eat()
					
				if (pred2 == 0):
					self.board[newLoc.row][newLoc.col].organism = None
					self.board[newLoc.row][newLoc.col].orgtype = OrgType.DIRT
				else:
					self.board[newLoc.row][newLoc.col].move = True
					self.board[newLoc.row][newLoc.col].organism.Eat()

		elif (self.board[newLoc.row][newLoc.col].orgtype == OrgType.PREY):
			self.board[newLoc.row][newLoc.col].orgtype = curNode.orgtype
			self.board[newLoc.row][newLoc.col].organism = curNode.organism
			self.board[newLoc.row][newLoc.col].moved = True
			self.board[newLoc.row][newLoc.col].organism.Eat()
			curNode.organism = None
			curNode.orgtype = None
		
		elif (self.board[newLoc.row][newLoc.col].empty()):				
			self.board[newLoc.row][newLoc.col].organism = curNode.organism
			self.board[newLoc.row][newLoc.col].organism.currLoc = newLoc
			self.board[newLoc.row][newLoc.col].orgtype = curNode.orgtype
			self.board[newLoc.row][newLoc.col].moved = True											
			curNode.organism = None
			curNode.orgtype = None