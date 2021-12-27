class SummaryRanges:

    def __init__(self):
        self.vals = []

    def addNum(self, val: int) -> None:
        if val not in self.vals:
            self.vals.append(val)
            self.vals.sort()

    def getIntervals(self) -> List[List[int]]:
        i = 0
        l = len(self.vals)
        o = []
        x = [self.vals[0], self.vals[0]]
        while i + 1 != l:
            if self.vals[i] + 1 == self.vals[i + 1]:
                x[1] = self.vals[i + 1]
                i += 1            
            else:
                o.append(x)
                i += 1
                x = [self.vals[i], self.vals[i]]
        o.append(x)
        return o
            

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()