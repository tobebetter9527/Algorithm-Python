# author: tobebetter9527
# since: 2023/3/22 10:21

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        idx = self.lastRemaining(n - 1, m)
        return (idx + m) % n

    def lastRemaining2(self, n: int, m: int) -> int:
        idx = 0
        for i in range(2, n + 1):
            idx = (idx + m) % i
        return idx
