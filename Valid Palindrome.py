class Solution:
    def isPalindrome(self, s: str) -> bool:
        values = []
        for v in s.lower():
            x = ord(v)
            if 97 <= x <= 122:
                values.append(v)
            elif 48 <= x <= 57:
                values.append(v)
        
        return values[::-1] == values