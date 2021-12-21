class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right - left > 10000:
            return 0
        s = left & left
        for i in range(left, right + 1):
            s = i & s
            if s == 0:
                break
        return s