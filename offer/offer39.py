# author: tobebetter9527
# since: 2023/3/2 15:37
from typing import List


class Solution:
    def majorityElement3(self, nums: List[int]) -> int:
        count, candicate = 0, 0
        for num in nums:
            if count == 0:
                candicate = num
            count += 1 if num == candicate else -1
        return candicate

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement1(self, nums: List[int]) -> int:
        map = {}
        half_len = len(nums) // 2
        for num in nums:
            count = map.get(num, 0)
            map[num] = count + 1
        for k, v, in map.items():
            if v > half_len:
                return k
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solu = Solution()
    ans = solu.majorityElement(nums)
    print(ans)
