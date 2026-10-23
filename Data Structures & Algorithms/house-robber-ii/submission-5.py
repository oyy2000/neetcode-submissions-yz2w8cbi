class Solution:
    def rob(self, nums: list[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        
        def helper(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[1], arr[0])
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

            return dp[n - 1]
        
        ans1 = helper(nums[:-1])
        ans2 = helper(nums[1:])

        return max(ans1, ans2)


