class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        lookup = mat[0]
        answer = []
        for item in lookup:
            ctr = 0
            for row in mat[1:]:
                if item in row:
                    ctr+=1
            if ctr == len(mat)-1:
                answer.append(item)
        return -1 if answer ==[] else min(answer)

s = Solution()
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(s.smallestCommonElement(mat))