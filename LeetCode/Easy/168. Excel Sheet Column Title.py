class Solution:
	def convertToTitle( self, columnNumber: int ) -> str:
		ans = ""

		while columnNumber > 0:
			n = columnNumber % 26

			if n == 0:
				n = 26
			
			ans = chr( n + 64 ) + ans
			columnNumber = ( columnNumber - n ) // 26

		return ans
