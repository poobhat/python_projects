"""
Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j)
such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.

Example 1:

Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
Output: 1
Explanation: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.
Example 2:

Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
Output: 5
Explanation: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.
"""

class Solution:
    def countPairs(self, nums1: [int], nums2: [int]):
        list1=[]
        list2=[]
        for i in range(0,len(nums1)-1):
            list1.append(nums1[i]-nums2[i])
            j=i+1
            list2.append(nums2[j]-nums1[j])

        for num in list1:
            low=0
            high=len(list1)-1
            while high > low:
                mid = (low+high)//2
                pass

        print(list1)
        print(list2)

s = Solution()
nums1 = [1,10,6,2]
nums2 = [1,4,1,5]
# nums1 = [2,1,2,1]
# nums2 = [1,2,1,2]
print(s.countPairs(nums1, nums2))