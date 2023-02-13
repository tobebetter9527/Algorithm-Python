# author: tobebetter9527
# since: 2023/02/13 20:41
from offer.TreeNode import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.mirrorTree(root.left)
            right = self.mirrorTree(root.right)
            root.left, root.right = right, left
        return root
