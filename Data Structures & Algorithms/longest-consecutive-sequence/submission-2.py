class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in numset:
            if num - 1 in numset:
                continue
            else:
                i = 0
                while i + num in numset:
                    i += 1
                res = max(i, res)
        return res

