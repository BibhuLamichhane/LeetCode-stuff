class Solution:
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[0, 0]]
        x, y = 0, 0
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
        l1 = len(matrix)
        l2 = len(matrix[0])
        matrix[0][0] = 1
        z = 2
        flag = True 
        while flag:   
            flag = False   
            y += 1 
            while y < l2 and ([x, y] not in visited):
                matrix[x][y] = z
                z += 1
                visited.append([x, y])
                y += 1
                flag = True
            y -= 1
            x += 1 
            while  x < l1 and ([x, y] not in visited):
                matrix[x][y] = z
                z += 1
                visited.append([x, y])
                x += 1
                flag = True   
            x -= 1
            y -= 1 
            while y > -1 and ([x, y] not in visited):
                matrix[x][y] = z
                z += 1
                visited.append([x, y])
                y -= 1
                flag = True 
            y += 1
            x -= 1  
            while x > -1 and ([x, y] not in visited):
                matrix[x][y] = z
                z += 1
                visited.append([x, y])
                x -= 1
                flag = True
            x += 1

        return matrix 