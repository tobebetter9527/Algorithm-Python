class Solution:
    def calculate(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum

    def isConfirmed(self, num1: int, num2: int, k: int) -> bool:
        return self.calculate(num1) + self.calculate(num2) > k

    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False] * m] * n

        # visited = [[False for j in range(m)] for i in range(n)]
        def recursive(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or visited[row][col]:
                return 0
            visited[row][col] = True
            if self.isConfirmed(row, col, k):
                return 0
            sum = recursive(row + 1, col) + recursive(row - 1, col) + recursive(row, col + 1) + recursive(row, col - 1)
            return sum + 1

        return recursive(0, 0)


if __name__ == '__main__':
    m, n, k = 2, 3, 1
    solu = Solution()
    sum = solu.movingCount(m, n, k)
    print(sum)
