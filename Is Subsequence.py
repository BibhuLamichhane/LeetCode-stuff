class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        i = 0
        t = [i for i in t]
        
        for i in s:
            if i in t:
                t = t[t.index(i) + 1: ]
            else:
                return False
        return True