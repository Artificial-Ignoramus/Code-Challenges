def solution( s ):
	return "".join( ch if ch.islower() else " " + ch for ch in s )
