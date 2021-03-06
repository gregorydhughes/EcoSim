from enum import Enum
import random

class Point:	
	def __init__(self, row = 0, col = 0):
		self.row = int(row)
		self.col = int(col)

class Organism:	
	def __init__(self, name = '', currLoc = Point(0, 0), hungry = 0):
		# org char value
		self.name = name		
		# current location of organism
		self.currLoc = currLoc
		# have they eaten recently
		self.hungry = hungry

	def Move(self, surroundingLocs = []):
		spot = random.randint(0, 7)
		return surroundingLocs[spot]

	def hunger(self):
		self.hungry += 1

	def Eat(self):
		self.hungry = 0
	
class Prey(Organism):
	def __init__(self, name = '`', currLoc = Point(0, 0), hungry = 0):
		super().__init__(name, currLoc, hungry)			
	

class Predator(Organism):
	def __init__(self, name = '', currLoc = Point(0, 0), hungry = 0):
		super().__init__(name, currLoc, hungry)

	def Fight(self):
		return random.randint(0, 1)

class OrgType(Enum):
	DIRT = 0
	GRASS = 1
	PREY = 2
	PRED = 3
