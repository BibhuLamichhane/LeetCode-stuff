class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [i for i in s]
        indices = []
        vowels = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                indices.append(i)
                vowels.append(s[i])
        l = len(indices)
        for i in range(l):
            s[indices[i]] = vowels[l - 1 - i]
        
        o = ''
        for i in s:
            o += i
        return o
            