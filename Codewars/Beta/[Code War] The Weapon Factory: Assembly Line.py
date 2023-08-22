def assembler( weapon_body, weapon_parts, magazine_location ):
	m, n = map( int, magazine_location.split( ":" ) )
	weapon_parts = list( weapon_parts )
	
	def mf( *args ):
		return weapon_body( *( weapon_parts[ : m ] + [ arg for arg in args ] + weapon_parts[ m : ] ) )
	
	return mf
