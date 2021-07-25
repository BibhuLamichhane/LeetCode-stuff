class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        o = [1]
        
        for i in range(n):
            v = 1
            for j in range(i + 1):
                v *= n - j
    
            v /= math.factorial(i + 1)
            o.append(int(v))
        
        return o