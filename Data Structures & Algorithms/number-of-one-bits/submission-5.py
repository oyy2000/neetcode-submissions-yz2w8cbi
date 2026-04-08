class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n:
            res += 1
            n = n & (n-1)
        return res
        # for num in list(n):
        #     if num == 1:
        #         count += 1
        # return count