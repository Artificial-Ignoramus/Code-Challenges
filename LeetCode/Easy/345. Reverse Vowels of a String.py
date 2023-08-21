class Solution:
	def reverseVowels( self, s: str ) -> str:
		i, j = 0, len( s ) - 1
		vowels = "aeiou"
		s = list( s )
		
		while i < j:
			if s[i] in vowels and s[j] in vowels:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1

			while i < j and s[i] not in vowels:
				i += 1

			while j > i and s[j] not in vowels:
				j -= 1

		return "".join( s )
