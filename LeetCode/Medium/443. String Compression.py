class Solution:
	def compress( self, chars: List[str] ) -> int:
		start = i = 0
		
		while i < len ( chars ):
			if chars[i] != chars[ i - 1 ]:
				if start + 1 < i:
					chars[ start + 1 : i ] = list( str( i - start ) )
					i = start + len( str( i - start ) ) + 1
					
				start = i
				
			i += 1

		if start + 1 < i:
			chars[ start + 1 : i ] = list( str( i - start ) )
			
		return len( chars )
