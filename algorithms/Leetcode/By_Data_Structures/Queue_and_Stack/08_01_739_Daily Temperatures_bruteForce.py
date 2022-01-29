"""
Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the ith
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
##################################################################
"""
Brute Force: Time Limit Exceeded
"""
class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        n = len(temperatures)
        answer = [0]*n
        for left in range(n):
            for right in range(left,n):
                if temperatures[left] < temperatures[right]:
                    answer[left] = right - left
                    break
        return answer

s = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
# temperatures = [55,38,53,81,61,93,97,32,43,78]
print(s.dailyTemperatures(temperatures))
# [3,1,1,2,1,1,0,1,1,0]
# [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]







