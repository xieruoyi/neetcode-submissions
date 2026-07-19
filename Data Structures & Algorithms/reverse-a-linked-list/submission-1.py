class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # 保存下一个节点
            curr.next = prev     # 指针反转
            prev = curr          # prev 前进一步
            curr = nxt           # curr 前进一步

        return prev