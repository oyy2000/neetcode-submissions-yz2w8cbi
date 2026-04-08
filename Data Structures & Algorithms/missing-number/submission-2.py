class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res = res ^ i ^ nums[i]

        # for i in range(1, n - 1):
            # res = res ^ nums[i]

        return res