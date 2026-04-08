class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        for i in range(32):
            if (1 << i) & n:
                res += 1 
        return res
        # for num in list(n):
        #     if num == 1:
        #         count += 1
        # return count