class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        for i in nums1:
            nums.append(i)
        for i in nums2:
            nums.append(i)
        nums = sorted(nums)
        n = len(nums)
        median = (n + 1) / 2
        if median == int(median):
            print(median)
            return nums[int(median) - 1]
        else:
            median -= 1
            n1 = int(median)
            n2 = n1 + 1
            median = (nums[n1] + nums[n2]) / 2
            return median