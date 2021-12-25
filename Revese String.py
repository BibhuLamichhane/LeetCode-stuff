class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x = s[::-1]
        for i in range(len(x)):
            s[i] = x[i]