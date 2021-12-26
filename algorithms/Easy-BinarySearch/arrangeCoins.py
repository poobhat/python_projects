"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 0

        while high >= low:
            mid = (high+low)//2
            k = mid*(mid+1)//2
            if k==n:
                return mid
            elif k<n:
                low = mid+1
            else:
                high = mid-1
        return high




s = Solution()
n = 15
print(s.arrangeCoins(n))