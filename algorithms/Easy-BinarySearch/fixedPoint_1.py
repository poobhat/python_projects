class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = len(arr) - 1
        res = -1

        while start <= end:
            mid = start + (end-start) // 2
            if arr[mid] == mid:
                res = mid
                end = mid - 1
            elif arr[mid] < mid:
                start = mid + 1
            else:
                end = mid - 1

        return res if res != -1 else -1

s = Solution()
arr = [-10,-5,-2,0,4,5,6,7,8,9,10]
print(s.fixedPoint(arr))