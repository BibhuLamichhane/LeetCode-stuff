class Solution:
    def foo(self, v):
        a = v//26
        b = v/26 - a
        c = round(26 * b)
        if c == 0:
            c = 26
            a -= 1
        return a, chr(64+c)
    
    def convertToTitle(self, columnNumber: int) -> str:
        o = ''
        v = columnNumber
        while v > 26:
            v, temp = self.foo(v)
            o = temp + o
        o = chr(64 + v) + o
        return o