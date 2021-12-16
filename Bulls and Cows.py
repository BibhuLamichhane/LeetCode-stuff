class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l_s = [i for i in secret]
        l_g = [i for i in guess]
        b_c = 0
        c_c = 0
        for i in range(len(l_g)):
            if l_g[i] == l_s[i]:
                b_c += 1
                l_s[i] = 'x'
                l_g[i] = 'y'
        for i in range(len(l_g)):
            if l_g[i] in l_s:
                l_s[l_s.index(l_g[i])] = 'x'
                c_c += 1
        return f'{b_c}A{c_c}B'