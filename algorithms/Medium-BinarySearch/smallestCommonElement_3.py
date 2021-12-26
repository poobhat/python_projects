class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        lookup = mat[0]
        i = 0
        while i < len(lookup):
            target = lookup[i]
            ctr = 0
            # print(lookup, target)
            rLow = 1
            while rLow < len(mat):
                row = mat[rLow]
                if target in row:
                    ctr+=1
                rLow+=1
            if ctr == len(mat)-1:
                return target
            else:
                i+=1
        return -1



s = Solution()
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(s.smallestCommonElement(mat))