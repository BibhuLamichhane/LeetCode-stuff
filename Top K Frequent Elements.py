class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = list(set(nums))
        vals_count = []
        for i in set(nums):
            vals_count.append(nums.count(i))
        o = []
        for i in range(k):
            o.append(vals[vals_count.index(max(vals_count))])
            vals_count[vals_count.index(max(vals_count))] = float('-inf')
        return o