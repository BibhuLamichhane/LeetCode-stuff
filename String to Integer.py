class Solution:
    def myAtoi(self, string: str) -> int:
        num = ''
        u = 2 ** 31 - 1
        l = -2 ** 31
        string = string.strip()
        if len(string) > 0:
            if string[0] not in '-+0123456789 ':
                return 0
            else:
                num += string[0]
            for i in range(1, len(string)):
                if string[i] in '.0123456789':
                    num += string[i]
                else:
                    try:
                        num = int(float(num))
                        if num > u:
                            num = u
                        elif num < l:
                            num = l
                        return num
                    except:
                        return 0
            try:
                num = int(float(num))
            except:
                return 0
            if num > u:
                num = u
            elif num < l:
                num = l
            return num
        else:
            return 0

