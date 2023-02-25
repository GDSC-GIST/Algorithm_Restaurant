# 94ms, 14MB, 0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cur = []
        for c in s:
            for i in range(len(cur)):
                if c == cur[i]:
                    cur = cur[i+1:] + [c]
                    break
            else:
                cur += [c]
            ans = max(ans, len(cur))
        return ans
