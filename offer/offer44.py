# author: tobebetter9527
# since: 2023/5/25 15:00
import math


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit
        idx = (digit - 1) - (n - 1) % digit
        return num // 10 ** idx % 10


if __name__ == '__main__':
    solu = Solution()
    print(solu.findNthDigit(1000000000))