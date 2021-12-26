class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ctr = 0
        for i in grid:
            for j in range(len(i)):
                if i[j] < 0:
                    ctr += len(i) - j
                    break
        return ctr


if __name__=="__main__":
    obj = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(obj.countNegatives(grid))