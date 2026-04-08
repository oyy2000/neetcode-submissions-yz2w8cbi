class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def L(nums, i):
            if i == len(nums) - 1:
                return 1
            
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(1 + L(nums, j), max_len)
            return max_len

        return max(L(nums, i) for i in range(len(nums)))



