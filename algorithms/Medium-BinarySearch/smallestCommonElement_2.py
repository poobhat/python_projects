class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        mat.sort()
        print(mat)
        lookup = mat[len(mat)-1]
        i = 0
        while i <= len(lookup)-1:
            target = lookup[i]
            ctr = 0
            print(lookup, target)
            rLow = len(mat)-2
            while rLow >= 0:
                row = mat[rLow]
                high = len(row)-1
                low = 0
                while low <= high:
                    mid = (low+high)//2
                    if row[mid] == target:
                        ctr+=1
                        break
                    elif row[mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                rLow-=1
            if ctr == len(mat)-1:
                return target
            else:
                i+=1
        return -1



s = Solution()
mat = [[1,2,3],[2,3,4],[2,3,5]]
print(s.smallestCommonElement(mat))