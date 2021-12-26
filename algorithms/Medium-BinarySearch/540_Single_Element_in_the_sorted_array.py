class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        high = len(nums)-1
        low = 0
        while high > low:
            mid = low + (high-low)//2
            half_even = (high-mid)%2==0
            if nums[mid] == nums[mid+1]:
                if half_even:
                    low = mid+2
                else:
                    high = mid-1
            elif nums[mid] == nums[mid-1]:
                if half_even:
                    high = mid-2
                else:
                    low = mid+1
            else:
                return nums[mid]
        return nums[low]

s=Solution()
nums = [2,2,3,3,4,4,5]
print(s.singleNonDuplicate(nums))