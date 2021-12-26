"""
Given an array nums of integers and integer k, return the maximum sum such that there
exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

"""

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = -1
        nums.sort()
        # print(nums)
        high = len(nums)-1
        low = 0
        while high > low:
            sum = nums[high] + nums[low]
            # print(f"sum:{sum} high:{nums[high]} low:{nums[low]}")
            if sum < k:
                low+=1
                if sum > answer:
                    answer = sum
            elif sum >= k:
                high-=1

        return answer

if __name__ == "__main__":
    nums = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
    k = 200
    obj = Solution()
    print(obj.twoSumLessThanK(nums, k))

