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
run time complexity should be O(log (m+n)).
"""

import math
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x = len(nums1)
        y = len(nums2)

        low = 0
        high = x
        while low <= high:
            partitionX = (high+low)//2
            partitionY = ((x+y+1)//2) - partitionX

            maxLeftX = -math.inf if partitionX == 0 else nums1[partitionX-1]
            minRightX = math.inf if partitionX == x else nums1[partitionX]

            maxLeftY = -math.inf if partitionY == 0 else nums2[partitionY-1]
            minRightY = math.inf if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if not (x+y)%2:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX-1
            else:
                low = partitionX+1

        raise ValueError

s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1, nums2))