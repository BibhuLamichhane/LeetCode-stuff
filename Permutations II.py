class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        vals = list(itertools.permutations(nums))
        o = []
        for i in range(len(vals)):
            vals[i] = list(vals[i])
            if vals[i] not in o:
                o.append(vals[i])
        return o