# author: tobebetter9527
# since: 2023/5/10 11:22
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 0 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    n = 10
    solu = Solution()
    print(solu.sumNums(n))
