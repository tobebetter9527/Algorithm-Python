import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = []
        deque = collections.deque()
        for right in range(k):
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)

        res.append(nums[deque[0]])

        for right in range(k, length):
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)

            if deque[0] <= (right - k):
                deque.popleft()

            res.append(nums[deque[0]])

        return res


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solu = Solution()
    print(solu.maxSlidingWindow(nums, k))
