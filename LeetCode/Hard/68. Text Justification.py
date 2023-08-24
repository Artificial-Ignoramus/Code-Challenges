class Solution:
	def fullJustify( self, words: List[str], maxWidth: int ) -> List[str]:
		ans = []
		len1 = len( words )
		i = j = 0

		while i < len1:
			m = n = -1

			while j < len1 and m + len( words[j] ) + 1 <= maxWidth:
				m += len( words[j] ) + 1
				n += 1
				j += 1

			o = ( maxWidth - m )

			if j == len1 or n == 0:
				ans.append( " ".join( words[ i : j ] ) + " " * o )
			else:
				p = ( o + n ) // n
				q = ( o + n ) % n

				for k in range( q ):
					words[ i + k ] += " "

				ans.append( ( " " * p ).join( words[ i : j ] ) )

			i = j

		return ans
