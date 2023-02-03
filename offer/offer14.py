# author: tobebetter9527
# since: 2023/2/3 10:51

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2


if __name__ == '__main__':
    n = 10
    solu = Solution()
    res = solu.cuttingRope(n)
    print(res)