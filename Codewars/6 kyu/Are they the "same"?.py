from collections import Counter

def comp( array1, array2 ):
	if array1 is None or array2 is None:
		return False
	
	return Counter( num * num for num in array1 ) == Counter( array2 )
