import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        temp = copy.deepcopy(matrix)
        for i in range(l):
            for j in range(l - 1, -1, -1):
                matrix[i][abs(j - l + 1)] = temp[j][i]