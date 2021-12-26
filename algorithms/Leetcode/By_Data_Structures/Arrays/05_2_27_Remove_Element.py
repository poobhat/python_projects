"""
WIP

This solution doesn't work for inputs
[2] 3
[2] 2
[5,4] 4

"""

class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        valOccurence = 0
        n = len(nums)-1
        for i in range(n+1):
            if i > n - valOccurence: break
            if nums[i] == val:
                if i == n - valOccurence:
                    n-=1
                    break
                valOccurence+=1
        last = n - valOccurence
        for i in range(last+1):
            if nums[i] == val:
                nums[i], nums[i+valOccurence] = nums[i+valOccurence], nums[i]
        print(nums)
        return last

s = Solution()
# nums = [0,1,2,2,3,0,4,2]
# output = [0,1,3,0,4,2,2,2]
# nums = [2]
# val =  2

nums = [4,5]
val = 4
print(s.removeElement(nums, val))