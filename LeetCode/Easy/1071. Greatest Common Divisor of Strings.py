class Solution:
	def gcdOfStrings( self, str1: str, str2: str ) -> str:
		m, n = len( str1 ), len( str2 )
		o = gcd( m, n )
		s = str1[ : o ]

		for i in range( o, m, o ):
			if s != str1[ i : i + o ]:
				return ""
		
		for i in range( 0, n, o ):
			if s != str2[ i : i + o ]:
				return ""

		return s
