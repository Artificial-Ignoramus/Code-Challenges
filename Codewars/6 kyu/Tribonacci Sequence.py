def tribonacci( signature, n ):
	for i in range( n - 3 ):
		signature.append( signature[i] + signature[ i + 1 ] + signature[ i + 2 ] )
		
	return signature[ : n ]
