class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force O(n^2)
        res = 0
        length = len(prices)
        if length <=1 :
            return res
        i, j = 0, 1 
        while j < length:
            diff = prices[j] - prices[i]
            if prices[j] <= prices[i]:
                i = j
            else:
                res = max(diff, res)
            j += 1
        return res

                    
