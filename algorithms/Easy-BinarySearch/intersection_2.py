class Solution(object):

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]


    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


if __name__=="__main__":
    obj = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(obj.intersection(nums1=nums1, nums2=nums2))





