"""
Given an array of n elements where the elements are between 0 to n-1, print the duplicates
to the console
Space complexity should be O(1)

"""

class Solution:
    def findDuplication(self, arr):
        n = len(arr)
        for i in range(0, n):
            if arr[abs(arr[i])] >= 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                print(abs(arr[i]))

s = Solution()
arr = [1,2,7,1,4,5,4,3,2]
s.findDuplication(arr)
