class Solution:
	def moveZeroes( self, nums: List[int] ) -> None:
		i = j = 0
		n = len( nums )

		while j < n:
			while j < n and nums[j] == 0:
				j += 1

			if j < n:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j += 1
