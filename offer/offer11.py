# author: tobebetter9527
# since: 2023/02/01 20:28
from random import random
from typing import List


class Solution:

    def minArray(self, numbers: List[int]) -> int:
        idx, right = 0, len(numbers) - 1
        while idx < right and numbers[idx] <= numbers[idx + 1]:
            idx += 1
        return numbers[0] if idx == right else numbers[idx + 1]


def ge_arr(max_val: int, max_len: int) -> List[int]:
    length = ge_val(max_len) + 1
    return [ge_val(max_val) for _ in range(length)]


def ge_val(max_len: int) -> int:
    return int(random() * max_len)


if __name__ == '__main__':
    test_times, max_val, max_len = 1000000, 20, 60
    for _ in range(test_times):
        nums = ge_arr(max_val, max_len)
        nums.sort()
        min1 = nums[0]

        length = len(nums)
        rotate_num = ge_val(length) + 1  # 旋转1到n次
        numbers = nums[rotate_num:] + nums[0:rotate_num]
        solu = Solution()
        min2 = solu.minArray(numbers)

        if min1 != min2:
            print(f"min1: {min1}, min2: {min2}", min1, min2)
            print(nums)
            print(numbers)
    print("done!")
