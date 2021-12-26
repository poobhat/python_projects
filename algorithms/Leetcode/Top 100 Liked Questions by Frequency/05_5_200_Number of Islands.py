"""
Union-find aka disjoint set
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        rowLength = len(grid)
        colLength = len(grid[0])
        self.answer = sum(grid[i][j]=='1' for i in range(rowLength) for j in range(colLength)) # Total number of 1's in the grid
        parent = list(range(rowLength * colLength)) # Expand the grid giving 1-dimensional index value (parent-index) for each element

        def find(x):
            if parent[x]!= x:
                return find(parent[x]) # Traverse back through the parent vertices, until you find a parent which is also the root vertex
            return parent[x] # If parent[x] == x, then x is a root vertex. Don't change its parent

        def union(x,y):
            xroot, yroot = find(x),find(y) # To union 2 vertices, find out their root vertices first
            if xroot == yroot: return # If both the vertices already have same roots, then they are already part of a union set. Do nothing further
            parent[xroot] = yroot # If they both have different roots, merge with the root of one of the two. In this case, root of y
            self.answer -= 1 # Since we added one more 1 to the union, decrement the total count (answer) by 1

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == '0':
                    continue
                index = i*colLength + j
                if j < colLength-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < rowLength-1 and grid[i+1][j] == '1':
                    union(index, index+colLength)
        return self.count

s=Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))