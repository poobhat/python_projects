"""You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF
as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a
gate, it should be filled with INF.

Input: rooms =
[[2147483647,-1,0,2147483647],
[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],
[2,2,1,-1],
[1,-1,2,-1],
[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""
"""
BFS with Array
"""
"""
Runtime: 341 ms, faster than 52.35%
Memory Usage: 18 MB, less than 34.48%

Complexity analysis
Time complexity : O(mn).
If you are having difficulty to derive the time complexity, start simple.
Let us start with the case with only one gate. The breadth-first search takes at most m 
times m×n steps to reach all rooms, therefore the time complexity is O(mn). But what if 
you are doing breadth-first search from k gates?

Once we set a room's distance, we are basically marking it as visited, which means each 
room is visited at most once. Therefore, the time complexity does not depend on the number 
of gates and is O(mn)

Space complexity : O(mn). 
The space complexity depends on the queue's size. We insert at most m times m×n points 
into the queue.
"""
class Solution:
    def wallsAndGates(self, rooms: [[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        length = len(rooms)
        breadth = len(rooms[0])
        queue = []
        for i in range(length):
            for j in range(breadth):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        for i,j in queue:
            dist = rooms[i][j]+1
            for I,J in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0 <= I < length and 0 <= J < breadth and rooms[I][J] > 2**30:
                    rooms[I][J] = dist
                    queue.append((I,J))
