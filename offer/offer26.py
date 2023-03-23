from offer.TreeNode import TreeNode


class Solution:
    def isSubStructure(self, a: TreeNode, b: TreeNode) -> bool:
        def isSameStru(a, b):
            if not b:
                return True
            if not a or a.val != b.val:
                return False
            return isSameStru(a.left, b.left) and isSameStru(a.right, b.right)

        if not a or not b:
            return False
        return isSameStru(a, b) or self.isSubStructure(a.left, b) or self.isSubStructure(a.right, b)
