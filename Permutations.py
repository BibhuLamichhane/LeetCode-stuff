class Solution:
    def conditions(self, vals):
        x = []
        l = len(vals)
            
        for i in range(l):
            for j in range(l):
                if i != j:
                    curr = [vals[i], vals[j]]
                    curr.sort()
                    if curr not in x:
                        x.append(curr)
        o = ''
        for v in x:
            o += f'{v[0]} != {v[1]} and '
        o = o[:-4]
        return o
    
    def permute(self, nums):
        o = []
        l = len(nums)
        vals = []
        if l <= 1:
            o.append(nums)
        else:
            for i in range(l):
                vals.append(chr(65 + i))
            code = ''
            x = 65
            for i in range(l):
                curr = '\t' * i 
                curr += f'for {chr(x)} in range ({l}):\n'
                code += curr
                x += 1
            code += ('\t' * l) + 'if ' + self.conditions(vals) + ':\n' 
            a = 'o.append(['
            for v in vals:
                a += f'nums[{v}],'
            a = a[:-1] + '])'
            code += ('\t' * (l + 1)) + a
            print(code)
            exec(code)
        return o