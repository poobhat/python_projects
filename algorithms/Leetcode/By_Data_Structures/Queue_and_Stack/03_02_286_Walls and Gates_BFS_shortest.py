class Solution:
    def wallsAndGates(self, rooms: [[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        """
        Runtime: 307 ms, faster than 63.17%
        Memory Usage: 18 MB, less than 32.97%
        """
        q = [(i,j) for i, row in enumerate(rooms) for j, ro in enumerate(row) if not ro]
        for i,j in q:
            for I,J in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                    rooms[I][J] = rooms[i][j]+1
                    q.append((I,J))