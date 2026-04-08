class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # 把 small 的最大值推到 large，保持 small <= large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # 如果 large 比 small 多一个以上，就搬回去一个
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

        
        