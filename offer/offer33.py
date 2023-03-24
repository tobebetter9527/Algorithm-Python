# author: tobebetter9527
# since: 2023/3/24 17:
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recursive(start, end):
            if start >= end:
                return True
            p = start
            root = postorder[end]
            while postorder[p] < root:
                p += 1
            m = p
            while postorder[p] > root:
                p += 1
            return p == end and recursive(start, m - 1) and recursive(m, end - 1)
        return recursive(0, len(postorder) - 1)
