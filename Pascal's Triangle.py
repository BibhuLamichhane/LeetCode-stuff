class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        o = [[1]]
        
        if numRows > 1:
            o.append([1,1])
        
        if numRows > 2:
            for i in range(2, numRows):
                new = [1]
                curr = o[i - 1]
                for j in range(len(curr) - 1):
                    new.append(curr[j] + curr[j + 1])
                new.append(1)
                o.append(new)
                
        return o

    def generate2(self, numRows:int) -> List[List[int]]: # second solution
        vals = []
        for n in range(numRows):
            o = [1]

            for i in range(n):
                v = 1
                for j in range(i + 1):
                    v *= n - j

                v /= math.factorial(i + 1)
                o.append(int(v))
            print(o)
            vals.append(o)
        
        return vals