class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1 
        n = len(s)
        l, r = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                mp = {}
                for q in range(i, j + 1):
                    if s[q] in mp:
                        mp[s[q]] = mp.get(s[q]) + 1
                        break
                    else:
                        mp[s[q]] = 1
                res = max(len(mp.keys()), res)
        return res