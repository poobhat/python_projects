"""
Sliding window problem

In any sliding window based problem we have two pointers. One right pointer whose job is to expand the current window and then we have
the left pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other one remains fixed.


The solution is pretty intuitive. We keep expanding the window by moving the right pointer. When the window has reached the limit of 0's allowed, we contract (if possible) and save the longest window till now.

The answer is the longest desirable window.

Algorithm

Initialize two pointers. The two pointers help us to mark the left and right end of the window/subarray with contiguous 1's.

left = 0, right = 0, window_size = 0

We use the right pointer to expand the window until the window/subarray is desirable. i.e. number of 0's in the window are in
the allowed range of [0, k].

Once we have a window which has more than the allowed number of 0's, we can move the left pointer ahead one by one until we encounter
0 on the left too. This step ensures we are throwing out the extra zero.

Note: As suggested in the discussion forum. We can solve this problem a little efficiently.
Since we have to find the MAXIMUM window, we never reduce the size of the window. We either increase the size of the window or remain same but never reduce the size
"""

class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:

        left = right = 0
        windowSize = 0
        zeros = 0
        answer = 0

        while left <= right < len(nums) :
            zeros = (zeros + 1) if nums[right] == 0 else zeros
            if zeros <= k:
                windowSize+=1
                answer=max(answer, windowSize)
                right+=1
            else:
                zeros = (zeros-1) if nums[left] == 0 else zeros
                left+=1
                right+=1
        return answer

s = Solution()
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k=3
print(s.longestOnes(nums, k))