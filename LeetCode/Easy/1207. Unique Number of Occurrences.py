class Solution:
	def uniqueOccurrences( self, arr: List[int] ) -> bool:
		arr = Counter( arr )
		return len( set( arr.values() ) )== len( arr )
