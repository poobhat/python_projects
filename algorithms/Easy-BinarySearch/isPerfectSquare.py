"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        high = num//2
        low = 0
        while low <= high:
            mid = (high+low)//2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr < num:
                low = mid+1
            else:
                high = mid-1
        return True if num == 1 else False

s = Solution()
num = 3
print(s.isPerfectSquare(num))