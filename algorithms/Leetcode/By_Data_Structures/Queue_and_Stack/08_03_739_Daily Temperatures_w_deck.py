"""
Runtime: 1261 ms, faster than 64.96%
Memory Usage: 25.3 MB, less than 62.28%
"""
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        answer=[0]*len(temperatures)
        stack = deque()
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer