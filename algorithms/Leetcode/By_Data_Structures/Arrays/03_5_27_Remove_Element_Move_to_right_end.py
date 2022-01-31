"""
Runtime: 32 ms, faster than 84.87%
Memory Usage: 13.9 MB, less than 97.02%
"""
class Solution:
    def removeElement(self, nums: [int], val: int):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]
                i+=1
        print(nums)
        return i
s= Solution()
n1, v1 = [1,2,3,3,2,1], 3
n2, v2 = [2,2],2
n3, v3 = [1,1,5,4,3], 1
n4, v4 = [3,2,1,1,1,1], 1
s.removeElement(n1,v1)
s.removeElement(n2,v2)
s.removeElement(n3, v3)
s.removeElement(n4, v4)