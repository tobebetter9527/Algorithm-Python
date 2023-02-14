# author: tobebetter9527
# since: 2023/2/14 17:28
from queue import Queue

from offer.TreeNode import TreeNode


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recursive(left, right):
            if not left and not right:
                return True
            elif left and not right:
                return False
            elif not left and right:
                return False
            return left.val == right.val and recursive(left.left, right.right) and recursive(left.right, right.left)

        return recursive(root.left, root.right)

    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = Queue()
        q.put(root.left)
        q.put(root.right)
        while not q.empty():
            left = q.get()
            right = q.get()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            q.put(left.left)
            q.put(right.right)
            q.put(left.right)
            q.put(right.left)

        return True
