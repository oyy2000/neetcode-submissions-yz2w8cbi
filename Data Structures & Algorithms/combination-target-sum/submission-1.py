class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        n = len(nums)
        nums.sort()
        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
            
            for i in range(start, n):
                x = nums[i]
                if x > remain:
                    break
                path.append(x)
                dfs(i, remain - x)
                path.pop()

        dfs(0, target)
        return res
