def remove_smallest( numbers ):
	if len( numbers ) < 1:
		return numbers
	
	copy = numbers.copy()
	copy.remove( min( copy ) )
	
	return copy
