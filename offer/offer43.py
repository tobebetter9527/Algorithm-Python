class Solution:
    def countDigitOne(self, n: int) -> int:
        high, low, cur, digit, count = n, 0, 0, 1, 0
        while high != 0:
            cur = high % 10
            high //= 10
            low = n % digit
            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += high * digit + digit
            digit *= 10
        return count


if __name__ == '__main__':
    n = 1004
    solu = Solution()
    print(solu.countDigitOne(n))
