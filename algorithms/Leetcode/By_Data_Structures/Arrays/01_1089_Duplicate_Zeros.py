"""

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining
elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications
to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9

"""

class Solution:
    def duplicateZerosToRight(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] == 0:
                for j in range(n-1, i+1, -1):
                   arr[j] = arr[j-1]
                arr[i+1]=0
        print(arr)

    def duplicateZerosToLeft(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(1,n):
            if arr[i] == 0:
                for j in range(1, i):
                    # print(arr[j-1], arr[j])
                    arr[j-1] = arr[j]
                arr[i-1]=0
        print(arr)





s = Solution()
arr = [1,0,1,2,3,4,5,0]
s.duplicateZerosToLeft(arr)