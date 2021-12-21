class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        vals = list(itertools.combinations([i for i in range(1, 10)], k))
        o = []
        for v in vals:
            if sum(v) == n:
                o.append(list(v))
                
        return o