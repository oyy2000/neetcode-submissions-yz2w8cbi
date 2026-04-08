class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def L(nums, i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 1
            
            max_len = 1
            # memo[j] = L(nums, j)
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(1 + L(nums, j), max_len)
            memo[i] = max_len
            return max_len

        return max(L(nums, i) for i in range(len(nums)))



