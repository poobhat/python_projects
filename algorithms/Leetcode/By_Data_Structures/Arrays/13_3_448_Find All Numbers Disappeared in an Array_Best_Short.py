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

Follow up: Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""
#########################################################################
"""
Runtime: 360 ms, faster than 73.55%
Memory Usage: 21.8 MB, less than 85.20%
"""
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        for num in nums:
            index = abs(num)-1
            nums[index] = - abs(nums[index])
        return [i+1 for i,n in enumerate(nums) if n > 0]

s = Solution()
# nums = [4,3,2,7,8,2,3,1]
# nums = [1,2,3,3,5,5,7,7,9,9]
nums=[1,1,1]
print(s.findDisappearedNumbers(nums))
