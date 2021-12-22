class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        o = []
        c = 0
        for i in set(nums):
            if nums.count(i) == 1:
                o.append(i)
                c += 1
            if c == 2:
                break
                
        return o
                