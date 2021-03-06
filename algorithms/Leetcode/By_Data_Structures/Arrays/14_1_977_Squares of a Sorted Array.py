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
Two-pointer approach

Runtime: 226 ms, faster than 79.11%
Memory Usage: 16.3 MB, less than 13.01%
"""
class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:

        n = len(nums)
        num, left, right = 0,0, n-1
        answer = [0]*n

        for i in range(n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                num = nums[left]
                left+=1
            else:
                num = nums[right]
                right-=1
            answer[i] = num*num

        return answer

s = Solution()
nums = [-4,-1,0,3,10]
n1=[-4,-3,-2,-1,0]
print(s.sortedSquares(n1))





