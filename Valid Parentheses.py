class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        while True:
            if '()' in s:
                index = s.index('()')
                s = s[:index] + s[index + 2:]
            elif '{}' in s:
                index = s.index('{}')
                s = s[:index] + s[index + 2:]
            elif '[]' in s:
                index = s.index('[]')
                s = s[:index] + s[index + 2:]
            else:
                break

        if s == '':
            return True
        else:
            return False
