class Solution:
    def calculate(self, s: str):
        while ')' in s:
            i = s.index(')')
            j = len(s[:i]) - s[:i][::-1].index('(') - 1
            eqn = s[j:i+1]
            eqn_list = self.eqn_to_list(eqn[1:-1])
            solved_eqn = self.solve(eqn_list)
            s = s[: j] + solved_eqn + s[i + 1:]
            
        return int(self.solve(self.eqn_to_list(s)))
        
    def solve(self, eqn):
        while len(eqn) > 1:
            if eqn[1] == '+':
                eqn[2] = int(eqn[0]) + int(eqn[2])
                eqn.pop(0)
                eqn.pop(0)
            else:
                eqn[2] = int(eqn[0]) - int(eqn[2])
                eqn.pop(0)
                eqn.pop(0)
        return str(eqn[0])

    def eqn_to_list(self, s):
        o = []
        flag = True
        x = '0'
        for i in range(len(s)):
            if s[i] in '+-':
                o.append(x)
                o.append(s[i])
                x = '0'
            else:
                x += s[i].strip()
        o.append(x)
        while '0' in o:
            i = o.index('0')
            if i == 0:
                o[2] = o[1] + o[2]
                o.pop(1)
                o.remove('0')
            else:
                if o[i - 1] == o[i + 1]:
                    o = o[:i - 1] + ['+'] + o[i + 2:]
                else:
                    o = o[:i - 1] + ['-'] + o[i + 2:]
                    
        return o