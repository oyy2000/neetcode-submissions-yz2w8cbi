class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        
        def dfs(i, target):
            if target == 0:
                return 1
            elif target < 0 or i == len(coins):
                return 0

            if (i, target) in memo:
                return memo[(i, target)]
            take = dfs(i, target - coins[i]) 
            skip = dfs(i + 1, target) 
            memo[(i, target)] = take + skip
            return take + skip

        return dfs(0, amount)