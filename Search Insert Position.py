class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        out = -1
        l = 0
        h = len(nums) - 1
        if target in nums:
            while True:
                mid = (l + h)//2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] > target:
                        h = mid - 1
                    else:
                        l = mid + 1
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
            
