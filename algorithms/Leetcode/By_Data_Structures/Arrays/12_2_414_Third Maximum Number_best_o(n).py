"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?
"""
#################################################################
"""
Runtime: 48 ms, faster than 93.03%
Memory Usage: 14.8 MB, less than 95.00%
"""
class Solution:
    def thirdMax(self, nums: [int]) -> int:
        a = b = c = -float("inf")
        for num in nums:
            if num in (a, b, c): continue
            if num > a:   # (4, -inf, -inf), (5, 4, -inf), (6, 5, 4), (7, 6, 5)
                num, a = a, num
            if num > b: # (9, -inf, -inf), (9, 6, -inf),  (9,7,6)
                num, b = b, num
            if num > c: # (1, -inf, -inf), (2,1,-inf)
                num, c = c, num
        return a if c==-float("inf") else c

s = Solution()
n1, n2, n3 = [1,2], [4,5,6,7], [9,6,3,7,1]
print(s.thirdMax(n1))
print(s.thirdMax(n2))
print(s.thirdMax(n3))
