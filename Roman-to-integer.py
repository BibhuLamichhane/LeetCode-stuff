class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'M': 1000, 'D': 500, 
            'C': 100, 'L': 50, 
            'X': 10, 'V': 5, 
            'I': 1
        }
        num = 0
        curr = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            curr = symbol[s[i]]
            if curr < prev:
                num -= curr
            else:
                num += curr
            prev = curr
        return num