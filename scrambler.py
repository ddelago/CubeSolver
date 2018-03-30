"""
Cube Scrambler
"""
import random

# Function
def CreateScramble (list):
	new_scramble = []
	for x in range(0, 30):
		new_scramble.append(random.choice(list))

	return new_scramble	

# Main
if __name__ == '__main__':

	move_list = ['R','L','F','B','U','D','r','l','f','b','u','d',]
	scramble = CreateScramble(move_list)

	print(scramble)




