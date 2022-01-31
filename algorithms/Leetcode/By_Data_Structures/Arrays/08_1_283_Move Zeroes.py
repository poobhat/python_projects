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
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        i = 0
        while i <= n:
            if nums[i] == 0:
                nums.pop(i)     # Whenever the current element is zero, pop it
                                # and append 0 at the end of the list
                nums.append(0)
                n-=1            # Length of the array to lookup is now reduced by 1 element
            else:
                i+=1            # If current element is non-zero, move the pointer forward by 1
        return nums

s = Solution()
arr = [0,1,0,3,12]
print(s.moveZeroes(arr))