class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        p1=p2=0
        nums1.sort()
        nums2.sort()
        print(nums1, nums2)
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1] > nums2[p2]:
                p2+=1
            else:
                p1+=1
        return result


s = Solution()
a1 = [4,9,5]
a2 = [9,4,9,8,4]
print(s.intersect(a1, a2))
