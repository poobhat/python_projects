class Solution(object):
    def __init__(self):
        self.lookup = []
        self.target = []
        self.result = []

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        self.lookup = set(nums1)
        self.target = set(nums2)

        if len(self.lookup) > len(self.target):
            self.lookup, self.target = self.target, self.lookup

        for each in self.lookup:
            if each in self.target:
                self.result.append(each)

        return self.result

if __name__=="__main__":
    obj = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(obj.intersection(nums1=nums1, nums2=nums2))





