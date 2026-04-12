class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = 0
        if total % 2 != 0:
            return False
        else:
            target = total // 2

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t + nums[i])

            dp = nextDP
        return True if target in dp else False



        return dfs(0, target)