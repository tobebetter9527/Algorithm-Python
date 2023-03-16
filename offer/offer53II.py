# author: tobebetter9527
# since: 2023/03/03 20:49
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n, low, high = len(nums) + 1, 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > mid:
                high = nums[mid] - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    nums = [1, 2]
    solu = Solution()
    ans = solu.missingNumber(nums)
    print(ans)
