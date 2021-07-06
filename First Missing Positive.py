class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        low = min(nums)
        high = max(nums)
        if low == 1 and high == len(set(nums)):
            return high + 1
        if 1 not in nums:
            return 1
        else:
            return_val = -99
            if low <= 0:
                low = 1
            for i in range(low, high + 1):
                if i not in nums:
                    return_val = i
                    break
        if return_val == -99:
            return high + 1
        else:
            return return_val