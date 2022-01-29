"""
Runtime: 48 ms, faster than 28.35%
Memory Usage: 13.9 MB, less than 99.72%
"""
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ""