import Organism

class Environment:
	# length of a side of the board
	boardSize
	# starting location of colony
	homeLoc
	# the actual board
	board

	def __init__(self, boardSize = 20):
		self.boardSize = boardSize

	# builds the board
	def buildBoard(self):
		[[Node() for j in range(boardSize)] for i in range(boardSize)]

	def addPredator(self, name = "", number = 1, homeLoc = Point(0, 0)):
		emptyPoint = getEmptyPointNear(homeLoc)
	
	def getEmptyPointNear(self, loc = Point(0, 0)):
		board(0,0)

class Node:
	# type of organism on the board
	orgtype
	# actual organism on the board
	organism

	def __init__(self, orgtype = OrgType.DIRT, organism = None):
		self.orgtype = orgtype
		self.organism = organism