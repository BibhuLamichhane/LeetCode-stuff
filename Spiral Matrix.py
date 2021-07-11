class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[0, 0]]
        o = [matrix[0][0]]

        x, y = 0, 0
        l1 = len(matrix)
        l2 = len(matrix[0])
            
            
        flag = True
            
        while flag:
                
            flag = False
                
            y += 1
                
            while y < l2 and ([x, y] not in visited):
                o.append(matrix[x][y])
                visited.append([x, y])
                y += 1
                flag = True
                    
      
                
            y -= 1
            x += 1
                
            while  x < l1 and ([x, y] not in visited):
                o.append(matrix[x][y])
                visited.append([x, y])
                x += 1
                flag = True
                

            x -= 1
            y -= 1
                
            while y > -1 and ([x, y] not in visited):
                o.append(matrix[x][y])
                visited.append([x, y])
                y -= 1
                flag = True
                

            y += 1
            x -= 1
                
            while x > -1 and ([x, y] not in visited):
                o.append(matrix[x][y])
                visited.append([x, y])
                x -= 1
                flag = True
                

            x += 1
        return o
            