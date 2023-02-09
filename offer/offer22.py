# author: tobebetter9527
# since: 2023/02/09 21:53
from offer.ListNode import ListNode


class Solution:

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow

    def get_kth_from_end(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        num = 0
        cur = head
        while cur:
            cur = cur.next
            num += 1
        num = num - k
        cur = head
        while num > 0:
            cur = cur.next
            num -= 1
        return cur
