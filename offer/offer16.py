# author: tobebetter9527
# since: 2023/2/7 19:59

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        ans = 1.0
        if n < 0:
            x, n = 1 / x, -n

        while n > 0:
            if (n & 1) == 1:
                ans *= x
            x *= x
            n >>= 1
        return ans


if __name__ == '__main__':
    x = 2.0
    n = 2
    solu = Solution()
    ans = solu.myPow(x, n)
    print(ans)
