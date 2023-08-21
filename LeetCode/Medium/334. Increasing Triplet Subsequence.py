class Solution:
	def increasingTriplet( self, nums: List[int] ) -> bool:
		q = deque()
		q.append( [ nums[0] ] )

		for num in nums[ 1 : ]:
			if num < q[0][0]:
				q.appendleft( [ num ] )
				continue

			for i in q:
				t = False

				for j in i:
					if num > j:
						if t:
							return True
						else:
							t = True
							continue
					elif t:
						if num < j:
							i[1] = num

						t = False
						break
					else:
						break

				if t:
					i.append( num )
