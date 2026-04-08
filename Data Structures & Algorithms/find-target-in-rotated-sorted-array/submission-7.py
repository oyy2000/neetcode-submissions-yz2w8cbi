class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            # left sorted portion
            if nums[low] <= nums[mid]:
                if target > nums[mid]:
                    low = mid + 1
                elif target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            # right sorted portion
            else:
                if nums[mid] > target:
                    # go left
                    high = mid - 1
                elif target > nums[high]:
                    high = mid - 1
                else: 
                    low = mid + 1
        return -1