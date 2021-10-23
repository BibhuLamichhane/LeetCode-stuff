class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        if len(x) > 0:
            return len(x[-1])
        else:
            return 0