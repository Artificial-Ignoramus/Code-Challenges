class Solution:
	def compress( self, chars: List[str] ) -> int:
		i, start = 0, 1
		
		while i < len ( chars ):
			if chars[i] != chars[ i - 1 ]:
				if start < i:
					chars[ start : i ] = list( str( i - start + 1) )
					i = start + len( str( i - start + 1 ) )
					
				start = i + 1
				
			i += 1

		if start < i:
			chars[ start : i ] = list( str( i - start + 1 ) )
			
		return len( chars )
