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

class Solution():
    def sortArrayByParity(self, arr):
        # arr.sort(key = lambda x: x % 1)
        arr.sort(key = lambda x : x%2 )
        return arr

    def moveZeros(self, arr):
        arr.sort(key = lambda x: x==0)
        return arr

s = Solution()
arr = [1,2,3,0,4,0,5,6]
print(s.sortArrayByParity(arr))
arr = [-4,0,5,1,0,3,0]
print(s.moveZeros(arr))