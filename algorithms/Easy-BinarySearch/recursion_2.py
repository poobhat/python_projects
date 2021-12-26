"""
Count the number of items in a list using recursion
"""

def countt(nums):
    if not nums:
        return 0
    else:
        return 1 + countt(nums[1:])

nums = [0]
print(countt(nums=nums))

