class Solution:
    def isInteger(self, n):
        val = ''
        for i in n:
            val += i
        try:
            int(val)
            return True
        except:
            return False
    
    def isDecimal(self, n):
        val = ''
        for i in n:
            val += i
        try:
            float(val)
            return True
        except:
            return False
            
    def isNumber(self, s: str) -> bool:
        vals = [i for i in s.lower()]
        
        if 'e' in vals:
            before = vals[:vals.index('e')]
                
            if '.' in before:
                if not self.isDecimal(before):
                    return False
            else:
                if not self.isInteger(before):
                    return False
            after = vals[vals.index('e') + 1:]
            if not self.isInteger(after):
                return False
        else:
            if '.' in vals:
                if not self.isDecimal(vals):
                    return False
            else:
                if not self.isInteger(vals):
                    return False
                                
        return True