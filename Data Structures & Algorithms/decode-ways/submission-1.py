class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * n
        dp[0] = 1  # 第一位非 0 时，只有一种解码方式

        for i in range(1, n):
            # 单个字符合法（非 0）
            if s[i] != '0':
                dp[i] = dp[i - 1]
            
            # 两个字符合法（10–26）
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                if i >= 2:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1  # 前面没有字符时，相当于 dp[-1] = 1
        
        return dp[-1]
