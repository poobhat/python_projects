"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
####################################################################
"""
Runtime: 140 ms, faster than 15.69% 
Memory Usage: 14.7 MB, less than 99.46%
"""

class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        i=0
        n=len(nums)
        for j in range(n):
            if not nums[j]%2:
                if nums[i]%2:
                    nums[i], nums[j] = nums[j], nums[i]
                i+=1
        return nums

s = Solution()
nums = [8,3,1,2,4,5,6,0]
print(s.sortArrayByParity(nums))

