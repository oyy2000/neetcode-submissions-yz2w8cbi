class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            diff = 0 - nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total < diff:
                    l += 1
                elif total > diff:
                    r -= 1
                else: 
                    res.append([nums[l], nums[r], a])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
