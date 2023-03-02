# author: tobebetter9527
# since: 2023/3/2 17:30
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -math.inf
        count = 0
        for num in nums:
            count += num
            if count > ans:
                ans = count
            if count < 0:
                count = 0
        return ans
