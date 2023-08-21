class Solution:
	def canPlaceFlowers( self, flowerbed: List[int], n: int ) -> bool:
		pot = 0

		for i in [ 0 ] + flowerbed + [ 0 ]:
			if i == 0:
				pot += 1
			else:
				n -= ( pot - 1 ) // 2
				pot = 0

		return n - ( pot - 1 ) // 2 <= 0
