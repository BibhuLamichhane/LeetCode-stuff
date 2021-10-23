class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = [-1, -1]
        if target in nums:
            out[0] = nums.index(target)
            nums[out[0]] = None
            if target in nums:
                while target in nums:
                    out[1] = nums.index(target)
                    nums[out[1]] = None
            else:
                out[1] = out[0]
        return out
