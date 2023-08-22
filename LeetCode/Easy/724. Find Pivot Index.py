class Solution:
	def pivotIndex( self, nums: List[int] ) -> int:
		m, n = 0, sum( nums[ 1 : ] )
		
		if m == n:
			return 0

		for i in range( 1, len( nums ) ):
			m += nums[ i - 1 ]
			n -= nums[i]

			if m == n:
				return i

		return -1
