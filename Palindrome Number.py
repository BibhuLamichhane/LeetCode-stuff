class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Converting int to string
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False

        # Without converting int to str
        if x < 0:
            return False
        else:
            a = x
            num = 0
            while a != 0:
                r = a % 10
                num = (num * 10) + r
                a = a // 10
            if num == x:
                return True
            else:
                return False