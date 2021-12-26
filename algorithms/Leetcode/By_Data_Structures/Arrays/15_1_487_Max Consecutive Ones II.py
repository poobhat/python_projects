"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can
flip at most one 0.

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping,
the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

Follow up: What if the input numbers come in one by one as an infinite stream? In other words,
you can't store all numbers coming from the stream as it's too large to hold in memory.
Could you solve it efficiently?

"""

"""
Brute force - Quadratic solution
Time complexity : O(n2)
Space complexity : O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        longest_sequence = 0
        for i in range(len(nums)):
            num_zeroes = 0
            for j in range(i, len(nums)):   # check every consecutive sequence
                if nums[j] == 0:               # count how many 0's
                    num_zeroes += 1
                if num_zeroes == 2:
                    break
                if num_zeroes <= 1:                # update answer if it's valid
                    longest_sequence = max(longest_sequence, j - i + 1)
        return longest_sequence

s = Solution()
nums = [1,0,1,1,0]
print(s.findMaxConsecutiveOnes(nums))
