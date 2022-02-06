class Solution:
    def frequencySort(self, s: str) -> str:
        c = []
        s = [i for i in s]

        set_s = list(set(s))

        for i in set_s:
            c.append(s.count(i))

        l = len(c)
        o = ''
        while c != [-9999] * l:
            i = c.index(max(c))
            o += set_s[i] * max(c)
            c[i] = -9999
        
        return o
