import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length % 2 == 1:
            return self.nums[length // 2]
        else:
            return (self.nums[length // 2] + self.nums[(length - 1) // 2]) / 2
        