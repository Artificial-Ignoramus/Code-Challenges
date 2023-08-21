class Solution:
	def increasingTriplet( self, nums: List[int] ) -> bool:
		array = [ [ nums[0] ] ]

		for num in nums[ 1 : ]:
			t = True

			for arr in array:
				if num > arr[-1]:
					arr.append( num )

					if len( arr ) == 3:
						return True
					
					t = False
					break
				
			if t:
				array.append( [ num ] )
