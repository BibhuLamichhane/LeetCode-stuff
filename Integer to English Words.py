class Solution:
    def numberToWords(self, num: int) -> str:
        a = {
            '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten',
            '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen',
            '19': 'Nineteen', '20': 'Twenty', '30': 'Thirty', '40': 'Forty', '50': 'Fifty',
            '60': 'Sixty', '70': 'Seventy', '80': 'Eighty', '90' : 'Ninety', '0': ''
        }
        b = {'3': 'Hundred',
             '4': 'Thousand',
             '7': 'Million', 
             '10': 'Billion'}

        def tens(n):
            if n[0] == '1':
                return a[n].strip()
            elif n[0] == '0':
                return a[n[-1]].strip()
            else:
                return f"{a[n[0] + '0']} {a[n[-1]]}".strip()
        
        def hundreds(n):
            o = ''
            if n[0] == '0':
                return tens(n[1:]).strip()
            else:
                o += f'{a[n[0]]} Hundred '
                o += tens(n[1:])
            return o.strip()

            
        def thousands(n):
            o = ''
            l = len(n)
            if l == 4:
                if n[0] == '0':
                    return hundreds(n[1:]).strip()
                o += f'{a[n[0]]} Thousand '
                o += hundreds(n[1:])
            elif l == 5:
                if n[0] == '0':
                    return thousands(n[1:]).strip()
                else:
                    o += f"{tens(n[:2])} Thousand "
                    o += hundreds(n[2:])
            else:
                if n[0] == '0':
                    return thousands(n[1:]).strip()
                else:
                    o += f"{hundreds(n[:3])} Thousand "
                    o += hundreds(n[3:])
            return o.strip()
            
        def millions(n):
            o = ''
            l = len(n)
            if l == 7:
                if n[0] == '0':
                    return thousands(n[1:]).strip()
                o += f'{a[n[0]]} Million '
                o += thousands(n[1:])
            elif l == 8:
                if n[0] == '0':
                    return millions(n[1:]).strip()
                else:
                    o += f"{tens(n[:2])} Million "
                    o += thousands(n[2:])
            else:
                if n[0] == '0':
                    return millions(n[1:]).strip()
                else:
                    o += f"{hundreds(n[:3])} Million "
                    o += thousands(n[3:])
            return o.strip()
        
        def billions(n):
            o = ''
            l = len(n)
            if l == 10:
                if n[0] == '0':
                    return millions(n[1:]).strip()
                o += f'{a[n[0]]} Billion '
                o += millions(n[1:])
            elif l == 11:
                if n[0] == '0':
                    return billions(n[1:]).strip()
                else:
                    o += f"{tens(n[:2])} Billion "
                    o += millions(n[2:])
            else:
                if n[0] == '0':
                    return billions(n[1:]).strip()
                else:
                    o += f"{hundreds(n[:3])} Billion "
                    o += millions(n[3:])
            return o.strip()
        
        x = str(num)
        l = len(x)
        if x == '0':
            return 'Zero'
        if l == 1:
            return a[x]
        elif l == 2:
            return tens(x)
        elif l == 3:
            return hundreds(x)
        elif 3 < l < 7:
            return thousands(x)
        elif 7 <= l < 10:
            return millions(x)
        else:
            return billions(x)