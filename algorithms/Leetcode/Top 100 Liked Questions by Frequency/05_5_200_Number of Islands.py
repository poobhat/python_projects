"""
Union-find aka disjoint set : 82% faster, 14% memory optimum

Time complexity : O(M×N) where M is the number of rows and N is the number
of columns. Note that Union operation takes essentially constant time[1] when UnionFind is
implemented with both path compression and union by rank.

Space complexity : O(M×N) as required by UnionFind data structure.
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
            # Note: If the roots are distinct, the trees are combined by attaching the root of one to the root of the other.
            # If this is done naively, such as by always making x a child of y, the height of the trees can grow as O(n)
            self.answer -= 1 # Since we added one more 1 to the union, decrement the total count (answer) by 1

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == '0': # When a 0 is encountered, do nothing, continue
                    continue
                index = i * colLength + j  # This is the formula for calculating index in a m x n - array
                if j < colLength-1 and grid[i][j+1] == '1': # If there is a horizontally adjacent 1, add it to the union set
                    union(index, index+1)
                if i < rowLength-1 and grid[i+1][j] == '1': # If there is a vertically adjacent 1, add it to the union set
                    union(index, index+colLength)
        return self.answer

s=Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))