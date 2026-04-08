class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        

    def add(self, val: int) -> int:
        n = len(self.nums)
        for i in range(n + 1):
            if i < n:
                if self.nums[i] < val:
                    continue
                else:
                    self.nums.insert(i, val)
                    break
            else:
                self.nums.insert(i, val)
        print(self.nums)
        print(n - self.k + 1)
        return self.nums[n - self.k + 1]

