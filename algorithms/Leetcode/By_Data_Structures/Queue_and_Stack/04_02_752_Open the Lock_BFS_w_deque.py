"""
Breadth-First-Search:

We are given a string start = "0000" and asked to reach target by turning (minimum times)
a digit forward or backward one at a time without reaching any of the strings in deadends.

We can't just turn a digit forward or backward just based on which turn gets us quicker to
the corresponding digit of target faster because this approach may lead us towards a
deadend. So, it makes sense to try and turn a digit in both the direction and return the
one that leads to target in minimum moves.

The solution can be modelled as a BFS traversal, wherein we try to shift each digit of
current string curstr in both the possible direction. We increment turns at each level of
BFS and return when target is reached during the traversal.

We use a hashset to insert all the deadends string for efficient check on whether we reach
a deadend at anytime. Similarly, we store all the visited string in visited to ensure that
we won't revisit a string again. For BFS traversal, we would also require to maintain a
queue. The algorithm can be summed up into following steps:-

Insert all strings from deadends into a hashset and also maintain a visited set for all
strings traversed so far. --> This is the key to avoid TLE errors!!!!!!!!!!!!!!!!!

Start BFS traversal from "0000" by pushing it into the queue and looping till the queue
becomes empty.
At each level of BFS, take the current string and try turning each digit in both forward &
backward direction. For eg. we can apply the turning process on "0000" to
get ["1000", "9000", "0100", "0900", "0010", "0090", "0001", "0009"].
If any of the strings after applying turning process become equal to target, return the
turns required till now.
Else, just push the turned strings into the queue, insert it into visited set and repeat
the same process for all strings in the queue.
If the queue becomes empty, we have tried all possible paths to reach target and failed.
So return -1.
"""
###############################################################
"""
Runtime: 688 ms, faster than 67.79%
Memory Usage: 15.2 MB, less than 91.29%
"""
###############################################################
"""
Time Complexity : O(N), where N is the number of strings in deadends 
and O(N) is required to insert all the strings into the hashset. 

The BFS traversal requires O(1). It may be strange but that's how you calculate big O 
complexity. The time required by our BFS traversal doesn't depend on the input and in the 
worst case, we end up making 10000 iterations at max. 

Space Complexity : O(N)
"""


from collections import deque
class Solution:
    def openLock(self, deadends: [str], target: str) -> int:
        def neighbours(code):
            for i in range(len(code)):
                val = int(code[i])
                for nei in (val+1, val-1):
                    neighbour = (nei+10)%10
                    yield code[:i] + str(neighbour) + code[i+1:]

        if "0000" in deadends: return -1
        steps = 0
        queue = deque(["0000"])
        visited = set(deadends)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return steps
                visited.add(curr)

                for neighbour in neighbours(curr):
                    if neighbour in visited: continue
                    queue.append(neighbour)
                    visited.add(neighbour)
            steps += 1
        return -1