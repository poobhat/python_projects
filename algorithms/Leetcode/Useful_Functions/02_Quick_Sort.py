class Solution:
    def quickSort(self, array):
        if len(array) < 2:
            return array

        pivot = array[0]
        lesser = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return self.quickSort(lesser) + [pivot] + self.quickSort(greater)

s = Solution()
array = [9,6,8,3,1,6,8,8,7]
print(s.quickSort(array))
