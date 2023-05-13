# author: tobebetter9527
# since: 2023/5/10 10:03
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return list()
        n, temp = len(a), 1
        b = [1] * n
        for i in range(1, n):
            b[i] = b[i - 1] * a[i - 1]
        for i in range(n - 2, -1, -1):
            temp = temp * a[i + 1]
            b[i] = b[i] * temp
        return b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    solu = Solution()
    print(solu.constructArr(a))
