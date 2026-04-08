class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = -1, len(nums)
        while low + 1 != high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid 
        return -1