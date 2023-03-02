# author: tobebetter9527
# since: 2023/3/2 19:46
import collections


class Solution:
    # 3.6 字典是默认有序字典
    def firstUniqChar(self, s: str) -> str:
        dic = {}  # collections.OrderedDict
        for x in s:
            dic[x] = not x in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '

    def firstUniqChar2(self, s: str) -> str:
        f = collections.Counter(s)
        for i, ch, in enumerate(s):
            if f[ch] == 1:
                return ch
        return ' '


if __name__ == '__main__':
    s = 'leetcode'
    solu = Solution()
    ch = solu.firstUniqChar2(s)
    print(ch)