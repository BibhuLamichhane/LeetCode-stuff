class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        x = [[0]*(len(p)) for i in range(len(s))]
        x[0][0] = 1

        for j in range(1, len(p)):
            if p[j] == '*':
                x[0][j] = x[0][j-2]

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] in {s[i], '.'}:
                    x[i][j] = x[i-1][j-1]
                elif p[j] == "*":
                    x[i][j] = x[i][j-2] or int(x[i-1][j] and p[j-1] in {s[i], '.'})

        return bool(x[-1][-1])