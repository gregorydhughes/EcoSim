from enum import Enum
import random

class Point:	
	def __init__(self, row = 0, col = 0):
		self.row = int(row)
		self.col = int(col)

class Organism:	
	def __init__(self, name = '', fight = 1.0, spot = 1.0, mate = 1.0, home = Point(0, 0), currLoc = Point(0, 0)):
		# org char value
		self.name = name		
		# have they eaten recently
		self.hungry = 0
		# chance to fight
		self.fight = fight
		# chance to see predator
		self.spot = spot
		# chance to mate when running into same species
		self.mate = mate		
		# where home is
		self.home = home
		# current location of organism
		self.currLoc = currLoc
	
class Prey(Organism):
	def __init__(self, name = '', fight = 1.0, spot = 1.0, mate = 1.0, home = Point(0, 0), currLoc = Point(0, 0)):
		super().__init__(name, fight, spot, mate, home, currLoc)

	def Move(self):
		return Point(0, 0)

	def Mate(self):
		return True

	def Spot(self):
		return Point(0, 0)
	
	def Eat(self):
		self.hungry = 0


class Predator(Organism):
	def __init__(self, name = '', fight = 1.0, spot = 1.0, mate = 1.0, home = Point(0, 0), currLoc = Point(0, 0)):
		super().__init__(name, fight, spot, mate, home, currLoc)
	
	def Move(self, surroundingLocs = []):	
		spot = random.randint(0, 7)
		return surroundingLocs[spot]

	def Mate(self):
		return True

	def Spot(self):
		return Point(0, 0)
	
	def Eat(self):
		self.hungry = 0
		
	def Fight(self):
		return False

	def ReturnHome(self):
		return Point(0, 0)

class OrgType(Enum):
	DIRT = 0
	GRASS = 1
	PREY = 2
	PRED = 3
