class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxA = -1
        for i in range(length):
            for j in range(i + 1, length):
                maxA = max(min(heights[i], heights[j]) * (j - i), maxA)
        return maxA
