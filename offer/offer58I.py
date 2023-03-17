# author: tobebetter9527
# since: 2023/3/17 10:58
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        s = s.strip()
        left, right = len(s) - 1, len(s) - 1
        res = []
        while left >= 0:
            while left >= 0 and s[left] != ' ':
                left -= 1
            res.append(s[left+1:right+1])
            while left >= 0 and s[left] == ' ':
                left -= 1
            right = left
        return ' '.join(res)
