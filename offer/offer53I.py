# author: tobebetter9527
# since: 2023/3/3 14:13
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f_idx = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if low == mid or nums[mid - 1] != target:
                    f_idx = mid
                    break
                else:
                    high = mid - 1
        s_idx = -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if high == mid or nums[mid + 1] != target:
                    s_idx = mid
                    break
                else:
                    low = mid + 1
        if f_idx == -1 and s_idx == -1:
            return 0
        elif f_idx == -1 or s_idx == -1:
            return 1
        else:
            return s_idx - f_idx + 1
