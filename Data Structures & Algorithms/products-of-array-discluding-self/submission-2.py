class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        res = [0] * length
        for i in range(1, length):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        print(prefix)
        print(suffix)
        for i in range(length):
            res[i] = suffix[i] * prefix[i]
        return res