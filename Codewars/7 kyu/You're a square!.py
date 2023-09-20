from math import floor

def is_square( n ):
	if n < 0:
		return False
	
	return pow( n, 0.5 ) == floor( pow( n, 0.5 ) )
