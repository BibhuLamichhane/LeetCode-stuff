class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = []
        while i < j:
            if height[i] < height[j]:
                min_height = height[i]
                min_heightIndex = i
            else:
                min_height = height[j]
                min_heightIndex = j
            area.append((j - i) * min_height)
            if i + 1 == min_heightIndex + 1:
                i += 1
            else:
                j -= 1
        return max(area)
