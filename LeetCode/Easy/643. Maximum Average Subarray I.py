class Solution:
	def findMaxAverage( self, nums: List[int], k: int ) -> float:
		ans = curr = sum( nums[ : k ] )

		for i in range( len( nums ) - k ):
			curr += nums[ i + k ] - nums[i]
			ans = max( curr, ans )

		return ans / k
