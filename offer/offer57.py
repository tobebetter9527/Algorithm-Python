# author: tobebetter9527
# since: 2023/03/04 10:25
from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        s = {num for num in nums}
        for num in nums:
            temp = target - num
            if temp in s:
                return [temp, num]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []
