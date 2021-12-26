"""
Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest
common element in all rows.

If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Example 2:

Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2

"""

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        hashMap = {}
        for row in mat:
            for each in row:
                if each not in hashMap.keys():
                    hashMap[each] = 1
                else:
                    hashMap[each]+=1
        answer = [k for k,v in hashMap.items() if v==len(mat)]
        return -1 if answer == [] else min(answer)


s = Solution()
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(s.smallestCommonElement(mat))








