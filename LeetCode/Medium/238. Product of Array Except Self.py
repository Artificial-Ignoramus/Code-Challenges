class Solution:
	def productExceptSelf( self, nums: List[int] ) -> List[int]:
		total = reduce( operator.__mul__, nums )

		return [ reduce( operator.__mul__, nums[ : i ] + nums[ i + 1 : ] ) if nums[i] == 0 else total // nums[i] for i in range( len ( nums ) ) ]
