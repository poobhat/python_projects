"""
Union-find : Union by Rank - Disjoint Set
"""

"""
**** Why use union-by-rank ?

If the roots are distinct, the trees are combined by attaching the root of one to the root of the other. 
If this is done naively, such as by always making x a child of y, the height of the trees can grow as O(n). 
To prevent this union by rank or union by size is used.

Union by rank always attaches the shorter tree to the root of the taller tree. Thus, the resulting tree is no taller than 
the originals unless they were of equal height, in which case the resulting tree is taller by one node.
To implement union by rank, each element is associated with a rank. Initially a set has one element and a rank of zero. 
If two sets are unioned and have the same rank, the resulting set's rank is one larger; otherwise, if two sets are unioned 
and have different ranks, the resulting set's rank is the larger of the two. Ranks are used instead of height or depth because 
path compression will change the trees' heights over time

"""

"""
68.15% faster, 17.89% more memory savvy 

Time complexity : O(M×N) where M is the number of rows and N is the number 
of columns. Note that Union operation takes essentially constant time[1] when UnionFind is 
implemented with both path compression and union by rank.

Space complexity : O(M×N) as required by UnionFind data structure.

"""

class Solution(object):
    def numIslands(self, grid):

        if not grid: return 0

        rowLength = len(grid)
        colLength = len(grid[0])
        self.answer = sum(grid[i][j] == '1' for i in range(rowLength) for j in range(colLength))
        parent = list(range(rowLength * colLength))
        rank = [0] * rowLength * colLength

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot
            parent[yroot] = xroot
            rank[xroot] = max(rank[xroot],rank[yroot]+1)
            self.answer-=1

        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == '0':
                    continue
                index = i * colLength + j
                if i < rowLength-1 and grid[i+1][j] == '1':
                    union(index, index+colLength)
                if j < colLength-1 and grid[i][j+1] == '1':
                    union(index, index+1)
        return self.answer


s=Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

# grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]]
print(s.numIslands(grid))







