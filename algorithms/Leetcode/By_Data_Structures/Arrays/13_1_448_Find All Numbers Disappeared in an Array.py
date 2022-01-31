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

"""
Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def findDisappearedNumbers(self, arr: [int]) -> [int]:
        hashMap = {}
        for num in arr:
            hashMap[num] = 1

        result = []

        for num in range(1, len(arr)+1):
            if num not in hashMap:
                result.append(num)

        return result

s = Solution()
nums = [4,3,2,7,8,2,3,1]
# nums = [1,2,3,3,5,5,7,7,9,9]
# nums=[1,1,1]
print(s.findDisappearedNumbers(nums))



