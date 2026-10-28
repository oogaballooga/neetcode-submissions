class MedianFinder:

    def __init__(self):
        self.smallMax = []
        self.bigMin = []

    def addNum(self, num: int) -> None:
        if len(self.bigMin) == 0:
            self.bigMin.append(num)
            return

        if num >= self.bigMin[0]:
            heapq.heappush(self.bigMin, num)
        else:
            heapq.heappush(self.smallMax, -num)
        
        if len(self.smallMax) - len(self.bigMin) > 1:
            heapq.heappush(self.bigMin, -heapq.heappop(self.smallMax))
        elif len(self.bigMin) - len(self.smallMax) > 1:
            heapq.heappush(self.smallMax, -heapq.heappop(self.bigMin))

        

    def findMedian(self) -> float:

        if len(self.smallMax) == len(self.bigMin):
            return (-self.smallMax[0] + self.bigMin[0]) / 2.0

        if len(self.smallMax) > len(self.bigMin):
            return -self.smallMax[0]
        
        return self.bigMin[0]
