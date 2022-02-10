class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x = len(grid[0])
        y = len(grid)
        c = 0
        
        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    if i == 0:
                        c += 1
                    elif grid[i - 1][j] == 0:
                        c += 1
                        
                    if i == y - 1:
                        c += 1
                    elif grid[i + 1][j] == 0:
                        c += 1
                    
                    if j == 0:
                        c += 1
                    elif grid[i][j - 1] == 0:
                        c += 1
                    
                    if j == x - 1:
                        c += 1
                    elif grid[i][j + 1] == 0:
                        c += 1
        return c