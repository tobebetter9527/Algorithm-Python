# author: tobebetter9527
# since: 2023/02/11 10:08
from offer.ListNode import ListNode


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        def recursive(pre, cur):
            if cur is None:
                return pre
            ans = recursive(cur, cur.next)
            cur.next = pre
            return ans

        return recursive(None, head)
