class Solution():
    """Replace with highest element on the right side"""
    def replaceElements(self, arr):

        n = len(arr)
        last = arr[-1]
        arr[-1] = -1

        for i in range(n-2,-1,-1):
            arr[i], last = last, max(last, arr[i])

        return arr

    """Replace with highest element on the left side"""
    def replaceLeft(self, nums):

        n = len(nums)
        first = nums[0]
        nums[0] = -1

        for i in range(1,n):
            nums[i], first = first, max(nums[i], first)
        return nums


s = Solution()
# arr =[17,18,5,4,6,1]
arr = [17,18,5,4,6,1]
# print(s.replaceElements(arr))
nums = [3,4,5,3,2,1]

print(s.replaceLeft(nums))