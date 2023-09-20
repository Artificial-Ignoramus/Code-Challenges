def is_isogram( string ):
	string = string.upper()
	
	return len( string ) == len( set( string ) )