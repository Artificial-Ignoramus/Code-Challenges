class Solution:
	def middleNode( self, head: Optional[ListNode] ) -> Optional[ListNode]:
		curr = head

		while curr is not None:
			curr = curr.next
			
			if curr is not None:
				curr = curr.next
				head = head.next

		return head	  
