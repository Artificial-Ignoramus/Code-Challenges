class Solution:
	def maxOperations( self, nums: List[int], k: int ) -> int:
		nums = Counter( nums )
		s = set( nums )
		ans = 0

		while len( s ) > 0:
			m = s.pop()
			n = k - m

			if m == n:
				ans += nums[m] // 2
			elif n in s:
				s.remove( n )
				ans += min( nums[m], nums[n] )
				
		return ans
