from Environment import Environment

# Python pseudo-constants
cycles = 1000
boardSize = 50
speciesTotal = 7

print("Runnning for {} time slices".format(cycles))
print("Running with an environment of {} square units".format(boardSize * boardSize))

# Max of 4 predators
preds = [4, 3, 2, 1]
pNames = ['A', 'B', 'C', 'D']

for numPredator in preds:
	ecoOut = 'boardOut_{}.dat'.format(numPredator)
	ecosystem = Environment(boardSize, ecoOut)

	for i in range(numPredator):
		name = pNames[i]
		ecosystem.addPredator(name, speciesTotal, ecosystem.getHomeLoc())

	totalPrey = numPredator * boardSize
	ecosystem.addPrey(totalPrey)

	filename = 'out_{}.dat'.format(numPredator)

	file = open(filename, 'w')

	pStr = 'for {} predators.'.format(numPredator)

	for cycle in range(cycles):
		file.write("Slice:\t{}\n".format(cycle))
		file.write("Remaining predators:\t{}\n".format(ecosystem.countRemainingPredators()))
		ecosystem.updateEnvironment(cycle)
		print("Simulation {}% complete".format(round(((cycle * 100) / cycles), 2)), pStr)

	print("Simulation complete".format(round(((cycle * 100) / cycles), 2)), pStr, '\n')
	ecosystem.closeFileOutputForClass()
	file.close()
print('Simulation for 4 environments completed')