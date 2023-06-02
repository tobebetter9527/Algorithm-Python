# author: tobebetter9527
# since: 2023/5/18 9:16
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1 for _ in range(n)]
        a, b, c = 0, 0, 0
        for i in range(1, n):
            x2 = ans[a] * 2
            x3 = ans[b] * 3
            x5 = ans[c] * 5
            ans[i] = min(x2, x3, x5)
            if ans[i] == x2:
                a += 1
            if ans[i] == x3:
                b += 1
            if ans[i] == x5:
                c += 1
        return ans[-1]
