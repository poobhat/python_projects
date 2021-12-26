def binary_search(nums, l, h, target):
    mid = (l+h) // 2
    if h >= 1:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums, l, mid-1, target)
        elif nums[mid] < target:
            return binary_search(nums, mid+1, h, target)
    else:
        return None
nums = [1,2,3,4,5,6,7]
target = 3
print(binary_search(nums, 0, len(nums)-1, target))