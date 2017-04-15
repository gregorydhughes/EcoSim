from Environment import Environment

cycles = 1000

ecosytem = Environment()

#eco

while (cycles >= 0):
 	ecosytem.updateEnvironment()
	#print("In that while")
	cycles -= 1
