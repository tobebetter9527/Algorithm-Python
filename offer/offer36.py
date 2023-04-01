# author: tobebetter9527
# since: 2023/04/01 10:54
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                cur.left = self.pre
                self.pre.right = cur
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        self.pre = None
        self.head = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        def in_order(lst: List[Node], root: Node):
            if not root:
                return
            in_order(lst, root.left)
            lst.append(root)
            in_order(lst, root.right)

        if not root:
            return None
        lst = []
        in_order(lst, root)
        n = len(lst)
        for i in range(n):
            node = lst[i]
            node.left = lst[(i - 1 + n) % n]
            node.right = lst[(i + 1) % n]
        return lst[0]
