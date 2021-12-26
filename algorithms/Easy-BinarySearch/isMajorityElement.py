class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        return True if nums.count(target) >= len(nums)//2 else False