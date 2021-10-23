class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        o = [[]]
        for i in range(1, len(nums) + 1):
            vals = itertools.combinations(nums, i)
            for v in vals:
                o.append(list(v))
        return o