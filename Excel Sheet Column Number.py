class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        x = len(columnTitle) - 1
        o = 0
        for i in columnTitle:
            o += (26 ** x) * (ord(i) - 64)
            x -= 1
        return o