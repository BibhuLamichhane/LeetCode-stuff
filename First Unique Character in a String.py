class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = [i for i in s]
        for i in range(len(x)):
            temp = x[i]
            x[i] = None
            if temp in x:
                pass
            else:
                return i
            x[i] = temp
        return -1