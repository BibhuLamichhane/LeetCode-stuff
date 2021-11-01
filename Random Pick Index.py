class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        indices = []
        while target in self.nums:
            x = self.nums.index(target)
            indices.append(x)
            self.nums[x] = ''
        while '' in self.nums:
            x = self.nums.index('')
            self.nums[x] = target
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)