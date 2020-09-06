class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            0:'', 1: 'I', 2: 'II', 
            3: 'III', 4: 'IV', 5: 'V', 
            6: 'VI', 7: 'VII', 8: 'VIII', 
            9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX',
            40: 'XL', 50: 'L', 60: 'LX', 
            70: 'LXX', 80: 'LXXX', 90: 'XC' ,
            100: 'C', 200: 'CC', 300: 'CCC', 
            400: 'CD', 500: 'D', 600: 'DC', 
            700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
            2000: 'MM',  3000: 'MMM'
        }
        nums = [int(i) for i in str(num)]
        c = len(nums) - 1
        counter = 0
        while c != 0:
            nums[counter] = nums[counter] * 10 ** c
            counter += 1
            c -= 1
        print(nums)
        s = ''
        for num in range(len(nums)):
            x = symbols.get(nums[num])
            s += x
        return s