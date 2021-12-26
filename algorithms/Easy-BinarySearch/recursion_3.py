def findMax(nums):
    if not nums:
        return 0
    else:
        answer =  max(nums[0], findMax(nums[1:]))
        print(answer)
        return answer

nums=[10, 9, 5, 4, 1]
print(findMax(nums))