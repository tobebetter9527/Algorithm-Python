# author: tobebetter9527
# since: 2023/03/03 21:54
from typing import List

from offer.TreeNode import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def in_order(root: TreeNode, lst: List[TreeNode]):
            if root:
                in_order(root.left, lst)
                lst.append(root)
                in_order(root.right, lst)

        lst = []
        in_order(root, lst)
        return lst[-k].val

    def kthLargest2(self, root: TreeNode, k: int) -> int:
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
