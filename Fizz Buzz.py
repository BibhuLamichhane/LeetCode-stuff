class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            o = ''
            flag = True
            if not i % 3:
                o += 'Fizz'
                flag = False
            if not i % 5:
                o += 'Buzz'
                flag = False
                
            if flag:
                o = str(i)              
            out.append(o)
        return out
