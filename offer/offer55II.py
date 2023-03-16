# author: tobebetter9527
# since: 2023/03/04 9:19
import math

from offer.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recursive(root: TreeNode):
            if not root:
                return True, 0
            lb, lh = recursive(root.left)
            rb, rh = recursive(root.right)
            nb = lb and rb and math.fabs(lh - rh) <= 1
            return nb, max(lh, rh) + 1

        b, h = recursive(root)
        return b

    def isBalanced(self, root: TreeNode) -> bool:
        def recursive(root: TreeNode):
            if not root:
                return 0
            left = recursive(root.left)
            right = recursive(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return recursive(root) >= 0
