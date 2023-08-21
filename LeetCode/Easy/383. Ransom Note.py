class Solution:
	def canConstruct( self, ransomNote: str, magazine: str ) -> bool:
		m = Counter( magazine )

		for i, j in Counter( ransomNote ).items():
			if i not in m or m[i] < j:
				return False

		return True
