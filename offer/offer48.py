# author: tobebetter9527
# since: 2023/5/19 17:06
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        map = dict()
        left = -1
        for right in range(len(s)):
            if s[right] in map:
                left = max(left, map[s[right]])
            ans = max(ans, right - left)
            map[s[right]] = right
        return ans
