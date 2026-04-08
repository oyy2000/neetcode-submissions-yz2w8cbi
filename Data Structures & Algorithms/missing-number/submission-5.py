class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n + 1):
            res = res ^ i #^ nums[i]
        for i in range(1, n):
            res = res ^ nums[i]

        return res