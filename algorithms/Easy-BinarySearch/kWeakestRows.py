class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        strength = [sum(x) for x in mat]
        hashMap = {}
        for i in range(len(strength)):
           hashMap[i] = strength[i]
        return [k for k,v in sorted(hashMap.items(), key=lambda item: item[1])[:3]]

s = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(s.kWeakestRows(mat, k))
