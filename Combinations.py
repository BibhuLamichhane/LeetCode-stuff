import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        o = []
        vals = list(itertools.combinations(range(1, n + 1), k))
        for v in vals:
            o.append(list(v))
        return o