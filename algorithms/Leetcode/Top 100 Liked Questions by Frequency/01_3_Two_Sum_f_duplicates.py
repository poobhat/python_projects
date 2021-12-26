class Solution:
    def __init__(self):
        self.hashMap = {}

    def getKey(self, value):
        for key, val in self.hashMap.items():
            if val == value:
                return key
        return None

    def twoSum(self, nums: [int], target: [int]) -> [int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            otherKey = self.getKey(diff)
            if otherKey is not None:
                return [otherKey, i]
            else:
                self.hashMap[i] = nums[i]
        return [-1, -1]

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))