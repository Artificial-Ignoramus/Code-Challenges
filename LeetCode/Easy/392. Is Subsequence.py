class Solution:
	def isSubsequence( self, s: str, t: str ) -> bool:
		if s == "":
			return True
			
		i, len1 = 0, len( s )

		for ch in t:
			if s[i] == ch:
				i += 1

				if i == len1:
					return True

		return False
