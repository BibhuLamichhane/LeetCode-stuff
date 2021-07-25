class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        o = [[]]
        for i in range(1, len(nums) + 1):
            vals = itertools.combinations(nums, i)
            for v in vals:
                t = list(v)
                t.sort()
                if t not in o:
                    o.append(t)
        return o