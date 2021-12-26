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
87.16% faster than all of python submission
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        lengthWithZeros, withoutZeros, answer = 0, 0, 0
        for num in nums:
            if num == 1:
                lengthWithZeros += 1
                withoutZeros += 1
            else:
                lengthWithZeros = withoutZeros+1
                withoutZeros = 0
            answer = max(answer, lengthWithZeros)
        return answer
s = Solution()
nums = [1,0,1,0,1,1]
print(s.findMaxConsecutiveOnes(nums))


