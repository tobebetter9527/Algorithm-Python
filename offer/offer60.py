from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            temp = [0] * (i * 5 + 1)
            for j in range(len(dp)):
                for k in range(6):
                    temp[j + k] += dp[j] / 6
            dp = temp
        return dp


if __name__ == '__main__':
    n = 2
    solu = Solution()
    print(solu.dicesProbability(n))
