class SumFunction(object):

    def sumIt(self, nums):
       answer = 0
       for i in nums:
           answer += i
       return answer

    def addUp(self, nums, idx=0, answer=0):
        if idx == len(nums):
            return answer
        else:
            answer = nums[idx] + self.addUp(nums, idx+1, answer)
        return answer

    def addThem(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return nums[0] + self.addThem(nums[1:])

s = SumFunction()
aList = [1,2,3,4]
print(s.addUp(aList))