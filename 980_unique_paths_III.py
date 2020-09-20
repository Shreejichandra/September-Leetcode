'''On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.total_path = 0
        total_zero = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_zero += 1
                    
        def dfs(i, j, covered_cells):
            if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1):
                return
            
            cell = grid[i][j]
            if cell == 2 and covered_cells == total_zero:
                self.total_path += 1
                return
            
            if cell == 0:
                grid[i][j] = -1
                dfs(i+1, j, covered_cells + 1)
                dfs(i-1, j, covered_cells + 1)
                dfs(i, j+1, covered_cells + 1)
                dfs(i, j-1, covered_cells + 1)
                grid[i][j] = 0
        
        flag = False
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 1
                    
                    dfs(i + 1, j, 0)
                    dfs(i - 1, j, 0)
                    dfs(i, j + 1, 0)
                    dfs(i, j - 1, 0)
                    
                    flag = True
                    break
                   
        return (self.total_path)
        
