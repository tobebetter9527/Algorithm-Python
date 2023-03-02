# author: tobebetter9527
# since: 2023/3/2 14:51
import collections
from typing import List

from offer.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [], []
        queue.append(root)
        while queue:
            lst = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(lst)
        return ans
