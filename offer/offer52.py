# author: tobebetter9527
# since: 2023/3/3 11:00
from offer.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = headB if not nodeA else nodeA.next
            nodeB = headA if not nodeB else nodeB.next
        return nodeA
