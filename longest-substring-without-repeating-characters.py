class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        string = ''
        a = {x for x in s}
        if len(a) == len(s):
            return len(s)
        else:
            for i in range(len(s)):
                string = s[i]
                for j in range(i + 1, len(s)):
                    if s[j] in string:
                        substrings.append(string)
                        break
                    else:
                        string += s[j]
                substrings.append(string)
            lengths = [len(substring) for substring in substrings]
            return max(lengths)