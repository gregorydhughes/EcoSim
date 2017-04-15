from enum import Enum

class Organism:
	# have they eaten recently
	hungry
	# chance to fight
	fight
	# chance to see predator
	spot
	# chance to mate when running into same species
	mate
	# where home is
	home
	# current location of organism
	currLoc
	def __init__(self, fight, spot, mate, home, currLoc):
		self.fight = fight
		self.spot = spot
		self.mate = mate
		self.home = home
		self.currLoc = currLo
	

class Prey(Organism):
	def __init__(self, fight, spot, mate, home, currLoc):
		super().__init__(fight, spot, mate, home, currLoc)

	def Move(self):
		return Point(0, 0)

	def Mate(self):
		return True

	def Spot(self):
		return Point(0, 0)
	
	def Eat(self):
		hungry -= 5


class Predator(Organism):
	counter
	def __init__(self, fight, spot, mate, home, currLoc):
		super().__init__(fight, spot, mate, home, currLoc)
	
	def Move(self):
		return Point(0, 0)

	def Mate(self):
		return True

	def Spot(self):
		return Point(0, 0)
	
	def Eat(self):
		hungry -= 5
		
	def Fight(self):
		return False

	def ReturnHome(self):
		return Point(0, 0)

class Point:
	row
	col
	def __init__(self, row = 0, col = 0):
		self.row = row
		self.col = col

class OrgType(Enum):
	DIRT = 0
	GRASS = 1
	PREY = 2
	PRED = 3
