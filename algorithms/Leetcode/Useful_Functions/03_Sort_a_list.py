class Solution:
    def sortedArray(self, array):
        return sorted(array)

    def reverseSort(self, array):
        return sorted(array, reverse=True)

s = Solution()
nums=[7,4,6,2,5,6,2,1]
print(s.sortedArray(nums))
print(s.reverseSort(nums))