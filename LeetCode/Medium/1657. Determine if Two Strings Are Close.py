class Solution:
	def closeStrings( self, word1: str, word2: str ) -> bool:
		word1, word2 = Counter( word1 ), Counter( word2 )
		return word1.keys() == word2.keys() and Counter( word1.values() ) == Counter( word2.values() )
