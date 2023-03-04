# author: tobebetter9527
# since: 2023/03/04 11:07
import collections
from typing import List

from offer.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, q = [], collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res
