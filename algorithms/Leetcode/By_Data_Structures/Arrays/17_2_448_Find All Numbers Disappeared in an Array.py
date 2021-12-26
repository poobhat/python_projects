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

class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        #[4,3,2,7,8,2,3,1]
        answer = []

        # Iterate over each element in the array
        for i in range(len(nums)):

            # Treat every element as a new index and negate the element at the new index
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        print(nums)

        # If a number is still not negative, the number corresponding to that index is missing
        for i in range(1, len(nums)):
            if nums[i] > 0:
                answer.append(i+1)
        return answer

s = Solution()
# nums = [4,3,2,7,8,2,3,1]
# nums = [1,2,3,3,5,5,7,7,9,9]
nums=[1,1,1]
print(s.findDisappearedNumbers(nums))
