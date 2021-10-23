class Solution:
    def isHappy(self, n: int) -> bool:
        s = n
        val = [n]
        while s != 1:
            s = 0
            while n != 0:
                s += (n % 10)**2
                n = n // 10
            n = s
            if n in val:
                return False
            else:
                val.append(n)
        return True
    