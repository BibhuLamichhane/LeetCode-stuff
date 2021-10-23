class Solution:
    def trailingZeroes(self, n: int) -> int:
        v = 1
        for i in range(n, 0, -1):
            v *= i
        v = str(v)
        c = 0
        for i in range(len(v)-1, -1, -1):
            if v[i] == '0':
                c+= 1
            else:
                break
        return c