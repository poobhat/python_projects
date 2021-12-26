# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n
        low = 0
        mid = 0
        while high > low:
            mid = (high+low)//2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == -1:
                high = mid - 1
            elif check == 1:
                low = mid + 1
        return mid