class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        strength = [(sum(v),idx) for idx,v in enumerate(mat)]
        strength.sort()
        return [idx for idx,v in strength][:k]

s = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(s.kWeakestRows(mat, k))
