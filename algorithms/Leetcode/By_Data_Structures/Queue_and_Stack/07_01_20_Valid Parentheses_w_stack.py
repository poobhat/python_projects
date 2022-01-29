"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
##########################################
"""
Runtime: 52 ms, faster than 21.28%
Memory Usage: 13.7 MB, less than 100.00%
"""
##########################################
"""
Complexity analysis
Time complexity : O(n)O(n) because we simply traverse the given string one character 
at a time and push and pop operations on a stack take O(1)O(1) time.

Space complexity : O(n)O(n) as we push all opening brackets onto the stack and in the 
worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')':'(' ,']':'[', '}':'{'}
        stack = []
        for each in s:
            if each in lookup:
                if not stack or stack.pop() != lookup[each]:
                    return False
            else:
                stack.append(each)
        return stack == []


