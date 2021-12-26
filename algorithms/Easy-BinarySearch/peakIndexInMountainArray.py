class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in arr:
            if arr[i] < arr[i+1]:
                pass
            else:
                return i