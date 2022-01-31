"""
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?

"""
"""
Timesort O(N)
Runtime: 224 ms, faster than 83.62%
Memory Usage: 16.4 MB, less than 5.51%
"""
class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        sorted_nums = sorted(nums, key=lambda x:abs(x))
        return [x**2 for x in sorted_nums]

s = Solution()
nums = [-4,-1,0,3,10]
n1=[-4,-3,-2,-1,0]
print(s.sortedSquares(n1))





