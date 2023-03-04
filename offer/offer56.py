# author: tobebetter9527
# since: 2023/03/04 22:08
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x, a, b = 0, 0, 0
        for num in nums:
            x ^= num
        right_one = x & (-x)
        for num in nums:
            if num & right_one:
                a ^= num
            else:
                b ^= num
        return a, b


if __name__ == '__main__':
    nums = [1, 2, 5, 2]
    solu = Solution()
    res = solu.singleNumbers(nums)
    print(res)
