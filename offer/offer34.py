# author: tobebetter9527
# since: 2023/03/25 22:01
from typing import List

from offer.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []

        def back_track(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            back_track(root.left, target)
            back_track(root.right, target)
            path.pop()

        back_track(root, target)
        return res
