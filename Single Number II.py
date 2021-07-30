class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        while True:
            temp = nums[0]
            nums.remove(temp)
            if temp in nums:
                nums.remove(temp)
                nums.remove(temp)
            else:
                return temp