class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        while nums[nums[0]] != nums[0]:
           nums[nums[0]],nums[0] = nums[0], nums[nums[0]]
        return nums[0]


s=Solution()
nums = [1,2,2,4,5,6,8,7,10,9]
print(s.findDuplicate(nums))