class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        self.vals.append(num)
        
    def findMedian(self) -> float:
        self.vals.sort()
        l = len(self.vals)
        if l % 2:
            return self.vals[(int((l / 2) + 0.5)) - 1]
        else:
            return (self.vals[int(l / 2)] + (self.vals[int((l / 2) - 1)])) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()