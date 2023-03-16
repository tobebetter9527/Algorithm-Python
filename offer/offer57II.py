# author: tobebetter9527
# since: 2023/3/16 9:25
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right, ans = 1, 2, [];
        s = left + right
        while left < right:
            if s == target:
                ans.append(list(range(left, right + 1)))
            if s >= target:
                s -= left
                left += 1
            else:
                right += 1
                s += right
        return ans

if __name__ == '__main__':
    target = 9
    solu = Solution()
    ans = solu.findContinuousSequence(target)
    print(ans)