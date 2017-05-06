from Environment import Environment


cycles = int(input("How many cycles to run for: "))
boardSize = int(input("What size board: "))

ecosystem = Environment(boardSize)

predators = int(input("How many predators in EcoSim: "))
while (predators > 4):
	predators = int(input("MAXSIZE = {}. How many predators in EcoSim: ".format(4)))

speciesTotal = 7

#Const names already in use.
namesInUse = ['.', '-', '*', '`']
realPred = []

for i in range(predators):
	name = input("Single character name for predator {}: ".format(i))
	while name in namesInUse:
		name = input("Already Used. Single character name for predator {}: ".format(i))
	
	namesInUse.append(name)
	realPred.append(name)
	ecosystem.addPredator(name, speciesTotal, ecosystem.getHomeLoc())

totalPrey = predators * boardSize
ecosystem.addPrey(totalPrey)

for cycle in range(cycles):
	#print("CYCLE {}:".format(cycle))
	ecosystem.updateEnvironment()
