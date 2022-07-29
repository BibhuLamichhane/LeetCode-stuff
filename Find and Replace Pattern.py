class Solution:
    def hash(self, val):
        x = dict()
        c = 0
        o = ''
        for i in val:
            if x.get(i) is None:
                x[i] = c
                c += 1
                o += str(x[i])
            else:
                o += str(x.get(i))
        return o
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        a = self.hash(pattern)
        o = []
        for i in words:
            if self.hash(i) == a:
                o.append(i)
        return o