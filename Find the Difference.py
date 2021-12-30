class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = [i for i in s]
        for i in t:
            if i not in s:
                return i
            else:
                s.remove(i)