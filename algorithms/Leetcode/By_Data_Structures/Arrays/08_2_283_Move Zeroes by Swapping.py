"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums: [int]) -> None:

        zeroPtr = 0

        for ptr in range(len(nums)):
            # Swap zero with non-zero element
            if nums[ptr] != 0 and nums[zeroPtr] == 0:
                nums[ptr], nums[zeroPtr] = nums[zeroPtr], nums[ptr]
            # When zero pointer is at a non-zero element increment it
            if nums[zeroPtr] != 0:
                zeroPtr += 1

        return nums

s = Solution()
arr = [0,1,0,3,12]
print(s.moveZeroes(arr))