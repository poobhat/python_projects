"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears
exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

"""


class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                left,right = right+1, right+2
            else:
                return nums[left]
        return nums[left]


s=Solution()
nums = [18]
print(s.singleNonDuplicate(nums))