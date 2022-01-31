"""
Runtime: 53 ms, faster than 24.96%
Memory Usage: 14 MB, less than 97.02%
"""
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx+=1
        return idx
