# author: tobebetter9527
# since: 2023/01/30 20:23
from random import random
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

    def generate_arr(self, max_len, max_value):
        length = int(random() * max_len)
        return [int(random() * max_value) for _ in range(length)]

    def check_arr(self, nums):
        length, idx = len(nums), 0
        while idx < length and nums[idx] % 2 == 1:
            idx += 1
        while idx < length and nums[idx] % 2 == 0:
            idx += 1
        if idx < length:
            print("algo is wrong", nums)


if __name__ == "__main__":
    test_times, max_value, max_len = 1000, 100, 100
    for i in range(test_times):
        solu = Solution()
        nums = solu.generate_arr(max_len, max_value)
        solu.exchange(nums)
        solu.check_arr(nums)
    print("done")
