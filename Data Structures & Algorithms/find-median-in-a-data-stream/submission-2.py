class MedianFinder:
    def __init__(self):
        self.size = 0
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            mid = self.size // 2
            return (self.arr[mid] + self.arr[mid - 1])/ 2
        else: 
            mid = self.size // 2
            return self.arr[mid]
        # return arr[]
        
        