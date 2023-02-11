# author: tobebetter9527
# since: 2023/02/11 11:14
from offer.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(1)
        cur = pre_head
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next, l2 = l2, l2.next
            else:
                cur.next, l1 = l1, l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return pre_head.next
