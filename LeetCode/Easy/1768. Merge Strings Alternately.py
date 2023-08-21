class Solution:
	def mergeAlternately( self, word1: str, word2: str ) -> str:
		len1 = len( word1 )
		len2 = len( word2 )
		min_len = min( len1, len2 )
		ans = ""
		
		for i in range( min_len ):
			ans += word1[i] + word2[i]

		for i in range( min_len, len1 ):
			ans += word1[i]

		for i in range( min_len, len2 ):
			ans += word2[i]

		return ans
