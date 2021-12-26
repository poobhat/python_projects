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
Approach : Sliding window

We need to establish some rules on how to move our sequence forward.

1) If our sequence is valid, let's continue expanding our sequence (because our goal is to get 
the largest sequence possible).

2) If our sequence is invalid, let's stop expanding and contract our sequence (because an 
invalid sequence will never count towards our largest sequence).

The pattern that comes to mind for expanding/contracting sequences is the sliding window.
Let's define valid and invalid states.

Valid State = one or fewer 0's in our current sequence
Invalid State = two 0's in our current sequence

Algorithm :

Great. How do we apply all this to the sliding window?

Let's use left and right pointers to keep track of the current sequence a.k.a. our window. 
Let's expand our window by moving the right pointer forward until we reach a point where 
we have more than one 0 in our window. When we reach this invalid state, let's contract our 
window by moving the left pointer forward until we have a valid window again. 
By expanding and contracting our window from valid and invalid states, we are able to 
traverse the array efficiently without repeated overlapping work.

Now we can break this approach down into a few actionable steps:

While our window is in bounds of the array...

Add the rightmost element to our window
Check if our window is invalid. If so, contract the window until valid.
Update our the longest sequence we've seen so far
Continue to expand our window

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        left, right, zeros, longestSequence = 0, 0, 0, 0

        while right < len(nums):
            if nums[right] == 0: # Expand the window while counting zeros
                zeros += 1

            while zeros == 2:  # Check if the sequence is valid

                if nums[left] == 0: # Contract the window until the sequence is valid again
                    zeros-=1
                left += 1

            # Check the window size in each iteration to see if the current sequence is the longest yet
            longestSequence = max(longestSequence, right-left+1)
            right += 1

        return longestSequence

s = Solution()
nums = [1,0,1,1,0,1]
print(s.findMaxConsecutiveOnes(nums))

