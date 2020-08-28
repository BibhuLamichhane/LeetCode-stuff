class Solution:

    def Convert(self, string):
        list1=[]
        list1[:0]=string
        return list1

    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        a = self.Convert(s)
        b = set(a)
        if len(b) == 1:
            return s
        for i in range(len(s)):
            for j in range(len(s), -1, -1):
                string = s[i : j]
                if string[::-1] == string:
                    palindromes.append(string)
        lengths = [len(palindrome) for palindrome in palindromes]
        try:
            output = palindromes[lengths.index(max(lengths))]
        except:
            output = s
        return output