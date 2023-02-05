# author: tobebetter9527
# since: 2023/02/05 10:13

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if ((n >> i) & 1) == 1:
                res += 1
        return res


if __name__ == '__main__':
    n = 11
    solu = Solution()
    res = solu.hammingWeight(n)
    print(res)
