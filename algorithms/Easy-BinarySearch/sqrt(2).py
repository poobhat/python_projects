class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x
        while result * result > x:
            result = round((result + x/result)/2, 5)
            print(result)
        return int(result)

if __name__ == "__main__":
    obj = Solution()
    input = 15
    print(obj.mySqrt(input))