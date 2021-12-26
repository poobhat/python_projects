"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
# [4,3,2,7,8,2,3,1]
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        n = len(nums)
        nums = list(set(nums))
        nums.sort()
        return list(range(nums[-1],n+1))

s = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1,1,2,2]
print(s.findDisappearedNumbers(nums))
