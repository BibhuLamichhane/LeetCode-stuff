class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)
        y = ((32 - len(x[2:])) * '0' + x[2:])
        y = y[::-1]
        s = 0
        for i in range(len(y) - 1, -1, -1):
            if y[i] == '1':
                s += 2**((len(y) - 1) - i)
        return s
