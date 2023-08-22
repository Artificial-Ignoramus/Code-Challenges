class Solution:
	def equalPairs( self, grid: List[List[int]] ) -> int:
		p, q = defaultdict( int ), defaultdict( int )
		n = len( grid )
		ans = 0
		for i in range( n ):
			p[ tuple( grid[i] ) ] += 1
			q[ tuple( grid[j][i] for j in range( n ) ) ] += 1

		for i in p:
			if i in q:
				ans += p[i] * q[i]

		return ans
