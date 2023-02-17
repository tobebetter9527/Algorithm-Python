# author: tobebetter9527
# since: 2023/02/17 17:23
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        ans = []
        start_row, start_col, end_row, end_col = 0, 0, len(matrix) - 1, len((matrix[0])) - 1
        while start_row <= end_row and start_col <= end_col:
            if start_row == end_row:
                for i in range(start_col, end_col + 1):
                    ans.append(matrix[start_row][i])
            elif start_col == end_col:
                for i in range(start_row, end_row + 1):
                    ans.append(matrix[i][end_col])
            else:
                for i in range(start_col, end_col):
                    ans.append(matrix[start_row][i])
                for i in range(start_row, end_row):
                    ans.append(matrix[i][end_col])
                for i in range(end_col, start_col, -1):
                    ans.append(matrix[end_row][i])
                for i in range(end_row, start_row, -1):
                    ans.append(matrix[i][start_col])
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solu = Solution()
    ans = solu.spiralOrder(matrix)
    print(ans)
