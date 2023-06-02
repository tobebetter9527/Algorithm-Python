import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_role(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_role))
        return "".join(strs)


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    solu = Solution()
    print(solu.minNumber(nums))
