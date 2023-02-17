# author: tobebetter9527
# since: 2023/02/17 17:23
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        ans = []
        startRow, startCol, endRow, endCol = 0, 0, len(matrix) - 1, len((matrix[0])) - 1
        while startRow <= endRow and startCol <= endCol:
            if startRow == endRow:
                for i in range(startCol, endCol + 1):
                    ans.append(matrix[startRow][i])
            elif startCol == endCol:
                for i in range(startRow, endRow + 1):
                    ans.append(matrix[i][endCol])
            else:
                for i in range(startCol, endCol):
                    ans.append(matrix[startRow][i])
                for i in range(startRow, endRow):
                    ans.append(matrix[i][endCol])
                for i in range(endCol, startCol, -1):
                    ans.append(matrix[endRow][i])
                for i in range(endRow, startRow, -1):
                    ans.append(matrix[i][startCol])
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solu = Solution()
    ans = solu.spiralOrder(matrix)
    print(ans)
