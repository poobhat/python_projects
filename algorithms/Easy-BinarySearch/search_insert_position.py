import math


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high) //2
            if nums[mid] == target:
                return mid

            if nums[mid]<target:
                low = mid+1
                print("low")
            else:
                high = mid-1
                print("high")
            print(low,high)
        return high+1

if __name__ == "__main__":
    obj = Solution()
    nums = [1,3,5,6]
    target =8

    print(obj.searchInsert(nums, target))