# author: tobebetter9527
# since: 2023/03/05 8:31
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
        ans = 0
        for i in range(32):
            if bits[i] % 3 != 0:
                ans |= 1 << i
        return ans


if __name__ == '__main__':
    nums = [9,1,7,9,7,9,7]
    solu = Solution()
    ans = solu.singleNumber(nums)
    print(ans)
