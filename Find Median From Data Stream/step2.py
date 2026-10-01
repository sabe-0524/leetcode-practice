import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.flag = True

    def addNum(self, num: int) -> None:
        if self.flag:
            heapq.heappush(self.min_heap, -num)
            carried = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -carried)
        
        else:
            heapq.heappush(self.max_heap, num)
            carried = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -carried)
        
        self.flag = not self.flag

    def findMedian(self) -> float:
        if self.flag:
            return (-self.min_heap[0] + self.max_heap[0]) / 2
        else:
            return self.max_heap[0]
        