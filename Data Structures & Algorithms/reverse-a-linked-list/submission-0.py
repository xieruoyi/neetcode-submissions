class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prevhead = ListNode(head.val)
        head = head.next

        while head is not None:
            newhead = ListNode(head.val)
            newhead.next = prevhead
            prevhead = newhead
            head = head.next

        return prevhead