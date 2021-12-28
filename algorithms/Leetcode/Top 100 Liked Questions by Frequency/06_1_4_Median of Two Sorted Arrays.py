"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
"""
O(n) solution
"""
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        # print(merged)
        if len(merged)%2!=0:
            median = len(merged)//2
            return merged[median]
        else:
            median = len(merged)//2
            # print( merged[median], merged[median-1])
            return (merged[median] + merged[median-1])/2

s = Solution()
nums1 = [1,3]
nums2 = [2,3]
print(s.findMedianSortedArrays(nums1, nums2))
