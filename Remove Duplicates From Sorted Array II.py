class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        for i in set(nums):
            if nums.count(i) > 2:
                while nums.count(i) > 2:
                    nums.remove(i)
                    c += 1
                    nums.append('_')
        return len(nums) - c