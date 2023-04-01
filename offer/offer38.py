# author: tobebetter9527
# since: 2023/04/01 21:25
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        ans, path, visited = [], ['1'] * len(s), [False] * len(s)
        arr = sorted(list(s))

        def back_track(idx: int):
            if idx == len(s):
                ans.append(''.join(path))
                return
            for i in range(len(s)):
                if visited[i] or (i > 0 and not visited[i - 1] and arr[i - 1] == arr[i]):
                    continue
                path[idx] = arr[i]
                visited[i] = True
                back_track(idx + 1)
                visited[i] = False

        back_track(0)
        return ans


if __name__ == '__main__':
    s = "abac"
    solu = Solution()
    ans = solu.permutation(s)
    print(ans)
