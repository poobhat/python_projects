"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]


Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

"""
Array, sorting
"""

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        # sort intervals
        # compare the end of the previous interval with beginning of the current
        # interval

        intervals.sort()
        answer = []

        for interval in intervals:
            # To the empty answer list, append the first inveral
            # Keep on appending intervals as long as there are no overlaps of intervals
            if answer == [] or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:                                               # When there is overalp of intervals ..
                                                                # .. the end value of the existing interval should be the max of the end values of overlapping intervals
                answer[-1][1] = max(answer[-1][1], interval[1])

        return answer



s = Solution()
intervals = [[1,5],[2,6],[8,10],[15,18]]
print(s.merge(intervals))





