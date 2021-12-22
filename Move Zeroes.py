class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = nums[:]
        while 0 in a:
            a.remove(0)
            nums.remove(0)
            nums.append(0)
        