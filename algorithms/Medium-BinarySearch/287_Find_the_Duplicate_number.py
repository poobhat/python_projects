"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

"""
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 0
        high = len(nums)-1
        duplicate=0

        while low <= high:
            cur = (low + high) // 2
            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1

        return duplicate

s=Solution()
nums = [1,2,3,2,4,5,6,8,7,9]
print(s.findDuplicate(nums))