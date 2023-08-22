class Solution:
	def largestAltitude( self, gain: List[int] ) -> int:
		ans = curr = 0

		for i in gain:
			curr += i
			ans = max( curr, ans )

		return ans
