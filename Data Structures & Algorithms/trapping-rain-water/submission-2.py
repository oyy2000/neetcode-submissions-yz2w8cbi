class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        prefix = [0] * (n + 2)
        suffix = [0] * (n + 2)
        for i in range(1, n):  
            prefix[i] = max(prefix[i - 1], height[i - 1])
        for i in range(n , 1, -1):  
            suffix[i-1] = max(suffix[i], height[i-1])

        print(prefix)
        print(suffix)

        for i in range(n):
            shift_n = n + 1
            res += max(0, min(prefix[i+1], suffix[i+1]) - height[i])
        return res