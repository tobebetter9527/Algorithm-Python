# author: tobebetter9527
# since: 2023/2/2 19:30
from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.__dfs(board, i, j, m, n, word, 0, visited):
                    return True
        return False

    def __dfs(self, board, i, j, m, n, word, idx, visited):
        if not 0 <= i < m or not 0 <= j < n or visited[i][j] or board[i][j] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        visited[i][j] = True
        flag = self.__dfs(board, i + 1, j, m, n, word, idx + 1, visited) or \
               self.__dfs(board, i - 1, j, m, n, word, idx + 1, visited) or \
               self.__dfs(board, i, j + 1, m, n, word, idx + 1, visited) or \
               self.__dfs(board, i, j - 1, m, n, word, idx + 1, visited)
        visited[i][j] = False
        return flag


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABAB"
    solu = Solution()
    flag = solu.exist(board, word)
    print(flag)
