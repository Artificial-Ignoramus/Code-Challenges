def find_even_index( arr ):
	total = sum( arr )
	curr = i = 0
	
	while i < len( arr ):
		if curr == ( total - arr[i] ) / 2:
			return i
		
		curr += arr[i]
		i += 1
		
	return -1
