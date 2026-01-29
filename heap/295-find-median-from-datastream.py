import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:

        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # rebalance
        if len(self.maxheap)> len(self.minheap) +1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap)> len(self.maxheap) :
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]

        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]

        else:
            a = self.minheap[0]
            b = -self.maxheap[0]
            return (a + b) / 2
