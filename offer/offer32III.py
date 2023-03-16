# author: tobebetter9527
# since: 2023/03/04 19:01
import collections
from typing import List

from offer.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        flag = False
        while q:
            lst = collections.deque()
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if flag:
                    lst.appendleft(node.val)
                else:
                    lst.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append([x for x in lst])
            flag = not flag
        return ans
