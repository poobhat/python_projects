"""
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

Return an integer array answer, where each answer[i] is the answer to the ith query.
"""

class Solution:
    def __init__(self):
        self.qFlist = []
        self.wFList = []
        self.answer = []
    def getFrequency(self, s):
        smallest = min(s)
        return s.count(smallest)

    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:

        for each in queries:
            self.qFlist.append(self.getFrequency(each))
        for each in words:
            self.wFList.append(self.getFrequency(each))

        self.wFList.sort()

        print(f"qFlist: {self.qFlist}", f"wFlist: {self.wFList}")
        q = self.qFlist
        w = self.wFList
        for each in self.qFlist:
            low = 0
            high = len(self.wFList)-1
            while low <= high:
                mid = (low+high)//2
                lookup = self.wFList[mid]
                if lookup <= each:
                    low = mid+1
                else:
                    high = mid-1
            self.answer.append(len(self.wFList[low:]))
        return self.answer

s = Solution()
# queries = ["bbb","cc"]
# words = ["a","aa","aaa","aaaa"]
queries = ["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"]
words = ["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"]
# queries = ["aabbabbb","abbbabaa","aabbbabaa","aabba","abb","a","ba","aa","ba","baabbbaaaa","babaa","bbbbabaa"]
# words = ["b","aaaba","aaaabba","aa","aabaabab","aabbaaabbb","ababb","bbb","aabbbabb","aab","bbaaababba","baaaaa"]
print(s.numSmallerByFrequency(queries, words))

