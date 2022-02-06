class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = list(set(nums))
        x = [nums.count(i) for i in s]
        return s[x.index(max(x))]
