"""
Runtime: 32 ms, faster than 93.65%
Memory Usage: 13.9 MB, less than 99.92%
"""
class Solution:
    def merge(self, nums1:[int], m: int, nums2:[int], n: int) -> None:
        while n: # if n is 0, nums1 will remain unaltered
            if m and nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1]=nums1[m-1]
                m-=1
            else: # In case m is 0, we update nums1 from nums2 in the else section
                nums1[m+n-1] = nums2[n-1]
                n-=1

s = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
nums1 = [1,2,3]
m = 3
nums2 = [0]
n = 0
s.merge(nums1, m, nums2, n)