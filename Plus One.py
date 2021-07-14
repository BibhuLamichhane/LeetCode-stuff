class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        n = 1 + int(s)
        return [int(i) for i in str(n)]