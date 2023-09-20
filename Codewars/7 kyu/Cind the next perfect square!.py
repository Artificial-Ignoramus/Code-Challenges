from math import floor

def find_next_square( sq ):
	i = pow( sq, 0.5 )
	j = floor( i )
	
	return pow( j + 1, 2 ) if i == j else -1
