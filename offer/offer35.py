# author: tobebetter9527
# since: 2023/03/26 9:07

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        cur = head
        while cur:
            nextnext = cur.next
            cur.next = Node(cur.val)
            cur.next.next = nextnext
            cur = nextnext

        cur = head
        while cur:
            random = cur.random
            copyCur = cur.next
            if random:
                copyCur.random = random.next
            cur = copyCur.next

        newHead = head.next
        cur = head
        while cur:
            next = cur.next
            cur.next = next.next if next else None
            cur = next
        return newHead

    def copyRandomList2(self, head: 'Node') -> 'Node':
        if not head:
            return None
        map = {}

        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            map[cur].next = map.get(cur.next)
            map[cur].random = map.get(cur.random)
            cur = cur.next
        return map[head]
