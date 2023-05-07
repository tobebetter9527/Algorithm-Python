class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        str = str.strip()
        if not str:
            return 0

        res, sign, idx, boundary = 0, 1, 1, 2 ** 31 // 10

        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            idx = 0

        for c in str[idx:]:
            if c < '0' or c > '9':
                break
            if res > boundary or (res == boundary and c > '7'):
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            res = res * 10 + (ord(c) - ord('0'))

        return res * sign


if __name__ == '__main__':
    str = " -1224243333333333sdf"
    solu = Solution()
    print(solu.strToInt(str))
