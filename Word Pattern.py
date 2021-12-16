class Solution:
    def indices(self, vals, x):
        o = []
        while x in vals:
            n = vals.index(x)
            o.append(n)
            vals[n] = None
        return o
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        l_s = s.split()
        l_p = [i for i in pattern]
        s_p = list(set(l_p))
        s_s = list(set(l_s))
        
        if len(l_s) != len(l_p):
            return False
        
        if len(s_s) != len(s_p):
            return False
        for i in s_p:
            index = self.indices(l_p[:], i)

            x = l_s[index[0]]
            for j in range(1, len(index)):
                if x != l_s[index[j]]:
                    return False
        return True 
            