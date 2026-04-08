class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, 0, [], result)
        return result
        
    def dfs(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path.copy())
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
        
            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])

            self.dfs(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()

