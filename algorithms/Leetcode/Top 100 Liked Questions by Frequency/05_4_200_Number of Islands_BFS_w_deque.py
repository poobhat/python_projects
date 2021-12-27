"""
BFS : Breadth First Search - 62% faster

Time complexity : O(M×N) where M is the number of rows and N is the number
of columns.

Space complexity : O(min(M,N)) because in worst case where the grid is filled
with lands, the size of queue can grow up to min(M,N).

"""
from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid,i,j)
                    answer += 1
        return answer

    def bfs(self,grid,i,j):
        qu = deque([(i,j)])
        while qu:
            i,j = qu.popleft()
            for i,j in (i+1,j), (i-1,j), (i, j+1), (i, j-1):
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j]='0'
                    qu.append((i,j))
s=Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))