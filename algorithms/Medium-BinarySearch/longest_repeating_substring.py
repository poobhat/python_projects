class Solution:
    def search(self, L: int, n: int, s: str):
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # Subtask 2 : TODO
        subList=[]
        for i in range(0,n-L+1):
            substr = s[i:i+L]
            if substr in subList:
                print(substr)
                return i
            else:
                subList.append(substr)
        return -1


    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # binary search, L = repeating string length

        low, high = 1, n
        while low <= high:
            L = low + (high - low) // 2
            if self.search(L, n, S) != -1:
                low = L + 1
            else:
                high = L - 1

        return low - 1

so = Solution()
s = "aaaaa"
print(so.longestRepeatingSubstring(s))