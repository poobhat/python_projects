"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

"""
Brute force; Time limit exeeded
"""
class Solution:
    def trap(self, height: [int]) -> int:
        answer = 0
        n = len(height)
        for i in range(n): # For the current entry, find out the max value to its left and to its right
            left_max, right_max = 0, 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])  # Get the maximum in comparison to the current value itself, both towards its right and the left
            for j in range(i,n):
                right_max = max(right_max, height[j])
            answer += min(left_max, right_max) - height[i]
        return answer

s = Solution()
height = [4,2,0,3,2,5]
print(s.trap(height))
