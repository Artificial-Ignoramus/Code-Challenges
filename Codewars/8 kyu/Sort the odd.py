def sort_array( source_array ):
	odd = sorted( i for i in source_array if i % 2 == 1 )

	for i in range( len( source_array ) ):
		if source_array[i] % 2 == 1:
			source_array[i] = odd.pop( 0 )

	return source_array
