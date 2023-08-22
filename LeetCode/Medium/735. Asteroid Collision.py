class Solution:
	def asteroidCollision( self, asteroids: List[int] ) -> List[int]:
		ans = []

		for a in asteroids[ : : -1 ]:
			if a < 0:
				ans.insert( 0, a )
			else:
				while len( ans ) > 0:
					if ans[0] < 0:
						if a == -ans[0]:
							ans.pop( 0 )
						elif a > -ans[0]:
							ans.pop( 0 )
							continue
					else:
						ans.insert( 0, a )
						
					break
				else:
					ans.insert( 0, a )

		return ans
