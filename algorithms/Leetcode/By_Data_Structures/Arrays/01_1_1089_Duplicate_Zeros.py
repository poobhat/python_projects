"""
Reverse duplicate_zero_to_right to left
"""
class Solution:

    def duplicateZeros(self, arr: [int]) -> None:

        additionalZeros = 0
        n = len(arr)-1

        for i in range(n+1,-1,-1):
            if i < n - additionalZeros:
                break
            if arr[i] == 0:
                if i == n - additionalZeros:
                    # arr[n] = 0
                    n-= 1
                    break
                additionalZeros += 1

        last = n - additionalZeros

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i+additionalZeros] = 0
                additionalZeros -= 1
                arr[i+additionalZeros] = 0
            else:
                arr[i+additionalZeros] = arr[i]


        print(arr)

s = Solution()
arr = [1,1,2,0,3,4]
s.duplicateZeros(arr)
