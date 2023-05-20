from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2
        return self.mergeSort(nums, left, mid) + self.mergeSort(nums, mid + 1, right) + self.merge(nums, left, mid,
                                                                                                   right)

    def merge(self, nums, left, mid, right) -> int:
        length = right - left + 1
        temp = [0 for _ in range(length)]
        idx = length - 1
        index1, index2, pairs = mid, right, 0

        while index1 >= left and index2 >= mid + 1:
            if nums[index1] > nums[index2]:
                pairs += index2 - (mid + 1) + 1
                temp[idx] = nums[index1]
                index1 -= 1
            else:
                temp[idx] = nums[index2]
                index2 -= 1
            idx -= 1
        while index1 >= left:
            temp[idx] = nums[index1]
            index1 -= 1
            idx -= 1
        while index2 >= mid + 1:
            temp[idx] = nums[index2]
            index2 -= 1
            idx -= 1

        for i in range(length):
            nums[left + i] = temp[i]
        return pairs


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    solu = Solution()
    print(solu.reversePairs(nums))
