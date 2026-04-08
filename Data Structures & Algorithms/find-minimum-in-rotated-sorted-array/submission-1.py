class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        low, high = 0, length
        res = nums[0]

        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= res:
                low = mid + 1
            else:
                high = mid
        if low == len(nums):
            return nums[0]
        return nums[low]
            
