"""
Runtime: 60 ms, faster than 98.95%
Memory Usage: 14.9 MB, less than 61.82%
"""
class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        zeros = arr.count(0) #O(n)
        n = len(arr)
        for i in range(n-1,-1,-1):
            if i+zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < n:
                    arr[i+zeros] = 0
                if not zeros:
                    break


s= Solution()
arr = [1,0]
#     [0,1,2,3,4,5,6,7]
s.duplicateZeros(arr)
# Output: [1,0,0,2,3,0,0,4]
#         [0,1,2,3,4,5,6,7]
