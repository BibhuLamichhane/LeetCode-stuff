class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        vals = {}
        for i in set(nums):
            vals[i] = nums.count(i)
        
        o = []
        l = len(nums)
        for i in vals:
            if vals[i] > l/3:
                o.append(i)
        return o