from Environment import Environment

cycles = int(input("How many cycles to run for: "))
boardSize = int(input("What size board: "))

ecosystem = Environment(boardSize)

predators = int(input("How many predators in EcoSim: "))
while (predators > 4):
	predators = int(input("MAXSIZE = {}. How many predators in EcoSim: ".format(4)))

speciesTotal = int(input("How many of each predator species in EcoSim: "))
while (speciesTotal > (boardSize / 10)):
	speciesTotal = int(input("MAXSIZE = {}. How many of each predator species in EcoSim: ".format(boardSize / 10)))


predNames = ['.', '-', 'G']

for i in range(predators):
	name = input("Single character name for predator {}: ".format(i))	
	while name in predNames:
		name = input("Already Used. Single character name for predator {}: ".format(i))
	
	predNames.append(name)
	ecosystem.addPredator(name, speciesTotal, ecosystem.getHomeLoc())


for cycle in range(cycles):
	print("CYCLE {}:".format(cycle))
	ecosystem.updateEnvironment()