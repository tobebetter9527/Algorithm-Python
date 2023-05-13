# author: tobebetter9527
# since: 2023/5/10 14:01
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit, pre = 0, prices[0],
        for i in range(1, len(prices)):
            if prices[i] > pre:
                profit = max(profit, (prices[i] - pre))
            else:
                pre = prices[i]
        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 6, 3]
    solu = Solution()
    print(solu.maxProfit(prices))
