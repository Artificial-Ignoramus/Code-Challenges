def move_zeros( lst ):
	a = [ i for i in lst if i != 0 ]
	
	return a + [ 0 ] * ( len( lst ) - len( a ) )
