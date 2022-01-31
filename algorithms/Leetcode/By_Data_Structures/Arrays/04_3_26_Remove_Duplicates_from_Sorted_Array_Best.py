"""
Runtime: 84 ms, faster than 87.79%
Memory Usage: 15.7 MB, less than 48.34%
"""
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
        print(nums[:i+1])

s = Solution()
n1 = [1,1,2,3,4,4,5,6,7,7,7,7,8]
n2=[1,1]
s.removeDuplicates(n2)
