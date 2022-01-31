"""
Runtime: 48 ms, faster than 33.34%
Memory Usage: 13.9 MB, less than 99.25%
"""
class Solution:
    def removeElement(self, nums: [int], val: int):
        ptr = 0
        n = len(nums)
        while ptr < n:
            if nums[ptr] == val:
                nums.pop(ptr)
                n-=1
            else:
                ptr+=1
    """
    Runtime: 51 ms, faster than 28.39%
    Memory Usage: 13.9 MB, less than 99.25%
    """
    def remElement(self, nums: [int], val: int):
        while val in nums: nums.remove(val)
