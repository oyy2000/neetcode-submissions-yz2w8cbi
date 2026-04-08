class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0

        if t == "":
            return ""
        
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need = len(countT)

        res, resLen = [-1, -1], float("inf")
        l = 0
        
        countS = {}
        for r in range(len(s)):
            c = s[r]
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        print(l, r)
        
        return s[l : r + 1] 