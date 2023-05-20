class Solution:
    def translateNum(self, num: int) -> int:
        if num == 0:
            return 1
        p1 = self.translateNum(num // 10)
        p2 = 0
        temp = num % 100
        if num >= 10 and temp >= 10 and temp <= 25:
            p2 = self.translateNum(num // 100)
        return p1 + p2

    def translateNum2(self, num: int) -> int:
        a, b, y = 1, 1, num % 10
        while num != 0:
            num = num // 10
            x = num % 10
            a, b = a + b if 10 <= 10 * x + y <= 25 else a, b
            y = x
        return a


if __name__ == '__main__':
    num = 12258
    solu = Solution()
    print(solu.translateNum2(num))
