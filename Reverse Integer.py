class Solution:
    def reverse(self, x: int) -> int:
        u = 2 ** 31 - 1
        l = -2 ** 31
        y = str(abs(x))[::-1]
        if x < 0:
            y = int(y) * - 1
        else:
            y = int(y)
        if y > u or y < l:
            return 0
        else:
            return y