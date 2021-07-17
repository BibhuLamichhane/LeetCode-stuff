class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        record = []
        l1 = len(matrix)
        l2 = len(matrix[0])
        for i in range(l1):
            for j in range(l2):
                if matrix[i][j] == 0:
                    record.append([i, j])
                    
        for i in record:
            x, y = i
            while x != -1:
                matrix[x][y] = 0
                x -= 1
            x, y = i
            while x != l1:
                matrix[x][y] = 0
                x += 1
            x,y = i
            while y != -1:
                matrix[x][y] = 0
                y -= 1
            x, y = i
            while y != l2:
                matrix[x][y] = 0
                y += 1