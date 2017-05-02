from enum import Enum
import random

class Point:	
	def __init__(self, row = 0, col = 0):
		self.row = int(row)
		self.col = int(col)

class Organism:	
	def __init__(self, name = '', fight = 1.0, spot = 1.0, mate = 1.0, currLoc = Point(0, 0)):
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
		# current location of organism
		self.currLoc = currLoc

	def Move(self, surroundingLocs = []):
		spot = random.randint(0, 7)
		return surroundingLocs[spot]

	def hunger(self):
		self.hungry += 1

	def Eat(self):
		self.hungry = 0
	
class Prey(Organism):
	def __init__(self, name = '^', fight = 1.0, spot = 1.0, mate = 1.0, currLoc = Point(0, 0)):
		super().__init__(name, fight, spot, mate, currLoc)			
	

class Predator(Organism):
	def __init__(self, name = '', fight = 1.0, spot = 1.0, mate = 1.0, currLoc = Point(0, 0)):
		super().__init__(name, fight, spot, mate, currLoc)

	def Fight(self):
		return random.randint(0, 1)

class OrgType(Enum):
	DIRT = 0
	GRASS = 1
	PREY = 2
	PRED = 3
