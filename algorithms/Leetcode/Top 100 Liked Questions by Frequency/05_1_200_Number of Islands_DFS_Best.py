"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""
"""
DFS - 88% faster

Time complexity : O(M×N) where M is the number of rows and N is the number of columns.

Space complexity : worst case O(M×N) in case that the grid map is filled with lands 
where DFS goes by M×N deep.
"""

class Solution:
    """
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    """

    def numIslands(self, grid):
        answer = 0
        for rowIdx in range(len(grid)):
            for columnIdx in range(len(grid[0])):
                if grid[rowIdx][columnIdx] == '1': #Check the root for Depth first search
                    self.dfs(grid, rowIdx, columnIdx)
                    # print(grid)
                    answer += 1
        return answer

    def dfs(self, grid, rowIdx, columnIdx):
        grid[rowIdx][columnIdx] = '#'   #mark the already visited vertex with '#' Check the neighbours of the root vertex for 1
        for rOp,cOp in (-1,0),(1,0),(0,1),(0,-1):
            r = rowIdx + rOp
            c = columnIdx + cOp
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                self.dfs(grid, r, c)


        # The above expression can be expanded as below
        # self.dfs(grid, rowIdx-1, columnIdx)
        # self.dfs(grid, rowIdx+1, columnIdx)
        # self.dfs(grid, rowIdx, columnIdx-1)
        # self.dfs(grid, rowIdx, columnIdx+1)

s=Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))