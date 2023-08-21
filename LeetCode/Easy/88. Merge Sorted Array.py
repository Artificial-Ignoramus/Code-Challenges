class Solution:
	def merge( self, nums1: List[int], m: int, nums2: List[int], n: int ) -> None:
		m -= 1
		n += m

		for m >= 0 and num in nums2[ : : -1 ]:
			while nums1[m] > num:
				nums1[n] = nums1[m]
				m -= 1
				n -= 1
			
			nums1[n] = num
			n -= 1

		return nums1
