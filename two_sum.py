class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            index = i
            curr_num = nums[i]
            diff = target - curr_num
            if diff in nums:
                index2 = nums.index(diff)
                if index != index2:
                    return [index, index2]