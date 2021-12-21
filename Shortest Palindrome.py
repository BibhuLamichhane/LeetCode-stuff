class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = -1
        p = ''
        while p + s != (p + s)[::-1] and abs(i) < len(s):
            p += s[i]
            i -= 1
        return p+s