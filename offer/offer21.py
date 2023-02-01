# author: tobebetter9527
# since: 2023/01/30 20:23
from typing import List


class Solution:

    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and (nums[left] & 1) == 1:
                left += 1
            while left < right and (nums[right] & 1 == 0):
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
