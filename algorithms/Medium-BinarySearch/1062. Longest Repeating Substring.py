"""
Given a string s, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: s = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
"""

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        subList=[]
        size=0
        for i in range(2,len(s)):
            substr = s[:i]
            subList.append(substr)
        print([(x,len(x)) for x in subList])
        for sub in subList:
            pos = s.find(sub)
            if pos > -1:
                if s.find(sub,pos+1) > -1:
                    size = max(size, len(sub))
                    print(sub, size)
        return size

so = Solution()
s = "aabaabbaabbbabbbaaaabbaaaaaabbbaabbbbbbbbbaaaabbabbaba"
print(so.longestRepeatingSubstring(s))
