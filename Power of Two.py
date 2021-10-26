class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while not n % 2:
            n = n // 2
            if n == 1:
                break
        return n == 1