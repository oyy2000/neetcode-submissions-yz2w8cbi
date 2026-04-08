class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = [-1] * len(s)
        
        def dp(i):
            if i == len(s):
                return True
            
            if memo[i] != -1:
                return False if memo[i] == 0 else True

            for length in range(1, len(s) - i + 1):
                prefix = s[i: i + length]
                if prefix in wordDict:
                    sub_problem = dp(i + length)
                    if sub_problem == True:
                        memo[i] = 1
                        return True
            memo[i] = 0
            return False

        return dp(0)
