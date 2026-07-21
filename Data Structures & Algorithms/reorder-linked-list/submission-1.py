class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return

        # 找到链表中点
        dummy = head
        double_head = head

        while double_head.next and double_head.next.next:
            dummy = dummy.next
            double_head = double_head.next.next

        # dummy 是 first half 的最后一个节点
        first_half = head
        head = dummy.next
        dummy.next = None

        # 反转 second half
        current = head
        prev = None

        while current:
            dummy = current.next
            current.next = prev
            prev = current
            current = dummy

        current = prev  # reversed second half

        # 合并 first half 和 reversed second half
        while current:
            double_head = first_half.next
            dummy = current.next

            first_half.next = current
            current.next = double_head

            first_half = double_head
            current = dummy