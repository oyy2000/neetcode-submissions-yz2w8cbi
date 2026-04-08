class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = float("-inf")
        for i in range(len(nums)):
            #make choice 
            if curSum < 0:
                curSum = nums[i]
            else: 
                curSum += nums[i]
            res = max(res, curSum)
        return res