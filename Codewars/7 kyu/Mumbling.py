def accum( s ):
	s = s.lower()
	
	return "-".join( s[i].upper() + s[i] * i for i in range( len( s ) ) )
