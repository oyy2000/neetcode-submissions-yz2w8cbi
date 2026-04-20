class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)

        l = 1
        r = maxi
        while l < r:
            k = (r - l) // 2 + l
            
            total = 0
            for pile in piles:
                x = math.ceil(pile / k)
                total += x
            if total <= h:
                r = k
            else: 
                l = k + 1
        return l