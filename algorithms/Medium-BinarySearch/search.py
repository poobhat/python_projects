# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        first = reader.get(0)
        high = abs(target-first)+1
        low = 0
        while high >= low:
            mid = (high+low)//2
            output = reader.get(mid)
            if output == (2**31)-1:
                high = mid-1
            elif output == target:
                return mid
            elif output > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

