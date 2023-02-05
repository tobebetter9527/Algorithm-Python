# author: tobebetter9527
# since: 2023/02/05 9:29

class Solution:

    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1

        quotient, remaider, p, rem = n // 3 - 1, n % 3, 1000000007, 1
        for _ in range(quotient):
            rem = rem * 3 % p;

        if remaider == 0:
            return 3 * rem % p
        elif remaider == 1:
            return rem * 4 % p
        else:
            return rem * 3 * 2 % p


if __name__ == '__main__':
    n = 10
    solu = Solution()
    res = solu.cuttingRope(n)
    print(res)
