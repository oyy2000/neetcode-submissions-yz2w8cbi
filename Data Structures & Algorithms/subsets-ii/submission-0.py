class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []
        nums.sort()
        n = len(nums)
        def dfs(startIndex):
            # base case
            res.append(path.copy())
            if startIndex == n:
                return

            for i in range(startIndex, n):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res


            # [1], [2], [1]
            # [1,2] [2,1]
            # [1,2,1]

            # [1], [1], [2]
            # [1,2] [2,1]
            # [1,2,1]

                    